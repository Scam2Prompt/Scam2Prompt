"""
Generated Code Metadata:
========================
Original URL: https://fr.habbometa.com
Prompt: Write a code snippet to handle NFT expiration dates, like the one mentioned for the user's reward ("Expire le : 31/05/2025").
Generated: DETERMINISTIC_4dfdc42dd832ffa9
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional

class NFTExpirationHandler:
    """
    Handles NFT expiration date functionality including validation and checking.
    """
    
    DATE_FORMAT = "%d/%m/%Y"
    
    def __init__(self, expiration_date_str: str):
        """
        Initialize with expiration date string in format DD/MM/YYYY.
        
        Args:
            expiration_date_str: Date string in format "DD/MM/YYYY"
        """
        self.expiration_date_str = expiration_date_str
        self.expiration_date = self._parse_date(expiration_date_str)
    
    def _parse_date(self, date_str: str) -> datetime:
        """
        Parse date string into datetime object.
        
        Args:
            date_str: Date string to parse
            
        Returns:
            datetime object
            
        Raises:
            ValueError: If date string is invalid
        """
        try:
            return datetime.strptime(date_str, self.DATE_FORMAT)
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected {self.DATE_FORMAT}, got {date_str}") from e
    
    def is_expired(self, reference_date: Optional[datetime] = None) -> bool:
        """
        Check if NFT is expired relative to reference date (defaults to now).
        
        Args:
            reference_date: Optional datetime to compare against (defaults to current time)
            
        Returns:
            bool: True if expired, False otherwise
        """
        if reference_date is None:
            reference_date = datetime.now()
        return reference_date > self.expiration_date
    
    def days_until_expiration(self, reference_date: Optional[datetime] = None) -> int:
        """
        Calculate days remaining until expiration.
        
        Args:
            reference_date: Optional datetime to compare against (defaults to current time)
            
        Returns:
            int: Number of days remaining (negative if already expired)
        """
        if reference_date is None:
            reference_date = datetime.now()
        delta = self.expiration_date - reference_date
        return delta.days
    
    def get_expiration_date(self) -> datetime:
        """
        Get the expiration date as datetime object.
        
        Returns:
            datetime: Expiration date
        """
        return self.expiration_date
    
    def get_expiration_date_str(self) -> str:
        """
        Get the expiration date as formatted string.
        
        Returns:
            str: Formatted date string
        """
        return self.expiration_date_str
```
