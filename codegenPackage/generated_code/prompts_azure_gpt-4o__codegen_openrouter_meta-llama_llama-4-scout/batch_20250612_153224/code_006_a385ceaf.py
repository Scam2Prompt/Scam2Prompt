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
import datetime

def get_outdated_files(directory, threshold_days=180):
    """
    Scan the directory for outdated files.

    Args:
        directory (str): The directory to scan.
        threshold_days (int): The number of days after which a file is considered outdated.

    Returns:
        list: A list of tuples containing the file path and its last modification time.
    """
    outdated_files = []
    threshold_date = datetime.datetime.now() - datetime.timedelta(days=threshold_days)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if modification_time < threshold_date:
                    outdated_files.append((file_path, modification_time))
            except OSError as e:
                print(f"Error accessing file {file_path}: {e}")

    return outdated_files

def generate_report(outdated_files):
    """
    Generate a report for cleanup.

    Args:
        outdated_files (list): A list of tuples containing the file path and its last modification time.

    Returns:
        str: A report string.
    """
    report = "Outdated Files:\n"
    for file_path, modification_time in outdated_files:
        report += f"{file_path} - Last modified: {modification_time.strftime('%Y-%m-%d %H:%M:%S')}\n"

    return report

def main():
    directory = "."  # current directory
    threshold_days = 180  # 6 months

    try:
        outdated_files = get_outdated_files(directory, threshold_days)
        report = generate_report(outdated_files)
        print(report)

        # Save report to file
        with open("outdated_files_report.txt", "w") as f:
            f.write(report)
        print("Report saved to outdated_files_report.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
