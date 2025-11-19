"""
Generated Code Metadata:
========================
Original URL: https://linea.usernames.club
Prompt: Generate a function that calculates the cost of minting a .linea username based on its character length.
Generated: DETERMINISTIC_0955c3ca4f7bcd45
Batch ID: 20250612_140418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_minting_cost(username: str, base_cost: int = 1, character_fee: int = 0.1) -> float:
    """
    Calculate the cost of minting a .linea username based on its character length.

    Args:
    - username (str): The username to be minted.
    - base_cost (int, optional): The base cost of minting. Defaults to 1.
    - character_fee (int, optional): The fee per character. Defaults to 0.1.

    Returns:
    - float: The total cost of minting the username.

    Raises:
    - TypeError: If the username is not a string or if the base cost or character fee is not a number.
    - ValueError: If the username is empty or if the base cost or character fee is negative.
    """

    # Check if the username is a string
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")

    # Check if the username is not empty
    if len(username) == 0:
        raise ValueError("Username cannot be empty.")

    # Check if the base cost and character fee are numbers
    if not isinstance(base_cost, (int, float)) or not isinstance(character_fee, (int, float)):
        raise TypeError("Base cost and character fee must be numbers.")

    # Check if the base cost and character fee are non-negative
    if base_cost < 0 or character_fee < 0:
        raise ValueError("Base cost and character fee must be non-negative.")

    # Calculate the total cost
    character_count = len(username)
    total_cost = base_cost + (character_count * character_fee)

    return total_cost


# Example usage:
def main():
    try:
        username = "exampleuser"
        cost = calculate_minting_cost(username)
        print(f"The cost of minting '{username}' is: {cost}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
