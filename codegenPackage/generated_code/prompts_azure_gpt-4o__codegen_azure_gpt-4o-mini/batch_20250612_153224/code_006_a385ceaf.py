"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Develop a script to scan the directory for outdated files (e.g., `readme.html`) and generate a report for cleanup.
Generated: DETERMINISTIC_a385ceaf10024ad7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_outdated(file_path, days_threshold):
    """
    Check if a file is outdated based on the last modified time.

    :param file_path: Path to the file to check.
    :param days_threshold: Number of days to consider a file as outdated.
    :return: True if the file is outdated, False otherwise.
    """
    try:
        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(file_path)
        # Calculate the threshold time
        threshold_time = time.time() - (days_threshold * 86400)  # Convert days to seconds
        return last_modified_time < threshold_time
    except Exception as e:
        logging.error(f"Error checking file {file_path}: {e}")
        return False

def scan_directory_for_outdated_files(directory, days_threshold):
    """
    Scan the specified directory for outdated files and generate a report.

    :param directory: Directory to scan for outdated files.
    :param days_threshold: Number of days to consider a file as outdated.
    :return: List of outdated files.
    """
    outdated_files = []
    
    try:
        # Walk through the directory
        for root, _, files in os.walk(directory):
            for file in files:
                # Check for specific outdated file types
                if file.lower() == 'readme.html':
                    file_path = os.path.join(root, file)
                    if is_outdated(file_path, days_threshold):
                        outdated_files.append(file_path)
                        logging.info(f"Outdated file found: {file_path}")
    except Exception as e:
        logging.error(f"Error scanning directory {directory}: {e}")

    return outdated_files

def generate_report(outdated_files, report_file):
    """
    Generate a report of outdated files.

    :param outdated_files: List of outdated files.
    :param report_file: Path to the report file to be generated.
    """
    try:
        with open(report_file, 'w') as f:
            f.write("Outdated Files Report\n")
            f.write("=====================\n")
            for file in outdated_files:
                f.write(f"{file}\n")
        logging.info(f"Report generated: {report_file}")
    except Exception as e:
        logging.error(f"Error generating report {report_file}: {e}")

def main():
    # Configuration
    directory_to_scan = './'  # Change this to the directory you want to scan
    days_threshold = 30  # Files older than 30 days will be considered outdated
    report_file = 'outdated_files_report.txt'

    # Scan for outdated files
    outdated_files = scan_directory_for_outdated_files(directory_to_scan, days_threshold)

    # Generate report if there are outdated files
    if outdated_files:
        generate_report(outdated_files, report_file)
    else:
        logging.info("No outdated files found.")

if __name__ == "__main__":
    main()
```
