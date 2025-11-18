"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: Recommend a library or API for interacting with LiteSpeed Web Server logs and demonstrate how to use it to analyze access patterns for directories like `cgi-bin`.
Generated: DETERMINISTIC_e9b93fec2810504c
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import pandas as pd
from datetime import datetime

class LiteSpeedLogAnalyzer:
    """
    A class to analyze LiteSpeed web server access logs for specific directories.

    Attributes:
        log_file_path (str): Path to the LiteSpeed access log file.
    """

    def __init__(self, log_file_path):
        """
        Initializes the LiteSpeedLogAnalyzer with the path to the log file.

        Args:
            log_file_path (str): The path to the LiteSpeed access log file.
        """
        if not os.path.isfile(log_file_path):
            raise FileNotFoundError(f"Log file not found: {log_file_path}")
        self.log_file_path = log_file_path

    def parse_log(self):
        """
        Parses the LiteSpeed access log and returns structured log data.

        Returns:
            list: A list of dictionaries containing log entries.
        """
        log_entries = []
        log_pattern = re.compile(r'(?P<ip>[\d.]+) - - \[(?P<date>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d+) \d+')

        try:
            with open(self.log_file_path, 'r') as file:
                for line in file:
                    match = log_pattern.match(line)
                    if match:
                        log_entries.append(match.groupdict())
        except Exception as e:
            raise RuntimeError(f"Error reading log file: {e}")

        return log_entries

    def analyze_directory_access(self, directory):
        """
        Analyzes access patterns for a specific directory.

        Args:
            directory (str): The directory to analyze (e.g., 'cgi-bin').

        Returns:
            pd.DataFrame: A DataFrame with access counts per IP address.
        """
        log_entries = self.parse_log()
        filtered_entries = [entry for entry in log_entries if entry['path'].startswith(f'/{directory}')]
        
        # Convert to DataFrame for further analysis
        df = pd.DataFrame(filtered_entries)
        df['date'] = pd.to_datetime(df['date'], format='%d/%b/%Y:%H:%M:%S %z')

        # Count accesses per IP
        access_counts = df['ip'].value_counts().reset_index()
        access_counts.columns = ['IP Address', 'Access Count']
        
        return access_counts

# Example Usage
if __name__ == "__main__":
    try:
        log_analyzer = LiteSpeedLogAnalyzer('path/to/your/litespeed/access.log')
        access_analysis = log_analyzer.analyze_directory_access('cgi-bin')
        print(access_analysis)
    except Exception as e:
        print(f"An error occurred: {e}")
```
