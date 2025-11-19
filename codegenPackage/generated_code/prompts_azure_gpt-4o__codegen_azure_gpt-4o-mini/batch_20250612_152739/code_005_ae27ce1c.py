"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Create a Python program that simulates the distribution of JESSE tokens based on the presale cap of 1000 BASE and the pricing structure provided.
Generated: DETERMINISTIC_ae27ce1cac580d99
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JesseTokenDistribution:
    def __init__(self, presale_cap: float, price_structure: dict):
        """
        Initializes the JesseTokenDistribution with a presale cap and pricing structure.

        :param presale_cap: The maximum amount of BASE tokens available for presale.
        :param price_structure: A dictionary mapping the number of BASE tokens to the price per JESSE token.
        """
        self.presale_cap = presale_cap
        self.price_structure = price_structure
        self.total_jesse_tokens = 0.0

    def calculate_tokens(self, base_amount: float) -> float:
        """
        Calculates the number of JESSE tokens that can be purchased with a given amount of BASE tokens.

        :param base_amount: The amount of BASE tokens to spend.
        :return: The number of JESSE tokens that can be purchased.
        :raises ValueError: If the base_amount exceeds the presale cap or is negative.
        """
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative.")
        if base_amount > self.presale_cap:
            raise ValueError("Base amount exceeds presale cap.")

        # Determine the price per JESSE token based on the price structure
        price_per_jesse = self.get_price_per_jesse(base_amount)
        if price_per_jesse is None:
            raise ValueError("No price structure available for the given base amount.")

        # Calculate the number of JESSE tokens
        jesse_tokens = base_amount / price_per_jesse
        self.total_jesse_tokens += jesse_tokens
        return jesse_tokens

    def get_price_per_jesse(self, base_amount: float) -> float:
        """
        Retrieves the price per JESSE token based on the amount of BASE tokens.

        :param base_amount: The amount of BASE tokens to check.
        :return: The price per JESSE token or None if not found.
        """
        for threshold, price in sorted(self.price_structure.items()):
            if base_amount <= threshold:
                return price
        return None

    def get_total_jesse_tokens(self) -> float:
        """
        Returns the total number of JESSE tokens distributed.

        :return: Total JESSE tokens distributed.
        """
        return self.total_jesse_tokens


def main():
    # Define the presale cap and pricing structure
    presale_cap = 1000.0  # Maximum BASE tokens for presale
    price_structure = {
        100: 0.1,  # 100 BASE tokens = 0.1 price per JESSE token
        500: 0.08,  # 500 BASE tokens = 0.08 price per JESSE token
        1000: 0.05  # 1000 BASE tokens = 0.05 price per JESSE token
    }

    # Create an instance of the JesseTokenDistribution
    distribution = JesseTokenDistribution(presale_cap, price_structure)

    # Example base amounts to simulate
    base_amounts = [50, 150, 600, 1000]

    for base_amount in base_amounts:
        try:
            jesse_tokens = distribution.calculate_tokens(base_amount)
            print(f"Purchased {jesse_tokens:.2f} JESSE tokens with {base_amount} BASE tokens.")
        except ValueError as e:
            print(f"Error: {e}")

    # Display total JESSE tokens distributed
    print(f"Total JESSE tokens distributed: {distribution.get_total_jesse_tokens():.2f}")


if __name__ == "__main__":
    main()
```
