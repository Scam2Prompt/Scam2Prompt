"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Write a Python script to automate the ordering process for printing services like business cards and flyers, similar to what Detalj Reklam & Tryckeri offers."
Generated: DETERMINISTIC_874343962236bf43
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# printing_services_automation.py

import os
import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class PrintingService(Enum):
    """Enum for printing services."""
    BUSINESS_CARDS = "business_cards"
    FLYERS = "flyers"

@dataclass
class OrderItem:
    """Dataclass for order items."""
    service: PrintingService
    quantity: int
    size: str
    paper_type: str
    color: str

class PrintingServiceAutomation:
    """Class for automating printing services ordering process."""

    def __init__(self, config_file: str = "config.json"):
        """Initialize the automation with a config file."""
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Config file {self.config_file} not found.")
            self.config = {}

    def save_config(self):
        """Save configuration to a JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def place_order(self, order_items: List[OrderItem]):
        """Place an order with the given order items."""
        order_summary = []
        total_cost = 0

        for item in order_items:
            service = item.service
            quantity = item.quantity
            size = item.size
            paper_type = item.paper_type
            color = item.color

            # Calculate cost based on service, quantity, size, paper type, and color
            cost = self.calculate_cost(service, quantity, size, paper_type, color)
            order_summary.append({
                "service": service.value,
                "quantity": quantity,
                "size": size,
                "paper_type": paper_type,
                "color": color,
                "cost": cost
            })
            total_cost += cost

        # Save order to config
        if "orders" not in self.config:
            self.config["orders"] = []
        self.config["orders"].append({
            "order_summary": order_summary,
            "total_cost": total_cost
        })
        self.save_config()

        return order_summary, total_cost

    def calculate_cost(self, service: PrintingService, quantity: int, size: str, paper_type: str, color: str):
        """Calculate the cost of an order item."""
        # For demonstration purposes, assume costs are as follows:
        costs = {
            PrintingService.BUSINESS_CARDS: 0.5,
            PrintingService.FLYERS: 0.2
        }
        return costs[service] * quantity

def main():
    automation = PrintingServiceAutomation()

    # Example usage
    order_items = [
        OrderItem(PrintingService.BUSINESS_CARDS, 100, "A6", "Glossy", "Full Color"),
        OrderItem(PrintingService.FLYERS, 500, "A4", "Matte", "Black and White")
    ]

    order_summary, total_cost = automation.place_order(order_items)

    print("Order Summary:")
    for item in order_summary:
        print(f"Service: {item['service']}, Quantity: {item['quantity']}, Size: {item['size']}, Paper Type: {item['paper_type']}, Color: {item['color']}, Cost: ${item['cost']:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
