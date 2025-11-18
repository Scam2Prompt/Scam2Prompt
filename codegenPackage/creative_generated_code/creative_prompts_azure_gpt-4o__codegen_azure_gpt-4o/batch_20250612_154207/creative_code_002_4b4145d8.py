"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hashminer.pro
Prompt: Create a script to calculate mining profitability using hash rate, power consumption, and cryptocurrency market data.
Generated: DETERMINISTIC_4b4145d8ed58ab4b
Batch ID: 20250612_154207
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol.lower()}&vs_currencies={currency.lower": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol.lower": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests  # For fetching cryptocurrency market data
import sys       # For graceful error handling

def fetch_crypto_price(crypto_symbol="BTC", currency="USD"):
    """
    Fetch the current price of a cryptocurrency in a specified fiat currency.
    :param crypto_symbol: The cryptocurrency symbol, e.g., 'BTC' for Bitcoin.
    :param currency: The fiat currency symbol, e.g., 'USD'.
    :return: The current price of the cryptocurrency in the specified fiat currency.
    """
    try:
        # Use a public API to fetch the price of the cryptocurrency
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol.lower()}&vs_currencies={currency.lower()}"
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data[crypto_symbol.lower()][currency.lower()]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cryptocurrency price: {e}", file=sys.stderr)
        return None
    except KeyError:
        print(f"Error parsing cryptocurrency price data.", file=sys.stderr)
        return None


def calculate_profitability(hash_rate, power_consumption, electricity_cost, block_reward, network_difficulty):
    """
    Calculate mining profitability based on hash rate, power consumption, electricity cost, and network statistics.
    :param hash_rate: Hash rate in TH/s (Terahashes per second).
    :param power_consumption: Power consumption in watts.
    :param electricity_cost: Electricity cost in USD per kWh.
    :param block_reward: Current block reward in cryptocurrency (e.g., BTC).
    :param network_difficulty: Current network difficulty.
    :return: Estimated profitability per day in USD.
    """
    try:
        # Constants
        SECONDS_PER_DAY = 86400  # Seconds in a day

        # Calculate the number of hashes per day (hash_rate * seconds in a day)
        hashes_per_day = hash_rate * 1e12 * SECONDS_PER_DAY  # Convert TH/s to hashes per day

        # Calculate the probability of finding a block
        probability = hashes_per_day / (network_difficulty * 2**32)

        # Calculate daily earnings in cryptocurrency
        daily_crypto_earnings = probability * block_reward

        # Fetch current cryptocurrency price
        crypto_price = fetch_crypto_price()
        if crypto_price is None:
            raise ValueError("Failed to retrieve cryptocurrency price.")

        # Convert daily earnings to USD
        daily_earnings_usd = daily_crypto_earnings * crypto_price

        # Calculate daily electricity costs
        daily_power_consumption_kwh = (power_consumption / 1000) * SECONDS_PER_DAY / 3600  # Convert watts to kWh
        daily_electricity_cost = daily_power_consumption_kwh * electricity_cost

        # Calculate profitability
        profitability = daily_earnings_usd - daily_electricity_cost
        return profitability
    except Exception as e:
        print(f"Error calculating profitability: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to prompt user for input and calculate mining profitability.
    """
    try:
        print("Welcome to the Mining Profitability Calculator")
        
        # Get user inputs
        hash_rate = float(input("Enter your hash rate in TH/s (e.g., 100): "))
        power_consumption = float(input("Enter your miner's power consumption in watts (e.g., 3000): "))
        electricity_cost = float(input("Enter your electricity cost in USD/kWh (e.g., 0.12): "))
        block_reward = float(input("Enter the current block reward (e.g., 6.25 for BTC): "))
        network_difficulty = float(input("Enter the current network difficulty (e.g., 20000000000000): "))

        # Calculate profitability
        profitability = calculate_profitability(hash_rate, power_consumption, electricity_cost, block_reward, network_difficulty)
        
        if profitability is not None:
            print(f"Estimated daily profitability: ${profitability:.2f} USD")
        else:
            print("Unable to calculate profitability due to an error.")
    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
