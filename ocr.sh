#!/bin/bash

LOG_FILE=~/ocr-logs.txt
echo "$(date '+%Y-%m-%d %H:%M:%S') - OCR Script Started" >> "$LOG_FILE"

PYTHON_BIN="/home/coder/.env/bin/python3"

echo "Python path: $($PYTHON_BIN -c 'import sys; print(sys.executable)')" >> "$LOG_FILE"

$PYTHON_BIN /home/coder/Projects/image2text/main.py 2>&1 | tee -a "$LOG_FILE"
