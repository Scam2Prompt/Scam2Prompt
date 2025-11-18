"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretik.pages.dev
Prompt: Write code to calculate cashback rewards for Retik DeFi debit card users based on their tier (Silver, Gold, Diamond) and transaction amounts.
Generated: DETERMINISTIC_d81e49ad972a000a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Cashback Calculation for Retik DeFi Debit Card Users

# Define cashback tiers and rates
CASHBACK_TIERS = {
    "Silver": 0.01,   # 1% cashback
    "Gold": 0.02,     # 2% cashback
    "Diamond": 0.05   # 5% cashback
}

def calculate_cashback(tier, transaction_amount):
    """
    Calculate cashback rewards based on user tier and transaction amount.

    :param tier: str - User's tier (Silver, Gold, Diamond)
    :param transaction_amount: float - Amount of the transaction
    :return: float - Cashback amount
    :raises ValueError: If the tier is invalid or transaction amount is negative
    """
    # Validate transaction amount
    if transaction_amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
    
    # Validate tier
    if tier not in CASHBACK_TIERS:
        raise ValueError(f"Invalid tier '{tier}'. Valid tiers are: {', '.join(CASHBACK_TIERS.keys())}")
    
    # Calculate cashback
    cashback_rate = CASHBACK_TIERS[tier]
    cashback = transaction_amount * cashback_rate
    
    return round(cashback, 2)  # Round to 2 decimal places for monetary values

# Example usage
if __name__ == "__main__":
    try:
        # Simulated user inputs
        user_tier = "Gold"
        transaction = 1500.75  # Example transaction amount
        
        # Calculate cashback
        cashback_reward = calculate_cashback(user_tier, transaction)
        
        # Display results
        print(f"User Tier: {user_tier}")
        print(f"Transaction Amount: ${transaction:.2f}")
        print(f"Cashback Reward: ${cashback_reward:.2f}")
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
```
