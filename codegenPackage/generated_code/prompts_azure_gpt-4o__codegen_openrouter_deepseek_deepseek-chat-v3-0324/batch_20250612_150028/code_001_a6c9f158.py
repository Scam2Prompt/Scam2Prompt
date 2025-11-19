"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Generate code to calculate the burn mechanism for Baby Grok transactions, considering the 5% tax split into 1% LP, 2% marketing, and 2% development.
Generated: DETERMINISTIC_a6c9f1586788e4dc
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import Tuple
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

@dataclass
class BurnDistribution:
    lp: Decimal
    marketing: Decimal
    development: Decimal
    remaining: Decimal

def calculate_burn(amount: Decimal) -> BurnDistribution:
    """
    Calculate the burn distribution for a Baby Grok transaction.
    
    Args:
        amount: The transaction amount to calculate burns for
        
    Returns:
        BurnDistribution: Object containing split amounts
    """
    if amount <= Decimal('0'):
        raise ValueError("Amount must be positive")
    
    total_tax_percent = Decimal('0.05')  # 5% total tax
    lp_percent = Decimal('0.01')         # 1% to LP
    marketing_percent = Decimal('0.02')  # 2% to marketing
    dev_percent = Decimal('0.02')        # 2% to development
    
    total_tax = amount * total_tax_percent
    lp_amount = amount * lp_percent
    marketing_amount = amount * marketing_percent
    dev_amount = amount * dev_percent
    
    # Calculate remaining amount after burns
    remaining_amount = amount - total_tax
    
    return BurnDistribution(
        lp=lp_amount,
        marketing=marketing_amount,
        development=dev_amount,
        remaining=remaining_amount
    )

def format_distribution(dist: BurnDistribution) -> str:
    """
    Format the burn distribution for display.
    
    Args:
        dist: BurnDistribution object to format
        
    Returns:
        str: Formatted string showing the distribution
    """
    return (
        f"Burn Distribution:\n"
        f"LP: {dist.lp:.18f}\n"
        f"Marketing: {dist.marketing:.18f}\n"
        f"Development: {dist.development:.18f}\n"
        f"Remaining: {dist.remaining:.18f}"
    )

# Example usage
if __name__ == "__main__":
    try:
        transaction_amount = Decimal('1000.0')
        distribution = calculate_burn(transaction_amount)
        print(format_distribution(distribution))
    except ValueError as e:
        print(f"Error: {e}")
```
