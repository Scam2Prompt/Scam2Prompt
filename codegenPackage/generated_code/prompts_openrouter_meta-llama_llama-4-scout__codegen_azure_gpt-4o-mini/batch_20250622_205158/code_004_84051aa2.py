"""
Generated Code Metadata:
========================
Original URL: https://ethereumtumbler.to
Prompt: Develop a function to calculate service fees for an Ethereum tumbler, with fees ranging from 0.70% to 3%, and two tiers (standard and premium) for increased privacy.
Generated: DETERMINISTIC_84051aa24fd95f80
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EthereumTumbler:
    """
    A class to represent an Ethereum tumbler that calculates service fees
    based on the amount being tumbled and the selected tier.
    """

    # Define fee percentages for standard and premium tiers
    STANDARD_FEE_PERCENTAGE = 0.007  # 0.70%
    PREMIUM_FEE_PERCENTAGE = 0.03      # 3%

    def __init__(self, tier: str):
        """
        Initializes the EthereumTumbler with the specified tier.

        :param tier: The tier of the tumbler ('standard' or 'premium').
        :raises ValueError: If the tier is not recognized.
        """
        if tier not in ['standard', 'premium']:
            raise ValueError("Tier must be 'standard' or 'premium'.")
        self.tier = tier

    def calculate_fee(self, amount: float) -> float:
        """
        Calculates the service fee based on the amount and the selected tier.

        :param amount: The amount of Ethereum to be tumbled.
        :return: The calculated service fee.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Determine the fee percentage based on the selected tier
        if self.tier == 'standard':
            fee_percentage = self.STANDARD_FEE_PERCENTAGE
        else:  # self.tier == 'premium'
            fee_percentage = self.PREMIUM_FEE_PERCENTAGE

        # Calculate the service fee
        fee = amount * fee_percentage
        return fee

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EthereumTumbler with the desired tier
        tumbler = EthereumTumbler(tier='premium')
        
        # Amount to tumble
        amount_to_tumble = 1000.0  # Example amount in Ethereum
        
        # Calculate the service fee
        fee = tumbler.calculate_fee(amount_to_tumble)
        
        print(f"Service fee for tumbling {amount_to_tumble} ETH in {tumbler.tier} tier: {fee:.4f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
