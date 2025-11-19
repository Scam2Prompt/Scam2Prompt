"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Explain how Trade GPT helps users understand different types of investments, including cryptocurrencies and mutual funds.
Generated: DETERMINISTIC_de56d1311b7f0bab
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code in Python that fulfills the request:

```python
"""
trade_gpt_investments.py

This script defines a class TradeGPT that helps users understand different types of investments,
including cryptocurrencies and mutual funds. It includes methods to provide information about
these investment types and offers examples to educate users.
"""

import json

class TradeGPT:
    """
    TradeGPT class facilitates understanding of different types of investments.
    """

    def __init__(self):
        """
        Initializes the TradeGPT instance with data about investment types.
        """
        self.investment_data = {
            "cryptocurrencies": {
                "description": (
                    "Cryptocurrencies are digital or virtual currencies secured by cryptography. "
                    "They operate on decentralized networks based on blockchain technology."
                ),
                "examples": ["Bitcoin (BTC)", "Ethereum (ETH)", "Ripple (XRP)", "Litecoin (LTC)"],
                "pros": [
                    "High potential for growth",
                    "Decentralized and secure",
                    "Global accessibility"
                ],
                "cons": [
                    "Volatile and risky",
                    "Regulatory uncertainty",
                    "Limited adoption in some areas"
                ]
            },
            "mutual_funds": {
                "description": (
                    "Mutual funds are professionally managed investment funds that pool money from many investors "
                    "to purchase a diversified portfolio of stocks, bonds, or other securities."
                ),
                "examples": ["Index Funds", "Equity Funds", "Bond Funds", "Money Market Funds"],
                "pros": [
                    "Diversification reduces risk",
                    "Professionally managed",
                    "Accessible with low minimum investments"
                ],
                "cons": [
                    "Management fees can reduce returns",
                    "Limited control over investments",
                    "Performance tied to market conditions"
                ]
            }
        }

    def get_investment_details(self, investment_type):
        """
        Fetches detailed information about a specific investment type.

        Args:
            investment_type (str): The type of investment to query (e.g., 'cryptocurrencies', 'mutual_funds').

        Returns:
            dict: A dictionary with details about the specified investment type.
        """
        try:
            # Check if the requested investment type exists in the data
            if investment_type in self.investment_data:
                return self.investment_data[investment_type]
            else:
                raise ValueError(f"Invalid investment type: {investment_type}. Please choose from: "
                                 f"{', '.join(self.investment_data.keys())}.")
        except ValueError as e:
            # Return error message in case of invalid investment type
            return {"error": str(e)}

    def get_all_investment_types(self):
        """
        Provides a list of all available investment types.

        Returns:
            list: A list of strings representing available investment types.
        """
        return list(self.investment_data.keys())


# Example usage
if __name__ == "__main__":
    # Create an instance of TradeGPT
    trade_gpt = TradeGPT()

    # Display all available investment types
    print("Available Investment Types:")
    print(json.dumps(trade_gpt.get_all_investment_types(), indent=4))

    # Fetch details about cryptocurrencies
    print("\nCryptocurrency Details:")
    print(json.dumps(trade_gpt.get_investment_details("cryptocurrencies"), indent=4))

    # Fetch details about mutual funds
    print("\nMutual Funds Details:")
    print(json.dumps(trade_gpt.get_investment_details("mutual_funds"), indent=4))

    # Attempt to fetch details about an unsupported investment type
    print("\nInvalid Investment Type Query:")
    print(json.dumps(trade_gpt.get_investment_details("stocks"), indent=4))
```
