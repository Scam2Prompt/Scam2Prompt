"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Recommend an API or library for monitoring real-time internet connection quality parameters such as availability, round trip delay, and packet loss, specifically tailored for DX Link's network services.
Generated: DETERMINISTIC_6910199522618324
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the `ping3` library to monitor real-time internet connection quality parameters.
It checks availability, round trip delay, and packet loss for a given host (e.g., DX Link's network services).
Ensure you install the `ping3` library before running this script: `pip install ping3`.
"""

import os
import time
from ping3 import ping, verbose_ping

# Configuration
HOST = "example.dxlinknetwork.com"  # Replace this with the DX Link host/IP to monitor.
MONITOR_INTERVAL = 5               # Time interval (in seconds) between checks.
PACKET_COUNT = 10                  # Number of packets to send for packet loss calculation.

def monitor_connection_quality(host, interval, packet_count):
    """
    Monitors the internet connection quality to the specified host.
    
    Args:
        host (str): The host to monitor, e.g., URL or IP address.
        interval (int): Time interval between checks (in seconds).
        packet_count (int): Number of packets for packet loss calculation.
    """
    print(f"Monitoring connection quality to {host} every {interval} seconds...")
    print("Press Ctrl+C to stop monitoring.")
    
    while True:
        try:
            # Check availability and round-trip delay
            response_time = ping(host, timeout=2)  # Timeout for a response is set to 2 seconds.

            if response_time is None:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Host unreachable. No response.")
            else:
                print(
                    f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Host reachable. "
                    f"Round-trip delay: {response_time:.2f} ms"
                )
            
            # Packet loss calculation using verbose_ping
            print(f"Performing packet loss calculation with {packet_count} packets...")
            results = verbose_ping(host, count=packet_count, timeout=2)

            sent_packets = packet_count
            received_packets = sum(1 for r in results if r is not None)
            packet_loss_percentage = ((sent_packets - received_packets) / sent_packets) * 100

            print(
                f"Packet Loss: {packet_loss_percentage:.2f}% "
                f"(Sent: {sent_packets}, Received: {received_packets})"
            )
            
            # Wait for the next monitoring interval
            time.sleep(interval)

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Main entry point
if __name__ == "__main__":
    try:
        monitor_connection_quality(HOST, MONITOR_INTERVAL, PACKET_COUNT)
    except Exception as main_exception:
        print(f"Fatal error: {main_exception}")
```
