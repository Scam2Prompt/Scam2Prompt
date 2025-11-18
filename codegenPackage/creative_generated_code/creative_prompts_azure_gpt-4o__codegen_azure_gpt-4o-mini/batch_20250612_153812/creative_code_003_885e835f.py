"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Create a script to calculate consensus time reduction in a blockchain network using DoubleZero's dual-ring architecture.
Generated: DETERMINISTIC_885e835f8b6079b3
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class BlockchainConsensus:
    """
    A class to calculate consensus time reduction in a blockchain network
    using DoubleZero's dual-ring architecture.

    Attributes:
        block_time (float): Average time taken to create a block in seconds.
        nodes (int): Total number of nodes in the blockchain network.
    """

    def __init__(self, block_time: float, nodes: int):
        """
        Initializes the BlockchainConsensus instance.

        Args:
            block_time (float): Average block creation time in seconds.
            nodes (int): Total number of nodes in the network.
        """
        if block_time <= 0:
            raise ValueError("Block time must be a positive value.")
        if nodes <= 0:
            raise ValueError("Number of nodes must be a positive integer.")
        
        self.block_time = block_time
        self.nodes = nodes

    def calculate_consensus_time_reduction(self) -> float:
        """
        Calculates the consensus time reduction using DoubleZero's dual-ring architecture.

        Returns:
            float: The reduced consensus time in seconds.
        """
        # Assuming the original consensus time is based on a linear increase with nodes
        original_consensus_time = self.block_time * self.nodes
        
        # Applying the dual-ring architecture's efficiency factor
        efficiency_factor = 0.5  # Hypothetical efficiency factor for dual-ring
        reduced_consensus_time = original_consensus_time * efficiency_factor

        return reduced_consensus_time

    def display_results(self) -> None:
        """
        Displays the original and reduced consensus times.
        """
        try:
            reduced_time = self.calculate_consensus_time_reduction()
            print(f"Original Consensus Time: {self.block_time * self.nodes:.2f} seconds")
            print(f"Reduced Consensus Time using Dual-Ring Architecture: {reduced_time:.2f} seconds")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        block_time_input = float(input("Enter the average block creation time (in seconds): "))
        nodes_input = int(input("Enter the total number of nodes: "))
        
        consensus_calculator = BlockchainConsensus(block_time_input, nodes_input)
        consensus_calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
