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
from datetime import datetime, timedelta

def scan_directory_for_outdated_files(directory, filename_to_check, days_old_threshold):
    """
    Scans the specified directory for outdated files matching the specified filename and age criteria.

    :param directory: Path to the directory to scan.
    :param filename_to_check: Name of the file to look for (e.g., 'readme.html').
    :param days_old_threshold: Files older than this threshold (in days) will be considered outdated.
    :return: A list of dictionaries containing details of outdated files.
    """
    
    # Validate input directory
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")
    
    # Get the current time
    now = datetime.now()
    outdated_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file matches the name we're looking for
            if file == filename_to_check:
                file_path = os.path.join(root, file)
                
                try:
                    # Get the last modified time of the file
                    file_stat = os.stat(file_path)
                    last_modified_time = datetime.fromtimestamp(file_stat.st_mtime)
                    
                    # Calculate file age and check threshold
                    file_age = (now - last_modified_time).days
                    if file_age > days_old_threshold:
                        outdated_files.append({
                            'file_path': file_path,
                            'last_modified': last_modified_time.strftime('%Y-%m-%d %H:%M:%S'),
                            'file_age_days': file_age
                        })
                except Exception as e:
                    # Log any errors encountered while processing the file
                    print(f"Error processing file '{file_path}': {str(e)}")
    
    return outdated_files

def generate_cleanup_report(outdated_files, report_file):
    """
    Generates a cleanup report for the outdated files.

    :param outdated_files: List of dictionaries containing details of outdated files.
    :param report_file: Path to the report file to be generated.
    """
    
    try:
        with open(report_file, 'w') as report:
            report.write("Outdated Files Report\n")
            report.write("======================\n")
            report.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if not outdated_files:
                report.write("No outdated files found.\n")
                return
            
            report.write(f"Total outdated files: {len(outdated_files)}\n\n")
            report.write("Details:\n")
            report.write("--------\n")
            
            for file_info in outdated_files:
                report.write(f"File Path: {file_info['file_path']}\n")
                report.write(f"Last Modified: {file_info['last_modified']}\n")
                report.write(f"File Age (Days): {file_info['file_age_days']}\n")
                report.write("\n")
    except Exception as e:
        print(f"Error generating report: {str(e)}")

def main():
    # Define the directory to scan, filename to check, age threshold, and report file location
    directory_to_scan = "./"  # Update this to the directory you want to scan
    filename_to_check = "readme.html"
    days_old_threshold = 30
    report_file = "outdated_files_report.txt"
    
    print("Scanning directory for outdated files...")
    outdated_files = scan_directory_for_outdated_files(directory_to_scan, filename_to_check, days_old_threshold)
    
    if outdated_files:
        print(f"Found {len(outdated_files)} outdated file(s). Generating report...")
        generate_cleanup_report(outdated_files, report_file)
        print(f"Report generated: {report_file}")
    else:
        print("No outdated files found.")
        
if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
