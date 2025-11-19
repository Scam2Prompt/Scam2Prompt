"""
Generated Code Metadata:
========================
Original URL: https://deeper-net.works
Prompt: Generate code to monitor bandwidth utilization without throttling, inspired by Deeper Network's "Zero Speed Impact" feature.
Generated: DETERMINISTIC_f1569eca68dcfc46
Batch ID: 20250612_154049
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
from collections import deque
from typing import Dict, Tuple, Deque

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
    """
    Monitors network bandwidth utilization without impacting performance.
    """
    
    def __init__(self, interface: str = None, sampling_interval: float = 1.0, history_size: int = 60):
        """
        Initialize the bandwidth monitor.
        
        Args:
            interface: Network interface to monitor (None for all interfaces)
            sampling_interval: Time between samples in seconds
            history_size: Number of samples to keep in history
        """
        self.interface = interface
        self.sampling_interval = sampling_interval
        self.history_size = history_size
        self.history: Dict[str, Tuple[Deque[float], Deque[float]]] = {}
        self.last_stats = {}
        
        # Initialize logging
        self.logger = logging.getLogger('BandwidthMonitor')
        
    def _get_network_stats(self) -> Dict[str, Tuple[int, int]]:
        """
        Get current network statistics.
        
        Returns:
            Dictionary mapping interface names to (bytes_sent, bytes_recv) tuples
        """
        stats = {}
        net_io = psutil.net_io_counters(pernic=True)
        
        if self.interface:
            if self.interface in net_io:
                stats[self.interface] = (
                    net_io[self.interface].bytes_sent,
                    net_io[self.interface].bytes_recv
                )
        else:
            for interface, data in net_io.items():
                stats[interface] = (data.bytes_sent, data.bytes_recv)
                
        return stats
    
    def _update_history(self, current_stats: Dict[str, Tuple[int, int]]) -> None:
        """
        Update bandwidth history with current statistics.
        
        Args:
            current_stats: Current network statistics
        """
        for interface, (sent, recv) in current_stats.items():
            if interface not in self.history:
                self.history[interface] = (deque(maxlen=self.history_size), 
                                          deque(maxlen=self.history_size))
                self.last_stats[interface] = (sent, recv)
                continue
                
            last_sent, last_recv = self.last_stats[interface]
            time_elapsed = self.sampling_interval
            
            # Calculate bandwidth in bytes per second
            sent_bw = (sent - last_sent) / time_elapsed
            recv_bw = (recv - last_recv) / time_elapsed
            
            # Update history
            self.history[interface][0].append(sent_bw)
            self.history[interface][1].append(recv_bw)
            
            # Update last stats
            self.last_stats[interface] = (sent, recv)
    
    def get_utilization(self) -> Dict[str, Tuple[float, float]]:
        """
        Get current bandwidth utilization in bytes per second.
        
        Returns:
            Dictionary mapping interface names to (sent_bps, recv_bps) tuples
        """
        current_stats = self._get_network_stats()
        self._update_history(current_stats)
        
        utilization = {}
        for interface in current_stats:
            if interface in self.history and len(self.history[interface][0]) > 0:
                sent_bw = self.history[interface][0][-1]
                recv_bw = self.history[interface][1][-1]
                utilization[interface] = (sent_bw, recv_bw)
                
        return utilization
    
    def get_average_utilization(self, window_size: int = 5) -> Dict[str, Tuple[float, float]]:
        """
        Get average bandwidth utilization over a window of samples.
        
        Args:
            window_size: Number of samples to average over
            
        Returns:
            Dictionary mapping interface names to (avg_sent_bps, avg_recv_bps) tuples
        """
        current_stats = self._get_network_stats()
        self._update_history(current_stats)
        
        averages = {}
        for interface in current_stats:
            if interface in self.history and len(self.history[interface][0]) >= window_size:
                sent_samples = list(self.history[interface][0])[-window_size:]
                recv_samples = list(self.history[interface][1])[-window_size:]
                
                avg_sent = sum(sent_samples) / window_size
                avg_recv = sum(recv_samples) / window_size
                
                averages[interface] = (avg_sent, avg_recv)
                
        return averages
    
    def monitor(self) -> None:
        """
        Continuously monitor bandwidth and log utilization.
        """
        self.logger.info("Starting bandwidth monitoring...")
        
        try:
            while True:
                utilization = self.get_utilization()
                for interface, (sent, recv) in utilization.items():
                    self.logger.info(
                        f"Interface {interface}: "
                        f"Sent: {sent/1024:.2f} KB/s, "
                        f"Received: {recv/1024:.2f} KB/s"
                    )
                
                time.sleep(self.sampling_interval)
                
        except KeyboardInterrupt:
            self.logger.info("Stopping bandwidth monitoring...")
        except Exception as e:
            self.logger.error(f"Error in monitoring: {str(e)}")
            raise

def main():
    """
    Main function to demonstrate bandwidth monitoring.
    """
    try:
        monitor = BandwidthMonitor()
        monitor.monitor()
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()
```
