"""
Generated Code Metadata:
========================
Original URL: https://rheinmetall-zulieferer.com
Prompt: Explain how Rheinmetall's supply chain impacts the manufacturing of military vehicles and suggest ways to optimize supplier relationships.
Generated: DETERMINISTIC_179b438a99a3ec94
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Rheinmetall Supply Chain Optimizer

class Supplier:
    """Represents a supplier in Rheinmetall's supply chain."""
    
    def __init__(self, name, lead_time, reliability):
        """
        Initializes a Supplier object.

        Args:
        - name (str): The supplier's name.
        - lead_time (int): The supplier's lead time in days.
        - reliability (float): The supplier's reliability (0-1).
        """
        self.name = name
        self.lead_time = lead_time
        self.reliability = reliability

class Component:
    """Represents a component in a military vehicle."""
    
    def __init__(self, name, supplier):
        """
        Initializes a Component object.

        Args:
        - name (str): The component's name.
        - supplier (Supplier): The component's supplier.
        """
        self.name = name
        self.supplier = supplier

class MilitaryVehicle:
    """Represents a military vehicle."""
    
    def __init__(self, name, components):
        """
        Initializes a MilitaryVehicle object.

        Args:
        - name (str): The vehicle's name.
        - components (list[Component]): The vehicle's components.
        """
        self.name = name
        self.components = components

def calculate_total_lead_time(vehicle):
    """
    Calculates the total lead time for a military vehicle.

    Args:
    - vehicle (MilitaryVehicle): The vehicle.

    Returns:
    - int: The total lead time in days.
    """
    return max(component.supplier.lead_time for component in vehicle.components)

def evaluate_supplier_performance(supplier):
    """
    Evaluates a supplier's performance.

    Args:
    - supplier (Supplier): The supplier.

    Returns:
    - float: The supplier's performance score (0-1).
    """
    return supplier.reliability

def optimize_supplier_relationships(vehicles):
    """
    Optimizes supplier relationships for a list of military vehicles.

    Args:
    - vehicles (list[MilitaryVehicle]): The vehicles.

    Returns:
    - dict: A dictionary of supplier names to their performance scores.
    """
    supplier_performance = {}
    for vehicle in vehicles:
        for component in vehicle.components:
            supplier = component.supplier
            if supplier.name not in supplier_performance:
                supplier_performance[supplier.name] = evaluate_supplier_performance(supplier)
    return supplier_performance

def main():
    try:
        # Create suppliers
        supplier1 = Supplier("Supplier 1", 30, 0.9)
        supplier2 = Supplier("Supplier 2", 60, 0.8)

        # Create components
        component1 = Component("Component 1", supplier1)
        component2 = Component("Component 2", supplier2)

        # Create military vehicle
        vehicle = MilitaryVehicle("Vehicle 1", [component1, component2])

        # Calculate total lead time
        total_lead_time = calculate_total_lead_time(vehicle)
        print(f"Total lead time: {total_lead_time} days")

        # Optimize supplier relationships
        supplier_performance = optimize_supplier_relationships([vehicle])
        print("Supplier performance:")
        for supplier, performance in supplier_performance.items():
            print(f"{supplier}: {performance:.2f}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
