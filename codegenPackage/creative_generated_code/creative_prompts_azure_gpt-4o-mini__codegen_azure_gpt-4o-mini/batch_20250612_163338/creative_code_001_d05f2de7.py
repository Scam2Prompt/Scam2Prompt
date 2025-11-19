"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-pacmoonio.pages.dev
Prompt: Write a function that calculates the amount of JENNER tokens received based on different ETH investment amounts during the presale.
Generated: DETERMINISTIC_d05f2de7ba2d0e8f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPresale:
    def __init__(self, eth_to_jenner_rate):
        """
        Initializes the presale with the given rate of ETH to JENNER tokens.

        Args:
            eth_to_jenner_rate (float): The number of JENNER tokens received per ETH invested.
        """
        if eth_to_jenner_rate <= 0:
            raise ValueError("ETH to JENNER rate must be greater than zero.")
        self.eth_to_jenner_rate = eth_to_jenner_rate

    def calculate_tokens(self, eth_investment):
        """
        Calculates the number of JENNER tokens received based on the ETH investment.

        Args:
            eth_investment (float): The amount of ETH to invest.

        Returns:
            float: The number of JENNER tokens received.

        Raises:
            ValueError: If eth_investment is negative.
        """
        if eth_investment < 0:
            raise ValueError("ETH investment cannot be negative.")

        # Calculate the amount of JENNER tokens
        tokens_received = eth_investment * self.eth_to_jenner_rate
        return tokens_received


# Example usage
if __name__ == "__main__":
    try:
        presale = TokenPresale(1000)  # Example rate: 1000 JENNER per 1 ETH
        investment = 0.5  # Example investment in ETH
        tokens = presale.calculate_tokens(investment)
        print(f"Tokens received for {investment} ETH: {tokens} JENNER")
    except ValueError as e:
        print(f"Error: {e}")
```
