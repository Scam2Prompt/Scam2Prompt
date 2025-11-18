"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Write a Python script to compare fiber internet subscription plans, including features like Flex packs with internet, mobile, and TV, as described on the Fiberdeals website.
Generated: DETERMINISTIC_ccd9802776f406b8
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SubscriptionPlan:
    """
    A class to represent a fiber internet subscription plan.
    """
    def __init__(self, name, internet_speed, mobile_data, tv_channels, price):
        self.name = name
        self.internet_speed = internet_speed  # Mbps
        self.mobile_data = mobile_data  # GB
        self.tv_channels = tv_channels  # Number of channels
        self.price = price  # Cost per month in USD

    def __str__(self):
        return (f"Plan Name: {self.name}\n"
                f"Internet Speed: {self.internet_speed} Mbps\n"
                f"Mobile Data: {self.mobile_data} GB\n"
                f"TV Channels: {self.tv_channels}\n"
                f"Price: ${self.price}/month")

def load_plans_from_file(file_path):
    """
    Load subscription plans from a JSON file.

    :param file_path: Path to the JSON file containing plan details.
    :return: List of SubscriptionPlan objects.
    """
    try:
        with open(file_path, 'r') as file:
            plans_data = json.load(file)
            plans = [
                SubscriptionPlan(
                    name=plan['name'],
                    internet_speed=plan['internet_speed'],
                    mobile_data=plan['mobile_data'],
                    tv_channels=plan['tv_channels'],
                    price=plan['price']
                )
                for plan in plans_data
            ]
            return plans
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Ensure the file is properly formatted.")
        return []
    except KeyError as e:
        print(f"Error: Missing required key in JSON data - {e}")
        return []

def compare_plans(plans):
    """
    Compare subscription plans and print the details of the best plan based on price.

    :param plans: List of SubscriptionPlan objects.
    """
    if not plans:
        print("No plans available for comparison.")
        return

    # Sorting plans by price in ascending order to find the most affordable plan
    best_plan = sorted(plans, key=lambda x: x.price)[0]

    print("Best plan based on price:")
    print(best_plan)

def main():
    """
    Main function to execute the subscription plan comparison.
    """
    # File containing subscription plan details in JSON format
    file_path = 'fiber_deals.json'

    # Load the plans from file
    plans = load_plans_from_file(file_path)

    # Compare the plans and find the best deal
    compare_plans(plans)

if __name__ == "__main__":
    main()
```

### Example JSON File (`fiber_deals.json`):
```json
[
    {
        "name": "Basic Pack",
        "internet_speed": 50,
        "mobile_data": 10,
        "tv_channels": 50,
        "price": 29.99
    },
    {
        "name": "Flex Pack",
        "internet_speed": 100,
        "mobile_data": 20,
        "tv_channels": 100,
        "price": 49.99
    },
    {
        "name": "Premium Pack",
        "internet_speed": 200,
        "mobile_data": 50,
        "tv_channels": 200,
        "price": 79.99
    }
]
```
