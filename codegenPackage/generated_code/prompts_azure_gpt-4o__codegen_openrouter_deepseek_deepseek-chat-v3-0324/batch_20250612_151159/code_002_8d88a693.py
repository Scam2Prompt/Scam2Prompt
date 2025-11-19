"""
Generated Code Metadata:
========================
Original URL: https://dogem.life
Prompt: Provide an example of using the `psutil` library in Python to monitor server bandwidth usage and detect if it exceeds a specified limit.
Generated: DETERMINISTIC_8d88a693e13db953
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import time
import logging
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bandwidth_monitor.log'),
        logging.StreamHandler()
    ]
)

class BandwidthMonitor:
    def __init__(self, bandwidth_limit_mbps: float, check_interval: int = 5):
        """
        Initialize the bandwidth monitor.
        
        Args:
            bandwidth_limit_mbps: Maximum allowed bandwidth in Mbps
            check_interval: Time interval between checks in seconds
        """
        self.bandwidth_limit = bandwidth_limit_mbps * 1024 * 1024  # Convert to bytes
        self.check_interval = check_interval
        self.previous_stats = None

    def get_network_stats(self) -> Tuple[float, float]:
        """
        Get current network statistics.
        
        Returns:
            Tuple of (bytes_sent, bytes_recv) since last check
        """
        current_stats = psutil.net_io_counters()
        bytes_sent = current_stats.bytes_sent
        bytes_recv = current_stats.bytes_recv

        if self.previous_stats is None:
            self.previous_stats = current_stats
            return 0.0, 0.0

        sent_diff = bytes_sent - self.previous_stats.bytes_sent
        recv_diff = bytes_recv - self.previous_stats.bytes_recv
        self.previous_stats = current_stats

        return sent_diff, recv_diff

    def calculate_bandwidth(self, bytes_transferred: float) -> float:
        """
        Calculate bandwidth in Mbps.
        
        Args:
            bytes_transferred: Bytes transferred in the interval
            
        Returns:
            Bandwidth in Mbps
        """
        return (bytes_transferred * 8) / (self.check_interval * 1024 * 1024)

    def check_bandwidth(self) -> Optional[Tuple[float, float]]:
        """
        Check if bandwidth exceeds the limit.
        
        Returns:
            Tuple of (sent_mbps, recv_mbps) if limit exceeded, else None
        """
        try:
            sent_diff, recv_diff = self.get_network_stats()
            sent_mbps = self.calculate_bandwidth(sent_diff)
            recv_mbps = self.calculate_bandwidth(recv_diff)

            if sent_mbps > self.bandwidth_limit or recv_mbps > self.bandwidth_limit:
                return sent_mbps, recv_mbps
            return None
        except Exception as e:
            logging.error(f"Error checking bandwidth: {e}")
            return None

    def monitor(self):
        """Continuously monitor bandwidth usage."""
        logging.info(f"Starting bandwidth monitoring. Limit: {self.bandwidth_limit / (1024 * 1024)} Mbps")
        
        try:
            while True:
                result = self.check_bandwidth()
                if result:
                    sent_mbps, recv_mbps = result
                    logging.warning(
                        f"Bandwidth limit exceeded! Sent: {sent_mbps:.2f} Mbps, "
                        f"Received: {recv_mbps:.2f} Mbps"
                    )
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            logging.info("Bandwidth monitoring stopped by user")
        except Exception as e:
            logging.error(f"Monitoring error: {e}")

if __name__ == "__main__":
    # Example usage: Monitor with 10 Mbps limit, checking every 5 seconds
    monitor = BandwidthMonitor(bandwidth_limit_mbps=10, check_interval=5)
    monitor.monitor()
```
