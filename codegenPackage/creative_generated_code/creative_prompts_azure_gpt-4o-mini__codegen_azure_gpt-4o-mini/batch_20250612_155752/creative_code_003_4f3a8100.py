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
def calculate_earnings_percentage(membership_level: str) -> float:
    """
    Calculate the earnings percentage based on the membership level.

    Parameters:
    membership_level (str): The membership level of the user. 
                            Accepted values are 'basic', 'premium', and 'elite'.

    Returns:
    float: The earnings percentage corresponding to the membership level.

    Raises:
    ValueError: If the membership level is not recognized.
    """

    # Define a dictionary mapping membership levels to their respective earnings percentages
    earnings_mapping = {
        'basic': 0.10,   # 10% earnings for basic members
        'premium': 0.15, # 15% earnings for premium members
        'elite': 0.20    # 20% earnings for elite members
    }

    # Normalize membership_level input to lowercase for consistency
    membership_level = membership_level.lower()

    # Check if the provided membership level is valid
    if membership_level not in earnings_mapping:
        raise ValueError(f"Invalid membership level: {membership_level}. "
                         "Accepted values are 'basic', 'premium', or 'elite'.")

    # Return the corresponding earnings percentage
    return earnings_mapping[membership_level]

# Example usage (commented out to avoid execution during imports)
# try:
#     percentage = calculate_earnings_percentage('Premium')
#     print(f"Earnings Percentage: {percentage * 100}%")
# except ValueError as e:
#     print(e)
```
