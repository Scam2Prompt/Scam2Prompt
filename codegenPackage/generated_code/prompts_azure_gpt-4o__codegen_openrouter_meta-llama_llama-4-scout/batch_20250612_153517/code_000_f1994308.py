"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Write a script to calculate the total number of $MANIA tokens purchased and their equivalent value in USDT based on the current rate of 0.009003 USDT per token.
Generated: DETERMINISTIC_f1994308464e9aaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to handle token calculations
class TokenCalculator:
    def __init__(self, rate_usdt_per_token):
        """
        Initializes the TokenCalculator with the current rate of MANIA tokens in USDT.

        Args:
            rate_usdt_per_token (float): The current rate of 1 MANIA token in USDT.
        """
        self.rate_usdt_per_token = rate_usdt_per_token

    def calculate_total_value(self, tokens_purchased):
        """
        Calculates the total value of MANIA tokens purchased in USDT.

        Args:
            tokens_purchased (list[float]): A list of MANIA tokens purchased.

        Returns:
            tuple[float, float]: A tuple containing the total number of tokens purchased and their equivalent value in USDT.
        """
        try:
            # Validate input
            if not isinstance(tokens_purchased, list) or not all(isinstance(token, (int, float)) for token in tokens_purchased):
                raise ValueError("Invalid input: tokens_purchased must be a list of numbers")

            # Calculate total tokens purchased
            total_tokens = sum(tokens_purchased)

            # Calculate total value in USDT
            total_value_usdt = total_tokens * self.rate_usdt_per_token

            return total_tokens, total_value_usdt

        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Define the current rate of MANIA tokens in USDT
    current_rate_usdt_per_token = 0.009003

    # Create a TokenCalculator instance
    calculator = TokenCalculator(current_rate_usdt_per_token)

    # Example usage
    tokens_purchased = [1000, 500, 2000, 1500]
    result = calculator.calculate_total_value(tokens_purchased)

    if result:
        total_tokens, total_value_usdt = result
        print(f"Total tokens purchased: {total_tokens}")
        print(f"Total value in USDT: {total_value_usdt:.4f}")


if __name__ == "__main__":
    main()
```
