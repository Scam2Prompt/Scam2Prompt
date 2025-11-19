"""
Generated Code Metadata:
========================
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Write a function that calculates the amount of $ONCHAIN tokens received based on the ETH sent during the presale.
Generated: DETERMINISTIC_ed771938573a12a2
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Presale:
    def __init__(self, eth_to_onchain_rate):
        """
        Initializes the Presale with a given ETH to $ONCHAIN token conversion rate.

        :param eth_to_onchain_rate: The rate at which ETH is converted to $ONCHAIN tokens.
        """
        if eth_to_onchain_rate <= 0:
            raise ValueError("ETH to $ONCHAIN conversion rate must be greater than zero.")
        self.eth_to_onchain_rate = eth_to_onchain_rate

    def calculate_onchain_tokens(self, eth_sent):
        """
        Calculates the amount of $ONCHAIN tokens received based on the ETH sent.

        :param eth_sent: The amount of ETH sent during the presale.
        :return: The amount of $ONCHAIN tokens received.
        :raises ValueError: If eth_sent is negative.
        """
        if eth_sent < 0:
            raise ValueError("ETH sent cannot be negative.")

        # Calculate the amount of $ONCHAIN tokens received
        onchain_tokens_received = eth_sent * self.eth_to_onchain_rate
        return onchain_tokens_received


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the presale with a conversion rate of 100 $ONCHAIN tokens per 1 ETH
        presale = Presale(eth_to_onchain_rate=100)

        # Amount of ETH sent by the user
        eth_sent = 1.5  # Example: User sends 1.5 ETH

        # Calculate the $ONCHAIN tokens received
        tokens_received = presale.calculate_onchain_tokens(eth_sent)
        print(f"Tokens received: {tokens_received} $ONCHAIN")
    except ValueError as e:
        print(f"Error: {e}")
```
