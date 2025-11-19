"""
Generated Code Metadata:
========================
Original URL: https://www.chatphetch.com
Prompt: "Write a script to compare the durability and maintenance costs of different types of flooring, including stamped concrete, epoxy, and PU flooring."
Generated: DETERMINISTIC_8d92001e0c71dee2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent flooring types
class FlooringType:
    def __init__(self, name, durability, maintenance_cost):
        """
        Initialize a FlooringType object.

        :param name: Name of the flooring type (e.g., "Stamped Concrete").
        :param durability: Durability rating (1-10, higher is better).
        :param maintenance_cost: Annual maintenance cost in USD.
        """
        self.name = name
        self.durability = durability
        self.maintenance_cost = maintenance_cost

    def __str__(self):
        """
        String representation of the flooring type.
        """
        return f"{self.name}: Durability={self.durability}, Maintenance Cost=${self.maintenance_cost:.2f}"


def compare_flooring_types(flooring_list):
    """
    Compare flooring types based on durability and maintenance cost.

    :param flooring_list: List of FlooringType objects.
    :return: Dictionary containing the flooring type with the highest durability and the lowest maintenance cost.
    """
    if not flooring_list:
        raise ValueError("Flooring list cannot be empty.")

    # Find flooring with the highest durability
    most_durable = max(flooring_list, key=lambda f: f.durability)

    # Find flooring with the lowest maintenance cost
    lowest_maintenance_cost = min(flooring_list, key=lambda f: f.maintenance_cost)

    return {
        "most_durable": most_durable,
        "lowest_maintenance_cost": lowest_maintenance_cost
    }


def main():
    """
    Main function to execute the flooring comparison script.
    """
    try:
        # Define flooring types
        flooring_data = [
            FlooringType("Stamped Concrete", durability=8, maintenance_cost=500),
            FlooringType("Epoxy Flooring", durability=9, maintenance_cost=300),
            FlooringType("PU Flooring", durability=7, maintenance_cost=400)
        ]

        # Compare flooring types
        comparison_result = compare_flooring_types(flooring_data)

        # Display results
        print("Flooring Comparison Results:")
        print(f"Most Durable Flooring: {comparison_result['most_durable']}")
        print(f"Lowest Maintenance Cost Flooring: {comparison_result['lowest_maintenance_cost']}")

        # Optionally save results to a JSON file
        with open("flooring_comparison_results.json", "w") as file:
            json.dump(
                {
                    "most_durable": {
                        "name": comparison_result['most_durable'].name,
                        "durability": comparison_result['most_durable'].durability,
                        "maintenance_cost": comparison_result['most_durable'].maintenance_cost
                    },
                    "lowest_maintenance_cost": {
                        "name": comparison_result['lowest_maintenance_cost'].name,
                        "durability": comparison_result['lowest_maintenance_cost'].durability,
                        "maintenance_cost": comparison_result['lowest_maintenance_cost'].maintenance_cost
                    }
                },
                file,
                indent=4
            )
        print("Comparison results saved to 'flooring_comparison_results.json'.")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
