"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethal222.rf.gd
Prompt: Generate code to monitor bandwidth usage on a hosting service that claims unlimited bandwidth and no daily process limits, such as iFastNet.
Generated: DETERMINISTIC_263063e498ed611d
Batch ID: 20250612_154400
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

# Configure logging to monitor bandwidth usage
logging.basicConfig(
    filename='bandwidth_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def monitor_bandwidth(interval=5):
    """
    Monitor bandwidth usage and log the upload/download speeds.
    
    Args:
        interval (int): The time interval in seconds to check bandwidth usage.
    """
    try:
        # Initial snapshot of network statistics
        initial_stats = psutil.net_io_counters()
        prev_bytes_sent = initial_stats.bytes_sent
        prev_bytes_recv = initial_stats.bytes_recv

        logging.info("Starting bandwidth monitor.")

        while True:
            time.sleep(interval)
            
            # Capture current network statistics
            current_stats = psutil.net_io_counters()
            current_bytes_sent = current_stats.bytes_sent
            current_bytes_recv = current_stats.bytes_recv
            
            # Calculate bandwidth usage
            bytes_sent_delta = current_bytes_sent - prev_bytes_sent
            bytes_recv_delta = current_bytes_recv - prev_bytes_recv
            
            # Update previous stats for the next interval
            prev_bytes_sent = current_bytes_sent
            prev_bytes_recv = current_bytes_recv
            
            # Convert bytes to kilobytes for reporting
            kb_sent = bytes_sent_delta / 1024
            kb_recv = bytes_recv_delta / 1024
            
            # Log bandwidth usage
            logging.info(f"Upload Speed: {kb_sent:.2f} KB/s, Download Speed: {kb_recv:.2f} KB/s")
    
    except KeyboardInterrupt:
        # Graceful shutdown on user interruption
        logging.info("Bandwidth monitor stopped by user.")
    except Exception as e:
        # Log unexpected errors
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    # Start monitoring bandwidth with a default interval of 5 seconds
    monitor_bandwidth(interval=5)
```
