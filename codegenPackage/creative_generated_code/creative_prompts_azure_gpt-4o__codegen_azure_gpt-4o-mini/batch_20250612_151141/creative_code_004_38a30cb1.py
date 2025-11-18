"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjojoexchange.pages.dev
Prompt: Write a function to calculate inviter rewards based on the 10% point-sharing rule for invitees, as specified in the JOJO activity rules.
Generated: DETERMINISTIC_38a30cb1e88d97a7
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_inviter_rewards(invitee_earnings):
    """
    Calculate the inviter rewards based on the 10% point-sharing rule.

    Args:
        invitee_earnings (list of float): A list of earnings from the invitees.
    
    Returns:
        float: Total rewards for the inviter, calculated as 10% of the total invitees' earnings.
    
    Raises:
        ValueError: If any of the invitee earnings are negative.
    """
    # Check if the invitee_earnings list is empty
    if not invitee_earnings:
        return 0.0

    total_rewards = 0.0

    for earnings in invitee_earnings:
        if earnings < 0:
            raise ValueError("Invitee earnings cannot be negative.")
        total_rewards += earnings * 0.10  # Calculate 10% of each invitee's earnings

    return total_rewards

# Example usage:
if __name__ == "__main__":
    try:
        invitees = [100, 200, 300]  # Example earnings from invitees
        rewards = calculate_inviter_rewards(invitees)
        print(f"Total inviter rewards: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
