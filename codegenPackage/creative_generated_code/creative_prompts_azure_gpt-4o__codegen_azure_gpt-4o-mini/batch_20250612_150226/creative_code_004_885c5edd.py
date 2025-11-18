"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiavwskgiww3elpabxoxlcv3n46mhlr4fohrwq3gyojtkwmivmo2bu.ipfs.dweb.link
Prompt: Write code to calculate the number of $BCKR tokens received for different ETH deposit amounts during the presale, referencing the conversion rate of 0.1 ETH = 99,500 BCKR.
Generated: DETERMINISTIC_885c5edd8833d9d6
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenCalculator:
    """
    A class to calculate the number of BCKR tokens received 
    based on the ETH deposit amount during the presale.
    """

    # Conversion rate constants
    ETH_TO_BCKR_RATE = 99500 / 0.1  # 99,500 BCKR for 0.1 ETH

    @staticmethod
    def calculate_bckr_tokens(eth_amount):
        """
        Calculate the number of BCKR tokens for a given ETH amount.

        Args:
            eth_amount (float): The amount of ETH deposited.

        Returns:
            int: The number of BCKR tokens received.

        Raises:
            ValueError: If the eth_amount is negative.
        """
        if eth_amount < 0:
            raise ValueError("ETH amount must be non-negative.")

        # Calculate the number of BCKR tokens
        bckr_tokens = eth_amount * TokenCalculator.ETH_TO_BCKR_RATE
        return int(bckr_tokens)  # Return as an integer

def main():
    """
    Main function to run the token calculator.
    """
    try:
        # Example ETH deposits for testing
        eth_deposits = [0.1, 0.5, 1.0, 2.0, -0.1]  # The last value will raise an error

        for eth in eth_deposits:
            tokens = TokenCalculator.calculate_bckr_tokens(eth)
            print(f"ETH Deposit: {eth} -> BCKR Tokens Received: {tokens}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
