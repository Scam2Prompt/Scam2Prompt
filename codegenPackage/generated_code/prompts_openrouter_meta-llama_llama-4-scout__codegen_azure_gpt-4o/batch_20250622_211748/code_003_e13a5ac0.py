"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: "Compare and contrast the Lemosho and Machame routes for a 7-day Kilimanjaro trek, including costs and success rates."
Generated: DETERMINISTIC_e13a5ac0e685ea76
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent a Kilimanjaro route
class KilimanjaroRoute:
    def __init__(self, name, duration_days, cost_usd, success_rate_percent, description):
        """
        Initialize a KilimanjaroRoute object.

        :param name: Name of the route
        :param duration_days: Duration of the trek in days
        :param cost_usd: Estimated cost in USD
        :param success_rate_percent: Average success rate percentage
        :param description: Brief description of the route
        """
        self.name = name
        self.duration_days = duration_days
        self.cost_usd = cost_usd
        self.success_rate_percent = success_rate_percent
        self.description = description

    def to_dict(self):
        """
        Convert the route object to a dictionary for easy serialization.

        :return: Dictionary representation of the route
        """
        return {
            "name": self.name,
            "duration_days": self.duration_days,
            "cost_usd": self.cost_usd,
            "success_rate_percent": self.success_rate_percent,
            "description": self.description,
        }


def compare_routes(route1, route2):
    """
    Compare two Kilimanjaro routes and return a summary of their differences.

    :param route1: First route (KilimanjaroRoute object)
    :param route2: Second route (KilimanjaroRoute object)
    :return: Dictionary summarizing the comparison
    """
    comparison = {
        "route1": route1.to_dict(),
        "route2": route2.to_dict(),
        "differences": {
            "cost_difference_usd": abs(route1.cost_usd - route2.cost_usd),
            "success_rate_difference_percent": abs(route1.success_rate_percent - route2.success_rate_percent),
            "duration_difference_days": abs(route1.duration_days - route2.duration_days),
        },
    }
    return comparison


def main():
    """
    Main function to compare the Lemosho and Machame routes for a 7-day Kilimanjaro trek.
    """
    try:
        # Define the Lemosho route
        lemosho = KilimanjaroRoute(
            name="Lemosho",
            duration_days=7,
            cost_usd=2500,
            success_rate_percent=90,
            description="A scenic and less crowded route with a high success rate."
        )

        # Define the Machame route
        machame = KilimanjaroRoute(
            name="Machame",
            duration_days=7,
            cost_usd=2200,
            success_rate_percent=85,
            description="A popular and challenging route known as the 'Whiskey Route'."
        )

        # Compare the routes
        comparison_result = compare_routes(lemosho, machame)

        # Print the comparison result in a readable format
        print("Comparison of Lemosho and Machame Routes:")
        print(json.dumps(comparison_result, indent=4))

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
