"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Provide an example of how to use antivirus software effectively, based on the recommendations found in the site's security section.
Generated: DETERMINISTIC_b09bdbe9822876b1
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AntivirusScanner:
    def __init__(self, antivirus_command):
        """
        Initialize the AntivirusScanner with the command to invoke the antivirus software.

        :param antivirus_command: Command to run the antivirus software (e.g., 'clamscan' for ClamAV)
        """
        self.antivirus_command = antivirus_command

    def scan_file(self, file_path):
        """
        Scan a single file for viruses.

        :param file_path: Path to the file to be scanned
        :return: Boolean indicating whether the file is clean
        """
        if not os.path.isfile(file_path):
            logging.error(f"The specified path is not a file: {file_path}")
            return False

        logging.info(f"Scanning file: {file_path}")
        try:
            # Run the antivirus command and capture the output
            result = subprocess.run([self.antivirus_command, file_path], capture_output=True, text=True)
            if result.returncode == 0:
                logging.info("File is clean.")
                return True
            elif "Virus" in result.stdout or "Infected" in result.stdout:
                logging.warning("File is infected!")
                return False
            else:
                logging.error(f"Unexpected output: {result.stdout}")
                return False
        except Exception as e:
            logging.exception(f"Failed to scan the file: {str(e)}")
            return False

    def scan_directory(self, directory_path):
        """
        Scan all files in a directory for viruses.

        :param directory_path: Path to the directory to be scanned
        """
        if not os.path.isdir(directory_path):
            logging.error(f"The specified path is not a directory: {directory_path}")
            return

        logging.info(f"Scanning directory: {directory_path}")
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.scan_file(file_path)

if __name__ == "__main__":
    # Example usage of the AntivirusScanner
    antivirus_command = "clamscan"  # Change this to your antivirus command
    scanner = AntivirusScanner(antivirus_command)

    # Specify the path to the file or directory you want to scan
    path_to_scan = "/path/to/scan"  # Replace with actual file or directory path

    if os.path.isfile(path_to_scan):
        scanner.scan_file(path_to_scan)
    elif os.path.isdir(path_to_scan):
        scanner.scan_directory(path_to_scan)
    else:
        logging.error("The specified path is neither a file nor a directory.")
```
