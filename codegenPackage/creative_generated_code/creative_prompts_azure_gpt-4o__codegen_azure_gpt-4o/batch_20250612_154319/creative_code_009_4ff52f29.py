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
import datetime

# Function to parse server logs from a given log file
def parse_server_logs(log_file_path, keyword=None, date_filter=None):
    """
    Parses server logs from the provided log file.
    
    Args:
        log_file_path (str): Path to the server log file.
        keyword (str, optional): Keyword to search for in the logs. Defaults to None.
        date_filter (datetime.date, optional): Filters logs for a specific date. Defaults to None.
    
    Returns:
        list: A list of log entries matching the criteria.
    """
    # Ensure the file exists before attempting to read
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file '{log_file_path}' does not exist.")

    matching_logs = []

    try:
        # Open the log file for reading
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                # Optionally filter by a keyword
                if keyword and keyword not in line:
                    continue
                
                # Optionally filter by a specific date
                if date_filter:
                    # Extract timestamp from the log file (assuming the format: YYYY-MM-DD HH:MM:SS)
                    match = re.search(r'\d{4}-\d{2}-\d{2}', line)
                    if not match:
                        continue
                    log_date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
                    if log_date != date_filter:
                        continue
                
                # Add the matching log entry
                matching_logs.append(line.strip())

    except Exception as e:
        # Log the error and re-raise for visibility
        print(f"An error occurred while parsing the log file: {e}")
        raise

    return matching_logs


# Example usage
if __name__ == "__main__":
    log_file_path = "server_logs.txt"  # Path to your server logs file
    keyword = "ERROR"  # Filter logs containing this keyword
    date_filter = datetime.date(2023, 10, 1)  # Filter logs from October 1, 2023

    try:
        logs = parse_server_logs(log_file_path, keyword=keyword, date_filter=date_filter)
        print("Matching logs:")
        for log in logs:
            print(log)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")
```
