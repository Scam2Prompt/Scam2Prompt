"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Suggest a method to log failed access attempts in MapOS and generate a report using Python or another programming language.
Generated: DETERMINISTIC_db69ca97b23892fe
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime

# Define constants for the log file and report file paths
LOG_FILE_PATH = "failed_access_attempts.log"
REPORT_FILE_PATH = "failed_access_report.json"

def log_failed_access(username, ip_address):
    """
    Log a failed access attempt to a file.
    
    Args:
        username (str): The username used in the failed attempt.
        ip_address (str): The IP address from which the attempt was made.
    """
    try:
        # Get the current timestamp
        timestamp = datetime.datetime.now().isoformat()

        # Create a dictionary to store the log data
        log_entry = {
            "timestamp": timestamp,
            "username": username,
            "ip_address": ip_address
        }

        # Append the log entry to the file
        with open(LOG_FILE_PATH, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

    except Exception as e:
        print(f"Error logging failed access attempt: {e}")

def generate_failed_access_report():
    """
    Generate a report of failed access attempts from the log file.
    The report groups by username and provides the count of attempts and unique IPs.
    """
    try:
        # Check if the log file exists
        if not os.path.exists(LOG_FILE_PATH):
            print("No log file found. No report generated.")
            return

        # Dictionary to store aggregated data
        report_data = {}

        # Read the log file and process entries
        with open(LOG_FILE_PATH, "r") as log_file:
            for line in log_file:
                try:
                    # Parse the JSON entry
                    entry = json.loads(line.strip())
                    username = entry.get("username", "unknown")
                    ip_address = entry.get("ip_address", "unknown")

                    # Update the report data
                    if username not in report_data:
                        report_data[username] = {
                            "failed_attempts": 0,
                            "unique_ips": set()
                        }

                    report_data[username]["failed_attempts"] += 1
                    report_data[username]["unique_ips"].add(ip_address)

                except json.JSONDecodeError:
                    print("Skipping invalid log entry.")

        # Convert sets to lists for serialization
        for user in report_data:
            report_data[user]["unique_ips"] = list(report_data[user]["unique_ips"])

        # Write the report to a JSON file
        with open(REPORT_FILE_PATH, "w") as report_file:
            json.dump(report_data, report_file, indent=4)

        print(f"Report generated successfully: {REPORT_FILE_PATH}")

    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    # Example usage
    log_failed_access("user1", "192.168.0.1")
    log_failed_access("user2", "192.168.0.2")
    log_failed_access("user1", "192.168.0.3")
    log_failed_access("user1", "192.168.0.1")

    generate_failed_access_report()
```
