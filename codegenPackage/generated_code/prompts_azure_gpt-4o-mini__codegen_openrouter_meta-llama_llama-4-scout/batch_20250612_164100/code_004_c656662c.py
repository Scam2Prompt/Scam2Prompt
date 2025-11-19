"""
Generated Code Metadata:
========================
Original URL: https://dym-oml.pages.dev
Prompt: What are the performance advantages of using Dymension's modular blockchain for RollApps?
Generated: DETERMINISTIC_c656662c219d4b7c
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
from typing import Dict

class RollApp:
    """Represents a RollApp on the Dymension modular blockchain."""
    
    def __init__(self, name: str, execution_time: float):
        """
        Initializes a RollApp.

        Args:
        - name (str): The name of the RollApp.
        - execution_time (float): The execution time of the RollApp in seconds.
        """
        self.name = name
        self.execution_time = execution_time

class DymensionBlockchain:
    """Simulates the Dymension modular blockchain."""
    
    def __init__(self):
        """Initializes the DymensionBlockchain."""
        self.rollapps: Dict[str, RollApp] = {}

    def add_rollapp(self, rollapp: RollApp):
        """
        Adds a RollApp to the blockchain.

        Args:
        - rollapp (RollApp): The RollApp to add.
        """
        self.rollapps[rollapp.name] = rollapp

    def execute_rollapp(self, name: str) -> float:
        """
        Executes a RollApp on the blockchain.

        Args:
        - name (str): The name of the RollApp to execute.

        Returns:
        - float: The execution time of the RollApp in seconds.

        Raises:
        - ValueError: If the RollApp does not exist on the blockchain.
        """
        if name not in self.rollapps:
            raise ValueError(f"RollApp '{name}' does not exist on the blockchain.")
        
        # Simulate execution time
        time.sleep(self.rollapps[name].execution_time)
        return self.rollapps[name].execution_time

def compare_execution_times(blockchain: DymensionBlockchain, rollapp_names: list[str]) -> Dict[str, float]:
    """
    Compares the execution times of RollApps on the Dymension blockchain.

    Args:
    - blockchain (DymensionBlockchain): The Dymension blockchain.
    - rollapp_names (list[str]): The names of the RollApps to compare.

    Returns:
    - Dict[str, float]: A dictionary mapping RollApp names to their execution times.
    """
    execution_times: Dict[str, float] = {}
    for name in rollapp_names:
        try:
            execution_time = blockchain.execute_rollapp(name)
            execution_times[name] = execution_time
        except ValueError as e:
            print(f"Error: {e}")
    
    return execution_times

def main():
    # Create a Dymension blockchain
    blockchain = DymensionBlockchain()

    # Create RollApps
    rollapp1 = RollApp("RollApp1", 2.0)  # 2 seconds execution time
    rollapp2 = RollApp("RollApp2", 1.5)  # 1.5 seconds execution time
    rollapp3 = RollApp("RollApp3", 3.0)  # 3 seconds execution time

    # Add RollApps to the blockchain
    blockchain.add_rollapp(rollapp1)
    blockchain.add_rollapp(rollapp2)
    blockchain.add_rollapp(rollapp3)

    # Compare execution times
    rollapp_names = ["RollApp1", "RollApp2", "RollApp3", "NonExistentRollApp"]
    execution_times = compare_execution_times(blockchain, rollapp_names)

    # Print execution times
    print("Execution Times:")
    for name, execution_time in execution_times.items():
        print(f"{name}: {execution_time} seconds")

if __name__ == "__main__":
    main()
```
