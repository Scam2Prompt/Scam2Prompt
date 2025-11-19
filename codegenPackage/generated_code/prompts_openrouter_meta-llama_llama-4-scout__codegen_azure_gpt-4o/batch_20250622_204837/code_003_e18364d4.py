"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Design a system to enable gas stations to customize their loyalty offerings for customers using CRUDO tokens for payments, including discounts, freebies, or exclusive deals."
Generated: DETERMINISTIC_e18364d4849b6742
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: loyalty_system.py

import json
from typing import List, Dict

# Custom exception for the loyalty system
class LoyaltySystemError(Exception):
    pass

# Class representing a gas station
class GasStation:
    def __init__(self, station_id: str, name: str):
        """
        Initialize a gas station with a unique ID and name.
        :param station_id: Unique identifier for the gas station.
        :param name: Name of the gas station.
        """
        self.station_id = station_id
        self.name = name
        self.loyalty_offers = []  # List to store loyalty offers

    def add_loyalty_offer(self, offer: Dict):
        """
        Add a loyalty offer to the gas station.
        :param offer: Dictionary containing offer details (e.g., discount, freebies, etc.).
        """
        if not isinstance(offer, dict):
            raise LoyaltySystemError("Offer must be a dictionary.")
        self.loyalty_offers.append(offer)

    def get_loyalty_offers(self) -> List[Dict]:
        """
        Retrieve all loyalty offers for the gas station.
        :return: List of loyalty offers.
        """
        return self.loyalty_offers

# Class representing a customer
class Customer:
    def __init__(self, customer_id: str, name: str, crudo_balance: float):
        """
        Initialize a customer with a unique ID, name, and CRUDO token balance.
        :param customer_id: Unique identifier for the customer.
        :param name: Name of the customer.
        :param crudo_balance: Initial balance of CRUDO tokens.
        """
        self.customer_id = customer_id
        self.name = name
        self.crudo_balance = crudo_balance

    def make_payment(self, amount: float):
        """
        Deduct CRUDO tokens from the customer's balance for a payment.
        :param amount: Amount of CRUDO tokens to deduct.
        """
        if amount > self.crudo_balance:
            raise LoyaltySystemError("Insufficient CRUDO balance.")
        self.crudo_balance -= amount

    def get_balance(self) -> float:
        """
        Retrieve the customer's current CRUDO token balance.
        :return: Current CRUDO token balance.
        """
        return self.crudo_balance

# Class representing the loyalty system
class LoyaltySystem:
    def __init__(self):
        """
        Initialize the loyalty system with empty lists for gas stations and customers.
        """
        self.gas_stations = {}  # Dictionary to store gas stations by ID
        self.customers = {}     # Dictionary to store customers by ID

    def register_gas_station(self, station_id: str, name: str):
        """
        Register a new gas station in the system.
        :param station_id: Unique identifier for the gas station.
        :param name: Name of the gas station.
        """
        if station_id in self.gas_stations:
            raise LoyaltySystemError("Gas station ID already exists.")
        self.gas_stations[station_id] = GasStation(station_id, name)

    def register_customer(self, customer_id: str, name: str, crudo_balance: float):
        """
        Register a new customer in the system.
        :param customer_id: Unique identifier for the customer.
        :param name: Name of the customer.
        :param crudo_balance: Initial balance of CRUDO tokens.
        """
        if customer_id in self.customers:
            raise LoyaltySystemError("Customer ID already exists.")
        self.customers[customer_id] = Customer(customer_id, name, crudo_balance)

    def apply_loyalty_offer(self, customer_id: str, station_id: str, offer_id: int):
        """
        Apply a loyalty offer to a customer at a specific gas station.
        :param customer_id: Unique identifier for the customer.
        :param station_id: Unique identifier for the gas station.
        :param offer_id: Index of the loyalty offer in the gas station's offer list.
        """
        if customer_id not in self.customers:
            raise LoyaltySystemError("Customer not found.")
        if station_id not in self.gas_stations:
            raise LoyaltySystemError("Gas station not found.")

        customer = self.customers[customer_id]
        gas_station = self.gas_stations[station_id]

        try:
            offer = gas_station.get_loyalty_offers()[offer_id]
        except IndexError:
            raise LoyaltySystemError("Invalid offer ID.")

        # Deduct CRUDO tokens if the offer requires payment
        if "price" in offer:
            customer.make_payment(offer["price"])

        return offer

    def export_data(self, file_path: str):
        """
        Export the loyalty system data to a JSON file.
        :param file_path: Path to the JSON file.
        """
        data = {
            "gas_stations": {
                station_id: {
                    "name": station.name,
                    "loyalty_offers": station.get_loyalty_offers()
                }
                for station_id, station in self.gas_stations.items()
            },
            "customers": {
                customer_id: {
                    "name": customer.name,
                    "crudo_balance": customer.get_balance()
                }
                for customer_id, customer in self.customers.items()
            }
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def import_data(self, file_path: str):
        """
        Import loyalty system data from a JSON file.
        :param file_path: Path to the JSON file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)

        self.gas_stations = {
            station_id: GasStation(station_id, station_data["name"])
            for station_id, station_data in data["gas_stations"].items()
        }
        for station_id, station_data in data["gas_stations"].items():
            for offer in station_data["loyalty_offers"]:
                self.gas_stations[station_id].add_loyalty_offer(offer)

        self.customers = {
            customer_id: Customer(
                customer_id,
                customer_data["name"],
                customer_data["crudo_balance"]
            )
            for customer_id, customer_data in data["customers"].items()
        }

# Example usage (uncomment to test):
# loyalty_system = LoyaltySystem()
# loyalty_system.register_gas_station("station1", "Gas Station 1")
# loyalty_system.register_customer("customer1", "John Doe", 100.0)
# loyalty_system.gas_stations["station1"].add_loyalty_offer({"description": "10% off", "price": 10.0})
# offer = loyalty_system.apply_loyalty_offer("customer1", "station1", 0)
# print("Applied Offer:", offer)
# print("Customer Balance:", loyalty_system.customers["customer1"].get_balance())
# loyalty_system.export_data("loyalty_data.json")
# loyalty_system.import_data("loyalty_data.json")
```
