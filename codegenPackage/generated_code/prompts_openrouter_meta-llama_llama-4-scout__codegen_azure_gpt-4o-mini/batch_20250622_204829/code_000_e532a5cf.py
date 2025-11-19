"""
Generated Code Metadata:
========================
Original URL: https://ethzao.com
Prompt: What is ETH Pledge and how does it relate to Ethereum staking?
Generated: DETERMINISTIC_e532a5cfbc90a270
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EthPledge:
    """
    A class to represent the ETH Pledge and its relation to Ethereum staking.
    """

    def __init__(self, total_supply: float, staking_ratio: float):
        """
        Initializes the EthPledge instance.

        :param total_supply: Total supply of ETH in circulation.
        :param staking_ratio: The ratio of ETH that is staked.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= staking_ratio <= 1):
            raise ValueError("Staking ratio must be between 0 and 1.")

        self.total_supply = total_supply
        self.staking_ratio = staking_ratio

    def calculate_staked_eth(self) -> float:
        """
        Calculates the amount of ETH that is currently staked.

        :return: The amount of staked ETH.
        """
        staked_eth = self.total_supply * self.staking_ratio
        return staked_eth

    def calculate_unstaked_eth(self) -> float:
        """
        Calculates the amount of ETH that is not staked.

        :return: The amount of unstaked ETH.
        """
        unstaked_eth = self.total_supply * (1 - self.staking_ratio)
        return unstaked_eth

    def pledge_info(self) -> dict:
        """
        Provides information about the ETH pledge and staking.

        :return: A dictionary containing total supply, staked ETH, and unstaked ETH.
        """
        return {
            "total_supply": self.total_supply,
            "staked_eth": self.calculate_staked_eth(),
            "unstaked_eth": self.calculate_unstaked_eth(),
            "staking_ratio": self.staking_ratio
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the EthPledge with total supply and staking ratio
        eth_pledge = EthPledge(total_supply=12000000, staking_ratio=0.65)

        # Retrieve and print pledge information
        pledge_info = eth_pledge.pledge_info()
        print(pledge_info)

    except ValueError as e:
        print(f"Error: {e}")
```
