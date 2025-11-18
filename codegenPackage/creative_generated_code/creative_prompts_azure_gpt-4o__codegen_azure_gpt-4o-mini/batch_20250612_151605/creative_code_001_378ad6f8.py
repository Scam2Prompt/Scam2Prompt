"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdusd-mixer.com
Prompt: Generate a script to calculate the fees for mixing FDUSD coins using the fee structure provided on FDUSD-Mixer.com (fixed fee of 0.001 FDUSD per address and less than 2% variable fee).
Generated: DETERMINISTIC_378ad6f83a717bb0
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class FdusdMixer:
    """
    A class to represent the FDUSD Mixer fee calculator.
    """

    FIXED_FEE_PER_ADDRESS = 0.001  # Fixed fee per address in FDUSD
    VARIABLE_FEE_PERCENTAGE = 0.02   # Maximum variable fee percentage

    def __init__(self, num_addresses, total_amount_fdusd):
        """
        Initialize the mixer with number of addresses and total FDUSD amount.

        :param num_addresses: The number of addresses to mix FDUSD coins.
        :param total_amount_fdusd: The total amount of FDUSD to be mixed.
        """
        if num_addresses < 1:
            raise ValueError("Number of addresses must be at least 1.")
        if total_amount_fdusd < 0:
            raise ValueError("Total amount of FDUSD must be non-negative.")

        self.num_addresses = num_addresses
        self.total_amount_fdusd = total_amount_fdusd

    def calculate_fees(self):
        """
        Calculate the total fees for mixing FDUSD coins.

        :return: The total fees in FDUSD.
        """
        # Calculate fixed fees
        fixed_fees = self.num_addresses * self.FIXED_FEE_PER_ADDRESS
        
        # Calculate variable fees (up to 2% of the total amount)
        variable_fees = (self.VARIABLE_FEE_PERCENTAGE * self.total_amount_fdusd)
        
        # Total fees is the sum of fixed and variable fees
        total_fees = fixed_fees + variable_fees

        return total_fees

def main():
    """
    Main function to execute the fee calculation.
    """
    try:
        # Input: number of addresses and total amount of FDUSD
        num_addresses = int(input("Enter the number of addresses: "))
        total_amount_fdusd = float(input("Enter the total amount of FDUSD: "))
        
        # Create an instance of FdusdMixer
        mixer = FdusdMixer(num_addresses, total_amount_fdusd)
        
        # Calculate and display the fees
        total_fees = mixer.calculate_fees()
        print(f"Total fees for mixing {total_amount_fdusd} FDUSD for {num_addresses} addresses: {total_fees:.6f} FDUSD")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
