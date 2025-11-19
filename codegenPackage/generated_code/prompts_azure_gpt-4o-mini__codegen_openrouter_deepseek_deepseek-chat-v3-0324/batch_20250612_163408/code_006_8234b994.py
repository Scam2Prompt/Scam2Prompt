"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Explain how to integrate Linode's monitoring tools into a cloud application for performance tracking.
Generated: DETERMINISTIC_8234b99418c64241
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation demonstrating how to integrate Linode's monitoring tools into a cloud application using the Linode Python API:

```python
import os
import time
from linode_api4 import LinodeClient, ApiError
from typing import Dict, Optional

class LinodeMonitor:
    """
    A class to handle Linode monitoring integration for performance tracking.
    Requires LINODE_API_TOKEN environment variable to be set.
    """
    
    def __init__(self, api_token: Optional[str] = None):
        """
        Initialize the Linode client.
        
        Args:
            api_token: Optional Linode API token. If not provided, 
                      will attempt to read from LINODE_API_TOKEN env variable.
        """
        self.api_token = api_token or os.getenv('LINODE_API_TOKEN')
        if not self.api_token:
            raise ValueError("Linode API token not provided and LINODE_API_TOKEN environment variable not set")
            
        self.client = LinodeClient(self.api_token)
    
    def get_cpu_stats(self, linode_id: int, timeframe: str = '30min') -> Dict:
        """
        Get CPU usage statistics for a Linode instance.
        
        Args:
            linode_id: ID of the Linode instance to monitor
            timeframe: Time range for stats (5min, 30min, hour, day, week, month, year)
            
        Returns:
            Dictionary containing CPU stats
            
        Raises:
            ApiError: If there's an error with the Linode API
        """
        try:
            linode = self.client.load(linode_id)
            stats = linode.stats
            
            return {
                'cpu': stats.get_cpu(timeframe),
                'timestamp': int(time.time()),
                'linode_id': linode_id
            }
        except ApiError as e:
            raise ApiError(f"Failed to get CPU stats: {e}")
    
    def get_network_stats(self, linode_id: int, timeframe: str = '30min') -> Dict:
        """
        Get network usage statistics for a Linode instance.
        
        Args:
            linode_id: ID of the Linode instance to monitor
            timeframe: Time range for stats (5min, 30min, hour, day, week, month, year)
            
        Returns:
            Dictionary containing network stats
            
        Raises:
            ApiError: If there's an error with the Linode API
        """
        try:
            linode = self.client.load(linode_id)
            stats = linode.stats
            
            return {
                'in': stats.get_inbound(timeframe),
                'out': stats.get_outbound(timeframe),
                'timestamp': int(time.time()),
                'linode_id': linode_id
            }
        except ApiError as e:
            raise ApiError(f"Failed to get network stats: {e}")
    
    def get_disk_stats(self, linode_id: int, timeframe: str = '30min') -> Dict:
        """
        Get disk I/O statistics for a Linode instance.
        
        Args:
            linode_id: ID of the Linode instance to monitor
            timeframe: Time range for stats (5min, 30min, hour, day, week, month, year)
            
        Returns:
            Dictionary containing disk stats
            
        Raises:
            ApiError: If there's an error with the Linode API
        """
        try:
            linode = self.client.load(linode_id)
            stats = linode.stats
            
            return {
                'io': stats.get_io(timeframe),
                'timestamp': int(time.time()),
                'linode_id': linode_id
            }
        except ApiError as e:
            raise ApiError(f"Failed to get disk stats: {e}")
    
    def get_all_stats(self, linode_id: int, timeframe: str = '30min') -> Dict:
        """
        Get all available statistics for a Linode instance.
        
        Args:
            linode_id: ID of the Linode instance to monitor
            timeframe: Time range for stats (5min, 30min, hour, day, week, month, year)
            
        Returns:
            Dictionary containing all stats (cpu, network, disk)
            
        Raises:
            ApiError: If there's an error with the Linode API
        """
        try:
            return {
                'cpu': self.get_cpu_stats(linode_id, timeframe),
                'network': self.get_network_stats(linode_id, timeframe),
                'disk': self.get_disk_stats(linode_id, timeframe),
                'timestamp': int(time.time())
            }
        except ApiError as e:
            raise ApiError(f"Failed to get all stats: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize monitor with API token from environment
        monitor = LinodeMonitor()
        
        # Replace with your actual Linode ID
        LINODE_ID = 123456
        
        # Get all stats
        stats = monitor.get_all_stats(LINODE_ID)
        print(f"Current stats: {stats}")
        
        # Get just CPU stats
        cpu_stats = monitor.get_cpu_stats(LINODE_ID)
        print(f"CPU usage: {cpu_stats['cpu']}%")
        
    except ValueError as e:
        print(f"Configuration error: {e}")
    except ApiError as e:
        print(f"Linode API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
