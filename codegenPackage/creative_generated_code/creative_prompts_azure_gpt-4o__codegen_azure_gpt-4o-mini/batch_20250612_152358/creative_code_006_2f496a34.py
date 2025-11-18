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
class CryptoMintingFeeCalculator:
    """A class to calculate minting fees for cryptocurrency based on transaction speed."""

    def __init__(self):
        """Initialize the fee rates for different transaction speeds."""
        self.fee_rates = {
            "slow": 1,     # fee in SATS/VB
            "average": 5,  # fee in SATS/VB
            "fast": 10     # fee in SATS/VB
        }

    def calculate_fee(self, transaction_size_vbytes, speed):
        """
        Calculate the minting fee based on transaction size and selected speed.

        Args:
            transaction_size_vbytes (int): Size of the transaction in virtual bytes.
            speed (str): Transaction speed ("slow", "average", "fast").

        Returns:
            int: Calculated fee in SATS.
        
        Raises:
            ValueError: If the transaction size is negative or if the speed is invalid.
        """
        if transaction_size_vbytes < 0:
            raise ValueError("Transaction size cannot be negative.")
        
        if speed not in self.fee_rates:
            raise ValueError(f"Invalid speed selected. Choose from: {list(self.fee_rates.keys())}")

        fee_rate = self.fee_rates[speed]
        calculated_fee = transaction_size_vbytes * fee_rate

        return calculated_fee

def main():
    """
    Main function to execute the fee calculator.
    This function interacts with the user to get input and display results.
    """
    print("Welcome to the Cryptocurrency Minting Fee Calculator!")
    try:
        transaction_size = int(input("Enter the transaction size in virtual bytes (VB): "))
        speed = input("Select transaction speed (slow, average, fast): ").lower()

        calculator = CryptoMintingFeeCalculator()
        fee = calculator.calculate_fee(transaction_size, speed)

        print(f"The calculated minting fee for a transaction size of {transaction_size} VB at {speed} speed is: {fee} SATS")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
