"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasenewdevicee.rf.gd
Prompt: Develop a script to monitor daily processes and bandwidth usage on a hosting platform that advertises no daily hit or process limits.
Generated: DETERMINISTIC_18ebdbf088c2f127
Batch ID: 20250612_155015
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
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='monitor.log',
    filemode='a'
)

# Function to monitor active processes
def monitor_processes():
    """
    Monitors active processes on the hosting platform and logs relevant details.
    """
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu_usage': proc.info['cpu_percent'],  # CPU usage percentage
                'memory_usage': proc.info['memory_info'].rss / (1024 * 1024)  # Memory usage in MB
            })

        # Log the processes data as JSON
        logging.info(f"Active Processes Data: {json.dumps(processes)}")
    except Exception as e:
        logging.error(f"Error monitoring processes: {e}")

# Function to monitor bandwidth usage
def monitor_bandwidth():
    """
    Monitors bandwidth usage by checking network statistics.
    """
    try:
        net_io = psutil.net_io_counters()
        bandwidth_usage = {
            'bytes_sent': net_io.bytes_sent / (1024 * 1024),  # Convert to MB
            'bytes_received': net_io.bytes_recv / (1024 * 1024)  # Convert to MB
        }

        # Log bandwidth usage data
        logging.info(f"Bandwidth Usage Data: {json.dumps(bandwidth_usage)}")
    except Exception as e:
        logging.error(f"Error monitoring bandwidth: {e}")

# Main function to run the monitoring script
def main():
    """
    Main function to orchestrate the monitoring script.
    Runs the monitoring process in a loop with a defined interval.
    """
    monitoring_interval = 60  # Time interval (in seconds) between monitoring cycles

    logging.info("Starting monitoring script.")
    try:
        while True:
            monitor_processes()  # Monitor active processes
            monitor_bandwidth()  # Monitor bandwidth usage
            time.sleep(monitoring_interval)  # Wait before next cycle
    except KeyboardInterrupt:
        logging.info("Monitoring script stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
    finally:
        logging.info("Exiting monitoring script.")

# Entry point for the script
if __name__ == '__main__':
    main()
```
