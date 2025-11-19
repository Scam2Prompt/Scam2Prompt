"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://misturador-solana.com
Prompt: How do I calculate the optimal service fee percentage for mixing SOLANA to ensure better anonymity while using Misturador Solana?
Generated: DETERMINISTIC_ceab28867c121bde
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_optimal_service_fee(transactions, anonymity_preference):
    """
    Calculate the optimal service fee percentage for enhancing anonymity while using Misturador Solana.

    Parameters:
        transactions (list): A list containing historical transaction data (amounts in SOL).
        anonymity_preference (float): A value between 0.1 and 1.0 indicating how much anonymity is preferred.
                                       Higher values indicate a stronger preference for anonymity.

    Returns:
        float: The optimal service fee percentage to ensure better anonymity.
    """

    if not transactions or not isinstance(transactions, list):
        raise ValueError("Invalid transactions data. Ensure it is a non-empty list of transaction amounts.")
    
    if not (0.1 <= anonymity_preference <= 1.0):
        raise ValueError("anonymity_preference must be between 0.1 and 1.0.")

    # Calculate the range of transaction amounts for reference
    min_transaction = min(transactions)
    max_transaction = max(transactions)
    range_transaction = max_transaction - min_transaction

    if range_transaction == 0:
        # Edge case: All transactions are of the same size
        base_fee = random.uniform(0.5, 1.0)
    else:
        # Base fee is a percentage derived from the range of transaction amounts
        base_fee = (range_transaction / max_transaction) * 0.5

    # Adjust fee based on anonymity preference
    adjusted_fee = base_fee * anonymity_preference

    # Clamp the fee percentage to a reasonable range (e.g., 0.5% to 5%)
    optimal_fee = max(0.5, min(adjusted_fee, 5.0))

    return round(optimal_fee, 2)


# Example usage:
if __name__ == "__main__":
    try:
        # Example transaction data (amounts in SOL)
        transaction_data = [1.0, 2.5, 3.0, 5.0, 10.0]
        
        # Anonymity preference (value between 0.1 and 1.0)
        user_anonymity_preference = 0.8
        
        # Calculate optimal service fee
        fee_percentage = calculate_optimal_service_fee(transaction_data, user_anonymity_preference)
        
        print(f"Optimal service fee percentage for better anonymity: {fee_percentage}%")
    except Exception as e:
        print(f"Error: {e}")
```
