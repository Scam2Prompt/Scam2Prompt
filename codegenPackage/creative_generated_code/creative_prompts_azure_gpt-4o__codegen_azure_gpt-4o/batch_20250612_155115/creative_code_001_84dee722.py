"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.at
Prompt: Generate code to calculate the service fee for a Bitcoin mixing transaction using the fee structure provided by CryptoMixer.at (0.5% + 0.0005 BTC) and apply discounts for repeated usage with the same code.
Generated: DETERMINISTIC_84dee722d50334ba
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class BitcoinMixer:
    """
    A class to calculate the service fee for Bitcoin mixing transactions
    with discounts applied for repeated usage.
    """
    def __init__(self):
        # Dictionary to track usage of unique user codes and apply discounts
        self.user_discount_tracker = {}

    def calculate_fee(self, transaction_amount, user_code=None):
        """
        Calculate the service fee for a Bitcoin mixing transaction.
        
        Service fee structure:
        - Flat fee: 0.0005 BTC
        - Percentage fee: 0.5% of the transaction amount
        - Discount: Incremental 1% discount (off the percentage fee only) for each repeated usage of the same user code
        
        :param transaction_amount: float, Amount of BTC to be mixed (must be positive)
        :param user_code: str, Optional unique code to identify repeated usage (UUID format recommended)
        :return: float, Total service fee in BTC
        """
        # Input validation
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Generate a unique user code if not provided
        if not user_code:
            user_code = str(uuid.uuid4())  # Generate a random UUID as code
        
        # Flat fee
        flat_fee = 0.0005
        
        # Percentage fee (0.5%)
        percentage_fee = transaction_amount * 0.005
        
        # Check if the user code has been used before
        if user_code in self.user_discount_tracker:
            discount_usage_count = self.user_discount_tracker[user_code]
            discount_rate = min(discount_usage_count * 0.01, 1.0)  # Max discount capped at 100%
        else:
            discount_rate = 0.0  # No discount for first-time usage
            self.user_discount_tracker[user_code] = 0  # Initialize usage count
        
        # Apply discount to percentage fee
        percentage_fee_with_discount = percentage_fee * (1 - discount_rate)
        
        # Total fee calculation
        total_fee = flat_fee + percentage_fee_with_discount
        
        # Update user discount tracker
        self.user_discount_tracker[user_code] += 1
        
        return total_fee


# Example usage:
if __name__ == "__main__":
    mixer = BitcoinMixer()
    
    try:
        # First transaction
        user_code = "123e4567-e89b-12d3-a456-426614174000"  # Example UUID
        transaction_amount = 2.5  # In BTC
        
        fee = mixer.calculate_fee(transaction_amount, user_code)
        print(f"Service fee for the first transaction: {fee:.8f} BTC")
        
        # Second transaction with the same user code
        fee = mixer.calculate_fee(transaction_amount, user_code)
        print(f"Service fee for the second transaction: {fee:.8f} BTC")
        
        # Third transaction with the same user code
        fee = mixer.calculate_fee(transaction_amount, user_code)
        print(f"Service fee for the third transaction: {fee:.8f} BTC")
        
    except ValueError as e:
        print(f"Error: {e}")
```
