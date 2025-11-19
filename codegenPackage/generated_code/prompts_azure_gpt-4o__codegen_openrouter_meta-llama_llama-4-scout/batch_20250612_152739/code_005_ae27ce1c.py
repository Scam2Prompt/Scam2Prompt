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
# jesse_token_distribution.py

class JesseTokenDistribution:
    def __init__(self, presale_cap: int, pricing_structure: dict):
        """
        Initializes the JesseTokenDistribution class.

        Args:
        - presale_cap (int): The presale cap in BASE.
        - pricing_structure (dict): A dictionary containing the pricing structure.
            It should have 'base_to_jesse' as key and the corresponding conversion rate as value.
        """
        self.presale_cap = presale_cap
        self.pricing_structure = pricing_structure

    def calculate_jesse_tokens(self, base_amount: int) -> float:
        """
        Calculates the JESSE tokens based on the provided BASE amount.

        Args:
        - base_amount (int): The amount of BASE.

        Returns:
        - float: The equivalent JESSE tokens.

        Raises:
        - ValueError: If the base amount is negative.
        - KeyError: If the pricing structure is not properly defined.
        """
        if base_amount < 0:
            raise ValueError("BASE amount cannot be negative.")

        try:
            conversion_rate = self.pricing_structure['base_to_jesse']
        except KeyError:
            raise KeyError("Pricing structure must contain 'base_to_jesse' key.")

        jesse_tokens = base_amount * conversion_rate
        return jesse_tokens

    def distribute_jesse_tokens(self, investors: dict) -> dict:
        """
        Simulates the distribution of JESSE tokens to investors based on their BASE contributions.

        Args:
        - investors (dict): A dictionary containing investor names as keys and their BASE contributions as values.

        Returns:
        - dict: A dictionary containing investor names as keys and their JESSE tokens as values.

        Raises:
        - ValueError: If the total BASE contribution exceeds the presale cap.
        """
        total_base_contribution = sum(investors.values())
        if total_base_contribution > self.presale_cap:
            raise ValueError("Total BASE contribution exceeds the presale cap.")

        jesse_token_distribution = {}
        for investor, base_contribution in investors.items():
            jesse_tokens = self.calculate_jesse_tokens(base_contribution)
            jesse_token_distribution[investor] = jesse_tokens

        return jesse_token_distribution


def main():
    # Define the presale cap and pricing structure
    presale_cap = 1000
    pricing_structure = {'base_to_jesse': 10}  # 1 BASE = 10 JESSE

    # Initialize the JesseTokenDistribution class
    jesse_distribution = JesseTokenDistribution(presale_cap, pricing_structure)

    # Define investors and their BASE contributions
    investors = {
        'Investor1': 100,
        'Investor2': 200,
        'Investor3': 300
    }

    try:
        # Simulate the distribution of JESSE tokens
        jesse_token_distribution = jesse_distribution.distribute_jesse_tokens(investors)
        print("JESSE Token Distribution:")
        for investor, jesse_tokens in jesse_token_distribution.items():
            print(f"{investor}: {jesse_tokens} JESSE")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
