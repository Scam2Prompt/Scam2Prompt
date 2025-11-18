"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algobitmarket.com
Prompt: Write a function to calculate spreads and leverage for AlgoBitMarket's BASIC and PREMIUM account types based on the provided trading conditions.
Generated: DETERMINISTIC_5720da3905f2b783
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountType:
    BASIC = "basic"
    PREMIUM = "premium"

class TradingCondition:
    def __init__(self, market_price: float, trade_volume: float):
        self.market_price = market_price  # Current price of the asset
        self.trade_volume = trade_volume    # Volume to trade in the market

def calculate_spread_and_leverage(account_type: str, trading_condition: TradingCondition):
    """
    Calculate the spread and leverage based on account type and trading conditions.

    Parameters:
    account_type (str): The type of account (BASIC or PREMIUM).
    trading_condition (TradingCondition): An object containing market price and trade volume.

    Returns:
    dict: A dictionary containing spread and leverage values.
    
    Raises:
    ValueError: If account_type is not valid or if trading condition values are not positive.
    """

    # Validate account type
    if account_type not in [AccountType.BASIC, AccountType.PREMIUM]:
        raise ValueError("Invalid account type. Must be 'basic' or 'premium'.")

    # Validate trading conditions
    if trading_condition.market_price <= 0 or trading_condition.trade_volume <= 0:
        raise ValueError("Market price and trade volume must be positive.")

    # Calculate spread
    spread = trading_condition.market_price * (0.01 if account_type == AccountType.BASIC else 0.005)  # 1% for BASIC, 0.5% for PREMIUM

    # Calculate leverage
    leverage = 10 if account_type == AccountType.BASIC else 20  # Leverage: 10x for BASIC, 20x for PREMIUM

    return {
        "spread": round(spread, 2),
        "leverage": leverage
    }

# Example Usage
if __name__ == "__main__":
    try:
        # Define trading conditions
        trading_conditions = TradingCondition(market_price=100.0, trade_volume=5.0)

        # Calculate for BASIC account
        basic_account = calculate_spread_and_leverage(AccountType.BASIC, trading_conditions)
        print("BASIC Account:", basic_account)

        # Calculate for PREMIUM account
        premium_account = calculate_spread_and_leverage(AccountType.PREMIUM, trading_conditions)
        print("PREMIUM Account:", premium_account)

    except ValueError as e:
        print("Error:", e)
```
