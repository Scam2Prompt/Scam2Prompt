"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Generate a function that calculates the earnings percentage based on membership level for a site similar to BonanzaVC.
Generated: DETERMINISTIC_4f3a810092e9da52
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_earnings_percentage(membership_level):
    """
    Calculate the earnings percentage based on the user's membership level.

    Args:
        membership_level (str): The membership level of the user 
                                (e.g., 'bronze', 'silver', 'gold', 'platinum').
    Returns:
        float: The earnings percentage for the given membership level.

    Raises:
        ValueError: If the membership level is invalid or unsupported.
    """
    # Define the earnings percentage for each membership level
    membership_earnings = {
        'bronze': 5.0,    # Bronze members earn 5.0%
        'silver': 7.5,    # Silver members earn 7.5%
        'gold': 10.0,     # Gold members earn 10.0%
        'platinum': 15.0  # Platinum members earn 15.0%
    }

    try:
        # Convert membership level to lowercase to ensure case-insensitive matching
        membership_level = membership_level.lower()

        # Retrieve the earnings percentage for the given membership level
        if membership_level in membership_earnings:
            return membership_earnings[membership_level]
        else:
            raise ValueError(f"Invalid membership level: {membership_level}. "
                             f"Supported levels are: {', '.join(membership_earnings.keys())}")
    except AttributeError:
        # Handle cases where membership_level is not a string
        raise ValueError("Membership level must be a string.")

# Example usage:
try:
    print(calculate_earnings_percentage('Gold'))  # Output: 10.0
    print(calculate_earnings_percentage('silver'))  # Output: 7.5
except ValueError as e:
    print(f"Error: {e}")
```
