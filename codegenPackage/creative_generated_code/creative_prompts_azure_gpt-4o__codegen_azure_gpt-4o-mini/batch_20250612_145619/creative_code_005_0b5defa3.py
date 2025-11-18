"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfor.com
Prompt: Develop a function to calculate fees for transactions on the TonFOR platform, considering the pool type and token denomination.
Generated: DETERMINISTIC_0b5defa3f629b3a7
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionFeeCalculator:
    """
    A class to calculate transaction fees on the TonFOR platform based on the pool type and token denomination.
    """

    # Define fee structure based on pool types and token denominations
    BASE_FEES = {
        'standard': {
            'ton': 0.01,  # 1% for TON
            'other': 0.02  # 2% for other tokens
        },
        'premium': {
            'ton': 0.005,  # 0.5% for TON
            'other': 0.015  # 1.5% for other tokens
        }
    }

    @staticmethod
    def calculate_fee(pool_type: str, token_type: str, transaction_amount: float) -> float:
        """
        Calculate the transaction fee based on pool type, token type, and transaction amount.

        Args:
            pool_type (str): The type of pool ('standard' or 'premium').
            token_type (str): The type of token ('ton' or 'other').
            transaction_amount (float): The total transaction amount.

        Returns:
            float: The calculated transaction fee.

        Raises:
            ValueError: If the pool type or token type is invalid or if the transaction amount is negative.
        """
        # Validate input parameters
        if pool_type not in TransactionFeeCalculator.BASE_FEES:
            raise ValueError(f"Invalid pool type: {pool_type}. Expected 'standard' or 'premium'.")
        
        if token_type not in TransactionFeeCalculator.BASE_FEES[pool_type]:
            raise ValueError(f"Invalid token type: {token_type}. Expected 'ton' or 'other'.")

        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")

        # Calculate the fee based on the pool type and token type
        fee_rate = TransactionFeeCalculator.BASE_FEES[pool_type][token_type]
        fee = fee_rate * transaction_amount

        return round(fee, 2)  # Round to two decimal places for currency representation


# Example usage:
if __name__ == "__main__":
    try:
        fee = TransactionFeeCalculator.calculate_fee('standard', 'ton', 100.00)
        print(f"Transaction Fee: {fee} TON")
    except ValueError as e:
        print(f"Error calculating fee: {e}")
```
