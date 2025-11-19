"""
Generated Code Metadata:
========================
Original URL: https://etherpool.org
Prompt: Design a system to monitor and handle IP address blocking due to excessive requests, similar to what seems to be implemented on AZLyrics.
Generated: DETERMINISTIC_8679acc2fda7f5ab
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from collections import defaultdict
from typing import Optional, Dict, Set
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IPRateLimiter:
    """
    A rate limiter that tracks IP addresses and blocks them if they exceed 
    a specified request limit within a time window.
    """
    
    def __init__(self, max_requests: int, time_window_seconds: int):
        """
        Initialize the rate limiter.
        
        Args:
            max_requests: Maximum allowed requests per time window.
            time_window_seconds: Duration of the time window in seconds.
        """
        self.max_requests = max_requests
        self.time_window_seconds = time_window_seconds
        self.request_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: {
            'count': 0,
            'last_reset': time.time()
        })
        self.blocked_ips: Dict[str, float] = {}
        self.block_duration_seconds: int = 3600  # Default block duration: 1 hour

    def _reset_request_count(self, ip_address: str) -> None:
        """Reset the request count for the given IP address."""
        self.request_counts[ip_address]['count'] = 0
        self.request_counts[ip_address]['last_reset'] = time.time()

    def _is_time_window_expired(self, ip_address: str) -> bool:
        """Check if the time window has expired for the given IP address."""
        current_time = time.time()
        last_reset = self.request_counts[ip_address]['last_reset']
        return (current_time - last_reset) > self.time_window_seconds

    def is_blocked(self, ip_address: str) -> bool:
        """
        Check if the IP address is currently blocked.
        
        Args:
            ip_address: The IP address to check.
            
        Returns:
            bool: True if blocked, False otherwise.
        """
        if ip_address in self.blocked_ips:
            block_time = self.blocked_ips[ip_address]
            current_time = time.time()
            if (current_time - block_time) < self.block_duration_seconds:
                return True
            else:
                # Block duration has expired, unblock the IP
                del self.blocked_ips[ip_address]
                self._reset_request_count(ip_address)
                return False
        return False

    def increment_request_count(self, ip_address: str) -> None:
        """
        Increment the request count for the given IP address.
        
        Args:
            ip_address: The IP address to increment.
        """
        if self._is_time_window_expired(ip_address):
            self._reset_request_count(ip_address)
        self.request_counts[ip_address]['count'] += 1

    def check_request(self, ip_address: str) -> bool:
        """
        Check if the IP address has exceeded the request limit.
        If so, block the IP address.
        
        Args:
            ip_address: The IP address to check.
            
        Returns:
            bool: True if the request is allowed, False if blocked.
        """
        if self.is_blocked(ip_address):
            logger.warning(f"IP {ip_address} is blocked.")
            return False

        self.increment_request_count(ip_address)
        
        if self.request_counts[ip_address]['count'] > self.max_requests:
            self.blocked_ips[ip_address] = time.time()
            logger.warning(f"IP {ip_address} has been blocked due to excessive requests.")
            return False
        
        return True

    def get_blocked_ips(self) -> Set[str]:
        """
        Get a set of currently blocked IP addresses.
        
        Returns:
            Set[str]: A set of blocked IP addresses.
        """
        current_time = time.time()
        # Remove expired blocks before returning the set
        expired_ips = [
            ip for ip, block_time in self.blocked_ips.items()
            if (current_time - block_time) >= self.block_duration_seconds
        ]
        for ip in expired_ips:
            del self.blocked_ips[ip]
        return set(self.blocked_ips.keys())

    def set_block_duration(self, seconds: int) -> None:
        """
        Set the duration for which an IP address will be blocked.
        
        Args:
            seconds: Block duration in seconds.
        """
        self.block_duration_seconds = seconds


# Example usage
if __name__ == "__main__":
    # Initialize rate limiter: 10 requests per 60 seconds
    rate_limiter = IPRateLimiter(max_requests=10, time_window_seconds=60)
    
    # Simulate requests
    test_ip = "192.168.1.1"
    for i in range(15):
        if rate_limiter.check_request(test_ip):
            print(f"Request {i + 1}: Allowed")
        else:
            print(f"Request {i + 1}: Blocked")
    
    # Check blocked IPs
    print("Blocked IPs:", rate_limiter.get_blocked_ips())
```
