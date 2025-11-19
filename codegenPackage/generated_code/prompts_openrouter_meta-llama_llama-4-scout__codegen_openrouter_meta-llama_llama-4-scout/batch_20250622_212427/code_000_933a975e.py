"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Write a Python script to calculate the bonus tokens a user would receive for participating in the Dopawing presale, given the current social media follower count and the tokenomics structure.
Generated: DETERMINISTIC_933a975eef9232fe
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dopawing_presale_bonus_calculator.py

"""
Calculates the bonus tokens a user would receive for participating in the Dopawing presale.

Tokenomics Structure:
- 1% bonus for 100-499 followers
- 2% bonus for 500-1999 followers
- 3% bonus for 2000-4999 followers
- 4% bonus for 5000-9999 followers
- 5% bonus for 10000+ followers
"""

def calculate_bonus_tokens(follower_count: int, total_tokens: float, token_price: float) -> float:
    """
    Calculates the bonus tokens based on the follower count.

    Args:
    - follower_count (int): The current social media follower count.
    - total_tokens (float): The total number of tokens allocated for the presale.
    - token_price (float): The price of one token in USD.

    Returns:
    - float: The bonus tokens the user would receive.
    """

    # Define the tokenomics structure
    tokenomics = [
        (100, 499, 0.01),  # 1% bonus for 100-499 followers
        (500, 1999, 0.02),  # 2% bonus for 500-1999 followers
        (2000, 4999, 0.03),  # 3% bonus for 2000-4999 followers
        (5000, 9999, 0.04),  # 4% bonus for 5000-9999 followers
        (10000, float('inf'), 0.05)  # 5% bonus for 10000+ followers
    ]

    # Validate inputs
    if follower_count < 0:
        raise ValueError("Follower count cannot be negative.")
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than zero.")
    if token_price <= 0:
        raise ValueError("Token price must be greater than zero.")

    # Calculate the bonus percentage
    bonus_percentage = next((bonus for min_followers, max_followers, bonus in tokenomics 
                             if min_followers <= follower_count <= max_followers), 0)

    # Calculate the bonus tokens
    bonus_tokens = total_tokens * bonus_percentage

    return bonus_tokens


def calculate_user_tokens(follower_count: int, total_tokens: float, token_price: float, 
                          presale_allocation: float) -> dict:
    """
    Calculates the total tokens a user would receive, including bonus tokens.

    Args:
    - follower_count (int): The current social media follower count.
    - total_tokens (float): The total number of tokens allocated for the presale.
    - token_price (float): The price of one token in USD.
    - presale_allocation (float): The user's allocated tokens for the presale.

    Returns:
    - dict: A dictionary containing the user's allocated tokens, bonus tokens, and total tokens.
    """

    bonus_tokens = calculate_bonus_tokens(follower_count, presale_allocation, token_price)
    total_user_tokens = presale_allocation + bonus_tokens

    return {
        "allocated_tokens": presale_allocation,
        "bonus_tokens": bonus_tokens,
        "total_tokens": total_user_tokens
    }


if __name__ == "__main__":
    try:
        follower_count = 15000
        total_tokens = 1000000.0
        token_price = 0.10
        presale_allocation = 10000.0

        user_tokens = calculate_user_tokens(follower_count, total_tokens, token_price, presale_allocation)

        print("User Token Breakdown:")
        print(f"Allocated Tokens: {user_tokens['allocated_tokens']}")
        print(f"Bonus Tokens: {user_tokens['bonus_tokens']}")
        print(f"Total Tokens: {user_tokens['total_tokens']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
