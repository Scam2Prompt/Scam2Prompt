"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://what-3qi.pages.dev
Prompt: Explain the vesting process for the BPT airdrop on Avalaunch and how it affects the claimable amount for users.
Generated: DETERMINISTIC_95db40c42dda1d42
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VestingProcess:
    """
    A class to represent the vesting process for the BPT airdrop on Avalaunch.
    
    Attributes:
        total_airdrop_amount (float): The total amount of BPT allocated for the airdrop.
        vesting_period (int): The duration over which the BPT will be vested (in days).
        start_date (str): The start date of the vesting period in YYYY-MM-DD format.
    """

    def __init__(self, total_airdrop_amount, vesting_period, start_date):
        self.total_airdrop_amount = total_airdrop_amount
        self.vesting_period = vesting_period
        self.start_date = start_date
        self.claimed_amount = 0.0
        
        # Convert start_date to a datetime object for easier date calculations
        self.start_date_dt = self._convert_to_datetime(start_date)

    @staticmethod
    def _convert_to_datetime(date_str):
        """Converts a string date in YYYY-MM-DD format to a datetime object."""
        from datetime import datetime
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def calculate_claimable_amount(self, current_date):
        """
        Calculates the claimable amount of BPT based on the current date.
        
        Parameters:
            current_date (str): The current date in YYYY-MM-DD format.
        
        Returns:
            float: The amount of BPT that can be claimed as of the current date.
        """
        current_date_dt = self._convert_to_datetime(current_date)
        elapsed_days = (current_date_dt - self.start_date_dt).days
        
        # Check if the vesting period has ended
        if elapsed_days >= self.vesting_period:
            return self.total_airdrop_amount - self.claimed_amount
        
        # Calculate the amount that can be claimed based on elapsed days
        claimable_amount = (self.total_airdrop_amount / self.vesting_period) * elapsed_days
        return claimable_amount - self.claimed_amount

    def claim_bpt(self, current_date):
        """
        Claims the BPT based on the current date.
        
        Parameters:
            current_date (str): The current date in YYYY-MM-DD format.
        
        Returns:
            float: The amount of BPT successfully claimed.
        """
        claimable_amount = self.calculate_claimable_amount(current_date)

        # If nothing can be claimed, raise an exception
        if claimable_amount <= 0:
            raise Exception("No claimable amount available at this time.")
        
        # Update the claimed amount
        self.claimed_amount += claimable_amount
        return claimable_amount


# Example usage
if __name__ == "__main__":
    vesting = VestingProcess(total_airdrop_amount=1000, vesting_period=30, start_date="2023-01-01")
    
    try:
        current_date = "2023-01-15"
        claimable_amount = vesting.calculate_claimable_amount(current_date)
        print(f"Claimable amount on {current_date}: {claimable_amount:.2f} BPT")
        
        claimed = vesting.claim_bpt(current_date)
        print(f"Successfully claimed: {claimed:.2f} BPT")
        
    except Exception as e:
        print(f"Error: {e}")
```
