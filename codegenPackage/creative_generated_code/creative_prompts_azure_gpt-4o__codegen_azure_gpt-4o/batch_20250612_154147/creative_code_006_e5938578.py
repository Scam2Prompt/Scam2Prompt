"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Create a script to streamline procurement workflows for branded swag, focusing on maximizing ROI and reducing manual effort, inspired by Avail Labs' procurement solutions.
Generated: DETERMINISTIC_e59385782210c8a0
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

# Configurations
CONFIG_FILE = "config.json"  # Path to configuration file
LOG_FILE = "procurement_log.txt"  # Path to log file
CATEGORIES = ["t-shirts", "mugs", "stickers", "notebooks"]  # Example swag categories

# Load configuration
def load_config(file_path):
    """Load configuration settings from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON: {e}")

# Log function
def log(message):
    """Log messages to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# Calculate ROI
def calculate_roi(order_cost, estimated_brand_exposure, lifetime_value_per_customer):
    """
    Calculate the Return on Investment (ROI) for a swag order.

    :param order_cost: Total cost of the order
    :param estimated_brand_exposure: Number of estimated impressions (e.g., views of the swag)
    :param lifetime_value_per_customer: Lifetime value of a single customer
    :return: ROI value
    """
    if order_cost <= 0:
        raise ValueError("Order cost must be positive.")
    if estimated_brand_exposure <= 0 or lifetime_value_per_customer <= 0:
        raise ValueError("Estimated brand exposure and lifetime value must be positive.")
    
    return (estimated_brand_exposure * lifetime_value_per_customer) / order_cost

# Procurement workflow
def streamline_procurement(config):
    """
    Streamline procurement workflows based on configurations provided.

    :param config: Dictionary containing procurement configurations
    """
    try:
        log("Starting procurement workflow...")
        
        # Validate configuration
        budget = config.get("budget")
        if budget is None or budget <= 0:
            raise ValueError("Budget must be specified and positive.")
        
        orders = config.get("orders")
        if not orders or not isinstance(orders, list):
            raise ValueError("Orders must be provided as a list.")

        for order in orders:
            category = order.get("category")
            if category not in CATEGORIES:
                log(f"Skipping order: invalid category '{category}'")
                continue
            
            order_cost = order.get("cost")
            estimated_exposure = order.get("estimated_exposure")
            customer_lifetime_value = order.get("customer_lifetime_value")

            # Calculate ROI
            try:
                roi = calculate_roi(order_cost, estimated_exposure, customer_lifetime_value)
                log(f"Order in category '{category}' has an ROI of {roi:.2f}.")
            except ValueError as e:
                log(f"Failed to calculate ROI for order in category '{category}': {e}")
                continue

            # Check if the order fits within the budget
            if order_cost <= budget:
                log(f"Order in category '{category}' approved within budget.")
                budget -= order_cost
            else:
                log(f"Order in category '{category}' exceeds budget and was skipped.")

        log("Procurement workflow completed.")

    except Exception as e:
        log(f"Error during procurement workflow: {e}")
        raise

# Main entry point
if __name__ == "__main__":
    try:
        # Load the configuration
        config = load_config(CONFIG_FILE)
        
        # Execute the procurement workflow
        streamline_procurement(config)

        print("Procurement workflow completed. Check the log file for details.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Place your `config.json` file in the same directory as the script, structured as follows:

```json
{
    "budget": 5000,
    "orders": [
        {
            "category": "t-shirts",
            "cost": 1500,
            "estimated_exposure": 10000,
            "customer_lifetime_value": 50
        },
        {
            "category": "mugs",
            "cost": 800,
            "estimated_exposure": 5000,
            "customer_lifetime_value": 30
        }
    ]
}
```
