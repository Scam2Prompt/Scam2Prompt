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
class Tokenomics:
    """
    A class to represent the tokenomics structure for the Dopawing presale.
    """

    def __init__(self, base_bonus: float, follower_bonus_rate: float):
        """
        Initializes the Tokenomics with base bonus and follower bonus rate.

        :param base_bonus: The base bonus tokens for participation.
        :param follower_bonus_rate: The rate at which bonus tokens are awarded per follower.
        """
        self.base_bonus = base_bonus
        self.follower_bonus_rate = follower_bonus_rate

    def calculate_bonus(self, follower_count: int) -> float:
        """
        Calculates the total bonus tokens based on follower count.

        :param follower_count: The number of social media followers.
        :return: The total bonus tokens.
        :raises ValueError: If follower_count is negative.
        """
        if follower_count < 0:
            raise ValueError("Follower count cannot be negative.")

        # Calculate bonus based on follower count
        follower_bonus = follower_count * self.follower_bonus_rate
        total_bonus = self.base_bonus + follower_bonus
        return total_bonus


def main():
    """
    Main function to execute the bonus token calculation.
    """
    # Define the tokenomics structure
    base_bonus = 100.0  # Base bonus tokens
    follower_bonus_rate = 0.5  # Bonus tokens per follower

    # Create a Tokenomics instance
    tokenomics = Tokenomics(base_bonus, follower_bonus_rate)

    try:
        # Input: Get the follower count from the user
        follower_count = int(input("Enter your social media follower count: "))

        # Calculate the bonus tokens
        bonus_tokens = tokenomics.calculate_bonus(follower_count)

        # Output: Display the result
        print(f"You will receive a total of {bonus_tokens} bonus tokens for participating in the presale.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
