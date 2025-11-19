"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a function that calculates the number of lottery tickets based on the Seedify minting rules.
Generated: DETERMINISTIC_e033baaccc9ceff0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_lottery_tickets(total_tickets: int, minting_rules: dict) -> int:
    """
    Calculate the number of lottery tickets that can be minted based on Seedify minting rules.

    Args:
        total_tickets (int): The total number of tickets available for minting.
        minting_rules (dict): A dictionary containing the minting rules. 
                              It should have the following keys:
                              - 'max_per_user' (int): The maximum number of tickets a single user can mint.
                              - 'total_users' (int): The total number of users eligible for minting.

    Returns:
        int: The number of lottery tickets that can be minted.

    Raises:
        ValueError: If total_tickets is less than zero.
        ValueError: If minting_rules is missing required keys or has invalid values.
    """
    
    # Validate input values
    if total_tickets < 0:
        raise ValueError("Total tickets must be a non-negative integer.")
    
    required_keys = ['max_per_user', 'total_users']
    for key in required_keys:
        if key not in minting_rules:
            raise ValueError(f"Missing required minting rule: {key}")
        if not isinstance(minting_rules[key], int) or minting_rules[key] < 0:
            raise ValueError(f"Minting rule '{key}' must be a non-negative integer.")

    max_per_user = minting_rules['max_per_user']
    total_users = minting_rules['total_users']

    # Calculate the total tickets that can be minted based on the rules
    total_allowed_tickets = min(total_tickets, max_per_user * total_users)

    return total_allowed_tickets

# Example usage
if __name__ == "__main__":
    try:
        tickets = calculate_lottery_tickets(100, {'max_per_user': 5, 'total_users': 20})
        print(f"Total lottery tickets that can be minted: {tickets}")
    except ValueError as e:
        print(f"Error: {e}")
```
