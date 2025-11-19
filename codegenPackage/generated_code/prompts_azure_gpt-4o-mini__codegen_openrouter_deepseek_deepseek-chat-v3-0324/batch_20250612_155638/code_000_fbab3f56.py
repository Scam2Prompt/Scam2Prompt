"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Generate code for a network performance management tool that incorporates RF engineering principles as described on the Ultious website.
Generated: DETERMINISTIC_fbab3f5674722be4
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import time
import subprocess
import platform
import psutil
import numpy as np
from typing import Dict, Tuple, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('network_performance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class NetworkPerformanceMonitor:
    """
    A network performance management tool incorporating RF engineering principles.
    """
    
    def __init__(self, target_host: str = "8.8.8.8", ping_count: int = 4, bandwidth_test_size: int = 1024):
        """
        Initialize the network performance monitor.
        
        Args:
            target_host: Host to test connectivity against (default: Google DNS)
            ping_count: Number of pings to send for latency test
            bandwidth_test_size: Data size for bandwidth test in KB
        """
        self.target_host = target_host
        self.ping_count = ping_count
        self.bandwidth_test_size = bandwidth_test_size
        self.system_info = self._get_system_info()
        
    def _get_system_info(self) -> Dict:
        """Collect basic system information."""
        return {
            "platform": platform.system(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname())
        }
    
    def measure_latency(self) -> Tuple[Optional[float], Optional[float]]:
        """
        Measure network latency using ping.
        
        Returns:
            Tuple of (average_latency_ms, packet_loss_percentage) or (None, None) if failed
        """
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, str(self.ping_count), self.target_host]
            
            output = subprocess.check_output(command).decode('utf-8')
            
            if 'unreachable' in output.lower():
                logger.error(f"Host {self.target_host} is unreachable")
                return None, None
                
            # Parse output based on OS
            if platform.system().lower() == 'windows':
                lines = output.split('\n')
                packet_loss_line = [line for line in lines if 'packets' in line][0]
                latency_line = [line for line in lines if 'Average' in line][0]
                
                packet_loss = float(packet_loss_line.split('%')[0].split('(')[1].strip())
                avg_latency = float(latency_line.split('=')[1].split('ms')[0].strip())
            else:
                lines = output.split('\n')
                stats_line = lines[-2]
                
                packet_loss = float(stats_line.split('%')[0].split(',')[2].strip().split(' ')[0])
                avg_latency = float(stats_line.split('/')[4])
            
            return avg_latency, packet_loss
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Ping failed: {e}")
            return None, None
        except Exception as e:
            logger.error(f"Error measuring latency: {e}")
            return None, None
    
    def measure_bandwidth(self, test_duration: int = 5) -> Optional[float]:
        """
        Estimate network bandwidth by measuring data transfer over time.
        
        Args:
            test_duration: Duration of test in seconds
            
        Returns:
            Bandwidth in Mbps or None if failed
        """
        try:
            start_time = time.time()
            end_time = start_time + test_duration
            
            total_bytes = 0
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            try:
                sock.connect((self.target_host, 80))
            except:
                logger.error(f"Could not connect to {self.target_host}:80 for bandwidth test")
                return None
                
            # Send dummy data
            dummy_data = b'0' * (self.bandwidth_test_size * 1024)
            
            while time.time() < end_time:
                try:
                    sent = sock.send(dummy_data)
                    total_bytes += sent
                except socket.error:
                    break
            
            elapsed = time.time() - start_time
            if elapsed <= 0:
                return None
                
            bandwidth = (total_bytes * 8) / (elapsed * 1000000)  # Convert to Mbps
            return round(bandwidth, 2)
            
        except Exception as e:
            logger.error(f"Error measuring bandwidth: {e}")
            return None
        finally:
            sock.close()
    
    def measure_signal_strength(self) -> Optional[float]:
        """
        Measure wireless signal strength (RSSI) if available.
        
        Returns:
            Signal strength in dBm or None if not available
        """
        try:
            if platform.system().lower() == 'windows':
                command = ['netsh', 'wlan', 'show', 'interfaces']
                output = subprocess.check_output(command).decode('utf-8')
                
                for line in output.split('\n'):
                    if 'signal' in line.lower():
                        return float(line.split(':')[1].strip().replace('%', ''))
                return None
                
            elif platform.system().lower() == 'linux':
                command = ['iwconfig']
                output = subprocess.check_output(command).decode('utf-8')
                
                for line in output.split('\n'):
                    if 'link quality' in line.lower():
                        parts = line.split(' ')
                        for part in parts:
                            if 'dBm' in part:
                                return float(part.replace('dBm', ''))
                return None
                
            elif platform.system().lower() == 'darwin':
                command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I']
                output = subprocess.check_output(command).decode('utf-8')
                
                for line in output.split('\n'):
                    if 'agrctlrssi' in line.lower():
                        return float(line.split(':')[1].strip())
                return None
                
            else:
                logger.warning("Signal strength measurement not supported on this platform")
                return None
                
        except Exception as e:
            logger.error(f"Error measuring signal strength: {e}")
            return None
    
    def measure_network_utilization(self) -> Dict[str, float]:
        """
        Measure current network utilization.
        
        Returns:
            Dictionary with upload and download speeds in Mbps
        """
        try:
            net_io = psutil.net_io_counters()
            start_bytes_sent = net_io.bytes_sent
            start_bytes_recv = net_io.bytes_recv
            
            time.sleep(1)  # Wait 1 second
            
            net_io = psutil.net_io_counters()
            end_bytes_sent = net_io.bytes_sent
            end_bytes_recv = net_io.bytes_recv
            
            upload_speed = (end_bytes_sent - start_bytes_sent) * 8 / 1000000  # Convert to Mbps
            download_speed = (end_bytes_recv - start_bytes_recv) * 8 / 1000000  # Convert to Mbps
            
            return {
                "upload_speed": round(upload_speed, 2),
                "download_speed": round(download_speed, 2)
            }
            
        except Exception as e:
            logger.error(f"Error measuring network utilization: {e}")
            return {"upload_speed": 0.0, "download_speed": 0.0}
    
    def calculate_path_loss(self, distance_km: float, frequency_mhz: float) -> float:
        """
        Calculate free space path loss using RF engineering principles.
        
        Args:
            distance_km: Distance between transmitter and receiver in kilometers
            frequency_mhz: Frequency in MHz
            
        Returns:
            Path loss in dB
        """
        try:
            # Free space path loss formula: 20log10(d) + 20log10(f) + 32.45
            # where d is in km and f is in MHz
            path_loss = 20 * np.log10(distance_km) + 20 * np.log10(frequency_mhz) + 32.45
            return round(path_loss, 2)
        except Exception as e:
            logger.error(f"Error calculating path loss: {e}")
            return 0.0
    
    def run_comprehensive_test(self) -> Dict:
        """
        Run all available tests and return comprehensive results.
        
        Returns:
            Dictionary containing all test results
        """
        timestamp = datetime.now().isoformat()
        
        latency, packet_loss = self.measure_latency()
        bandwidth = self.measure_bandwidth()
        signal_strength = self.measure_signal_strength()
        network_util = self.measure_network_utilization()
        
        return {
            "timestamp":
