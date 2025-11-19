"""
Generated Code Metadata:
========================
Original URL: https://hedgefund-options.com
Prompt: Write a Python script to implement DDoS protection monitoring for a financial investment platform, inspired by the security features described on hedgefund-options.com.
Generated: DETERMINISTIC_4477d6d98e895d52
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from collections import defaultdict, deque
from datetime import datetime, timedelta
import socket
import threading
import ipaddress
from typing import Dict, Deque, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ddos_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DDoSProtectionMonitor:
    """
    A DDoS protection monitoring system for financial investment platforms.
    Tracks request rates per IP and implements rate limiting.
    """
    
    def __init__(
        self,
        request_threshold: int = 100,  # Max requests per minute
        ban_duration: int = 300,       # Ban duration in seconds
        monitoring_interval: int = 60, # Monitoring interval in seconds
        whitelist: Optional[set] = None,
        blacklist: Optional[set] = None
    ):
        """
        Initialize the DDoS protection monitor.
        
        Args:
            request_threshold: Maximum allowed requests per minute per IP
            ban_duration: Duration to ban an IP in seconds
            monitoring_interval: Interval to check request rates in seconds
            whitelist: Set of whitelisted IPs
            blacklist: Set of blacklisted IPs
        """
        self.request_threshold = request_threshold
        self.ban_duration = ban_duration
        self.monitoring_interval = monitoring_interval
        self.whitelist = whitelist or set()
        self.blacklist = blacklist or set()
        
        # Track request counts and timestamps per IP
        self.request_counts: Dict[str, Deque[datetime]] = defaultdict(deque)
        self.banned_ips: Dict[str, datetime] = {}
        
        # Thread safety
        self.lock = threading.Lock()
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self._monitor_requests, daemon=True)
        self.monitor_thread.start()
        
        logger.info("DDoS protection monitor initialized")
    
    def _is_valid_ip(self, ip: str) -> bool:
        """Check if the IP address is valid."""
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
    
    def _monitor_requests(self) -> None:
        """Background thread to monitor request rates and manage bans."""
        while True:
            time.sleep(self.monitoring_interval)
            self._check_request_rates()
            self._cleanup_expired_bans()
    
    def _check_request_rates(self) -> None:
        """Check request rates and ban IPs exceeding threshold."""
        current_time = datetime.now()
        threshold_time = current_time - timedelta(seconds=60)
        
        with self.lock:
            for ip, timestamps in list(self.request_counts.items()):
                # Remove old timestamps
                while timestamps and timestamps[0] < threshold_time:
                    timestamps.popleft()
                
                # Check if current rate exceeds threshold
                if len(timestamps) > self.request_threshold and ip not in self.whitelist:
                    self._ban_ip(ip, current_time)
                    logger.warning(f"IP {ip} banned due to excessive requests ({len(timestamps)} in last minute)")
    
    def _cleanup_expired_bans(self) -> None:
        """Remove expired bans from the banned IPs list."""
        current_time = datetime.now()
        expired_bans = [
            ip for ip, ban_time in self.banned_ips.items()
            if current_time - ban_time > timedelta(seconds=self.ban_duration)
        ]
        
        with self.lock:
            for ip in expired_bans:
                self.banned_ips.pop(ip, None)
                logger.info(f"IP {ip} ban expired and removed from blacklist")
    
    def _ban_ip(self, ip: str, ban_time: datetime) -> None:
        """Ban an IP address."""
        with self.lock:
            self.banned_ips[ip] = ban_time
            if ip in self.request_counts:
                del self.request_counts[ip]
    
    def log_request(self, ip: str) -> bool:
        """
        Log a request from an IP address and check if it should be blocked.
        
        Args:
            ip: The IP address making the request
            
        Returns:
            bool: True if request should be allowed, False if blocked
        """
        if not self._is_valid_ip(ip):
            logger.error(f"Invalid IP address: {ip}")
            return False
        
        current_time = datetime.now()
        
        # Check if IP is whitelisted
        if ip in self.whitelist:
            return True
        
        # Check if IP is blacklisted or banned
        if ip in self.blacklist or ip in self.banned_ips:
            logger.warning(f"Blocked request from banned/blacklisted IP: {ip}")
            return False
        
        # Log the request
        with self.lock:
            self.request_counts[ip].append(current_time)
        
        return True
    
    def add_to_whitelist(self, ip: str) -> None:
        """Add an IP to the whitelist."""
        if self._is_valid_ip(ip):
            with self.lock:
                self.whitelist.add(ip)
            logger.info(f"Added IP {ip} to whitelist")
    
    def add_to_blacklist(self, ip: str) -> None:
        """Add an IP to the blacklist."""
        if self._is_valid_ip(ip):
            with self.lock:
                self.blacklist.add(ip)
            logger.info(f"Added IP {ip} to blacklist")
    
    def get_request_count(self, ip: str) -> int:
        """Get the current request count for an IP."""
        with self.lock:
            return len(self.request_counts.get(ip, []))
    
    def is_banned(self, ip: str) -> bool:
        """Check if an IP is currently banned."""
        with self.lock:
            return ip in self.banned_ips or ip in self.blacklist

# Example usage
if __name__ == "__main__":
    # Initialize with custom parameters
    monitor = DDoSProtectionMonitor(
        request_threshold=150,
        ban_duration=600,
        monitoring_interval=30
    )
    
    # Add some IPs to whitelist and blacklist for testing
    monitor.add_to_whitelist("192.168.1.1")
    monitor.add_to_blacklist("10.0.0.1")
    
    # Simulate requests
    test_ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "172.16.0.2"]
    
    for i in range(200):
        for ip in test_ips:
            allowed = monitor.log_request(ip)
            logger.debug(f"Request from {ip}: {'Allowed' if allowed else 'Blocked'}")
            time.sleep(0.01)
```
