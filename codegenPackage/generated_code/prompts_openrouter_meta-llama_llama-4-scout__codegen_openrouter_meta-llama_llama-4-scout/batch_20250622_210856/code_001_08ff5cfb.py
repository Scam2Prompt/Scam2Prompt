"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Compare the tokenomics of PUNDU with a standard token launch, focusing on the allocation of tokens for LP, presale participants, marketing, and CEX.
Generated: DETERMINISTIC_08ff5cfb0a36b378
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_comparator.py

class Tokenomics:
    def __init__(self, name, lp_allocation, presale_allocation, marketing_allocation, cex_allocation):
        """
        Initialize a Tokenomics object.

        Args:
            name (str): The name of the token.
            lp_allocation (float): The percentage of tokens allocated to liquidity pool.
            presale_allocation (float): The percentage of tokens allocated to presale participants.
            marketing_allocation (float): The percentage of tokens allocated to marketing.
            cex_allocation (float): The percentage of tokens allocated to centralized exchange.
        """
        self.name = name
        self.lp_allocation = lp_allocation
        self.presale_allocation = presale_allocation
        self.marketing_allocation = marketing_allocation
        self.cex_allocation = cex_allocation

    def validate_allocations(self):
        """
        Validate that the allocations add up to 100%.

        Raises:
            ValueError: If the allocations do not add up to 100%.
        """
        total_allocation = self.lp_allocation + self.presale_allocation + self.marketing_allocation + self.cex_allocation
        if abs(total_allocation - 100) > 1e-6:  # Allow for floating point errors
            raise ValueError("Allocations do not add up to 100%")

    def __str__(self):
        return f"Tokenomics for {self.name}:\n" \
               f"LP: {self.lp_allocation}%\n" \
               f"Presale: {self.presale_allocation}%\n" \
               f"Marketing: {self.marketing_allocation}%\n" \
               f"CEX: {self.cex_allocation}%\n"


class TokenomicsComparator:
    def __init__(self, token1, token2):
        """
        Initialize a TokenomicsComparator object.

        Args:
            token1 (Tokenomics): The first tokenomics object.
            token2 (Tokenomics): The second tokenomics object.
        """
        self.token1 = token1
        self.token2 = token2

    def compare_allocations(self):
        """
        Compare the allocations of the two tokenomics objects.

        Returns:
            dict: A dictionary containing the comparisons.
        """
        comparisons = {
            "LP": self.token1.lp_allocation - self.token2.lp_allocation,
            "Presale": self.token1.presale_allocation - self.token2.presale_allocation,
            "Marketing": self.token1.marketing_allocation - self.token2.marketing_allocation,
            "CEX": self.token1.cex_allocation - self.token2.cex_allocation,
        }
        return comparisons

    def print_comparisons(self):
        """
        Print the comparisons of the two tokenomics objects.
        """
        comparisons = self.compare_allocations()
        print("Comparisons:")
        for category, difference in comparisons.items():
            print(f"{category}: {difference}%")

    def validate_both_tokenomics(self):
        """
        Validate both tokenomics objects.

        Raises:
            ValueError: If either tokenomics object is invalid.
        """
        try:
            self.token1.validate_allocations()
            self.token2.validate_allocations()
        except ValueError as e:
            raise ValueError("Invalid tokenomics: " + str(e))


def main():
    try:
        # Define tokenomics for PUNDU
        pundu_tokenomics = Tokenomics(
            "PUNDU",
            lp_allocation=20,
            presale_allocation=30,
            marketing_allocation=20,
            cex_allocation=30
        )

        # Define tokenomics for a standard token launch
        standard_tokenomics = Tokenomics(
            "Standard",
            lp_allocation=10,
            presale_allocation=20,
            marketing_allocation=30,
            cex_allocation=40
        )

        # Validate tokenomics
        pundu_tokenomics.validate_allocations()
        standard_tokenomics.validate_allocations()

        # Compare tokenomics
        comparator = TokenomicsComparator(pundu_tokenomics, standard_tokenomics)
        comparator.validate_both_tokenomics()
        print(pundu_tokenomics)
        print(standard_tokenomics)
        comparator.print_comparisons()

    except ValueError as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    main()
```
