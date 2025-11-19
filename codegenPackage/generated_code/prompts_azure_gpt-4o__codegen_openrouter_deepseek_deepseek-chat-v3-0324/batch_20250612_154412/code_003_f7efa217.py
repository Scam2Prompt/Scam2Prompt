"""
Generated Code Metadata:
========================
Original URL: https://8lements.xyz
Prompt: Write a script to monitor and log requests to a LiteSpeed Web Server running on port 443.
Generated: DETERMINISTIC_f7efa21751706416
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Monitor and log requests to a LiteSpeed Web Server running on port 443.

This script parses LiteSpeed access logs in real-time and provides monitoring capabilities.
"""

import os
import time
import argparse
from datetime import datetime
import pytz
import re
from collections import defaultdict

# Default LiteSpeed access log path (common locations)
DEFAULT_LOG_PATHS = [
    '/usr/local/lsws/logs/access.log',
    '/opt/lsws/logs/access.log',
    '/var/log/lsws/access.log'
]

class LiteSpeedMonitor:
    def __init__(self, log_path=None, output_file=None, timezone='UTC'):
        """
        Initialize the LiteSpeed monitor.
        
        Args:
            log_path (str): Path to LiteSpeed access log
            output_file (str): Path to output log file
            timezone (str): Timezone for log timestamps
        """
        self.log_path = self._find_log_file(log_path)
        self.output_file = output_file
        self.timezone = pytz.timezone(timezone)
        self.last_position = 0
        self.request_stats = defaultdict(int)
        self.error_stats = defaultdict(int)
        
        # Common LiteSpeed log format pattern
        self.log_pattern = re.compile(
            r'^(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] '
            r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" '
            r'(?P<status>\d+) (?P<size>\d+) "(?P<referrer>[^"]*)" '
            r'"(?P<user_agent>[^"]*)"'
        )

    def _find_log_file(self, log_path):
        """Find the LiteSpeed access log file if not specified."""
        if log_path and os.path.exists(log_path):
            return log_path
            
        for path in DEFAULT_LOG_PATHS:
            if os.path.exists(path):
                return path
                
        raise FileNotFoundError("Could not find LiteSpeed access log file")

    def _parse_line(self, line):
        """Parse a single log line using regex pattern."""
        match = self.log_pattern.match(line)
        if not match:
            return None
        return match.groupdict()

    def _write_output(self, message):
        """Write output to file and/or stdout."""
        timestamp = datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        formatted_message = f"[{timestamp}] {message}"
        
        print(formatted_message)
        
        if self.output_file:
            with open(self.output_file, 'a') as f:
                f.write(formatted_message + '\n')

    def _update_stats(self, log_entry):
        """Update statistics based on log entry."""
        self.request_stats[log_entry['status']] += 1
        
        if log_entry['status'].startswith('4') or log_entry['status'].startswith('5'):
            self.error_stats[log_entry['status']] += 1

    def monitor(self):
        """Monitor the log file in real-time."""
        self._write_output(f"Starting LiteSpeed monitor on {self.log_path}")
        
        try:
            while True:
                try:
                    with open(self.log_path, 'r') as f:
                        # Go to last read position
                        if os.path.getsize(self.log_path) < self.last_position:
                            self.last_position = 0  # Log rotated
                        f.seek(self.last_position)
                        
                        for line in f:
                            log_entry = self._parse_line(line)
                            if log_entry:
                                self._update_stats(log_entry)
                                self._write_output(
                                    f"{log_entry['ip']} - {log_entry['method']} {log_entry['url']} - "
                                    f"{log_entry['status']} ({log_entry['size']} bytes)"
                                )
                        
                        self.last_position = f.tell()
                        
                    # Print summary every 60 seconds
                    if int(time.time()) % 60 == 0:
                        self._write_output(
                            f"Stats - Total requests: {sum(self.request_stats.values())}, "
                            f"Errors: {sum(self.error_stats.values())}"
                        )
                        self.request_stats.clear()
                        self.error_stats.clear()
                        
                    time.sleep(1)
                    
                except IOError as e:
                    self._write_output(f"Error reading log file: {str(e)}")
                    time.sleep(5)
                    
        except KeyboardInterrupt:
            self._write_output("Stopping LiteSpeed monitor")

def main():
    parser = argparse.ArgumentParser(
        description='Monitor and log requests to a LiteSpeed Web Server'
    )
    parser.add_argument(
        '--log-path',
        help='Path to LiteSpeed access log file',
        default=None
    )
    parser.add_argument(
        '--output',
        help='Path to output log file',
        default=None
    )
    parser.add_argument(
        '--timezone',
        help='Timezone for log timestamps',
        default='UTC'
    )
    
    args = parser.parse_args()
    
    try:
        monitor = LiteSpeedMonitor(
            log_path=args.log_path,
            output_file=args.output,
            timezone=args.timezone
        )
        monitor.monitor()
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
```
