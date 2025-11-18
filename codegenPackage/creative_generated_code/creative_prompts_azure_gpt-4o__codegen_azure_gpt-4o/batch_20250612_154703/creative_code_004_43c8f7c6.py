"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Create a script to automate order and freight handling processes for the timber industry, referencing the case study of Setra's future-proofing efforts mentioned on ForestX's webpage.
Generated: DETERMINISTIC_43c8f7c6c08e5752
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated script for order and freight handling in the timber industry.

This program is designed to streamline processes by automating order 
and freight management for timber businesses, inspired by Setra's 
future-proofing efforts from a ForestX case study.

Author: Professional Software Developer
Language: Python
Version: Python 3.9+
"""

import logging
import json
import sys
from datetime import datetime

# Configure logging for monitoring script performance and errors
logging.basicConfig(
    filename="timber_order_freight.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Constants
ORDER_FILE = "orders.json"  # Path to order data file
FREIGHT_FILE = "freight.json"  # Path to freight data file
OUTPUT_FILE = "processed_orders.json"  # Path for processed output


class OrderProcessor:
    """
    Handles order processing and freight assignment for timber industry operations.
    """

    def __init__(self, orders, freight):
        """
        Initializes the OrderProcessor with order and freight data.

        Args:
            orders (list): List of order dictionaries.
            freight (list): List of freight options dictionaries.
        """
        self.orders = orders
        self.freight = freight

    def assign_freight(self, order):
        """
        Assigns the most suitable freight option to an order based on weight and distance.

        Args:
            order (dict): Single order dictionary.

        Returns:
            dict: Updated order dictionary with assigned freight.
        """
        suitable_freight = [
            f
            for f in self.freight
            if f["max_weight"] >= order["weight"] and f["max_distance"] >= order["distance"]
        ]

        if not suitable_freight:
            raise ValueError(f"No suitable freight found for order ID {order['order_id']}.")
        
        # Assigning the freight with the lowest cost
        assigned_freight = min(suitable_freight, key=lambda x: x["cost_per_km"])
        order["freight_assigned"] = assigned_freight["name"]
        order["freight_cost"] = order["distance"] * assigned_freight["cost_per_km"]

        return order

    def process_orders(self):
        """
        Processes all orders and assigns freight.

        Returns:
            list: List of processed orders with freight details.
        """
        processed_orders = []
        for order in self.orders:
            try:
                processed_order = self.assign_freight(order)
                logging.info(f"Order ID {order['order_id']} processed successfully.")
                processed_orders.append(processed_order)
            except ValueError as e:
                logging.error(f"Error processing order ID {order['order_id']}: {str(e)}")
        return processed_orders


def load_data(file_path):
    """
    Loads JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Parsed JSON data as a list of dictionaries.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        sys.exit(1)


def save_processed_orders(processed_orders, file_path):
    """
    Saves processed orders to a JSON file.

    Args:
        processed_orders (list): List of processed order dictionaries.
        file_path (str): Path to save the file.

    Returns:
        None
    """
    try:
        with open(file_path, "w") as file:
            json.dump(processed_orders, file, indent=4)
        logging.info(f"Processed orders saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error saving processed orders to file: {str(e)}")
        sys.exit(1)


def main():
    """
    Main function to orchestrate the automation of order and freight handling.
    """
    logging.info("Starting timber order and freight process automation.")

    # Load data
    orders = load_data(ORDER_FILE)
    freight = load_data(FREIGHT_FILE)

    # Process orders
    processor = OrderProcessor(orders, freight)
    processed_orders = processor.process_orders()

    # Save processed orders
    save_processed_orders(processed_orders, OUTPUT_FILE)

    logging.info("Order and freight process automation completed successfully.")


if __name__ == "__main__":
    main()
```
