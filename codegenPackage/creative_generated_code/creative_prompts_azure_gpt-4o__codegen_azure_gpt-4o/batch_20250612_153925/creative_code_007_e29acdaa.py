"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominingtoken.web.app
Prompt: Create a script to track and display recent purchases of GoMining digital miners, including miner type, power, and holder details.
Generated: DETERMINISTIC_e29acdaa441ba894
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

# Simulated database for purchases
class GoMiningPurchasesDatabase:
    def __init__(self):
        self.purchases = []

    def add_purchase(self, purchase):
        """Add a new purchase to the database."""
        self.purchases.append(purchase)

    def get_recent_purchases(self, count=10):
        """Retrieve the most recent `count` purchases."""
        return sorted(self.purchases, key=lambda x: x['timestamp'], reverse=True)[:count]

# Function to validate purchase data
def validate_purchase_data(purchase):
    """
    Validate purchase data for required fields.
    :param purchase: Dictionary containing purchase details.
    :return: True if valid, False otherwise.
    """
    required_keys = {"miner_type", "power", "holder_details"}
    return all(key in purchase for key in required_keys)

# Function to display purchases
def display_purchases(purchases):
    """
    Display a list of purchases in a user-friendly format.
    :param purchases: List of dictionaries containing purchase details.
    """
    print("Recent Purchases:")
    print("=" * 50)
    for purchase in purchases:
        print(f"Miner Type: {purchase['miner_type']}")
        print(f"Power: {purchase['power']} TH/s")
        print(f"Holder Details: {purchase['holder_details']}")
        print(f"Timestamp: {purchase['timestamp']}")
        print("-" * 50)

# Main script
def main():
    # Initialize the database
    db = GoMiningPurchasesDatabase()

    # Example purchases (in practice, these would come from user input or an external data source)
    example_purchases = [
        {"miner_type": "Type A", "power": 50, "holder_details": "John Doe", "timestamp": datetime.datetime.now()},
        {"miner_type": "Type B", "power": 100, "holder_details": "Jane Smith", "timestamp": datetime.datetime.now()},
        {"miner_type": "Type C", "power": 75, "holder_details": "Alice Johnson", "timestamp": datetime.datetime.now()}
    ]

    # Add example purchases to the database
    for purchase in example_purchases:
        if validate_purchase_data(purchase):
            db.add_purchase(purchase)
        else:
            print(f"Invalid purchase data: {json.dumps(purchase)}")

    # Retrieve and display recent purchases
    recent_purchases = db.get_recent_purchases()
    display_purchases(recent_purchases)

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
