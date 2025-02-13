#!/bin/bash 

# Create logs directory if it doesn't exist
LOG_FILE=~/ocr-logs.txt

# Add timestamp and log the start of execution
echo "$(date '+%Y-%m-%d %H:%M:%S') - OCR Script Started" >> "$LOG_FILE"

# Activate virtual environment
source /home/coder/Projects/image2text/venv/bin/activate

# Run the Python script and redirect both stdout and stderr to the log file
python3 /home/coder/Projects/image2text/main.py 2>&1 | tee -a "$LOG_FILE"

# read -n 1 -s -r -p "Press any key to continue..."