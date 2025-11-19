"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write a script to calculate the total cost of building a Londritech computer with specified components like the RTX3050 and 16GB RAM.
Generated: DETERMINISTIC_ce9dd47faabcf397
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Londritech Computer Cost Calculator

class Component:
    """Class to represent a computer component with a name and price."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Computer:
    """Class to represent a computer built from various components."""
    
    def __init__(self):
        self.components = []

    def add_component(self, component: Component):
        """Add a component to the computer."""
        self.components.append(component)

    def total_cost(self) -> float:
        """Calculate the total cost of the computer."""
        return sum(component.price for component in self.components)

    def display_components(self):
        """Display all components and their prices."""
        for component in self.components:
            print(component)


def main():
    """Main function to build the Londritech computer and calculate its cost."""
    try:
        # Define components with their prices
        rtx_3050 = Component("NVIDIA RTX 3050", 249.99)
        ram_16gb = Component("16GB RAM", 79.99)
        cpu = Component("Intel i5 Processor", 199.99)
        motherboard = Component("Motherboard", 129.99)
        storage = Component("1TB SSD", 99.99)
        
        # Create a computer instance
        londritech_computer = Computer()
        
        # Add components to the computer
        londritech_computer.add_component(rtx_3050)
        londritech_computer.add_component(ram_16gb)
        londritech_computer.add_component(cpu)
        londritech_computer.add_component(motherboard)
        londritech_computer.add_component(storage)

        # Display components and total cost
        print("Londritech Computer Components:")
        londritech_computer.display_components()
        print(f"\nTotal Cost: ${londritech_computer.total_cost():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
