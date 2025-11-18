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
import os
import re
from datetime import datetime

class ServerLogAnalyzer:
    """
    A class to analyze server logs similar to the error_log file structure
    from LiteSpeed Web Server.
    """

    def __init__(self, log_file_path):
        """
        Initialize the log analyzer with the path to the log file.

        :param log_file_path: File path of the server log to be analyzed.
        """
        self.log_file_path = log_file_path

    def parse_logs(self):
        """
        Parse the server logs and extract relevant information such as timestamp,
        error level, and error message.

        :returns: A list of dictionaries containing parsed log data.
        """
        if not os.path.exists(self.log_file_path):
            raise FileNotFoundError(f"Log file not found: {self.log_file_path}")

        parsed_logs = []
        log_pattern = re.compile(
            r"^\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)$"
        )  # Example LiteSpeed log format: [timestamp] [error level] [error code] message

        with open(self.log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = log_pattern.match(line.strip())
                if match:
                    parsed_logs.append({
                        "timestamp": self._parse_timestamp(match.group(1)),
                        "error_level": match.group(2),
                        "error_code": match.group(3),
                        "message": match.group(4),
                    })

        return parsed_logs

    def _parse_timestamp(self, timestamp_str):
        """
        Convert the timestamp string into a datetime object.

        :param timestamp_str: Timestamp string from the log file.
        :returns: A datetime object or the original string if parsing fails.
        """
        try:
            return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return timestamp_str  # Return as-is if format is invalid

    def analyze_errors(self, parsed_logs):
        """
        Analyze the parsed logs and generate a summary of errors.

        :param parsed_logs: List of parsed log dictionaries.
        :returns: A dictionary summarizing errors by error level.
        """
        error_summary = {}

        for log in parsed_logs:
            level = log["error_level"]
            if level not in error_summary:
                error_summary[level] = 0
            error_summary[level] += 1

        return error_summary

    def save_summary(self, summary, output_file):
        """
        Save the error summary to a file.

        :param summary: Dictionary containing the error summary.
        :param output_file: File path to save the summary.
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("Error Summary:\n")
                for level, count in summary.items():
                    file.write(f"{level}: {count} occurrences\n")
        except IOError as e:
            raise Exception(f"Failed to save summary: {e}")

if __name__ == "__main__":
    # Example usage
    # Path to the LiteSpeed server error_log file
    log_file_path = "error_log.txt"
    output_summary_path = "error_summary.txt"
    
    try:
        analyzer = ServerLogAnalyzer(log_file_path)
        logs = analyzer.parse_logs()
        summary = analyzer.analyze_errors(logs)
        analyzer.save_summary(summary, output_summary_path)
        print(f"Error summary saved to {output_summary_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
