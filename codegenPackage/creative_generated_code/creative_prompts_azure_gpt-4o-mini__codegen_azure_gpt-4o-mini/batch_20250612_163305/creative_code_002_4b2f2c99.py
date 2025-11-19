"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-topg.pages.dev
Prompt: Write a script to calculate the amount of TOPG tokens received for different ETH contributions in a presale, based on the rates provided for $TOPG.
Generated: DETERMINISTIC_4b2f2c990368b30f
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TOPGTokenCalculator:
    def __init__(self, rate_per_eth):
        """
        Initializes the TOPGTokenCalculator with the provided rate for TOPG tokens per ETH.

        :param rate_per_eth: float, the number of TOPG tokens received for one ETH contribution.
        """
        if rate_per_eth <= 0:
            raise ValueError("Rate per ETH must be greater than zero.")
        self.rate_per_eth = rate_per_eth

    def calculate_tokens(self, eth_contribution):
        """
        Calculates the number of TOPG tokens received based on the ETH contribution.

        :param eth_contribution: float, the amount of ETH contributed.
        :return: float, the number of TOPG tokens received.
        """
        if eth_contribution < 0:
            raise ValueError("ETH contribution must not be negative.")
        return eth_contribution * self.rate_per_eth

    def calculate_multiple_contributions(self, contributions):
        """
        Calculates TOPG tokens for multiple ETH contributions.

        :param contributions: list of floats, each representing an ETH contribution.
        :return: dict, mapping each contribution to its corresponding TOPG tokens received.
        """
        if not isinstance(contributions, list):
            raise TypeError("Contributions must be provided as a list.")

        tokens_received = {}
        for eth in contributions:
            tokens_received[eth] = self.calculate_tokens(eth)
        return tokens_received

def main():
    """
    Main function to execute the TOPG token calculation based on user input.
    """
    # Example rate for TOPG tokens per ETH
    rate_per_eth = 1000.0  # Example: 1000 TOPG tokens per 1 ETH

    # Create the TOPGTokenCalculator object
    calculator = TOPGTokenCalculator(rate_per_eth)

    # Example contributions
    contributions = [0.1, 0.5, 1.0, 2.5, 0.0]  # ETH contributions

    try:
        # Calculate TOPG tokens for the given contributions
        results = calculator.calculate_multiple_contributions(contributions)

        # Output the results in a readable format
        print("ETH Contribution to TOPG Tokens Received:")
        print(json.dumps(results, indent=4))

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
