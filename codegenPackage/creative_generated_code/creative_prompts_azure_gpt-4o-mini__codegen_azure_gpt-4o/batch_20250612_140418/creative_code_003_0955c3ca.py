"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.usernames.club
Prompt: Generate a function that calculates the cost of minting a .linea username based on its character length.
Generated: DETERMINISTIC_0955c3ca4f7bcd45
Batch ID: 20250612_140418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_minting_cost(username: str) -> float:
    """
    Calculates the cost of minting a .linea username based on its character length.

    Args:
        username (str): The username for which minting cost is calculated.

    Returns:
        float: The calculated minting cost.

    Raises:
        ValueError: If the username is invalid (empty or contains non-alphanumeric characters).
    """
    
    # Validate the username
    if not username or not username.isalnum():
        raise ValueError("Invalid username. Usernames must be non-empty and contain only alphanumeric characters.")

    # Get the length of the username
    username_length = len(username)

    # Define cost tiers based on character length
    if username_length <= 3:
        minting_cost = 50.0  # Short usernames are premium
    elif username_length <= 6:
        minting_cost = 20.0  # Medium-length usernames are standard-priced
    else:
        minting_cost = 10.0  # Long usernames are cheaper

    return minting_cost


# Example usage:
# try:
#     cost = calculate_minting_cost("example")
#     print(f"The minting cost is: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}")
```
