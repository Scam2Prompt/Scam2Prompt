"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a program that calculates the total ETH earnings for a user who upgrades their ETHMiner affiliate rate to 50% and recruits a specified number of referrals.
Generated: DETERMINISTIC_c438c5d3942d018e
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ETHMiner:
    def __init__(self, base_rate=0.5):
        """
        Initializes the ETHMiner with a specified base affiliate rate.

        :param base_rate: Initial affiliate rate. Default is 0.5 (50%).
        """
        if not (0 <= base_rate <= 1):
            raise ValueError("Base rate must be between 0 and 1.")
        self.base_rate = base_rate

    def calculate_earnings(self, referrals, eth_per_referral):
        """
        Calculates total ETH earnings based on the number of referrals and ETH per referral.

        :param referrals: The number of referrals recruited.
        :param eth_per_referral: The amount of ETH earned per referral.
        :return: Total ETH earnings.
        """
        if referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")
        if eth_per_referral < 0:
            raise ValueError("ETH earned per referral cannot be negative.")

        total_earnings = referrals * eth_per_referral * self.base_rate
        return total_earnings

def main():
    """
    Main function to execute the ETHMiner earnings calculation.
    """
    try:
        # Initialize ETHMiner with a 50% affiliate rate
        eth_miner = ETHMiner(base_rate=0.5)

        # User inputs for referrals and ETH per referral
        referrals = int(input("Enter the number of referrals: "))
        eth_per_referral = float(input("Enter the ETH earned per referral: "))

        # Calculate total earnings
        total_earnings = eth_miner.calculate_earnings(referrals, eth_per_referral)

        # Display total earnings
        print(f"Total ETH earnings: {total_earnings:.4f} ETH")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
