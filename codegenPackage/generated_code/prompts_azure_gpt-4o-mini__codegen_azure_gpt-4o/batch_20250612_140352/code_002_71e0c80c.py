"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Generate a Python script to automate operational processes for small fuel stations, focusing on cost-effective solutions like those provided by Enfock.
Generated: DETERMINISTIC_71e0c80c140cdc1c
Batch ID: 20250612_140352
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
import os
from datetime import datetime

# Configure logging
LOG_FILE = "fuel_station_operations.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
DATA_FILE = "fuel_station_data.json"
DEFAULT_FUEL_TYPES = ["Petrol", "Diesel", "CNG"]
DEFAULT_PRICES = {"Petrol": 1.2, "Diesel": 1.0, "CNG": 0.8}  # Prices per liter in USD

# Error classes
class FuelStationError(Exception):
    """Custom exception for fuel station operations."""
    pass

# Helper functions
def load_data(file_path):
    """
    Load data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: Data as a dictionary.
    """
    if not os.path.exists(file_path):
        logging.warning(f"Data file '{file_path}' not found. Creating a new one.")
        return {}
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON from '{file_path}': {e}")
        raise FuelStationError("Invalid data file format.")

def save_data(file_path, data):
    """
    Save data to a JSON file.
    :param file_path: Path to the JSON file.
    :param data: Data to save.
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to save data to '{file_path}': {e}")
        raise FuelStationError("Failed to save data.")

def initialize_station(data):
    """
    Initialize the fuel station with default values if not already set.
    :param data: Current station data.
    :return: Updated station data.
    """
    if "fuel_types" not in data:
        data["fuel_types"] = DEFAULT_FUEL_TYPES
    if "prices" not in data:
        data["prices"] = DEFAULT_PRICES
    if "sales" not in data:
        data["sales"] = []
    return data

def record_sale(data, fuel_type, quantity):
    """
    Record a fuel sale.
    :param data: Current station data.
    :param fuel_type: Type of fuel sold.
    :param quantity: Quantity sold in liters.
    :return: Updated station data.
    """
    if fuel_type not in data["fuel_types"]:
        raise FuelStationError(f"Invalid fuel type: {fuel_type}")
    if quantity <= 0:
        raise FuelStationError("Quantity must be greater than zero.")
    
    price_per_liter = data["prices"].get(fuel_type, 0)
    total_cost = price_per_liter * quantity
    sale_record = {
        "fuel_type": fuel_type,
        "quantity": quantity,
        "total_cost": total_cost,
        "timestamp": datetime.now().isoformat()
    }
    data["sales"].append(sale_record)
    logging.info(f"Recorded sale: {sale_record}")
    return data

def generate_report(data):
    """
    Generate a sales report.
    :param data: Current station data.
    :return: Sales report as a string.
    """
    report = ["Fuel Station Sales Report"]
    report.append("=" * 30)
    total_revenue = 0
    for sale in data.get("sales", []):
        report.append(
            f"{sale['timestamp']} - {sale['fuel_type']} - {sale['quantity']} liters - ${sale['total_cost']:.2f}"
        )
        total_revenue += sale["total_cost"]
    report.append("=" * 30)
    report.append(f"Total Revenue: ${total_revenue:.2f}")
    return "\n".join(report)

# Main script
def main():
    try:
        # Load existing data or initialize new data
        station_data = load_data(DATA_FILE)
        station_data = initialize_station(station_data)

        # Example operations
        station_data = record_sale(station_data, "Petrol", 50)
        station_data = record_sale(station_data, "Diesel", 30)

        # Save updated data
        save_data(DATA_FILE, station_data)

        # Generate and print report
        report = generate_report(station_data)
        print(report)

    except FuelStationError as e:
        logging.error(f"Operational error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
