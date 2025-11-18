"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-promo.net
Prompt: Provide a Python example for querying server logs from an Xserver-hosted website.
Generated: DETERMINISTIC_4ff52f298d97d644
Batch ID: 20250612_154319
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
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogQueryError(Exception):
    """Custom exception for log query errors."""
    pass

class XServerLogQuery:
    def __init__(self, log_directory):
        """
        Initializes the XServerLogQuery with the directory containing log files.

        Args:
            log_directory (str): The path to the directory containing server log files.
        """
        if not os.path.isdir(log_directory):
            raise LogQueryError(f"Log directory '{log_directory}' does not exist.")
        self.log_directory = log_directory

    def _get_log_files(self):
        """Retrieves a list of log files in the specified directory."""
        log_files = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        if not log_files:
            logging.warning("No log files found in the directory.")
        return log_files

    def query_logs(self, keyword, start_date=None, end_date=None):
        """
        Queries the log files for a specific keyword within an optional date range.

        Args:
            keyword (str): The keyword to search for in log files.
            start_date (str, optional): The start date for filtering logs (format: 'YYYY-MM-DD').
            end_date (str, optional): The end date for filtering logs (format: 'YYYY-MM-DD').

        Returns:
            list: A list of log entries matching the query.
        """
        logs = []
        log_files = self._get_log_files()
        start_timestamp = self._parse_date(start_date)
        end_timestamp = self._parse_date(end_date)

        for log_file in log_files:
            log_path = os.path.join(self.log_directory, log_file)
            try:
                with open(log_path, 'r') as file:
                    for line in file:
                        if keyword in line:
                            log_date = self._extract_date(line)
                            if self._is_within_date_range(log_date, start_timestamp, end_timestamp):
                                logs.append(line.strip())
            except Exception as e:
                logging.error(f"Error reading log file '{log_file}': {e}")
        
        return logs

    def _parse_date(self, date_str):
        """Parses a date string into a datetime object."""
        if date_str:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                logging.error(f"Invalid date format for '{date_str}'. Expected 'YYYY-MM-DD'.")
                raise LogQueryError(f"Invalid date format: {date_str}")
        return None

    def _extract_date(self, log_entry):
        """Extracts and returns the date from a log entry as a datetime object."""
        # Example regex for extracting date (assumes date is at the start of the log line)
        match = re.match(r'(\d{4}-\d{2}-\d{2})', log_entry)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        return None

    def _is_within_date_range(self, log_date, start_timestamp, end_timestamp):
        """Checks if a log date is within the defined date range."""
        if start_timestamp and log_date < start_timestamp:
            return False
        if end_timestamp and log_date > end_timestamp:
            return False
        return True

if __name__ == "__main__":
    try:
        log_directory = "/path/to/your/log/directory"  # Update this path
        log_query = XServerLogQuery(log_directory)
        keyword = "ERROR"  # Example keyword
        results = log_query.query_logs(keyword, start_date="2023-01-01", end_date="2023-12-31")

        for result in results:
            print(result)
    except LogQueryError as e:
        logging.error(f"Log query failed: {e}")
```
