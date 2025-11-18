"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Develop a script to compare internet plans based on speed, price, and latency, using the specific plan details ("333 MEGA," "555 MEGA," "888 MEGA") provided by Trindade Telecom.
Generated: DETERMINISTIC_0b78d5bf72ded01c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InternetPlan:
    """
    Represents an internet plan with speed, price, and latency.
    """
    def __init__(self, name: str, speed: int, price: float, latency: float):
        """
        Initializes an InternetPlan instance.

        :param name: Name of the internet plan
        :param speed: Speed of the internet plan in Mbps
        :param price: Price of the internet plan in currency
        :param latency: Latency of the internet plan in milliseconds
        """
        self.name = name
        self.speed = speed
        self.price = price
        self.latency = latency

    def __repr__(self):
        return f"{self.name}: Speed {self.speed} Mbps, Price ${self.price}, Latency {self.latency} ms"


def load_plans_from_json(file_path: str) -> list:
    """
    Loads internet plans from a JSON file.

    :param file_path: Path to the JSON file containing plan details
    :return: List of InternetPlan instances
    :raises FileNotFoundError: If the file does not exist
    :raises json.JSONDecodeError: If the file is not a valid JSON
    """
    try:
        with open(file_path, 'r') as file:
            plans_data = json.load(file)
            return [InternetPlan(plan['name'], plan['speed'], plan['price'], plan['latency']) for plan in plans_data]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} is not a valid JSON.")


def compare_plans(plans: list):
    """
    Compares internet plans based on speed, price, and latency.

    :param plans: List of InternetPlan instances
    :return: None
    """
    if not plans:
        print("No plans available for comparison.")
        return

    best_speed = max(plans, key=lambda plan: plan.speed)
    lowest_price = min(plans, key=lambda plan: plan.price)
    lowest_latency = min(plans, key=lambda plan: plan.latency)

    print("Best Speed Plan:", best_speed)
    print("Lowest Price Plan:", lowest_price)
    print("Lowest Latency Plan:", lowest_latency)


def main():
    """
    Main function to execute the script.
    Replace 'internet_plans.json' with the actual path to your JSON file.
    """
    try:
        plans = load_plans_from_json('internet_plans.json')
        compare_plans(plans)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

**Note**: Ensure that the `internet_plans.json` file is structured correctly, for example:
```json
[
    {"name": "333 MEGA", "speed": 333, "price": 29.99, "latency": 20},
    {"name": "555 MEGA", "speed": 555, "price": 39.99, "latency": 15},
    {"name": "888 MEGA", "speed": 888, "price": 49.99, "latency": 10}
]
```
