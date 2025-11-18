"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tjsftc.com
Prompt: Generate code to calculate and display the profitability of leveraged trading on Binance, factoring in margin requirements and fees.
Generated: DETERMINISTIC_a4ce34ab776f6f72
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_leveraged_profitability(initial_balance, leverage, entry_price, exit_price, margin_fee_rate, trading_fee_rate):
    """
    Calculate profitability of a leveraged trade on Binance.
    
    Parameters:
        initial_balance (float): The account balance available for trading.
        leverage (float): The leverage used for the trade.
        entry_price (float): The price at which the trade is entered.
        exit_price (float): The price at which the trade is exited.
        margin_fee_rate (float): The margin fee rate (percentage expressed as a decimal).
        trading_fee_rate (float): The trading fee rate (percentage expressed as a decimal).
    
    Returns:
        dict: A dictionary containing profit, fees breakdown, and net profit.
    """

    try:
        # Validate input
        if initial_balance <= 0 or leverage <= 0 or entry_price <= 0 or exit_price <= 0:
            raise ValueError("All monetary inputs (balance, entry/exit price) and leverage must be positive numbers.")
        if margin_fee_rate < 0 or trading_fee_rate < 0:
            raise ValueError("Fee rates cannot be negative.")

        # Calculate position size
        position_size = initial_balance * leverage

        # Calculate gross profit
        gross_profit = position_size * ((exit_price - entry_price) / entry_price)

        # Calculate margin fees
        margin_fee = position_size * margin_fee_rate

        # Calculate trading fees (fees apply for both entry and exit trades)
        entry_fee = position_size * trading_fee_rate
        exit_fee = (position_size + gross_profit) * trading_fee_rate  # Exit fee accounts for position size + profit

        # Total fees
        total_fees = margin_fee + entry_fee + exit_fee

        # Net profit after fees
        net_profit = gross_profit - total_fees

        # Build and return result dictionary
        return {
            'gross_profit': gross_profit,
            'margin_fee': margin_fee,
            'entry_fee': entry_fee,
            'exit_fee': exit_fee,
            'total_fees': total_fees,
            'net_profit': net_profit,
        }

    except Exception as e:
        print(f"Error calculating leveraged profitability: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example inputs
    initial_balance = 1000.0  # Your initial account balance in USD
    leverage = 10.0           # Leverage used for the trade
    entry_price = 20000.0     # Entry price of the trade
    exit_price = 22000.0      # Exit price of the trade
    margin_fee_rate = 0.002   # Margin fee rate (0.2%)
    trading_fee_rate = 0.0004 # Trading fee rate (0.04%)

    # Calculate profitability
    result = calculate_leveraged_profitability(
        initial_balance,
        leverage,
        entry_price,
        exit_price,
        margin_fee_rate,
        trading_fee_rate
    )

    # Display results
    if result:
        print("Leveraged Trading Profitability:")
        print(f"Gross Profit: ${result['gross_profit']:.2f}")
        print(f"Margin Fee: ${result['margin_fee']:.2f}")
        print(f"Entry Fee: ${result['entry_fee']:.2f}")
        print(f"Exit Fee: ${result['exit_fee']:.2f}")
        print(f"Total Fees: ${result['total_fees']:.2f}")
        print(f"Net Profit: ${result['net_profit']:.2f}")
```
