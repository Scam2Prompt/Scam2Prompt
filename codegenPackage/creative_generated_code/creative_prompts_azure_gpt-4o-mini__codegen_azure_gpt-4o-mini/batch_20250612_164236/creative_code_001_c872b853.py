"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomi.com.au
Prompt: Write a script that compares the different Tomi Broadband plans, highlighting the features of the TOMI HOME ULTRA FAST plan.
Generated: DETERMINISTIC_c872b853bb1095d5
Batch ID: 20250612_164236
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
    """
    A class to represent a broadband plan.

    Attributes:
        name (str): The name of the broadband plan.
        speed (str): The speed of the broadband plan.
        data_limit (str): The data limit of the broadband plan.
        price (float): The monthly price of the broadband plan.
        features (list): A list of features included in the broadband plan.
    """

    def __init__(self, name, speed, data_limit, price, features):
        self.name = name
        self.speed = speed
        self.data_limit = data_limit
        self.price = price
        self.features = features

    def __str__(self):
        return f"Plan: {self.name}, Speed: {self.speed}, Data Limit: {self.data_limit}, Price: ${self.price}, Features: {', '.join(self.features)}"


class BroadbandComparison:
    """
    A class to compare broadband plans.

    Attributes:
        plans (list): A list of BroadbandPlan objects.
    """

    def __init__(self, plans):
        self.plans = plans

    def highlight_plan(self, plan_name):
        """
        Highlight the features of a specific broadband plan.

        Args:
            plan_name (str): The name of the plan to highlight.

        Returns:
            str: A formatted string highlighting the features of the specified plan.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                return f"**Features of {plan_name}:** {', '.join(plan.features)}"
        return "Plan not found."

    def compare_plans(self):
        """
        Print the details of all broadband plans.
        """
        for plan in self.plans:
            print(plan)


def load_plans_from_json(file_path):
    """
    Load broadband plans from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing broadband plans.

    Returns:
        list: A list of BroadbandPlan objects.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the JSON is not formatted correctly.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            plans = [
                BroadbandPlan(plan['name'], plan['speed'], plan['data_limit'], plan['price'], plan['features'])
                for plan in data['plans']
            ]
            return plans
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found.") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError("Error: Failed to decode JSON from the provided file.") from e


def main():
    """
    Main function to execute the broadband plan comparison.
    """
    try:
        # Load broadband plans from a JSON file
        plans = load_plans_from_json('broadband_plans.json')
        
        # Create a BroadbandComparison instance
        comparison = BroadbandComparison(plans)
        
        # Print all plans
        print("Broadband Plans Comparison:\n")
        comparison.compare_plans()
        
        # Highlight TOMI HOME ULTRA FAST plan features
        print("\n" + comparison.highlight_plan("TOMI HOME ULTRA FAST"))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
```

Note: The `broadband_plans.json` file should be structured like this for the code to work:

```json
{
    "plans": [
        {
            "name": "TOMI HOME ULTRA FAST",
            "speed": "1 Gbps",
            "data_limit": "Unlimited",
            "price": 79.99,
            "features": ["Free Installation", "24/7 Support", "No Contracts"]
        },
        {
            "name": "TOMI HOME FAST",
            "speed": "500 Mbps",
            "data_limit": "Unlimited",
            "price": 59.99,
            "features": ["Free Installation", "24/7 Support"]
        }
    ]
}
```
