"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://envisiontradezone.com
Prompt: Generate a script to automate cryptocurrency mining portfolio creation, referencing Envisiontradezone's features for mining strategies.
Generated: DETERMINISTIC_419d00d40f476523
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("portfolio_creation.log"),
        logging.StreamHandler()
    ]
)

# Constants
SUPPORTED_CRYPTOS = ['BTC', 'ETH', 'LTC', 'DOGE']  # List of supported cryptocurrencies
DEFAULT_PORTFOLIO_NAME = "My Mining Portfolio"

# Function to validate cryptocurrency
def validate_crypto(crypto):
    """
    Validates if the cryptocurrency is supported.

    :param crypto: Cryptocurrency symbol (e.g., 'BTC')
    :return: True if supported, False otherwise
    """
    return crypto.upper() in SUPPORTED_CRYPTOS

# Function to create a mining strategy
def create_mining_strategy(crypto):
    """
    Creates a mining strategy reference based on Envisiontradezone's features.

    :param crypto: Cryptocurrency symbol (e.g., 'BTC')
    :return: Dictionary containing the mining strategy
    """
    # Placeholder for actual Envisiontradezone integration
    # Currently generates a sample strategy
    return {
        "crypto": crypto.upper(),
        "hash_rate": "Medium",
        "electricity_cost": "Standard",
        "pool_preference": "Auto-select"
    }

# Function to create a cryptocurrency mining portfolio
def create_portfolio(name, cryptos):
    """
    Creates a cryptocurrency mining portfolio.

    :param name: Portfolio name
    :param cryptos: List of cryptocurrency symbols
    :return: Portfolio dictionary
    """
    logging.info("Starting portfolio creation...")
    portfolio = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "strategies": []
    }

    for crypto in cryptos:
        if not validate_crypto(crypto):
            logging.warning(f"Skipping unsupported cryptocurrency: {crypto}")
            continue
        
        strategy = create_mining_strategy(crypto)
        portfolio["strategies"].append(strategy)
        logging.info(f"Added strategy for {crypto}")

    logging.info("Portfolio creation completed.")
    return portfolio

# Main function
def main():
    """
    Main script function to automate cryptocurrency mining portfolio creation.
    """
    try:
        # User inputs
        portfolio_name = input(f"Enter portfolio name (default '{DEFAULT_PORTFOLIO_NAME}'): ") or DEFAULT_PORTFOLIO_NAME
        cryptos = input(f"Enter cryptocurrency symbols separated by commas (e.g., BTC,ETH): ").split(',')

        # Create and display portfolio
        portfolio = create_portfolio(portfolio_name.strip(), [crypto.strip() for crypto in cryptos])
        portfolio_json = json.dumps(portfolio, indent=4)
        
        # Save portfolio to JSON file
        with open("portfolio.json", "w") as json_file:
            json_file.write(portfolio_json)
        
        logging.info("Portfolio saved to 'portfolio.json'")
        print("Portfolio created successfully:")
        print(portfolio_json)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("An error occurred. Please check the logs for details.")

# Entry point
if __name__ == "__main__":
    main()
```
