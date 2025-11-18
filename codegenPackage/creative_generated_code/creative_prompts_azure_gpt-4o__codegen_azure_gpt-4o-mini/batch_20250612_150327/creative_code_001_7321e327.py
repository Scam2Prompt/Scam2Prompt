"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-airdrop.drcomputer.pk
Prompt: Generate code to analyze server logs, similar to the `error_log` file structure mentioned on a LiteSpeed Web Server.
Generated: DETERMINISTIC_7321e32782d55bdd
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime
import logging

# Setup logging for the analysis results
logging.basicConfig(filename='server_log_analysis.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ServerLogAnalyzer:
    """
    A class to analyze server logs similar to the error_log format of a LiteSpeed Web Server.
    """

    def __init__(self, log_file):
        """
        Initializes the ServerLogAnalyzer with the path to the log file.

        :param log_file: Path to the server log file
        """
        self.log_file = log_file
        self.log_entries = []

    def read_log_file(self):
        """
        Reads the log file and stores each log entry.

        :raises FileNotFoundError: If the log file does not exist
        """
        try:
            with open(self.log_file, 'r') as file:
                self.log_entries = file.readlines()
        except FileNotFoundError:
            logging.error(f"Log file not found: {self.log_file}")
            raise

    def parse_log_entry(self, entry):
        """
        Parses a single log entry and extracts relevant information.

        :param entry: A single line from the log file
        :return: A dictionary containing parsed log data
        """
        log_pattern = r'(\S+) (\S+) \[(.+?)\] "(\S+) (\S+) \S+" (\d{3})'
        match = re.match(log_pattern, entry)
        if match:
            return {
                'ip_address': match.group(1),
                'username': match.group(2),
                'timestamp': datetime.strptime(match.group(3), '%d/%b/%Y:%H:%M:%S %z'),
                'request_method': match.group(4),
                'requested_resource': match.group(5),
                'status_code': int(match.group(6)),
            }
        return None

    def analyze_logs(self):
        """
        Analyzes the log entries to identify status codes and aggregate statistics.
        
        :return: A dictionary with status code counts
        """
        status_code_count = {}
        
        for entry in self.log_entries:
            parsed_entry = self.parse_log_entry(entry)
            if parsed_entry:
                status_code = parsed_entry['status_code']
                if status_code not in status_code_count:
                    status_code_count[status_code] = 0
                status_code_count[status_code] += 1

        return status_code_count

    def display_analysis(self):
        """
        Displays the analysis results of the log entries.
        """
        status_counts = self.analyze_logs()
        for status_code, count in status_counts.items():
            logging.info(f"Status Code: {status_code}, Count: {count}")

if __name__ == "__main__":
    log_file_path = 'error_log'  # Replace with the path to your log file
    analyzer = ServerLogAnalyzer(log_file_path)

    try:
        analyzer.read_log_file()
        analyzer.display_analysis()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
