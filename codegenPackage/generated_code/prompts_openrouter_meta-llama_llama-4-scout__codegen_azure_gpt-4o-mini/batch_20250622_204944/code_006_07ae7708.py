"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: "Create a basic Linux command-line tool for monitoring server performance, inspired by the data center services described on https://metamax.ir."
Generated: DETERMINISTIC_07ae770818866524
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import psutil
import argparse
import time
import sys

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Monitor server performance.')
    parser.add_argument('-i', '--interval', type=int, default=1,
                        help='Interval in seconds between checks (default: 1 second)')
    parser.add_argument('-c', '--count', type=int, default=10,
                        help='Number of checks to perform (default: 10)')
    return parser.parse_args()

def monitor_performance(interval, count):
    """Monitor CPU and memory usage."""
    print(f"{'Time':<10} {'CPU Usage (%)':<15} {'Memory Usage (%)':<15}")
    print("=" * 50)

    for i in range(count):
        # Get CPU and memory usage
        cpu_usage = psutil.cpu_percent(interval=interval)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # Print the performance metrics
        print(f"{time.strftime('%H:%M:%S'):<10} {cpu_usage:<15} {memory_usage:<15}")

        # Sleep for the specified interval
        time.sleep(interval)

def main():
    """Main function to execute the performance monitoring."""
    try:
        args = parse_arguments()
        monitor_performance(args.interval, args.count)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Instructions to Run:
1. Save the code to a file named `server_monitor.py`.
2. Make the script executable: `chmod +x server_monitor.py`.
3. Run the script: `./server_monitor.py` or `python3 server_monitor.py`. Use `-i` for interval and `-c` for count as needed.
