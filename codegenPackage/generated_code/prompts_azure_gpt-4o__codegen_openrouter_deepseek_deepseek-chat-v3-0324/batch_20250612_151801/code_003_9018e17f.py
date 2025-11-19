"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Create an algorithm to calculate withdrawal eligibility based on the "to 5x bebas ip" rule described in the slot bonus system.
Generated: DETERMINISTIC_9018e17fcfb58bfa
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_withdrawal_eligibility(total_deposit, total_bonus, total_wagered, wagering_requirement=5):
    """
    Calculate withdrawal eligibility based on the "5x bebas ip" rule.
    
    The rule states that the total wagered amount must be at least 5 times the total bonus received
    before withdrawal is allowed. The eligible amount is the total deposit plus any bonus that has
    met the wagering requirement.
    
    Args:
        total_deposit (float): Total amount deposited by the player
        total_bonus (float): Total bonus amount received by the player
        total_wagered (float): Total amount wagered by the player
        wagering_requirement (int, optional): Wagering requirement multiplier. Defaults to 5.
    
    Returns:
        dict: {
            'eligible': bool,          # Whether withdrawal is allowed
            'eligible_amount': float,  # Amount available for withdrawal
            'remaining_wagering': float # Remaining amount to wager to meet requirement
        }
    """
    try:
        # Validate input types
        if not all(isinstance(x, (int, float)) for x in [total_deposit, total_bonus, total_wagered]):
            raise ValueError("All amount values must be numeric")
        
        # Validate positive values
        if any(x < 0 for x in [total_deposit, total_bonus, total_wagered]):
            raise ValueError("Amounts cannot be negative")
        
        required_wagering = total_bonus * wagering_requirement
        remaining_wagering = max(0, required_wagering - total_wagered)
        
        if remaining_wagering <= 0:
            # Full bonus is eligible
            eligible_amount = total_deposit + total_bonus
            eligible = True
        else:
            # No bonus is eligible yet
            eligible_amount = total_deposit
            eligible = False
        
        return {
            'eligible': eligible,
            'eligible_amount': eligible_amount,
            'remaining_wagering': remaining_wagering
        }
    
    except Exception as e:
        # Log the error in production (would be replaced with actual logging)
        print(f"Error calculating withdrawal eligibility: {str(e)}")
        return {
            'eligible': False,
            'eligible_amount': 0,
            'remaining_wagering': 0
        }
```
