"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltc-mixers.to
Prompt: Create a program that calculates the optimal mixing fee (between 1% and 5%) for a Litecoin mixer to maximize anonymity while minimizing costs. Include logic for setting a custom fee to prevent amount-based blockchain analysis.
Generated: DETERMINISTIC_7e85bceef5853d26
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LitecoinMixer:
    def __init__(self, min_fee=0.01, max_fee=0.05):
        """
        Initializes the LitecoinMixer with a minimum and maximum mixing fee.
        
        :param min_fee: Minimum mixing fee as a decimal (default is 1%).
        :param max_fee: Maximum mixing fee as a decimal (default is 5%).
        """
        self.min_fee = min_fee
        self.max_fee = max_fee

    def calculate_optimal_fee(self, transaction_amount):
        """
        Calculates the optimal mixing fee based on the transaction amount.
        
        :param transaction_amount: The amount of Litecoin to be mixed.
        :return: The optimal fee as a decimal and the fee amount.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Simple logic to determine fee based on transaction amount
        fee_percentage = self.min_fee + (self.max_fee - self.min_fee) * (transaction_amount / 10000)  # Scale fee
        fee_percentage = min(max(fee_percentage, self.min_fee), self.max_fee)  # Clamp to min and max

        fee_amount = transaction_amount * fee_percentage
        return fee_percentage, fee_amount

    def set_custom_fee(self, custom_fee):
        """
        Sets a custom mixing fee while ensuring it remains within the valid range.
        
        :param custom_fee: The desired custom fee as a decimal.
        """
        if custom_fee < self.min_fee or custom_fee > self.max_fee:
            raise ValueError(f"Custom fee must be between {self.min_fee*100}% and {self.max_fee*100}%.")
        self.custom_fee = custom_fee

    def mix(self, transaction_amount):
        """
        Simulates the mixing process with the calculated fee.
        
        :param transaction_amount: The amount of Litecoin to be mixed.
        :return: A summary of the mixing transaction.
        """
        fee_percentage, fee_amount = self.calculate_optimal_fee(transaction_amount)
        final_amount = transaction_amount - fee_amount

        return {
            "original_amount": transaction_amount,
            "fee_percentage": fee_percentage,
            "fee_amount": fee_amount,
            "final_amount": final_amount,
            "custom_fee": getattr(self, 'custom_fee', None)
        }

if __name__ == "__main__":
    try:
        mixer = LitecoinMixer()
        transaction_amount = float(input("Enter the amount of Litecoin to mix: "))
        
        # Optional: Set custom fee if desired (commented out for default behavior)
        # mixer.set_custom_fee(0.03)

        result = mixer.mix(transaction_amount)
        print("Mixing Summary:")
        print(f"Original Amount: {result['original_amount']} LTC")
        print(f"Fee Percentage: {result['fee_percentage'] * 100}%")
        print(f"Fee Amount: {result['fee_amount']} LTC")
        print(f"Final Amount After Mixing: {result['final_amount']} LTC")
        if result['custom_fee']:
            print(f"Custom Fee Set: {result['custom_fee'] * 100}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
