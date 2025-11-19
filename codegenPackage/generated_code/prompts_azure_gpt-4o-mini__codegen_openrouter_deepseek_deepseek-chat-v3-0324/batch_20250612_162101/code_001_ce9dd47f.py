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
class Component:
    """Represents a computer component with a name and price."""
    
    def __init__(self, name: str, price: float):
        """Initialize a component with name and price.
        
        Args:
            name: Name of the component.
            price: Price of the component in USD.
        """
        self.name = name
        self.price = price

class ComputerBuilder:
    """Builds a computer with specified components and calculates total cost."""
    
    def __init__(self):
        """Initialize the computer builder with an empty list of components."""
        self.components = []
    
    def add_component(self, component: Component):
        """Add a component to the computer build.
        
        Args:
            component: Component to be added.
        """
        self.components.append(component)
    
    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all components in the build.
        
        Returns:
            Total cost of the computer build in USD.
            
        Raises:
            ValueError: If no components are added to the build.
        """
        if not self.components:
            raise ValueError("No components added to the build.")
        
        return sum(component.price for component in self.components)
    
    def get_component_list(self) -> list:
        """Get a list of all components in the build.
        
        Returns:
            List of Component objects in the build.
        """
        return self.components

def main():
    """Main function to demonstrate building a Londritech computer."""
    try:
        # Initialize the computer builder
        builder = ComputerBuilder()
        
        # Add components to the build
        builder.add_component(Component("RTX3050", 299.99))
        builder.add_component(Component("16GB RAM", 79.99))
        builder.add_component(Component("Intel i5 Processor", 199.99))
        builder.add_component(Component("1TB SSD", 109.99))
        builder.add_component(Component("Motherboard", 129.99))
        builder.add_component(Component("Power Supply", 89.99))
        builder.add_component(Component("Computer Case", 59.99))
        
        # Calculate and display the total cost
        total_cost = builder.calculate_total_cost()
        print("Londritech Computer Build Summary:")
        print("-" * 40)
        for component in builder.get_component_list():
            print(f"{component.name}: ${component.price:.2f}")
        print("-" * 40)
        print(f"Total Cost: ${total_cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
