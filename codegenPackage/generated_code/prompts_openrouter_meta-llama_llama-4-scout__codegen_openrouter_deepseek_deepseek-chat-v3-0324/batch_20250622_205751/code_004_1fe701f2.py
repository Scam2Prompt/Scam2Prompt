"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Develop a function to determine if a user is eligible for holding rewards based on their $BANANA token balance and the 4-hour holding period requirement.
Generated: DETERMINISTIC_1fe701f24c494e2d
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, Optional

class BananaTokenRewardEligibility:
    """
    Determines if a user is eligible for rewards based on their $BANANA token balance
    and holding period requirements.
    """
    
    def __init__(self, min_balance: float = 100.0, holding_period_hours: float = 4.0):
        """
        Initialize with minimum balance and holding period requirements.
        
        Args:
            min_balance: Minimum $BANANA token balance required (default: 100.0)
            holding_period_hours: Required holding period in hours (default: 4.0)
        """
        self.min_balance = min_balance
        self.holding_period_seconds = holding_period_hours * 3600
        
    def check_eligibility(
        self,
        user_balance: float,
        first_balance_timestamp: float,
        current_timestamp: Optional[float] = None
    ) -> Dict[str, bool]:
        """
        Check if user meets both balance and holding period requirements.
        
        Args:
            user_balance: Current $BANANA token balance of the user
            first_balance_timestamp: Timestamp when user first had sufficient balance
            current_timestamp: Optional current timestamp (defaults to time.time())
            
        Returns:
            Dictionary with eligibility status and details:
            {
                'eligible': bool,
                'has_min_balance': bool,
                'meets_holding_period': bool
            }
        """
        if current_timestamp is None:
            current_timestamp = time.time()
            
        result = {
            'eligible': False,
            'has_min_balance': False,
            'meets_holding_period': False
        }
        
        # Check minimum balance requirement
        if user_balance >= self.min_balance:
            result['has_min_balance'] = True
            
            # Check holding period requirement
            holding_time = current_timestamp - first_balance_timestamp
            if holding_time >= self.holding_period_seconds:
                result['meets_holding_period'] = True
                result['eligible'] = True
                
        return result
```
