"""
Generated Code Metadata:
========================
Original URL: https://stargate-dwg.pages.dev
Prompt: What are the benefits of locking STG tokens on Stargate, and how does it relate to governance voting power via veSTG?
Generated: DETERMINISTIC_6de4471549c1f1a6
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the request is about explaining concepts rather than generating executable code, I'll provide a Python class that demonstrates the relationship between STG token locking and veSTG governance power with appropriate documentation:

```python
class StargateGovernance:
    """
    A class to demonstrate the relationship between STG token locking and veSTG governance power.
    """
    
    def __init__(self):
        """
        Initialize the governance system with default parameters.
        """
        self.max_lock_duration = 4 * 365 * 24 * 60 * 60  # 4 years in seconds
        self.min_lock_duration = 7 * 24 * 60 * 60  # 1 week in seconds
    
    def calculate_vestg_power(self, stg_amount: float, lock_duration: int) -> float:
        """
        Calculate veSTG voting power based on STG amount and lock duration.
        
        Args:
            stg_amount: Amount of STG tokens to lock
            lock_duration: Duration to lock tokens in seconds
            
        Returns:
            float: veSTG voting power
            
        Raises:
            ValueError: If lock duration is outside valid range
        """
        if lock_duration < self.min_lock_duration:
            raise ValueError("Lock duration must be at least 1 week")
        if lock_duration > self.max_lock_duration:
            raise ValueError("Lock duration cannot exceed 4 years")
            
        # Voting power is proportional to amount and linear with time
        time_factor = lock_duration / self.max_lock_duration
        return stg_amount * time_factor
    
    def get_benefits(self, stg_amount: float, lock_duration: int) -> dict:
        """
        Get the benefits of locking STG tokens.
        
        Args:
            stg_amount: Amount of STG tokens to lock
            lock_duration: Duration to lock tokens in seconds
            
        Returns:
            dict: Dictionary containing various benefits
        """
        try:
            vestg_power = self.calculate_vestg_power(stg_amount, lock_duration)
            
            return {
                'voting_power': vestg_power,
                'fee_sharing': True,
                'protocol_rewards': True,
                'boosted_yield': True,
                'lock_duration': lock_duration,
                'stg_amount': stg_amount
            }
        except ValueError as e:
            return {
                'error': str(e),
                'valid_min_duration': self.min_lock_duration,
                'valid_max_duration': self.max_lock_duration
            }
```
