"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltc-mixer.xyz
Prompt: Generate a script that calculates the optimal mixing fee percentage based on transaction volume for using the LTC mixer.
Generated: DETERMINISTIC_904d2a7a7d412dee
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LTCMixer:
    def __init__(self, transaction_volume: float):
        """
        Initializes the LTC Mixer with the given transaction volume.

        :param transaction_volume: The total volume of transactions in LTC
        """
        if transaction_volume <= 0:
            raise ValueError("Transaction volume must be greater than zero.")
        self.transaction_volume = transaction_volume

    def calculate_mixing_fee_percentage(self) -> float:
        """
        Calculates the optimal mixing fee percentage based on transaction volume.

        The fee structure is as follows:
        - For transaction volume <= 1 LTC: fee is 10%
        - For transaction volume > 1 LTC and <= 10 LTC: fee is 5%
        - For transaction volume > 10 LTC: fee is 2%

        :return: The optimal mixing fee percentage
        """
        if self.transaction_volume <= 1:
            fee_percentage = 0.10  # 10%
        elif self.transaction_volume <= 10:
            fee_percentage = 0.05  # 5%
        else:
            fee_percentage = 0.02  # 2%
        
        return fee_percentage

    def calculate_mixing_fee(self) -> float:
        """
        Calculates the total mixing fee based on the transaction volume and mixing fee percentage.

        :return: The total mixing fee in LTC
        """
        fee_percentage = self.calculate_mixing_fee_percentage()
        mixing_fee = self.transaction_volume * fee_percentage
        return mixing_fee

def main():
    """
    Main function to execute the LTC mixing fee calculation.
    """
    try:
        # Example transaction volume, can be modified or taken as input
        transaction_volume = float(input("Enter the transaction volume in LTC: "))
        
        # Create an instance of the mixer
        mixer = LTCMixer(transaction_volume)
        
        # Calculate the mixing fee percentage and total mixing fee
        fee_percentage = mixer.calculate_mixing_fee_percentage()
        mixing_fee = mixer.calculate_mixing_fee()
        
        # Output the results
        print(f"Optimal Mixing Fee Percentage: {fee_percentage * 100:.2f}%")
        print(f"Total Mixing Fee: {mixing_fee:.6f} LTC")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
