"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocols.web.app
Prompt: "Design a data management system for Crudo Protocol's comprehensive data and risk management solutions for oil and gas businesses, including live commodities price updates and ship AIS tracking."
Generated: DETERMINISTIC_a056c18b3009a288
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_management_system.py

import logging
import os
import json
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class CommodityPrice:
    """Represents a commodity price update."""

    def __init__(self, symbol: str, price: float, timestamp: datetime):
        """
        Initializes a CommodityPrice object.

        Args:
        - symbol (str): The commodity symbol (e.g., "WTI", "BRENT").
        - price (float): The current price of the commodity.
        - timestamp (datetime): The timestamp of the price update.
        """
        self.symbol = symbol
        self.price = price
        self.timestamp = timestamp

class ShipAIS:
    """Represents a ship's AIS (Automatic Identification System) data."""

    def __init__(self, ship_id: int, latitude: float, longitude: float, timestamp: datetime):
        """
        Initializes a ShipAIS object.

        Args:
        - ship_id (int): The unique identifier of the ship.
        - latitude (float): The current latitude of the ship.
        - longitude (float): The current longitude of the ship.
        - timestamp (datetime): The timestamp of the AIS data.
        """
        self.ship_id = ship_id
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

class DataManagementSystem:
    """Manages comprehensive data and risk management solutions for oil and gas businesses."""

    def __init__(self):
        """
        Initializes a DataManagementSystem object.
        """
        self.commodity_prices: Dict[str, CommodityPrice] = {}
        self.ship_ais_data: Dict[int, ShipAIS] = {}

    def update_commodity_price(self, symbol: str, price: float):
        """
        Updates the price of a commodity.

        Args:
        - symbol (str): The commodity symbol (e.g., "WTI", "BRENT").
        - price (float): The current price of the commodity.

        Raises:
        - ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.commodity_prices[symbol] = CommodityPrice(symbol, price, datetime.now())
        logging.info(f"Updated commodity price: {symbol} = {price}")

    def update_ship_ais_data(self, ship_id: int, latitude: float, longitude: float):
        """
        Updates the AIS data of a ship.

        Args:
        - ship_id (int): The unique identifier of the ship.
        - latitude (float): The current latitude of the ship.
        - longitude (float): The current longitude of the ship.

        Raises:
        - ValueError: If the latitude or longitude is out of range.
        """
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        self.ship_ais_data[ship_id] = ShipAIS(ship_id, latitude, longitude, datetime.now())
        logging.info(f"Updated ship AIS data: Ship {ship_id} at ({latitude}, {longitude})")

    def get_commodity_price(self, symbol: str) -> float:
        """
        Retrieves the current price of a commodity.

        Args:
        - symbol (str): The commodity symbol (e.g., "WTI", "BRENT").

        Returns:
        - float: The current price of the commodity.

        Raises:
        - KeyError: If the commodity symbol is not found.
        """
        try:
            return self.commodity_prices[symbol].price
        except KeyError:
            logging.error(f"Commodity symbol not found: {symbol}")
            raise

    def get_ship_ais_data(self, ship_id: int) -> Dict[str, float]:
        """
        Retrieves the current AIS data of a ship.

        Args:
        - ship_id (int): The unique identifier of the ship.

        Returns:
        - Dict[str, float]: A dictionary containing the ship's latitude and longitude.

        Raises:
        - KeyError: If the ship ID is not found.
        """
        try:
            ship_ais = self.ship_ais_data[ship_id]
            return {"latitude": ship_ais.latitude, "longitude": ship_ais.longitude}
        except KeyError:
            logging.error(f"Ship ID not found: {ship_id}")
            raise

def main():
    # Create a data management system
    dms = DataManagementSystem()

    # Update commodity prices
    dms.update_commodity_price("WTI", 75.50)
    dms.update_commodity_price("BRENT", 82.25)

    # Update ship AIS data
    dms.update_ship_ais_data(1234, 37.7749, -122.4194)
    dms.update_ship_ais_data(5678, 40.7128, -74.0060)

    # Retrieve commodity prices
    print(dms.get_commodity_price("WTI"))  # Output: 75.50
    print(dms.get_commodity_price("BRENT"))  # Output: 82.25

    # Retrieve ship AIS data
    print(json.dumps(dms.get_ship_ais_data(1234), indent=4))  # Output: {"latitude": 37.7749, "longitude": -122.4194}
    print(json.dumps(dms.get_ship_ais_data(5678), indent=4))  # Output: {"latitude": 40.7128, "longitude": -74.006}

if __name__ == "__main__":
    main()
```
