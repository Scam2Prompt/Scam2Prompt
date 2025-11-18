"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a Python program that simulates the distribution of JESSE tokens based on the presale cap of 1000 BASE and the pricing structure provided.
Generated: DETERMINISTIC_ae27ce1cac580d99
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class JesseTokenDistributor:
    """
    A class to simulate the distribution of JESSE tokens based on a presale cap and pricing structure.
    """

    def __init__(self, presale_cap: float, base_price: float, token_price: float):
        """
        Initializes the distributor with the given presale cap and pricing structure.

        Args:
            presale_cap (float): The maximum amount of BASE for the presale.
            base_price (float): Base price for the token in terms of BASE.
            token_price (float): The price of a JESSE token.
        """
        if presale_cap <= 0 or base_price <= 0 or token_price <= 0:
            raise ValueError("Presale cap, base price, and token price must be greater than zero.")
        
        self.presale_cap = presale_cap
        self.base_price = base_price
        self.token_price = token_price
        self.tokens_distributed = 0
        self.total_base_collected = 0

    def distribute_tokens(self, base_amount: float) -> float:
        """
        Distributes JESSE tokens based on the amount of BASE contributed.

        Args:
            base_amount (float): The amount of BASE contributed by the user.

        Returns:
            float: The number of JESSE tokens distributed.
        
        Raises:
            ValueError: If the base amount exceeds the presale cap or is non-positive.
        """
        if base_amount <= 0:
            raise ValueError("Base amount must be greater than zero.")
        
        if base_amount + self.total_base_collected > self.presale_cap:
            raise ValueError("Exceeds presale cap.")

        # Calculate the number of JESSE tokens to distribute
        tokens_to_distribute = base_amount / self.token_price
        
        # Update the state
        self.tokens_distributed += tokens_to_distribute
        self.total_base_collected += base_amount

        return tokens_to_distribute

    def get_distribution_summary(self) -> dict:
        """
        Returns a summary of the distribution.

        Returns:
            dict: A summary containing the total BASE collected and the total tokens distributed.
        """
        return {
            "total_base_collected": self.total_base_collected,
            "tokens_distributed": self.tokens_distributed
        }


def main():
    """
    Main function to run the token distribution simulation.
    Initializes the distributor and simulates some distributions.
    """
    try:
        # Initialize the distributor with a presale cap of 1000 BASE,
        # a base price of 1 BASE per token, and a JESSE token price of 0.1 BASE.
        distributor = JesseTokenDistributor(presale_cap=1000, base_price=1, token_price=0.1)

        # Simulate contributions
        contributions = [100, 200, 150, 500, 60]  # Example contributions

        for amount in contributions:
            tokens = distributor.distribute_tokens(amount)
            print(f"Distributed {tokens} JESSE tokens for {amount} BASE.")

        # Get and print the distribution summary
        summary = distributor.get_distribution_summary()
        print("Distribution Summary:", summary)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
