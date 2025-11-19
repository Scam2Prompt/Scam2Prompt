"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Compare and recommend different types of solar panels and inverters suitable for residential and commercial projects in Brazil, considering factors like efficiency, durability, and cost.
Generated: DETERMINISTIC_a4eef315d29fbbcb
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent solar panels and inverters
class SolarComponent:
    def __init__(self, name, type, efficiency, durability, cost):
        """
        Initialize a solar component with its attributes.

        :param name: Name of the component
        :param type: Type of the component (e.g., 'Panel' or 'Inverter')
        :param efficiency: Efficiency rating (percentage)
        :param durability: Durability rating (years)
        :param cost: Cost in USD
        """
        self.name = name
        self.type = type
        self.efficiency = efficiency
        self.durability = durability
        self.cost = cost

    def to_dict(self):
        """
        Convert the object to a dictionary for easy serialization.

        :return: Dictionary representation of the object
        """
        return {
            "name": self.name,
            "type": self.type,
            "efficiency": self.efficiency,
            "durability": self.durability,
            "cost": self.cost,
        }


def recommend_components(components, project_type):
    """
    Recommend solar components based on project type.

    :param components: List of SolarComponent objects
    :param project_type: Type of project ('Residential' or 'Commercial')
    :return: List of recommended components
    """
    try:
        # Filter components based on project type
        if project_type == "Residential":
            # Residential projects prioritize cost and efficiency
            recommended = sorted(
                components, key=lambda x: (x.cost, -x.efficiency)
            )
        elif project_type == "Commercial":
            # Commercial projects prioritize durability and efficiency
            recommended = sorted(
                components, key=lambda x: (-x.durability, -x.efficiency)
            )
        else:
            raise ValueError("Invalid project type. Use 'Residential' or 'Commercial'.")

        return recommended
    except Exception as e:
        print(f"Error in recommending components: {e}")
        return []


def main():
    """
    Main function to compare and recommend solar panels and inverters.
    """
    # Sample data for solar panels and inverters
    components = [
        SolarComponent("Panel A", "Panel", 18.5, 25, 200),
        SolarComponent("Panel B", "Panel", 20.0, 30, 250),
        SolarComponent("Inverter X", "Inverter", 95.0, 15, 500),
        SolarComponent("Inverter Y", "Inverter", 97.0, 20, 700),
    ]

    # Get user input for project type
    project_type = input("Enter project type ('Residential' or 'Commercial'): ").strip()

    # Recommend components based on project type
    recommended = recommend_components(components, project_type)

    # Display recommendations
    if recommended:
        print(f"\nRecommended components for {project_type} projects:")
        for component in recommended:
            print(json.dumps(component.to_dict(), indent=4))
    else:
        print("No recommendations available.")


if __name__ == "__main__":
    main()
```
