"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Write code to simulate telecommunication network planning and optimization, using Ultious's engineering solutions as a reference.
Generated: DETERMINISTIC_1aeecf7207983e35
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# telecommunication_network_planning.py

import numpy as np
from typing import List, Dict

class CellTower:
    """Represents a cell tower in the telecommunication network."""
    
    def __init__(self, id: int, x: float, y: float, capacity: int):
        """
        Initializes a CellTower object.

        Args:
        id (int): Unique identifier for the cell tower.
        x (float): X-coordinate of the cell tower.
        y (float): Y-coordinate of the cell tower.
        capacity (int): Maximum number of users the cell tower can support.
        """
        self.id = id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.users = 0  # Initialize the number of users to 0

    def add_users(self, num_users: int):
        """
        Adds users to the cell tower.

        Args:
        num_users (int): Number of users to add.

        Raises:
        ValueError: If the number of users exceeds the cell tower's capacity.
        """
        if self.users + num_users > self.capacity:
            raise ValueError("Exceeds cell tower capacity")
        self.users += num_users

    def remove_users(self, num_users: int):
        """
        Removes users from the cell tower.

        Args:
        num_users (int): Number of users to remove.

        Raises:
        ValueError: If the number of users to remove exceeds the current number of users.
        """
        if num_users > self.users:
            raise ValueError("Cannot remove more users than currently connected")
        self.users -= num_users


class TelecommunicationNetwork:
    """Represents a telecommunication network with multiple cell towers."""
    
    def __init__(self):
        self.cell_towers: Dict[int, CellTower] = {}  # Map of cell tower IDs to CellTower objects

    def add_cell_tower(self, cell_tower: CellTower):
        """
        Adds a cell tower to the network.

        Args:
        cell_tower (CellTower): CellTower object to add.
        """
        self.cell_towers[cell_tower.id] = cell_tower

    def remove_cell_tower(self, cell_tower_id: int):
        """
        Removes a cell tower from the network.

        Args:
        cell_tower_id (int): ID of the cell tower to remove.

        Raises:
        KeyError: If the cell tower ID does not exist in the network.
        """
        if cell_tower_id not in self.cell_towers:
            raise KeyError("Cell tower ID does not exist")
        del self.cell_towers[cell_tower_id]

    def optimize_network(self):
        """
        Optimizes the network by reassigning users from overloaded cell towers to underloaded ones.

        Returns:
        Dict[int, int]: Map of cell tower IDs to their new user counts.
        """
        overloaded_towers = [tower for tower in self.cell_towers.values() if tower.users > tower.capacity * 0.8]
        underloaded_towers = [tower for tower in self.cell_towers.values() if tower.users < tower.capacity * 0.2]

        for overloaded_tower in overloaded_towers:
            users_to_reassign = int(overloaded_tower.users * 0.1)  # Reassign 10% of users
            for underloaded_tower in underloaded_towers:
                if users_to_reassign == 0:
                    break
                available_capacity = underloaded_tower.capacity - underloaded_tower.users
                reassign_users = min(users_to_reassign, available_capacity)
                overloaded_tower.remove_users(reassign_users)
                underloaded_tower.add_users(reassign_users)
                users_to_reassign -= reassign_users

        return {tower.id: tower.users for tower in self.cell_towers.values()}


def simulate_network_planning(num_cell_towers: int, num_users: int):
    """
    Simulates telecommunication network planning and optimization.

    Args:
    num_cell_towers (int): Number of cell towers in the network.
    num_users (int): Total number of users in the network.

    Returns:
    Dict[int, int]: Map of cell tower IDs to their optimized user counts.
    """
    network = TelecommunicationNetwork()

    # Randomly distribute users across cell towers
    np.random.seed(0)
    for i in range(num_cell_towers):
        x = np.random.uniform(0, 100)
        y = np.random.uniform(0, 100)
        capacity = np.random.randint(100, 500)  # Random capacity between 100 and 500
        cell_tower = CellTower(i, x, y, capacity)
        network.add_cell_tower(cell_tower)

    # Add users to cell towers
    users_per_tower = num_users // num_cell_towers
    for tower in network.cell_towers.values():
        tower.add_users(users_per_tower)

    # Optimize the network
    optimized_user_counts = network.optimize_network()

    return optimized_user_counts


if __name__ == "__main__":
    num_cell_towers = 10
    num_users = 5000
    optimized_user_counts = simulate_network_planning(num_cell_towers, num_users)
    print("Optimized User Counts:")
    for cell_tower_id, user_count in optimized_user_counts.items():
        print(f"Cell Tower {cell_tower_id}: {user_count} users")
```
