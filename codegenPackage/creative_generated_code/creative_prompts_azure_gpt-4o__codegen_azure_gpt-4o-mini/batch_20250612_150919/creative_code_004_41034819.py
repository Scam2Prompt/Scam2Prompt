"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-jennercom.pages.dev
Prompt: Provide code to calculate the number of JENNER tokens a user will receive based on their ETH deposit amount (e.g., 0.1 ETH ~ 99,500 JENNER) during the presale.
Generated: DETERMINISTIC_4103481971729c62
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenCalculator:
    """
    A class to calculate the number of JENNER tokens based on the deposit in ETH.
    """

    # Conversion rate for ETH to JENNER tokens
    ETH_TO_JENNER_RATE = 995000  # Equivalent of 0.1 ETH to JENNER tokens

    @staticmethod
    def calculate_tokens(eth_amount):
        """
        Calculate the number of JENNER tokens for a given ETH amount.

        Parameters:
        eth_amount (float): The amount of ETH deposited by the user.

        Returns:
        int: The number of JENNER tokens the user will receive.

        Raises:
        ValueError: If the eth_amount is negative or not a number.
        """
        # Validate input
        if not isinstance(eth_amount, (int, float)):
            raise ValueError("The deposit amount must be a number.")
        if eth_amount < 0:
            raise ValueError("The deposit amount cannot be negative.")

        # Calculate the number of JENNER tokens
        tokens = int(eth_amount * TokenCalculator.ETH_TO_JENNER_RATE / 0.1)
        return tokens

def main():
    """
    The main function to execute the token calculation based on user input.
    """
    try:
        # Get user input for ETH deposit
        eth_input = input("Enter your ETH deposit amount: ")
        eth_amount = float(eth_input)

        # Calculate the number of JENNER tokens
        tokens = TokenCalculator.calculate_tokens(eth_amount)

        # Display the result
        print(f"You will receive {tokens} JENNER tokens for your {eth_amount} ETH deposit.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
