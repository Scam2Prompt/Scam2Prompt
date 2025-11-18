"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofibers.com
Prompt: Write code to display a list of JioFiber broadband plans, including speed, price, validity, and OTT subscriptions, for a specific city like Hyderabad or Bangalore.
Generated: DETERMINISTIC_033071f9034ecf4b
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BroadbandPlan:
    """Class to represent a broadband plan."""
    
    def __init__(self, speed, price, validity, ott_subscriptions):
        self.speed = speed  # Speed of the broadband plan in Mbps
        self.price = price  # Price of the broadband plan in INR
        self.validity = validity  # Validity of the plan in days
        self.ott_subscriptions = ott_subscriptions  # List of OTT subscriptions included

    def __str__(self):
        """Return a string representation of the broadband plan."""
        return f"Speed: {self.speed} Mbps, Price: ₹{self.price}, Validity: {self.validity} days, OTT: {', '.join(self.ott_subscriptions)}"


class JioFiber:
    """Class to manage JioFiber broadband plans."""

    def __init__(self):
        """Initialize the JioFiber class with available plans."""
        self.plans = self.load_plans()

    def load_plans(self):
        """Load broadband plans from a JSON file."""
        try:
            with open('jiofiber_plans.json', 'r') as file:
                plans_data = json.load(file)
                return [BroadbandPlan(**plan) for plan in plans_data]
        except FileNotFoundError:
            print("Error: Plans data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Plans data file is not valid JSON.")
            return []

    def display_plans(self):
        """Display available broadband plans."""
        if not self.plans:
            print("No plans available.")
            return
        
        print("Available JioFiber Broadband Plans:")
        for plan in self.plans:
            print(plan)


def main():
    """Main function to run the JioFiber broadband plan display."""
    jio_fiber = JioFiber()
    jio_fiber.display_plans()


if __name__ == "__main__":
    main()
```

**Sample JSON File (`jiofiber_plans.json`):**
```json
[
    {
        "speed": 100,
        "price": 499,
        "validity": 30,
        "ott_subscriptions": ["Netflix", "Amazon Prime"]
    },
    {
        "speed": 200,
        "price": 799,
        "validity": 30,
        "ott_subscriptions": ["Disney+", "Amazon Prime"]
    },
    {
        "speed": 500,
        "price": 1499,
        "validity": 30,
        "ott_subscriptions": ["Netflix", "Disney+", "Amazon Prime"]
    }
]
```

Make sure to create the `jiofiber_plans.json` file with the provided sample JSON data in the same directory as your Python script for the code to run successfully.
