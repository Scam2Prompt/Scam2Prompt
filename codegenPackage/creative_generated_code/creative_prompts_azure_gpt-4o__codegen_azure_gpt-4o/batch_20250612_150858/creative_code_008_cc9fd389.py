"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.to
Prompt: Generate code to simulate the TON mixing process, including input validation, fee selection, and transfer delay configuration, as described on ton-mixer.to.
Generated: DETERMINISTIC_cc9fd389f379dd1e
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class TONMixer:
    def __init__(self):
        # Initialize fee tiers (percentage of total amount mixed)
        self.fee_tiers = {
            "low": 0.005,  # 0.5%
            "medium": 0.01,  # 1%
            "high": 0.02  # 2%
        }
        # Initialize possible transfer delay ranges (in seconds)
        self.delay_ranges = {
            "short": (60, 300),  # 1 to 5 minutes
            "medium": (300, 900),  # 5 to 15 minutes
            "long": (900, 1800)  # 15 to 30 minutes
        }

    def validate_inputs(self, amount, fee_type, delay_type):
        """
        Validates the user inputs for amount, fee_type, and delay_type.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if fee_type not in self.fee_tiers:
            raise ValueError(f"Fee type must be one of {list(self.fee_tiers.keys())}.")
        if delay_type not in self.delay_ranges:
            raise ValueError(f"Delay type must be one of {list(self.delay_ranges.keys())}.")

    def calculate_fee(self, amount, fee_type):
        """
        Calculates the fee for the selected fee type.
        """
        fee_percentage = self.fee_tiers[fee_type]
        return amount * fee_percentage

    def get_transfer_delay(self, delay_type):
        """
        Returns a random transfer delay within the selected delay range.
        """
        delay_range = self.delay_ranges[delay_type]
        return random.randint(*delay_range)

    def mix_ton(self, amount, fee_type, delay_type):
        """
        Simulates the TON mixing process.
        """
        # Validate inputs
        self.validate_inputs(amount, fee_type, delay_type)

        # Calculate fee and final transfer amount
        fee = self.calculate_fee(amount, fee_type)
        final_amount = amount - fee

        # Configure transfer delay
        transfer_delay = self.get_transfer_delay(delay_type)

        print(f"TON Mixing started...")
        print(f"Amount: {amount:.2f} TON")
        print(f"Fee: {fee:.2f} TON ({fee_type.capitalize()} tier)")
        print(f"Final Transfer Amount: {final_amount:.2f} TON")
        print(f"Transfer delay: {transfer_delay} seconds")

        # Simulate transfer delay
        time.sleep(transfer_delay)

        print("Transfer completed successfully!")

if __name__ == "__main__":
    # Example usage
    try:
        mixer = TONMixer()
        amount = float(input("Enter the amount to mix (TON): "))
        fee_type = input("Select fee type (low, medium, high): ").strip().lower()
        delay_type = input("Select transfer delay type (short, medium, long): ").strip().lower()

        mixer.mix_ton(amount, fee_type, delay_type)
    except Exception as e:
        print(f"Error: {e}")
```
