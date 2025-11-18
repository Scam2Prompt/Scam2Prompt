"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Suggest an approach to handle faulty asset reporting and correction in a price monitoring system, referencing the PDL Watch Dog's methodology.
Generated: DETERMINISTIC_caaebb81634dde1d
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PriceMonitoringSystem:
    def __init__(self):
        # Store asset prices
        self.asset_prices: Dict[str, List[float]] = {}

    def report_asset_price(self, asset_id: str, price: float) -> None:
        """
        Report the price of an asset and log the event.

        :param asset_id: Identifier for the asset
        :param price: Reported price of the asset
        """
        if price < 0:
            logging.error(f"Attempted to report a negative price for asset {asset_id}. Price: {price}")
            raise ValueError("Price cannot be negative.")

        # Append the price to the asset's price list
        if asset_id not in self.asset_prices:
            self.asset_prices[asset_id] = []

        self.asset_prices[asset_id].append(price)
        logging.info(f"Reported price {price} for asset {asset_id}.")

    def detect_faulty_reports(self, threshold: float) -> List[str]:
        """
        Identify assets with faulty reports based on a threshold.

        :param threshold: The percentage change threshold to identify faults
        :return: List of asset IDs with detected faulty reports
        """
        faulty_assets = []

        for asset_id, prices in self.asset_prices.items():
            if len(prices) < 2:
                continue  # Need at least two prices to compare

            # Calculate percentage change
            last_price = prices[-1]
            previous_price = prices[-2]
            percentage_change = abs((last_price - previous_price) / previous_price) * 100

            if percentage_change > threshold:
                logging.warning(f"Detected faulty report for asset {asset_id}: {percentage_change:.2f}% change.")
                faulty_assets.append(asset_id)

        return faulty_assets

    def correct_faulty_reports(self, asset_id: str, corrected_price: float) -> None:
        """
        Correct the faulty report for a given asset.

        :param asset_id: Identifier for the asset
        :param corrected_price: The corrected price to be set
        """
        if asset_id not in self.asset_prices:
            logging.error(f"Attempted to correct a non-existent asset {asset_id}.")
            raise KeyError(f"Asset {asset_id} does not exist in the reporting system.")

        if corrected_price < 0:
            logging.error(f"Attempted to report a negative corrected price for asset {asset_id}. Corrected Price: {corrected_price}")
            raise ValueError("Corrected price cannot be negative.")

        # Replace last reported price with the corrected price
        self.asset_prices[asset_id][-1] = corrected_price
        logging.info(f"Corrected price for asset {asset_id} to {corrected_price}.")

# Example usage
if __name__ == "__main__":
    pms = PriceMonitoringSystem()

    try:
        pms.report_asset_price("asset_1", 100.0)
        pms.report_asset_price("asset_1", 120.0)
        pms.report_asset_price("asset_1", 500.0)  # Faulty report
        pms.report_asset_price("asset_1", 125.0)

        # Detect faulty reports with a threshold of 50%
        faulty_reports = pms.detect_faulty_reports(threshold=50.0)
        logging.info(f"Faulty reports detected for assets: {faulty_reports}")

        # Correct the faulty report
        if faulty_reports:
            pms.correct_faulty_reports(faulty_reports[0], 110.0)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
