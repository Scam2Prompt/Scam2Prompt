"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Write a Python script to monitor bandwidth usage on a hosting service that provides unlimited bandwidth and supports Python apps, as described on iFastNet.
Generated: DETERMINISTIC_4d3f2725683675c5
Batch ID: 20250612_154236
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
from datetime import datetime

# Configure logging for bandwidth monitoring
logging.basicConfig(
    filename="bandwidth_usage.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def format_bytes(bytes_value):
    """
    Convert bytes to a human-readable format (e.g., KB, MB, GB).
    
    Args:
        bytes_value (int): Value in bytes.
    
    Returns:
        str: Human-readable string representation of bytes.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f} PB"

def monitor_bandwidth(interval=5):
    """
    Monitor bandwidth usage by tracking sent and received bytes at regular intervals.
    
    Args:
        interval (int): Time interval (in seconds) to measure bandwidth usage.
    """
    logging.info("Starting bandwidth monitoring...")
    
    try:
        # Initial stats for comparison
        prev_stats = psutil.net_io_counters()
        prev_sent = prev_stats.bytes_sent
        prev_recv = prev_stats.bytes_recv

        while True:
            # Wait for the specified interval
            time.sleep(interval)

            # Current stats
            current_stats = psutil.net_io_counters()
            current_sent = current_stats.bytes_sent
            current_recv = current_stats.bytes_recv

            # Calculate bandwidth usage in the interval
            sent_per_interval = current_sent - prev_sent
            recv_per_interval = current_recv - prev_recv

            # Update previous values
            prev_sent = current_sent
            prev_recv = current_recv

            # Log bandwidth usage to file
            logging.info(
                f"Bandwidth usage in last {interval} seconds: "
                f"Sent: {format_bytes(sent_per_interval)}, "
                f"Received: {format_bytes(recv_per_interval)}"
            )
            
            # Print bandwidth usage to console
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"Sent: {format_bytes(sent_per_interval)}, "
                f"Received: {format_bytes(recv_per_interval)}"
            )

    except KeyboardInterrupt:
        # Gracefully handle script termination
        logging.info("Bandwidth monitoring stopped by user.")
        print("\nMonitoring stopped. Exiting...")
    except Exception as e:
        # Handle unforeseen errors
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the bandwidth monitoring script
    monitor_bandwidth(interval=5)
```
