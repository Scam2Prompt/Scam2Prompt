"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Create a simulation of a robot serving and collecting items in a restaurant, inspired by the functionalities of BellaBot and HolaBot described on the GSJ website.
Generated: DETERMINISTIC_3db892c9d285450b
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import List, Dict, Optional

class ItemStatus(Enum):
    """Enum representing the status of an item."""
    REQUESTED = "REQUESTED"
    SERVED = "SERVED"
    COLLECTED = "COLLECTED"

class Item:
    """Class representing an item in the restaurant."""
    def __init__(self, name: str, table_id: int):
        self.name = str(name)
        self.table_id = int(table_id)
        self.status = ItemStatus.REQUESTED
        self.request_time = time.time()

    def update_status(self, new_status: ItemStatus) -> None:
        """Update the status of the item."""
        self.status = new_status

    def __str__(self) -> str:
        return f"{self.name} (Table {self.table_id}) - {self.status.value}"

class Robot:
    """Class representing a serving/collecting robot."""
    def __init__(self, name: str, capacity: int):
        self.name = str(name)
        self.capacity = int(capacity)
        self.current_items: List[Item] = []
        self.is_available = True

    def can_accept_item(self) -> bool:
        """Check if robot can accept more items."""
        return len(self.current_items) < self.capacity and self.is_available

    def add_item(self, item: Item) -> bool:
        """Add an item to the robot if possible."""
        if not self.can_accept_item():
            return False
        
        self.current_items.append(item)
        item.update_status(ItemStatus.SERVED)
        return True

    def collect_item(self, item: Item) -> bool:
        """Collect an item from a table."""
        if not self.can_accept_item():
            return False
        
        self.current_items.append(item)
        item.update_status(ItemStatus.COLLECTED)
        return True

    def unload_items(self) -> List[Item]:
        """Unload all items from the robot."""
        unloaded = self.current_items.copy()
        self.current_items.clear()
        return unloaded

    def __str__(self) -> str:
        return f"{self.name} (Capacity: {len(self.current_items)}/{self.capacity})"

class Restaurant:
    """Class representing the restaurant environment."""
    def __init__(self, num_tables: int, robots: List[Robot]):
        self.tables: Dict[int, List[Item]] = {i: [] for i in range(1, num_tables + 1)}
        self.robots = robots
        self.item_log: List[Item] = []

    def request_item(self, item_name: str, table_id: int) -> Optional[Item]:
        """Request an item for a table."""
        if table_id not in self.tables:
            return None
        
        item = Item(item_name, table_id)
        self.tables[table_id].append(item)
        self.item_log.append(item)
        return item

    def serve_items(self) -> None:
        """Attempt to serve all requested items using available robots."""
        for table_id, items in self.tables.items():
            for item in items:
                if item.status == ItemStatus.REQUESTED:
                    for robot in self.robots:
                        if robot.add_item(item):
                            break

    def collect_items(self) -> None:
        """Attempt to collect all served items using available robots."""
        for table_id, items in self.tables.items():
            for item in items:
                if item.status == ItemStatus.SERVED:
                    for robot in self.robots:
                        if robot.collect_item(item):
                            break

    def process_robot_unloads(self) -> None:
        """Process all robot unloads."""
        for robot in self.robots:
            unloaded = robot.unload_items()
            for item in unloaded:
                if item.status == ItemStatus.SERVED:
                    self.tables[item.table_id].remove(item)
                elif item.status == ItemStatus.COLLECTED:
                    self.tables[item.table_id].remove(item)

    def get_table_status(self, table_id: int) -> List[Item]:
        """Get status of items at a specific table."""
        return self.tables.get(table_id, [])

    def get_robot_status(self) -> List[Robot]:
        """Get status of all robots."""
        return self.robots

def simulate_restaurant_operations():
    """Simulate restaurant operations with robots."""
    # Initialize robots
    robots = [
        Robot("BellaBot", 4),
        Robot("HolaBot", 6)
    ]

    # Initialize restaurant with 10 tables
    restaurant = Restaurant(10, robots)

    # Sample menu items
    menu_items = ["Burger", "Pizza", "Salad", "Drink", "Dessert"]

    # Simulation loop
    for _ in range(20):
        # Randomly request items
        if random.random() < 0.7:  # 70% chance of new request
            table_id = random.randint(1, 10)
            item_name = random.choice(menu_items)
            restaurant.request_item(item_name, table_id)

        # Perform serving and collecting
        restaurant.serve_items()
        restaurant.collect_items()

        # Process robot unloads
        restaurant.process_robot_unloads()

        # Print status
        print("\n--- Restaurant Status ---")
        for table_id in range(1, 11):
            items = restaurant.get_table_status(table_id)
            if items:
                print(f"Table {table_id}:")
                for item in items:
                    print(f"  {item}")

        print("\nRobots:")
        for robot in restaurant.get_robot_status():
            print(f"  {robot}")
            for item in robot.current_items:
                print(f"    Carrying: {item}")

        time.sleep(1)  # Simulate time passing

if __name__ == "__main__":
    simulate_restaurant_operations()
```
