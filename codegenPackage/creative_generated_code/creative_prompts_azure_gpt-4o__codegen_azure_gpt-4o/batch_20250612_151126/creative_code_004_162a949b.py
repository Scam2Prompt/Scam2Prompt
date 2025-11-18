"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfuili.epizy.com
Prompt: Create a Python script to monitor bandwidth usage on a hosting service with no daily hit or process limits.
Generated: DETERMINISTIC_162a949b5702bd2b
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import time
from datetime import datetime

def bytes_to_human_readable(bytes):
    """
    Convert bytes to a human-readable format (KB, MB, GB, etc.).
    :param bytes: Size in bytes
    :return: Human-readable string
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = bytes
    unit_index = 0

    while size > 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
    
    return f"{size:.2f} {units[unit_index]}"

def log_bandwidth_usage(file_path="bandwidth_log.txt", interval=60):
    """
    Monitor and log bandwidth usage periodically.
    :param file_path: Path to the log file
    :param interval: Time interval (in seconds) between checks
    """
    print(f"Monitoring bandwidth usage every {interval} seconds.")
    print(f"Logs will be written to {file_path}")
    
    try:
        # Initialize previous counters
        prev_sent = psutil.net_io_counters().bytes_sent
        prev_recv = psutil.net_io_counters().bytes_recv

        # Open log file for writing
        with open(file_path, 'a') as log_file:
            log_file.write("Timestamp,Bytes Sent (Human-Readable),Bytes Received (Human-Readable),Total Sent,Total Received\n")
            
            while True:
                # Fetch current bandwidth usage
                current_counters = psutil.net_io_counters()
                current_sent = current_counters.bytes_sent
                current_recv = current_counters.bytes_recv
                
                # Calculate difference since last check
                sent_diff = current_sent - prev_sent
                recv_diff = current_recv - prev_recv

                # Update previous counters
                prev_sent = current_sent
                prev_recv = current_recv
                
                # Generate human-readable bandwidth usage
                sent_hr = bytes_to_human_readable(sent_diff)
                recv_hr = bytes_to_human_readable(recv_diff)
                total_sent_hr = bytes_to_human_readable(current_sent)
                total_recv_hr = bytes_to_human_readable(current_recv)

                # Timestamp for logging
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Log data
                log_line = f"{timestamp},{sent_hr},{recv_hr},{total_sent_hr},{total_recv_hr}\n"
                log_file.write(log_line)
                log_file.flush()

                # Print to console for live monitoring
                print(f"[{timestamp}] Sent: {sent_hr}, Received: {recv_hr}")

                # Sleep until next interval
                time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")
        # Optional: log the error to the log file
        with open(file_path, 'a') as error_log:
            error_log.write(f"Error occurred: {e}\n")

if __name__ == '__main__':
    # Monitor bandwidth usage with a default interval of 60 seconds
    log_bandwidth_usage(interval=60)
```
