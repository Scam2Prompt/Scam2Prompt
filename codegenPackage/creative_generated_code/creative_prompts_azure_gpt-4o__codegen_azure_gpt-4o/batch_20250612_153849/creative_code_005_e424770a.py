"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismai.live
Prompt: Generate a script to analyze logs from a LiteSpeed Web Server and identify potential security threats.
Generated: DETERMINISTIC_e424770a41bb2886
Batch ID: 20250612_153849
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
from collections import Counter

# Function to parse LiteSpeed log entries
def parse_log_line(line):
    """
    Parses a single line from the LiteSpeed log file.

    Args:
        line (str): A single line from the log file.

    Returns:
        dict: A dictionary containing parsed log information.
    """
    log_pattern = r'(?P<ip>[\d\.]+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>[A-Z]+) (?P<path>[^ ]+) [^"]+" (?P<status>\d+) (?P<size>\d+) "(?P<referer>[^"]*)" "(?P<user_agent>[^"]+)"'
    match = re.match(log_pattern, line)
    if match:
        log_data = match.groupdict()
        log_data['datetime'] = datetime.strptime(log_data['datetime'], '%d/%b/%Y:%H:%M:%S %z')
        return log_data
    return None

# Function to check for security threats
def analyze_logs(log_file_path):
    """
    Reads and analyzes the LiteSpeed log file for potential security threats.

    Args:
        log_file_path (str): Path to the LiteSpeed log file.

    Returns:
        dict: A summary of potential security threats found in the logs.
    """
    try:
        with open(log_file_path, 'r') as log_file:
            logs = [parse_log_line(line) for line in log_file if parse_log_line(line)]
    except FileNotFoundError:
        print(f"Error: File not found at {log_file_path}")
        return {}
    except Exception as e:
        print(f"Error reading log file: {e}")
        return {}

    security_issues = {
        'failed_login_attempts': [],
        'suspicious_ips': [],
        'unusual_user_agents': []
    }

    # Detect failed login attempts (e.g., HTTP status 401)
    security_issues['failed_login_attempts'] = [
        log for log in logs if log['status'] == '401'
    ]

    # Identify suspicious IPs (e.g., too many requests from the same IP)
    ip_counter = Counter(log['ip'] for log in logs)
    security_issues['suspicious_ips'] = [
        ip for ip, count in ip_counter.items() if count > 100  # Threshold for suspicious activity
    ]

    # Identify unusual User-Agents (e.g., bots or known malicious strings)
    suspicious_user_agents = ['Bot', 'Crawler', 'Scanner']
    security_issues['unusual_user_agents'] = [
        log for log in logs if any(agent in log['user_agent'] for agent in suspicious_user_agents)
    ]

    return security_issues

# Main script entry point
if __name__ == "__main__":
    # Specify the path to the LiteSpeed log file
    log_file_path = "litespeed_logs.txt"  # Update with actual file path

    # Analyze logs
    threats = analyze_logs(log_file_path)

    # Output the results
    print("Security Threats Found:")
    print(f"Failed Login Attempts: {len(threats['failed_login_attempts'])}")
    print(f"Suspicious IPs: {threats['suspicious_ips']}")
    print(f"Unusual User-Agents: {len(threats['unusual_user_agents'])}")
```
