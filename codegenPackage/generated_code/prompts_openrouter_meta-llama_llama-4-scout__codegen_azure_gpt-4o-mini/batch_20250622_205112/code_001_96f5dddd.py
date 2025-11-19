"""
Generated Code Metadata:
========================
Original URL: https://bafybeiavwskgiww3elpabxoxlcv3n46mhlr4fohrwq3gyojtkwmivmo2bu.ipfs.dweb.link
Prompt: "Write a function to calculate the amount of $BCKR tokens received for a given ETH deposit in a presale, considering a presale cap of 1000 ETH and a total supply of 100,000,000 BCKR."
Generated: DETERMINISTIC_96f5dddd310729d8
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Presale:
    def __init__(self, eth_cap: float, total_supply: int):
        """
        Initialize the presale with a cap and total supply.

        :param eth_cap: The maximum amount of ETH that can be raised in the presale.
        :param total_supply: The total supply of BCKR tokens available.
        """
        self.eth_cap = eth_cap
        self.total_supply = total_supply

    def calculate_bckr_tokens(self, eth_deposit: float) -> float:
        """
        Calculate the amount of BCKR tokens received for a given ETH deposit.

        :param eth_deposit: The amount of ETH deposited by the user.
        :return: The amount of BCKR tokens received.
        :raises ValueError: If the ETH deposit is negative or exceeds the presale cap.
        """
        # Validate the ETH deposit
        if eth_deposit < 0:
            raise ValueError("ETH deposit cannot be negative.")
        if eth_deposit > self.eth_cap:
            raise ValueError(f"ETH deposit cannot exceed the presale cap of {self.eth_cap} ETH.")

        # Calculate the token price per ETH
        token_price_per_eth = self.total_supply / self.eth_cap

        # Calculate the amount of BCKR tokens received
        bckr_tokens_received = eth_deposit * token_price_per_eth

        return bckr_tokens_received


# Example usage
if __name__ == "__main__":
    try:
        presale = Presale(eth_cap=1000.0, total_supply=100_000_000)
        deposit = 10.0  # Example ETH deposit
        tokens = presale.calculate_bckr_tokens(deposit)
        print(f"Tokens received for {deposit} ETH deposit: {tokens} BCKR")
    except ValueError as e:
        print(f"Error: {e}")
```
