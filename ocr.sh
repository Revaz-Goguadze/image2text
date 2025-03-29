#!/bin/bash

LOG_FILE=~/ocr-logs.txt
echo "$(date '+%Y-%m-%d %H:%M:%S') - OCR Script Started" >> "$LOG_FILE"

# Use the correct Python from your general venv
PYTHON_BIN="/home/coder/.env/bin/python3"

# Log which Python is being used
echo "Python path: $($PYTHON_BIN -c 'import sys; print(sys.executable)')" >> "$LOG_FILE"

# Run OCR script
$PYTHON_BIN /home/coder/Projects/image2text/main.py 2>&1 | tee -a "$LOG_FILE"
