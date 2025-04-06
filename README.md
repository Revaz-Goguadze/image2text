# Hyprland Clipboard OCR Script

This is a simple script designed for Hyprland (Wayland compositor) on Linux to extract text from images copied to the clipboard using Tesseract OCR.

## Features

- Works by copying an image into the clipboard (e.g., via screenshot tools or image copy).
- Converts the clipboard image to text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
- Puts the extracted text back into your clipboard for easy pasting anywhere.
- Intended to be triggered by a custom keybinding in Hyprland for quick and seamless OCR workflow.

## Requirements

- Hyprland Wayland compositor
- `tesseract-ocr` installed
- Clipboard utilities compatible with Wayland (e.g., `wl-clipboard`)

## Usage

1. Copy or screenshot an image into your clipboard.
2. Trigger the script through your predefined Hyprland keybinding.
3. The script runs OCR on the clipboard image.
4. The resulting text is available back in your clipboard.

## Notes

- Make sure Tesseract OCR is properly installed and added to your PATH.
- Configure your `hyprland.conf` to bind a key combination for running the script for convenience.
- Modify the script as needed for your setup.