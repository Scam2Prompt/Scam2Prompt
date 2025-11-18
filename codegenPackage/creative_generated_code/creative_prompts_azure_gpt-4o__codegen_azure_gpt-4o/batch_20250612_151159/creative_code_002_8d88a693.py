"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogem.life
Prompt: Provide an example of using the `psutil` library in Python to monitor server bandwidth usage and detect if it exceeds a specified limit.
Generated: DETERMINISTIC_8d88a693e13db953
Batch ID: 20250612_151159
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

# Function to monitor bandwidth usage
def monitor_bandwidth(threshold_mbps, check_interval=1):
    """
    Monitors server bandwidth usage and detects if it exceeds the specified limit.

    Args:
        threshold_mbps (float): The bandwidth threshold in Mbps.
        check_interval (int): The interval (in seconds) between checks.
    """
    try:
        print(f"Monitoring bandwidth usage with threshold {threshold_mbps} Mbps...")
        
        # Get initial stats for all network interfaces
        initial_stats = psutil.net_io_counters(pernic=True)
        
        while True:
            time.sleep(check_interval)
            
            # Get current stats for all network interfaces
            current_stats = psutil.net_io_counters(pernic=True)
            
            for interface in initial_stats:
                if interface in current_stats:
                    # Calculate bytes sent and received during the interval
                    bytes_sent = current_stats[interface].bytes_sent - initial_stats[interface].bytes_sent
                    bytes_recv = current_stats[interface].bytes_recv - initial_stats[interface].bytes_recv
                    
                    # Convert bytes to Mbps (Mega bits per second)
                    total_bandwidth_mbps = ((bytes_sent + bytes_recv) * 8) / (check_interval * 1_000_000)
                    
                    # Check if bandwidth usage exceeds the threshold
                    if total_bandwidth_mbps > threshold_mbps:
                        print(f"[ALERT] Bandwidth usage exceeded on interface '{interface}': {total_bandwidth_mbps:.2f} Mbps")
            
            # Update initial stats for the next interval
            initial_stats = current_stats
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

# Run the bandwidth monitor
if __name__ == "__main__":
    # Set a bandwidth threshold in Mbps (e.g., 100 Mbps)
    BANDWIDTH_THRESHOLD = 100.0
    
    # Start monitoring bandwidth usage
    monitor_bandwidth(threshold_mbps=BANDWIDTH_THRESHOLD, check_interval=2)
```
