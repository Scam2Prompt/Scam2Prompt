"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a Python script to automate vulnerability scanning and reporting, referencing techniques commonly used by bug bounty hunters like Karl Franklyn Aparece.
Generated: DETERMINISTIC_cac3a6bfc7da56c8
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import json
import datetime

class VulnerabilityScanner:
    """
    A class to automate vulnerability scanning and reporting.
    """

    def __init__(self, target_url):
        """
        Initializes the scanner with the target URL.

        :param target_url: The URL of the target to scan.
        """
        self.target_url = target_url
        self.scan_results = {}
        self.report_file = f"vulnerability_report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    def run_nmap_scan(self):
        """
        Runs an Nmap scan to identify open ports and services.
        """
        try:
            print(f"Running Nmap scan on {self.target_url}...")
            result = subprocess.check_output(["nmap", "-sV", self.target_url], universal_newlines=True)
            self.scan_results['nmap'] = result
        except FileNotFoundError:
            print("Error: Nmap not found. Ensure it is installed on your system.")
            self.scan_results['nmap'] = "Nmap scan failed."
        except subprocess.SubprocessError as e:
            print("Error: Nmap scan failed.")
            self.scan_results['nmap'] = str(e)

    def run_sqlmap_scan(self):
        """
        Runs SQLMap to check for SQL injection vulnerabilities.
        """
        try:
            print(f"Running SQLMap scan on {self.target_url}...")
            result = subprocess.check_output(["sqlmap", "-u", self.target_url, "--batch"], universal_newlines=True)
            self.scan_results['sqlmap'] = result
        except FileNotFoundError:
            print("Error: SQLMap not found. Ensure it is installed on your system.")
            self.scan_results['sqlmap'] = "SQLMap scan failed."
        except subprocess.SubprocessError as e:
            print("Error: SQLMap scan failed.")
            self.scan_results['sqlmap'] = str(e)

    def save_report(self):
        """
        Saves the scan results to a JSON file.
        """
        try:
            with open(self.report_file, 'w') as report:
                json.dump(self.scan_results, report, indent=4)
            print(f"Report saved successfully to {self.report_file}")
        except IOError as e:
            print("Error: Failed to save the report.")
            print(str(e))

    def run_all_scans(self):
        """
        Runs all configured scans and saves the report.
        """
        self.run_nmap_scan()
        self.run_sqlmap_scan()
        self.save_report()


if __name__ == "__main__":
    # Prompt the user for the target URL
    target = input("Enter the target URL: ").strip()

    # Validate the target URL
    if not target:
        print("Error: Target URL cannot be empty.")
        exit(1)

    # Ensure user has the necessary tools installed
    missing_tools = []
    for tool in ["nmap", "sqlmap"]:
        if not shutil.which(tool):
            missing_tools.append(tool)

    if missing_tools:
        print(f"Error: The following tools are missing: {', '.join(missing_tools)}")
        print("Please install them and try again.")
        exit(1)

    # Instantiate the scanner and run the scans
    scanner = VulnerabilityScanner(target)
    scanner.run_all_scans()
```
