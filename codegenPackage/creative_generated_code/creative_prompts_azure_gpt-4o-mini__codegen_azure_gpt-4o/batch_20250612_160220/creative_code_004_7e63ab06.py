"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystakehomecrypto.com.neteliteoptions.com
Prompt: Develop an algorithm to calculate the profitability of Bitcoin mining based on the investment plans offered by Stake Home Crypto.
Generated: DETERMINISTIC_7e63ab064321dddd
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_mining_profitability(initial_investment, electricity_cost_per_kwh, hash_rate_th, power_consumption_w, mining_reward_btc, btc_to_usd_rate, mining_duration_days):
    """
    Calculate the profitability of Bitcoin mining based on investment parameters.

    Parameters:
    initial_investment (float): Initial investment in USD.
    electricity_cost_per_kwh (float): Electricity cost per kilowatt-hour in USD.
    hash_rate_th (float): Hash rate of the mining hardware in terahashes per second (TH/s).
    power_consumption_w (float): Power consumption of the mining hardware in watts.
    mining_reward_btc (float): Mining reward per day in BTC.
    btc_to_usd_rate (float): Conversion rate of BTC to USD.
    mining_duration_days (int): Duration of mining activity in days.

    Returns:
    dict: A dictionary containing profitability metrics like total revenue, total cost, net profit, and return on investment (ROI).
    """
    try:
        # Convert power consumption from watts to kilowatts
        power_consumption_kw = power_consumption_w / 1000

        # Calculate daily electricity cost
        daily_electricity_cost = power_consumption_kw * electricity_cost_per_kwh * 24

        # Total electricity cost for the mining duration
        total_electricity_cost = daily_electricity_cost * mining_duration_days

        # Total mining reward in BTC
        total_mining_reward_btc = mining_reward_btc * mining_duration_days

        # Convert mining reward to USD
        total_revenue_usd = total_mining_reward_btc * btc_to_usd_rate

        # Calculate total cost (initial investment + electricity cost)
        total_cost_usd = initial_investment + total_electricity_cost

        # Net profit calculation
        net_profit_usd = total_revenue_usd - total_cost_usd

        # ROI calculation (Return on Investment)
        roi_percentage = (net_profit_usd / initial_investment) * 100 if initial_investment > 0 else 0

        # Return results as a dictionary
        return {
            "Total Revenue (USD)": round(total_revenue_usd, 2),
            "Total Cost (USD)": round(total_cost_usd, 2),
            "Net Profit (USD)": round(net_profit_usd, 2),
            "ROI (%)": round(roi_percentage, 2)
        }
    except Exception as e:
        # Handle unexpected errors gracefully
        return {
            "Error": str(e)
        }


# Example usage:
if __name__ == "__main__":
    # Input parameters (use realistic values)
    initial_investment = 5000.00  # USD
    electricity_cost_per_kwh = 0.12  # USD/kWh
    hash_rate_th = 100.0  # TH/s (not directly used in this calculation)
    power_consumption_w = 3000.0  # Watts
    mining_reward_btc = 0.0005  # BTC per day
    btc_to_usd_rate = 27000.00  # USD per BTC
    mining_duration_days = 180  # Days

    # Calculate and print profitability metrics
    profitability = calculate_mining_profitability(
        initial_investment,
        electricity_cost_per_kwh,
        hash_rate_th,
        power_consumption_w,
        mining_reward_btc,
        btc_to_usd_rate,
        mining_duration_days
    )

    print("Bitcoin Mining Profitability Metrics:")
    for key, value in profitability.items():
        print(f"{key}: {value}")
```
