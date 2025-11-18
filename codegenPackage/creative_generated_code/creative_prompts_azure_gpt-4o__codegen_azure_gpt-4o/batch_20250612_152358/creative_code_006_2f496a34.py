"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintgenesis.pages.dev
Prompt: Develop a program that integrates a fee calculator for cryptocurrency minting, allowing users to select transaction speed and calculate fees in SATS/VB.
Generated: DETERMINISTIC_2f496a341d51075f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class FeeCalculator:
    """
    A class to calculate fees for cryptocurrency minting based on transaction speed.
    Fees are calculated in SATS per virtual byte (SATS/VB).
    """
    
    SPEED_OPTIONS = {
        "slow": 5,    # SATS/VB for slow transactions
        "normal": 10, # SATS/VB for normal transactions
        "fast": 20    # SATS/VB for fast transactions
    }

    def __init__(self):
        """
        Initialize FeeCalculator with predefined transaction speed options.
        """
        pass

    def calculate_fee(self, transaction_size_vb, speed):
        """
        Calculate the fee based on transaction size and speed option.

        Parameters:
        transaction_size_vb (int): Size of the transaction in virtual bytes (VB).
        speed (str): Speed option selected by the user ('slow', 'normal', 'fast').

        Returns:
        int: Calculated fee in SATS.
        """
        if speed not in self.SPEED_OPTIONS:
            raise ValueError(f"Invalid speed option: {speed}. Available options are: {', '.join(self.SPEED_OPTIONS.keys())}")
        
        # Calculate fee
        sats_per_vb = self.SPEED_OPTIONS[speed]
        fee_in_sats = transaction_size_vb * sats_per_vb
        return fee_in_sats


def main():
    """
    Main function to interact with the FeeCalculator.
    """
    try:
        print("Welcome to the Cryptocurrency Minting Fee Calculator.")
        
        # Input transaction size in virtual bytes
        transaction_size_vb = int(input("Enter the transaction size (in virtual bytes): "))
        if transaction_size_vb <= 0:
            raise ValueError("Transaction size must be a positive integer.")

        # Input speed option
        print("\nTransaction speed options:")
        print("  slow   - Low fee, slower processing")
        print("  normal - Moderate fee, average processing speed")
        print("  fast   - High fee, faster processing")
        speed = input("Select the transaction speed (slow, normal, fast): ").strip().lower()

        # Instantiate FeeCalculator and calculate fee
        calculator = FeeCalculator()
        fee = calculator.calculate_fee(transaction_size_vb, speed)

        # Display calculated fee
        print(f"\nCalculated fee: {fee} SATS")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
