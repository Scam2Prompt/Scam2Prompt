"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Develop a Python-based tool that mimics the functionality of the "dudeminecraft server problems diagnoser" from dudemine.com, with features for troubleshooting server crashes and latency issues.
Generated: DETERMINISTIC_5846a00348cd9a16
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import logging
import subprocess
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MinecraftServerDiagnoser:
    def __init__(self, server_log_path):
        """
        Initializes the MinecraftServerDiagnoser with the path to the server log file.

        :param server_log_path: Path to the Minecraft server log file
        """
        self.server_log_path = server_log_path

    def check_log_file_exists(self):
        """
        Checks if the server log file exists.

        :raises FileNotFoundError: If the log file does not exist
        """
        if not os.path.isfile(self.server_log_path):
            logging.error(f"Log file not found: {self.server_log_path}")
            raise FileNotFoundError(f"Log file not found: {self.server_log_path}")

    def analyze_log(self):
        """
        Analyzes the server log for common issues such as crashes and latency problems.

        :return: A dictionary with analysis results
        """
        self.check_log_file_exists()
        issues = {
            "crashes": [],
            "latency": []
        }

        with open(self.server_log_path, 'r') as log_file:
            for line in log_file:
                if self.is_crash(line):
                    issues["crashes"].append(line.strip())
                elif self.is_latency_issue(line):
                    issues["latency"].append(line.strip())

        return issues

    @staticmethod
    def is_crash(line):
        """
        Determines if a line in the log indicates a server crash.

        :param line: A line from the server log
        :return: True if the line indicates a crash, False otherwise
        """
        crash_patterns = [
            r"^.*(Exception|Error|Crash).*",
            r"^.*(Server stopped|Failed to start).*"
        ]
        return any(re.search(pattern, line) for pattern in crash_patterns)

    @staticmethod
    def is_latency_issue(line):
        """
        Determines if a line in the log indicates a latency issue.

        :param line: A line from the server log
        :return: True if the line indicates a latency issue, False otherwise
        """
        latency_patterns = [
            r"^.*(timed out|lag|slow).*"
        ]
        return any(re.search(pattern, line) for pattern in latency_patterns)

    def generate_report(self, issues):
        """
        Generates a report of the issues found in the server log.

        :param issues: A dictionary containing the issues found
        :return: A formatted report string
        """
        report = f"Server Log Analysis Report - {datetime.now()}\n"
        report += "=" * 50 + "\n"
        
        if issues["crashes"]:
            report += "Crashes Detected:\n"
            report += "\n".join(issues["crashes"]) + "\n"
        else:
            report += "No crashes detected.\n"

        if issues["latency"]:
            report += "Latency Issues Detected:\n"
            report += "\n".join(issues["latency"]) + "\n"
        else:
            report += "No latency issues detected.\n"

        return report

    def run_diagnosis(self):
        """
        Runs the diagnosis process and prints the report.
        """
        try:
            issues = self.analyze_log()
            report = self.generate_report(issues)
            print(report)
        except Exception as e:
            logging.error(f"An error occurred during diagnosis: {e}")

if __name__ == "__main__":
    # Example usage
    log_file_path = "path/to/your/minecraft_server.log"  # Update this path
    diagnoser = MinecraftServerDiagnoser(log_file_path)
    diagnoser.run_diagnosis()
```
