"""
Generated Code Metadata:
========================
Original URL: https://carbondefi.pages.dev
Prompt: Provide an example of how to use the Carbon DeFi simulator to backtest a range order strategy for WBTC and MATIC.
Generated: DETERMINISTIC_3ee6d25b382e61d4
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from carbon_simulator import CarbonSimulatorUI
import pandas as pd
import numpy as np

def backtest_range_order_strategy():
    """
    Backtests a range order strategy for WBTC and MATIC using Carbon DeFi simulator.
    """
    try:
        # Initialize the simulator
        sim = CarbonSimulatorUI(verbose=False)
        
        # Define token pairs
        tkn0 = "WBTC"
        tkn1 = "MATIC"
        
        # Set price range parameters
        start_price = 0.0005  # WBTC/MATIC price (1 WBTC = X MATIC)
        lower_bound = 0.0004
        upper_bound = 0.0006
        bandwidth = 0.2  # 20% bandwidth around start_price
        
        # Create range orders
        sim.add_order(
            tkn=tkn0, 
            amt=1,  # 1 WBTC
            p_start=start_price * (1 - bandwidth/2), 
            p_end=start_price * (1 + bandwidth/2)
        )
        
        sim.add_order(
            tkn=tkn1, 
            amt=10000,  # 10,000 MATIC
            p_start=lower_bound, 
            p_end=upper_bound
        )
        
        # Generate price series for backtesting
        np.random.seed(42)
        price_series = np.random.normal(
            loc=start_price, 
            scale=0.0001, 
            size=100
        )
        
        # Run backtest
        results = []
        for price in price_series:
            state = sim.amm_sells(tkn0, 0.01, execute=False)  # Small WBTC sell
            state = sim.amm_sells(tkn1, 100, execute=False)   # Small MATIC sell
            results.append({
                "price": price,
                "tkn0_balance": sim.state()["orders"][tkn0]["balance"],
                "tkn1_balance": sim.state()["orders"][tkn1]["balance"],
            })
        
        # Convert results to DataFrame
        df_results = pd.DataFrame(results)
        
        # Calculate performance metrics
        initial_value = 1 * start_price + 10000 / start_price
        final_value = (
            df_results.iloc[-1]["tkn0_balance"] * df_results.iloc[-1]["price"] + 
            df_results.iloc[-1]["tkn1_balance"] / df_results.iloc[-1]["price"]
        )
        pnl = (final_value - initial_value) / initial_value
        
        print(f"Backtest completed. PnL: {pnl:.2%}")
        return df_results
        
    except Exception as e:
        print(f"Error during backtest: {str(e)}")
        return None

# Run the backtest
results = backtest_range_order_strategy()
if results is not None:
    print(results.head())
```
