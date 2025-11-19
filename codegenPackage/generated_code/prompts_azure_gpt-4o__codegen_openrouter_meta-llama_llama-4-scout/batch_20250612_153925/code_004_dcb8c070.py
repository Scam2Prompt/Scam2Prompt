"""
Generated Code Metadata:
========================
Original URL: https://oksd7.cn
Prompt: Create a script to calculate optimal cross-chain paths for asset transfers, minimizing gas fees by 40%, as mentioned in the 欧易跨链资产雷达 feature.
Generated: DETERMINISTIC_dcb8c07042f877cc
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import heapq

class CrossChainPathCalculator:
    def __init__(self, graph, gas_fees):
        """
        Initialize the CrossChainPathCalculator.

        Args:
        - graph (networkx.DiGraph): A directed graph representing the cross-chain network.
        - gas_fees (dict): A dictionary of gas fees for each edge in the graph.
        """
        self.graph = graph
        self.gas_fees = gas_fees

    def calculate_optimal_path(self, source, target, amount):
        """
        Calculate the optimal cross-chain path for an asset transfer.

        Args:
        - source (str): The source chain.
        - target (str): The target chain.
        - amount (float): The amount of asset to transfer.

        Returns:
        - path (list): A list of chains representing the optimal path.
        - min_gas_fee (float): The minimum gas fee for the optimal path.

        Raises:
        - ValueError: If the source or target chain is not in the graph.
        """
        if source not in self.graph or target not in self.graph:
            raise ValueError("Source or target chain not in graph")

        # Create a priority queue to store nodes to visit, with their current gas fee
        queue = [(0, source, [source])]
        visited = set()

        while queue:
            (gas_fee, current_chain, path) = heapq.heappop(queue)

            if current_chain == target:
                return path, gas_fee

            if current_chain in visited:
                continue

            visited.add(current_chain)

            for neighbor in self.graph[current_chain]:
                edge_gas_fee = self.gas_fees[(current_chain, neighbor)]
                new_gas_fee = gas_fee + edge_gas_fee
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (new_gas_fee, neighbor, new_path))

        # If no path is found, return None
        return None

    def optimize_gas_fee(self, path):
        """
        Optimize the gas fee for a given path by reducing it by 40%.

        Args:
        - path (list): A list of chains representing the path.

        Returns:
        - optimized_gas_fee (float): The optimized gas fee.
        """
        gas_fee = 0
        for i in range(len(path) - 1):
            gas_fee += self.gas_fees[(path[i], path[i + 1])]
        optimized_gas_fee = gas_fee * 0.6  # Reduce gas fee by 40%
        return optimized_gas_fee


def main():
    # Create a sample graph
    graph = nx.DiGraph()
    graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

    # Define gas fees for each edge
    gas_fees = {
        ('A', 'B'): 10,
        ('A', 'C'): 20,
        ('B', 'D'): 15,
        ('C', 'D'): 25
    }

    calculator = CrossChainPathCalculator(graph, gas_fees)

    source = 'A'
    target = 'D'
    amount = 100

    try:
        path, min_gas_fee = calculator.calculate_optimal_path(source, target, amount)
        optimized_gas_fee = calculator.optimize_gas_fee(path)
        print(f"Optimal path: {path}")
        print(f"Minimum gas fee: {min_gas_fee}")
        print(f"Optimized gas fee: {optimized_gas_fee}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
