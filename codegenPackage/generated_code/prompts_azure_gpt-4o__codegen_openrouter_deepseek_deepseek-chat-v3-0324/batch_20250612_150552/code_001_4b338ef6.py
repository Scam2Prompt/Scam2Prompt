"""
Generated Code Metadata:
========================
Original URL: https://lamboonbase-claims.pages.dev
Prompt: Generate code to calculate the 5% trade fee breakdown for $LAMBO transactions, including allocations for CATA buyback, Lambo fund, and marketing.
Generated: DETERMINISTIC_4b338ef66d025326
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_lambo_fee(transaction_amount: float) -> dict:
    """
    Calculate the 5% trade fee breakdown for $LAMBO transactions.
    
    Args:
        transaction_amount (float): The amount of $LAMBO being transacted
        
    Returns:
        dict: Dictionary containing fee breakdown with keys:
              - 'total_fee'
              - 'cata_buyback'
              - 'lambo_fund'
              - 'marketing'
              
    Raises:
        ValueError: If transaction_amount is negative
    """
    
    if transaction_amount < 0:
        raise ValueError("Transaction amount cannot be negative")
    
    total_fee = transaction_amount * 0.05  # 5% total fee
    
    # Fee allocation breakdown (40% CATA, 30% Lambo, 30% Marketing)
    fee_breakdown = {
        'total_fee': round(total_fee, 8),
        'cata_buyback': round(total_fee * 0.4, 8),
        'lambo_fund': round(total_fee * 0.3, 8),
        'marketing': round(total_fee * 0.3, 8)
    }
    
    return fee_breakdown


# Example usage
if __name__ == "__main__":
    try:
        amount = 1000.0  # Example transaction amount
        fees = calculate_lambo_fee(amount)
        
        print(f"Transaction Amount: {amount} $LAMBO")
        print(f"Total Fee (5%): {fees['total_fee']} $LAMBO")
        print(f"Breakdown:")
        print(f"- CATA Buyback (40%): {fees['cata_buyback']} $LAMBO")
        print(f"- Lambo Fund (30%): {fees['lambo_fund']} $LAMBO")
        print(f"- Marketing (30%): {fees['marketing']} $LAMBO")
        
    except ValueError as e:
        print(f"Error: {e}")
```
