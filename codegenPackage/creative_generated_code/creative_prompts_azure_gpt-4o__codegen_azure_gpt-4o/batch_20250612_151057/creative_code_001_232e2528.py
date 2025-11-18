"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ststoned.pages.dev
Prompt: Generate code to calculate the slippage loss for withdrawing STONE tokens, considering the slippage protection limit of 0.3%.
Generated: DETERMINISTIC_232e2528f7a1e6cb
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
import sys

def calculate_slippage_loss(withdrawal_amount, market_price, slippage_limit=0.003):
    """
    Calculate the slippage loss for withdrawing STONE tokens.
    
    Args:
        withdrawal_amount (float): The number of STONE tokens to withdraw.
        market_price (float): The current market price of STONE tokens per unit.
        slippage_limit (float, optional): The slippage protection limit as a fraction 
                                          (default is 0.3% or 0.003).
    
    Returns:
        dict: A dictionary containing:
            - 'allowed_minimum_price': The minimum price allowed by slippage protection.
            - 'slippage_loss': The slippage loss incurred (if any).
            - 'status': A string indicating whether slippage is within the limit.
    Raises:
        ValueError: If withdrawal_amount or market_price is negative.
    """
    # Validate inputs
    if withdrawal_amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if market_price < 0:
        raise ValueError("Market price cannot be negative.")
    
    # Calculate the slippage protection threshold
    allowed_minimum_price = market_price * (1 - slippage_limit)
    
    # Simulate the actual price received during withdrawal (for demonstration)
    # In real-world applications, this would come from the exchange or trading system.
    actual_price_received = market_price * (1 - slippage_limit * 1.1)  # 10% beyond the limit for simulation
    
    # Calculate the slippage loss
    if actual_price_received < allowed_minimum_price:
        slippage_loss = withdrawal_amount * (market_price - actual_price_received)
        return {
            'allowed_minimum_price': allowed_minimum_price,
            'slippage_loss': slippage_loss,
            'status': "Slippage limit exceeded",
        }
    
    return {
        'allowed_minimum_price': allowed_minimum_price,
        'slippage_loss': 0.0,
        'status': "Slippage within acceptable limit",
    }


# Example usage
if __name__ == "__main__":
    try:
        # User inputs for the calculation
        withdrawal_amount = float(input("Enter the amount of STONE tokens to withdraw: "))
        market_price = float(input("Enter the current market price of STONE tokens: "))
        
        # Call the function to calculate slippage loss
        result = calculate_slippage_loss(withdrawal_amount, market_price)
        
        # Display the results
        print("\nSlippage Calculation Results:")
        print(f"Allowed Minimum Price: {result['allowed_minimum_price']:.6f}")
        print(f"Slippage Loss: {result['slippage_loss']:.6f}")
        print(f"Status: {result['status']}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
