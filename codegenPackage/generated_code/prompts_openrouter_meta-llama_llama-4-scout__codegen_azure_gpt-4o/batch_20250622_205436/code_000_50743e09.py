"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Write a Python script to evaluate and appraise oil and gas lease offers in Oklahoma, considering factors like location and market value.
Generated: DETERMINISTIC_50743e099fa70d1f
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeaseOffer:
    """
    Represents an oil and gas lease offer.
    """
    def __init__(self, location: str, acreage: float, bonus_per_acre: float, royalty_rate: float):
        """
        Initialize a lease offer.

        :param location: The location of the lease (e.g., county in Oklahoma).
        :param acreage: The size of the lease in acres.
        :param bonus_per_acre: The bonus payment per acre in USD.
        :param royalty_rate: The royalty rate as a percentage (e.g., 12.5 for 12.5%).
        """
        self.location = location
        self.acreage = acreage
        self.bonus_per_acre = bonus_per_acre
        self.royalty_rate = royalty_rate

    def calculate_total_bonus(self) -> float:
        """
        Calculate the total bonus payment for the lease.

        :return: Total bonus payment in USD.
        """
        return self.acreage * self.bonus_per_acre

    def evaluate_offer(self, market_bonus_per_acre: float, market_royalty_rate: float) -> Dict[str, str]:
        """
        Evaluate the lease offer against market values.

        :param market_bonus_per_acre: Average market bonus per acre in USD.
        :param market_royalty_rate: Average market royalty rate as a percentage.
        :return: Evaluation results as a dictionary.
        """
        evaluation = {
            "location": self.location,
            "bonus_evaluation": "Above Market" if self.bonus_per_acre > market_bonus_per_acre else "Below Market",
            "royalty_evaluation": "Above Market" if self.royalty_rate > market_royalty_rate else "Below Market",
        }
        return evaluation


def load_market_data(file_path: str) -> Dict[str, float]:
    """
    Load market data from a JSON file.

    :param file_path: Path to the JSON file containing market data.
    :return: Market data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            market_data = json.load(file)
        return market_data
    except FileNotFoundError:
        logging.error(f"Market data file not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        raise


def main():
    """
    Main function to evaluate oil and gas lease offers.
    """
    # Load market data
    market_data_file = "market_data.json"
    try:
        market_data = load_market_data(market_data_file)
        market_bonus_per_acre = market_data.get("bonus_per_acre", 0)
        market_royalty_rate = market_data.get("royalty_rate", 0)
    except Exception as e:
        logging.error(f"Failed to load market data: {e}")
        return

    # Example lease offers
    lease_offers = [
        LeaseOffer(location="Garfield County", acreage=100, bonus_per_acre=500, royalty_rate=12.5),
        LeaseOffer(location="Kingfisher County", acreage=200, bonus_per_acre=400, royalty_rate=15.0),
    ]

    # Evaluate each lease offer
    for offer in lease_offers:
        total_bonus = offer.calculate_total_bonus()
        evaluation = offer.evaluate_offer(market_bonus_per_acre, market_royalty_rate)

        logging.info(f"Lease Offer in {offer.location}:")
        logging.info(f"  Total Bonus: ${total_bonus:.2f}")
        logging.info(f"  Bonus Evaluation: {evaluation['bonus_evaluation']}")
        logging.info(f"  Royalty Evaluation: {evaluation['royalty_evaluation']}")


if __name__ == "__main__":
    main()
```
