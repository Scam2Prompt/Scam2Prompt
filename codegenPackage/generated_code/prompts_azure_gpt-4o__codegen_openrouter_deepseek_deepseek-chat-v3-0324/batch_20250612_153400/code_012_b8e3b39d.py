"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Create a Python script to calculate unstake periods and track the 10-day lock-in for unstaked EGLD tokens on MultiversX.
Generated: DETERMINISTIC_b8e3b39d647a8a48
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class UnstakeTracker:
    """
    A class to track unstaked EGLD tokens and their 10-day lock-in periods on MultiversX.
    """
    
    def __init__(self):
        """
        Initialize the tracker with an empty dictionary to store unstake records.
        """
        self.unstake_records: Dict[str, List[Dict[str, datetime.datetime]]] = {}
    
    def add_unstake(self, address: str, amount: float, unstake_time: Optional[datetime.datetime] = None) -> None:
        """
        Record an unstake event for a given address.
        
        Args:
            address: The wallet address performing the unstake
            amount: The amount of EGLD being unstaked
            unstake_time: Optional timestamp of unstake (defaults to current time)
        """
        if unstake_time is None:
            unstake_time = datetime.datetime.now()
        
        if address not in self.unstake_records:
            self.unstake_records[address] = []
            
        self.unstake_records[address].append({
            'amount': amount,
            'unstake_time': unstake_time,
            'lock_end_time': unstake_time + datetime.timedelta(days=10)
        })
    
    def get_active_unstakes(self, address: str, current_time: Optional[datetime.datetime] = None) -> List[Dict[str, datetime.datetime]]:
        """
        Get all active unstakes (still in 10-day lock period) for an address.
        
        Args:
            address: The wallet address to query
            current_time: Optional timestamp to use as reference (defaults to now)
            
        Returns:
            List of active unstake records for the address
        """
        if current_time is None:
            current_time = datetime.datetime.now()
            
        if address not in self.unstake_records:
            return []
            
        return [record for record in self.unstake_records[address] 
                if record['lock_end_time'] > current_time]
    
    def get_available_unstakes(self, address: str, current_time: Optional[datetime.datetime] = None) -> List[Dict[str, datetime.datetime]]:
        """
        Get all unstakes that have completed the 10-day lock period.
        
        Args:
            address: The wallet address to query
            current_time: Optional timestamp to use as reference (defaults to now)
            
        Returns:
            List of available unstake records for the address
        """
        if current_time is None:
            current_time = datetime.datetime.now()
            
        if address not in self.unstake_records:
            return []
            
        return [record for record in self.unstake_records[address] 
                if record['lock_end_time'] <= current_time]
    
    def get_total_locked(self, address: str, current_time: Optional[datetime.datetime] = None) -> float:
        """
        Calculate the total amount of EGLD still locked for an address.
        
        Args:
            address: The wallet address to query
            current_time: Optional timestamp to use as reference (defaults to now)
            
        Returns:
            Total amount of EGLD still in lock period
        """
        active_unstakes = self.get_active_unstakes(address, current_time)
        return sum(record['amount'] for record in active_unstakes)
    
    def get_total_available(self, address: str, current_time: Optional[datetime.datetime] = None) -> float:
        """
        Calculate the total amount of EGLD available to claim for an address.
        
        Args:
            address: The wallet address to query
            current_time: Optional timestamp to use as reference (defaults to now)
            
        Returns:
            Total amount of EGLD available to claim
        """
        available_unstakes = self.get_available_unstakes(address, current_time)
        return sum(record['amount'] for record in available_unstakes)
    
    def clear_available_unstakes(self, address: str, current_time: Optional[datetime.datetime] = None) -> None:
        """
        Remove all available (completed lock period) unstakes from records.
        
        Args:
            address: The wallet address to clear
            current_time: Optional timestamp to use as reference (defaults to now)
        """
        if current_time is None:
            current_time = datetime.datetime.now()
            
        if address in self.unstake_records:
            self.unstake_records[address] = self.get_active_unstakes(address, current_time)
    
    def get_time_until_available(self, address: str, current_time: Optional[datetime.datetime] = None) -> Optional[datetime.timedelta]:
        """
        Get the time remaining until the next unstake becomes available.
        
        Args:
            address: The wallet address to query
            current_time: Optional timestamp to use as reference (defaults to now)
            
        Returns:
            Time remaining until next unstake is available, or None if no active unstakes
        """
        if current_time is None:
            current_time = datetime.datetime.now()
            
        active_unstakes = self.get_active_unstakes(address, current_time)
        if not active_unstakes:
            return None
            
        next_available = min(record['lock_end_time'] for record in active_unstakes)
        return next_available - current_time
```
