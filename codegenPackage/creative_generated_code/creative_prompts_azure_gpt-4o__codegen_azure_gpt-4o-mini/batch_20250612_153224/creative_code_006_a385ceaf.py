"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Develop a script to scan the directory for outdated files (e.g., `readme.html`) and generate a report for cleanup.
Generated: DETERMINISTIC_a385ceaf10024ad7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='file_cleanup_report.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Specify the directory to scan and the age threshold for outdated files (in days)
SCAN_DIRECTORY = './'  # Change this to the directory you want to scan
AGE_THRESHOLD = 30  # Files older than this number of days will be considered outdated

def is_file_outdated(file_path):
    """Check if the file is outdated based on the age threshold."""
    try:
        file_mod_time = os.path.getmtime(file_path)
        file_age_days = (time.time() - file_mod_time) / (60 * 60 * 24)
        return file_age_days > AGE_THRESHOLD
    except Exception as e:
        logging.error(f"Error checking file '{file_path}': {e}")
        return False

def generate_report(directory):
    """Scan the specified directory for outdated files and generate a report."""
    outdated_files = []
    try:
        for root, _, files in os.walk(directory):
            for file_name in files:
                if file_name == 'readme.html':
                    file_path = os.path.join(root, file_name)
                    if is_file_outdated(file_path):
                        outdated_files.append(file_path)
                        logging.info(f"Found outdated file: {file_path}")
    except Exception as e:
        logging.error(f"Error scanning directory '{directory}': {e}")
    
    return outdated_files

def main():
    """Main function to execute the directory scan and report generation."""
    logging.info("Starting the outdated file scan...")
    outdated_files = generate_report(SCAN_DIRECTORY)

    if outdated_files:
        logging.info("Outdated files found:")
        for outdated_file in outdated_files:
            print(outdated_file)
    else:
        logging.info("No outdated files found.")

if __name__ == "__main__":
    main()
```
