import subprocess
import time
import hashlib
import io
from PIL import Image
import pytesseract
import notify2
import os
import sys

# Set Tesseract configs
if os.path.exists('/usr/share/tessdata'):
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    os.environ['TESSDATA_PREFIX'] = '/usr/share/tessdata'

def init_notifications():
    try:
        notify2.init("OCR Tool")
        return True
    except:
        return False

def notify(title, message):
    try:
        if hasattr(notify, 'notification_enabled'):
            n = notify2.Notification(title, message)
            n.show()
    except:
        pass

def get_clipboard_image_data():
    """
    Get image data from the clipboard using wl-paste
    """
    try:
        data = subprocess.check_output(["wl-paste", "--no-newline", "--type", "image/png"])
        return data if data else None
    except subprocess.CalledProcessError:
        return None

def copy_text_to_clipboard(text):
    """
    Copy text to clipboard using wl-copy
    """
    if not text.strip():
        return False
    try:
        # Clear clipboard first
        subprocess.run(['wl-copy', '--clear'], check=True)
        # Copy new text
        process = subprocess.run(['wl-copy'], input=text.encode(), check=True)
        # Verify the copy
        copied_text = subprocess.check_output(['wl-paste'], text=True).strip()
        return copied_text == text.strip()
    except subprocess.CalledProcessError as e:
        print(f"Failed to copy to clipboard: {e}")
        return False

def perform_ocr(image):
    try:
        # Configure Tesseract parameters for better accuracy
        custom_config = r'--oem 3 --psm 3'
        return pytesseract.image_to_string(image, config=custom_config).strip()
    except Exception as e:
        print(f"OCR Error: {e}")
        return None

def main():
    notify.notification_enabled = init_notifications()
    print("Waiting for image in clipboard...")
    
    max_attempts = 3
    attempt = 0
    
    while attempt < max_attempts:
        data = get_clipboard_image_data()
        if data:
            try:
                image = Image.open(io.BytesIO(data))
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                    
                text = perform_ocr(image)
                
                if text:
                    print("OCR Result:\n", text)
                    if copy_text_to_clipboard(text):
                        print("✓ Text successfully copied to clipboard")
                        notify("OCR Complete", "Text extracted and copied to clipboard")
                        sys.exit(0)
                    else:
                        print("✗ Failed to copy text to clipboard")
                        sys.exit(1)
                else:
                    print("No text detected in image")
                    sys.exit(1)
                    
            except Exception as e:
                print(f"Error during processing: {e}")
                sys.exit(1)
        
        attempt += 1
        if attempt < max_attempts:
            print(f"No image found, retrying... ({attempt}/{max_attempts})")
            time.sleep(0.5)
    
    print("No image found in clipboard after 3 attempts. Exiting...")
    sys.exit(1)

if __name__ == "__main__":
    main()

