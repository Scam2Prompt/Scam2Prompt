"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Generate a floor plan for a 7-story shopping mall, like Mall 118 in Merdeka 118 Tower, including a promenade, food court, and entertainment options.
Generated: DETERMINISTIC_1a19c3174927c7df
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mall_floor_plan.py

class Floor:
    def __init__(self, name, area):
        """
        Initialize a Floor object.

        Args:
            name (str): Name of the floor.
            area (float): Area of the floor in square meters.
        """
        self.name = name
        self.area = area
        self.occupancies = []

    def add_occupancy(self, occupancy):
        """
        Add an occupancy to the floor.

        Args:
            occupancy (Occupancy): Occupancy object to add.
        """
        self.occupancies.append(occupancy)


class Occupancy:
    def __init__(self, name, area, type):
        """
        Initialize an Occupancy object.

        Args:
            name (str): Name of the occupancy.
            area (float): Area of the occupancy in square meters.
            type (str): Type of occupancy (e.g. retail, food court, entertainment).
        """
        self.name = name
        self.area = area
        self.type = type


class Mall:
    def __init__(self, name, num_stories):
        """
        Initialize a Mall object.

        Args:
            name (str): Name of the mall.
            num_stories (int): Number of stories in the mall.
        """
        self.name = name
        self.num_stories = num_stories
        self.floors = []

    def add_floor(self, floor):
        """
        Add a floor to the mall.

        Args:
            floor (Floor): Floor object to add.
        """
        self.floors.append(floor)

    def print_floor_plan(self):
        """
        Print the floor plan of the mall.
        """
        for i, floor in enumerate(self.floors):
            print(f"Floor {i+1}: {floor.name} ({floor.area} sqm)")
            for occupancy in floor.occupancies:
                print(f"  - {occupancy.name} ({occupancy.area} sqm, {occupancy.type})")


def create_mall118():
    """
    Create a 7-story shopping mall like Mall118 in Merdeka118 Tower.
    """
    mall = Mall("Mall118", 7)

    # Ground Floor: Promenade
    ground_floor = Floor("Promenade", 10000)
    ground_floor.add_occupancy(Occupancy("Main Entrance", 1000, "promenade"))
    ground_floor.add_occupancy(Occupancy("Retail Shops", 5000, "retail"))
    mall.add_floor(ground_floor)

    # Level 1-2: Retail
    for i in range(2):
        floor = Floor(f"Retail Level {i+1}", 15000)
        floor.add_occupancy(Occupancy("Retail Shops", 10000, "retail"))
        floor.add_occupancy(Occupancy("Food Court", 2000, "food court"))
        mall.add_floor(floor)

    # Level 3: Food Court
    food_court_floor = Floor("Food Court Level", 5000)
    food_court_floor.add_occupancy(Occupancy("Food Court", 4000, "food court"))
    food_court_floor.add_occupancy(Occupancy("Beverage Shops", 1000, "retail"))
    mall.add_floor(food_court_floor)

    # Level 4-5: Entertainment
    for i in range(2):
        floor = Floor(f"Entertainment Level {i+1}", 10000)
        floor.add_occupancy(Occupancy("Cinema", 5000, "entertainment"))
        floor.add_occupancy(Occupancy("Game Zone", 2000, "entertainment"))
        mall.add_floor(floor)

    # Level 6-7: Leisure
    for i in range(2):
        floor = Floor(f"Leisure Level {i+1}", 8000)
        floor.add_occupancy(Occupancy("Bowling Alley", 3000, "leisure"))
        floor.add_occupancy(Occupancy("Fitness Center", 2000, "leisure"))
        mall.add_floor(floor)

    return mall


if __name__ == "__main__":
    mall118 = create_mall118()
    mall118.print_floor_plan()
```
