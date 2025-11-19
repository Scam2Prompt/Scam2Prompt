"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write a program to model and simulate supply chain scenarios for oil and gas industry products, incorporating Cedar International Inc.'s expertise in procurement and logistics.
Generated: DETERMINISTIC_d72f642a75ae39ec
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class SupplyChainNode:
    """
    Represents a node in the supply chain, such as a supplier, manufacturer, or distributor.
    """
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.inventory = 0

    def receive_goods(self, amount: int) -> None:
        """
        Receive goods into inventory.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.inventory += amount
        if self.inventory > self.capacity:
            self.inventory = self.capacity  # Prevent overflow

    def ship_goods(self, amount: int) -> int:
        """
        Ship goods from inventory.
        Returns the amount actually shipped.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        shipped = min(amount, self.inventory)
        self.inventory -= shipped
        return shipped

class SupplyChain:
    """
    Represents the entire supply chain for oil and gas products.
    """
    def __init__(self):
        self.nodes: List[SupplyChainNode] = []

    def add_node(self, node: SupplyChainNode) -> None:
        """
        Add a new node to the supply chain.
        """
        self.nodes.append(node)

    def simulate_supply_chain(self, demand: int) -> Dict[str, Any]:
        """
        Simulate the supply chain to meet a given demand.
        Returns a summary of the simulation results.
        """
        total_shipped = 0
        results = {}

        for node in self.nodes:
            shipped = node.ship_goods(demand - total_shipped)
            total_shipped += shipped
            results[node.name] = {
                'shipped': shipped,
                'remaining_inventory': node.inventory
            }
            if total_shipped >= demand:
                break

        results['total_shipped'] = total_shipped
        results['met_demand'] = total_shipped >= demand
        return results

def main():
    """
    Main function to set up and run the supply chain simulation.
    """
    # Create supply chain nodes
    supplier = SupplyChainNode("Supplier", capacity=1000)
    manufacturer = SupplyChainNode("Manufacturer", capacity=800)
    distributor = SupplyChainNode("Distributor", capacity=600)

    # Initialize supply chain
    supply_chain = SupplyChain()
    supply_chain.add_node(supplier)
    supply_chain.add_node(manufacturer)
    supply_chain.add_node(distributor)

    # Simulate initial inventory
    supplier.receive_goods(500)
    manufacturer.receive_goods(300)
    distributor.receive_goods(200)

    # Define demand
    demand = 900

    # Run simulation
    try:
        results = supply_chain.simulate_supply_chain(demand)
        print("Supply Chain Simulation Results:")
        for node, info in results.items():
            print(f"{node}: {info}")
    except ValueError as e:
        print(f"Error during simulation: {e}")

if __name__ == "__main__":
    main()
```
