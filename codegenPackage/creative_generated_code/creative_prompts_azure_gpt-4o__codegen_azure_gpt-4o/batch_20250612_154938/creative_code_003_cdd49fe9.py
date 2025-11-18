"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riarus.ru
Prompt: Provide a code example for calculating potential profit and risk when trading perpetual contracts on Perpetual Protocol with up to 10x leverage. Use Python for the implementation.
Generated: DETERMINISTIC_cdd49fe9b1e4edad
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_trade_metrics(entry_price, exit_price, leverage, position_size, risk_percentage):
    """
    Calculates potential profit and risk for trading perpetual contracts with leverage.

    Args:
        entry_price (float): The price at which the trade is entered.
        exit_price (float): The price at which the trade is exited.
        leverage (int): The leverage multiplier (e.g., 10 for 10x leverage).
        position_size (float): The size of the position (in base currency).
        risk_percentage (float): The percentage of capital at risk.

    Returns:
        dict: A dictionary containing profit, risk, and liquidation price.
    """
    try:
        if leverage < 1 or leverage > 10:
            raise ValueError("Leverage must be between 1x and 10x inclusive.")
        
        if entry_price <= 0 or exit_price <= 0 or position_size <= 0:
            raise ValueError("Entry price, exit price, and position size must be positive values.")
        
        # Calculate profit
        profit = leverage * position_size * (exit_price - entry_price)
        
        # Calculate risk
        risk = position_size * entry_price * (risk_percentage / 100)
        
        # Calculate liquidation price
        liquidation_price = entry_price - (entry_price / leverage)
        
        return {
            "profit": profit,
            "risk": risk,
            "liquidation_price": liquidation_price
        }
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Input parameters
    entry_price = 100.0  # Example entry price
    exit_price = 110.0   # Example exit price
    leverage = 10        # Leverage used (e.g., 10x)
    position_size = 1.0  # Position size in base currency
    risk_percentage = 2  # Risk percentage of total capital

    metrics = calculate_trade_metrics(entry_price, exit_price, leverage, position_size, risk_percentage)
    
    if metrics:
        logging.info(f"Profit: {metrics['profit']:.2f}")
        logging.info(f"Risk: {metrics['risk']:.2f}")
        logging.info(f"Liquidation Price: {metrics['liquidation_price']:.2f}")
    else:
        logging.error("Failed to calculate trade metrics.")
```
