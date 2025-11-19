"""
Generated Code Metadata:
========================
Original URL: https://link-presale-dogcoin.pages.dev
Prompt: Generate a Python script to calculate the number of $DOG tokens a user can buy based on the provided ETH amounts and the pre-sale rate.
Generated: DETERMINISTIC_24432f35d21bed33
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dog_token_calculator.py

class DogTokenCalculator:
    def __init__(self, presale_rate):
        """
        Initializes the DogTokenCalculator with the given presale rate.

        :param presale_rate: The number of DOG tokens per 1 ETH.
        """
        if presale_rate <= 0:
            raise ValueError("Presale rate must be a positive number.")
        self.presale_rate = presale_rate

    def calculate_tokens(self, eth_amount):
        """
        Calculates the number of DOG tokens that can be bought with the given ETH amount.

        :param eth_amount: The amount of ETH the user wants to spend.
        :return: The number of DOG tokens that can be purchased.
        """
        if eth_amount < 0:
            raise ValueError("ETH amount cannot be negative.")
        
        # Calculate the number of DOG tokens
        dog_tokens = eth_amount * self.presale_rate
        return dog_tokens

def main():
    """
    Main function to execute the DOG token calculation based on user input.
    """
    try:
        # Get user input for ETH amount and presale rate
        eth_amount = float(input("Enter the amount of ETH you want to spend: "))
        presale_rate = float(input("Enter the presale rate (DOG tokens per ETH): "))

        # Create an instance of DogTokenCalculator
        calculator = DogTokenCalculator(presale_rate)

        # Calculate the number of DOG tokens
        tokens = calculator.calculate_tokens(eth_amount)

        # Display the result
        print(f"You can buy {tokens} DOG tokens with {eth_amount} ETH at a presale rate of {presale_rate}.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
