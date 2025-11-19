"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script to calculate hashpower for a mining pool on the Solana blockchain, factoring in the increasing cost of mining equipment every 385 machines minted.
Generated: DETERMINISTIC_c93883366c40b6c3
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class MiningEquipment:
    """
    Represents mining equipment with cost and hashpower attributes.
    The cost increases every 385 machines minted.
    """
    def __init__(self, base_cost: float, base_hashpower: float, cost_increase_per_385: float):
        """
        Initialize mining equipment with base parameters.
        
        Args:
            base_cost: Initial cost of one machine
            base_hashpower: Hashpower per machine
            cost_increase_per_385: Cost increase after every 385 machines
        """
        self.base_cost = base_cost
        self.base_hashpower = base_hashpower
        self.cost_increase_per_385 = cost_increase_per_385

    def get_cost(self, total_machines_minted: int) -> float:
        """
        Calculate the current cost of one machine based on total minted.
        
        Args:
            total_machines_minted: Total number of machines minted so far
        
        Returns:
            Current cost of one machine
        """
        increase_multiplier = total_machines_minted // 385
        return self.base_cost + (increase_multiplier * self.cost_increase_per_385)

    def get_hashpower(self, total_machines_minted: int) -> float:
        """
        Calculate the current hashpower of one machine (constant in this implementation).
        
        Args:
            total_machines_minted: Total number of machines minted so far
        
        Returns:
            Current hashpower of one machine
        """
        return self.base_hashpower


class MiningPool:
    """
    Represents a mining pool on Solana blockchain.
    """
    def __init__(self, equipment: MiningEquipment):
        """
        Initialize mining pool with equipment specifications.
        
        Args:
            equipment: MiningEquipment instance
        """
        self.equipment = equipment
        self.total_machines_minted = 0
        self.total_hashpower = 0.0
        self.total_cost = 0.0

    def add_machines(self, count: int) -> None:
        """
        Add machines to the mining pool and update costs and hashpower.
        
        Args:
            count: Number of machines to add
        """
        if count <= 0:
            raise ValueError("Number of machines must be positive")
        
        for _ in range(count):
            current_cost = self.equipment.get_cost(self.total_machines_minted)
            current_hashpower = self.equipment.get_hashpower(self.total_machines_minted)
            
            self.total_cost += current_cost
            self.total_hashpower += current_hashpower
            self.total_machines_minted += 1

    def get_current_stats(self) -> dict:
        """
        Get current statistics of the mining pool.
        
        Returns:
            Dictionary containing:
            - total_machines: Total machines in pool
            - total_hashpower: Total hashpower of pool
            - total_cost: Total cost of all machines
            - avg_cost_per_machine: Average cost per machine
            - hashpower_per_machine: Hashpower per machine (average)
        """
        return {
            "total_machines": self.total_machines_minted,
            "total_hashpower": self.total_hashpower,
            "total_cost": self.total_cost,
            "avg_cost_per_machine": self.total_cost / self.total_machines_minted if self.total_machines_minted > 0 else 0,
            "hashpower_per_machine": self.total_hashpower / self.total_machines_minted if self.total_machines_minted > 0 else 0,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize mining equipment
        solana_miner = MiningEquipment(
            base_cost=1000.0,  # $1000 base cost
            base_hashpower=50.0,  # 50 H/s
            cost_increase_per_385=200.0  # $200 increase every 385 machines
        )
        
        # Create mining pool
        pool = MiningPool(solana_miner)
        
        # Add machines in batches
        pool.add_machines(400)  # First 400 machines
        stats = pool.get_current_stats()
        print(f"After 400 machines: {stats}")
        
        pool.add_machines(200)  # Next 200 machines (total 600)
        stats = pool.get_current_stats()
        print(f"After 600 machines: {stats}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
