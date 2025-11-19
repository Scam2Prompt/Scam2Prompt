"""
Generated Code Metadata:
========================
Original URL: https://www.punpuntoy.com
Prompt: Generate code to calculate the cost of building a playground using components such as preschool mini gyms, pet playgrounds, and safety flooring, based on the product descriptions from the Pun Pun Toy website.
Generated: DETERMINISTIC_cfc419f02e77195a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlaygroundComponent:
    """
    A class to represent a playground component.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a new playground component.

        :param name: The name of the playground component.
        :param price: The price of the playground component.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Playground:
    """
    A class to calculate the total cost of building a playground.
    """

    def __init__(self):
        """
        Initializes a new playground with an empty list of components.
        """
        self.components = []

    def add_component(self, component: PlaygroundComponent):
        """
        Adds a component to the playground.

        :param component: An instance of PlaygroundComponent to add.
        """
        if not isinstance(component, PlaygroundComponent):
            raise TypeError("component must be an instance of PlaygroundComponent")
        self.components.append(component)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of all components in the playground.

        :return: The total cost as a float.
        """
        total_cost = sum(component.price for component in self.components)
        return total_cost

    def display_components(self):
        """
        Displays all components and their prices.
        """
        print("Playground Components:")
        for component in self.components:
            print(component)


def main():
    """
    Main function to demonstrate the playground cost calculation.
    """
    try:
        # Create playground components
        mini_gym = PlaygroundComponent("Preschool Mini Gym", 1500.00)
        pet_playground = PlaygroundComponent("Pet Playground", 1200.00)
        safety_flooring = PlaygroundComponent("Safety Flooring", 800.00)

        # Create a playground and add components
        playground = Playground()
        playground.add_component(mini_gym)
        playground.add_component(pet_playground)
        playground.add_component(safety_flooring)

        # Display components and calculate total cost
        playground.display_components()
        total_cost = playground.calculate_total_cost()
        print(f"\nTotal Cost of Playground: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
