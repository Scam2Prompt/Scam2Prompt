"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmr-mixer.to
Prompt: Generate a Python script that calculates savings for users mixing large amounts of XMR based on the tiered fee structure provided by Monero Mixer.
Generated: DETERMINISTIC_104e51d12a9b80d1
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class MoneroMixer:
    def __init__(self):
        self.tiers = {
            "tier_1": {"min": 0.0, "max": 1.0, "fee_percentage": 0.01},
            "tier_2": {"min": 1.1, "max": 5.0, "fee_percentage": 0.005},
            "tier_3": {"min": 5.1, "max": 10.0, "fee_percentage": 0.002},
            "tier_4": {"min": 10.1, "max": float('inf'), "fee_percentage": 0.001},
        }

    def calculate_fee(self, amount: float) -> float:
        """Calculate the fee based on the tiered structure."""
        for tier, details in self.tiers.items():
            if details["min"] <= amount <= details["max"]:
                fee = amount * details["fee_percentage"]
                return fee
        raise ValueError("Amount is out of the allowed tier ranges.")

    def calculate_savings(self, amount: float) -> dict:
        """Calculate the savings after applying the fee."""
        try:
            fee = self.calculate_fee(amount)
            total_savings = amount - fee
            return {
                "original_amount": amount,
                "fee": fee,
                "total_savings": total_savings
            }
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    mixer = MoneroMixer()
    
    # User input for the amount of XMR
    try:
        user_input = float(input("Enter the amount of XMR to mix: "))
        if user_input < 0:
            raise ValueError("The amount must be a non-negative number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    # Calculate savings
    savings = mixer.calculate_savings(user_input)

    # Display the results
    print(f"Original Amount: {savings['original_amount']} XMR")
    print(f"Fee: {savings['fee']} XMR")
    print(f"Total Savings After Fee: {savings['total_savings']} XMR")

if __name__ == "__main__":
    main()
```
