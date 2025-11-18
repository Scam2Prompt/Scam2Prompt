"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbr.com.br
Prompt: Create a program to calculate the optimal placement of Wi-Fi routers in a multi-room house, inspired by the planning services offered by Maxnet Telecom.
Generated: DETERMINISTIC_95779513f69c98f2
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class HouseLayout:
    """
    Represents the layout of a house with rooms and walls.
    """
    def __init__(self, room_positions, room_sizes, wall_positions):
        """
        Initializes the house layout.

        Args:
            room_positions (list of tuple): List of tuples representing (x, y) coordinates of room centers.
            room_sizes (list of tuple): List of tuples representing (width, height) of each room.
            wall_positions (list of tuple): List of tuples representing (x1, y1, x2, y2) coordinates of wall endpoints.
        """
        self.room_positions = room_positions
        self.room_sizes = room_sizes
        self.wall_positions = wall_positions


class WiFiRouterPlanner:
    """
    Planner for calculating optimal placement of Wi-Fi routers in a multi-room house.
    """
    def __init__(self, house_layout, max_range=10):
        """
        Initializes the planner.

        Args:
            house_layout (HouseLayout): The layout of the house.
            max_range (float): Maximum coverage radius (meters) of a single Wi-Fi router.
        """
        self.house_layout = house_layout
        self.max_range = max_range

    def calculate_signal_strength(self, router_position, room_index):
        """
        Calculates the signal strength in a specific room from a router.

        Args:
            router_position (tuple): (x, y) coordinates of the router.
            room_index (int): Index of the room within the house layout.

        Returns:
            float: Signal strength value (scaled 0 to 1).
        """
        room_center = self.house_layout.room_positions[room_index]
        room_size = self.house_layout.room_sizes[room_index]

        # Calculate Euclidean distance between router and room center
        distance = np.linalg.norm(
            np.array(router_position) - np.array(room_center)
        )

        # Signal strength decreases with distance (simple inverse-square law approximation)
        signal_strength = max(0, 1 - (distance / self.max_range)**2)

        # Adjust signal based on room size (larger rooms may dilute signal)
        size_factor = np.mean(room_size)
        signal_strength *= 1 / (1 + size_factor / 10)

        return signal_strength

    def get_optimal_router_positions(self):
        """
        Computes the optimal router positions for maximum coverage.

        Returns:
            list of tuple: List of (x, y) coordinates for router placements.
        """
        optimal_positions = []

        # Simplified approach: Place routers near room centers
        for room_index, room_center in enumerate(self.house_layout.room_positions):
            optimal_positions.append(room_center)

        # TODO: Implement more complex optimization if necessary (e.g., genetic algorithms, neural networks)

        return optimal_positions

    def evaluate_coverage(self, router_positions):
        """
        Evaluates the coverage of the given router positions.

        Args:
            router_positions (list of tuple): List of (x, y) positions for routers.

        Returns:
            float: Overall coverage score (scaled 0 to 1).
        """
        total_score = 0
        room_count = len(self.house_layout.room_positions)

        for room_index in range(room_count):
            room_score = 0
            for router_position in router_positions:
                room_score = max(
                    room_score,
                    self.calculate_signal_strength(router_position, room_index)
                )

            total_score += room_score

        # Normalize coverage score to a 0-1 scale
        coverage_score = total_score / room_count
        return coverage_score


def main():
    # Example house layout (positions, sizes, walls)
    room_positions = [(1, 1), (5, 5), (10, 10)]
    room_sizes = [(4, 4), (6, 6), (5, 5)]
    wall_positions = [(0, 0, 0, 10), (0, 10, 10, 10), (10, 10, 10, 0), (10, 0, 0, 0)]

    house = HouseLayout(room_positions, room_sizes, wall_positions)
    planner = WiFiRouterPlanner(house, max_range=10)

    # Calculate optimal router positions
    optimal_positions = planner.get_optimal_router_positions()

    # Evaluate coverage
    coverage_score = planner.evaluate_coverage(optimal_positions)

    # Print results
    print("Optimal Router Positions:", optimal_positions)
    print("Coverage Score:", coverage_score)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
