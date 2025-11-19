"""
Generated Code Metadata:
========================
Original URL: https://balancer.pages.dev
Prompt: Generate a Python script that calculates the profitability of pool mining based on current Bitcoin prices and mining difficulty, referencing the topic "Is pool mining worth it" from the Balancer website.
Generated: DETERMINISTIC_c649fed68f04ef4f
Batch ID: 20250612_135940
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://blockchain.info/q/getdifficulty": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime

# Constants
BITCOIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
BLOCKCHAIN_INFO_URL = "https://blockchain.info/q/getdifficulty"
POOL_FEE_PERCENTAGE = 0.01  # 1% pool fee assumption
HASH_RATE = 50 * 10**12  # 50 TH/s example hashrate
POWER_CONSUMPTION = 3000  # 3 kW example power consumption
ELECTRICITY_COST = 0.10  # $0.10 per kWh example cost
BLOCKS_PER_HOUR = 6  # Average blocks mined per hour
BLOCK_REWARD = 6.25  # Current Bitcoin block reward in BTC

def fetch_bitcoin_price():
    """Fetch current Bitcoin price in USD from CoinGecko API."""
    try:
        response = requests.get(BITCOIN_API_URL)
        response.raise_for_status()
        data = response.json()
        return data["bitcoin"]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def fetch_mining_difficulty():
    """Fetch current Bitcoin mining difficulty from blockchain.info."""
    try:
        response = requests.get(BLOCKCHAIN_INFO_URL)
        response.raise_for_status()
        return float(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching mining difficulty: {e}")
        return None

def calculate_profitability(bitcoin_price, difficulty):
    """
    Calculate mining profitability based on current price and difficulty.
    Returns a dictionary with profitability metrics.
    """
    if not bitcoin_price or not difficulty:
        return None

    # Calculate daily revenue
    daily_revenue_btc = (HASH_RATE * BLOCKS_PER_HOUR * 24 * BLOCK_REWARD) / (difficulty * 2**32)
    daily_revenue_usd = daily_revenue_btc * bitcoin_price

    # Apply pool fee
    daily_revenue_after_fee = daily_revenue_usd * (1 - POOL_FEE_PERCENTAGE)

    # Calculate daily costs
    daily_power_cost = POWER_CONSUMPTION * 24 * ELECTRICITY_COST / 1000  # Convert W to kW

    # Calculate profit
    daily_profit = daily_revenue_after_fee - daily_power_cost
    monthly_profit = daily_profit * 30
    yearly_profit = daily_profit * 365

    return {
        "bitcoin_price_usd": bitcoin_price,
        "mining_difficulty": difficulty,
        "daily_revenue_btc": daily_revenue_btc,
        "daily_revenue_usd": daily_revenue_usd,
        "daily_revenue_after_fee": daily_revenue_after_fee,
        "daily_power_cost": daily_power_cost,
        "daily_profit": daily_profit,
        "monthly_profit": monthly_profit,
        "yearly_profit": yearly_profit,
        "timestamp": datetime.now().isoformat()
    }

def display_results(results):
    """Display the profitability calculation results in a readable format."""
    if not results:
        print("Unable to calculate profitability due to missing data.")
        return

    print("\nBitcoin Mining Profitability Calculator")
    print("--------------------------------------")
    print(f"Current Bitcoin Price: ${results['bitcoin_price_usd']:,.2f}")
    print(f"Current Mining Difficulty: {results['mining_difficulty']:,.0f}")
    print(f"\nAssumptions:")
    print(f"- Hash Rate: {HASH_RATE / 10**12:,.0f} TH/s")
    print(f"- Power Consumption: {POWER_CONSUMPTION} W")
    print(f"- Electricity Cost: ${ELECTRICITY_COST}/kWh")
    print(f"- Pool Fee: {POOL_FEE_PERCENTAGE * 100}%")
    print("\nResults:")
    print(f"Daily BTC Mined: {results['daily_revenue_btc']:.8f} BTC")
    print(f"Daily Revenue (Before Fees): ${results['daily_revenue_usd']:,.2f}")
    print(f"Daily Revenue (After Fees): ${results['daily_revenue_after_fee']:,.2f}")
    print(f"Daily Power Cost: ${results['daily_power_cost']:,.2f}")
    print(f"Daily Profit: ${results['daily_profit']:,.2f}")
    print(f"Monthly Profit: ${results['monthly_profit']:,.2f}")
    print(f"Yearly Profit: ${results['yearly_profit']:,.2f}")
    print(f"\nCalculation Time: {results['timestamp']}")

def main():
    """Main function to execute the profitability calculation."""
    print("Fetching current Bitcoin data...")
    bitcoin_price = fetch_bitcoin_price()
    difficulty = fetch_mining_difficulty()

    if bitcoin_price and difficulty:
        results = calculate_profitability(bitcoin_price, difficulty)
        display_results(results)
    else:
        print("Failed to fetch required data for calculation.")

if __name__ == "__main__":
    main()
```
