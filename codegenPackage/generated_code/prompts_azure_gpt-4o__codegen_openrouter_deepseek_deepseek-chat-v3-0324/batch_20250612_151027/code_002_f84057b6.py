"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Provide an example of how to split payouts in a decentralized economy using Moxie’s shared payout structure (50% to earning member, 20% to community/channel, etc.).
Generated: DETERMINISTIC_f84057b657f5c5c5
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Dict
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 6

@dataclass
class PayoutRecipient:
    """Represents a recipient of a payout with their share percentage."""
    name: str
    percentage: Decimal

class PayoutSplitter:
    """
    Handles splitting payouts according to predefined distribution rules.
    Implements Moxie's shared payout structure:
    - 50% to earning member
    - 20% to community/channel
    - 15% to platform
    - 10% to referrer
    - 5% to network
    """
    
    def __init__(self):
        """Initialize with Moxie's default payout structure."""
        self.recipients = [
            PayoutRecipient(name="earning_member", percentage=Decimal('0.50')),
            PayoutRecipient(name="community_channel", percentage=Decimal('0.20')),
            PayoutRecipient(name="platform", percentage=Decimal('0.15')),
            PayoutRecipient(name="referrer", percentage=Decimal('0.10')),
            PayoutRecipient(name="network", percentage=Decimal('0.05'))
        ]
        self._validate_percentages()

    def _validate_percentages(self):
        """Ensure the payout percentages sum to 100%."""
        total = sum(recipient.percentage for recipient in self.recipients)
        if total != Decimal('1.00'):
            raise ValueError(
                f"Payout percentages must sum to 100%. Current sum: {total * 100}%"
            )

    def calculate_payouts(self, total_amount: Decimal) -> Dict[str, Decimal]:
        """
        Calculate the payout amounts for each recipient based on the total amount.
        
        Args:
            total_amount: The total amount to be distributed.
            
        Returns:
            A dictionary mapping recipient names to their payout amounts.
            
        Raises:
            ValueError: If total_amount is negative.
        """
        if total_amount < Decimal('0'):
            raise ValueError("Total amount cannot be negative")
            
        payouts = {}
        for recipient in self.recipients:
            amount = total_amount * recipient.percentage
            payouts[recipient.name] = amount.quantize(Decimal('0.000001'))
            
        return payouts

# Example usage
if __name__ == "__main__":
    splitter = PayoutSplitter()
    total = Decimal('1000.00')
    
    try:
        payouts = splitter.calculate_payouts(total)
        for recipient, amount in payouts.items():
            print(f"{recipient}: ${amount:.2f}")
    except ValueError as e:
        print(f"Error calculating payouts: {e}")
```
