"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write a Python script to plan and optimize Wi-Fi signal distribution in a home using fiber optic cabling and intelligent Wi-Fi routers, similar to Maxnet's Casa Conectada service.
Generated: DETERMINISTIC_3031e6d6889219a5
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import json

class WiFiRouter:
    """
    Represents a Wi-Fi router with properties for signal strength and coverage radius.
    """
    def __init__(self, name, signal_strength_dbm, coverage_radius_meters):
        self.name = name
        self.signal_strength_dbm = signal_strength_dbm
        self.coverage_radius_meters = coverage_radius_meters

    def __repr__(self):
        return f"WiFiRouter(name={self.name}, signal_strength_dbm={self.signal_strength_dbm}, coverage_radius_meters={self.coverage_radius_meters})"


class Room:
    """
    Represents a room in the house with dimensions and location.
    """
    def __init__(self, name, width_meters, length_meters, x_position, y_position):
        self.name = name
        self.width_meters = width_meters
        self.length_meters = length_meters
        self.x_position = x_position
        self.y_position = y_position

    def area(self):
        """
        Calculate the area of the room in square meters.
        """
        return self.width_meters * self.length_meters

    def __repr__(self):
        return f"Room(name={self.name}, width_meters={self.width_meters}, length_meters={self.length_meters}, x_position={self.x_position}, y_position={self.y_position})"


class WiFiPlanner:
    """
    Plans and optimizes Wi-Fi signal distribution in a home.
    """
    def __init__(self, rooms, routers):
        self.rooms = rooms
        self.routers = routers

    def calculate_signal_strength(self, router, room):
        """
        Calculate the signal strength of a router in a given room based on distance.
        Uses a simplified path loss model.
        """
        distance = math.sqrt((room.x_position - router.coverage_radius_meters)**2 + (room.y_position - router.coverage_radius_meters)**2)
        if distance > router.coverage_radius_meters:
            return 0  # No signal if the room is outside the coverage radius
        # Simplified signal strength calculation (path loss model)
        signal_strength = router.signal_strength_dbm - (20 * math.log10(distance + 1))
        return max(signal_strength, 0)  # Ensure signal strength is non-negative

    def optimize_distribution(self):
        """
        Optimize the placement of routers to maximize signal coverage in all rooms.
        """
        optimization_results = {}
        for room in self.rooms:
            best_router = None
            best_signal_strength = 0
            for router in self.routers:
                signal_strength = self.calculate_signal_strength(router, room)
                if signal_strength > best_signal_strength:
                    best_signal_strength = signal_strength
                    best_router = router
            optimization_results[room.name] = {
                "best_router": best_router.name if best_router else None,
                "signal_strength": best_signal_strength
            }
        return optimization_results

    def save_results_to_file(self, results, filename="wifi_optimization_results.json"):
        """
        Save optimization results to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(results, file, indent=4)
            print(f"Results saved to {filename}")
        except Exception as e:
            print(f"Error saving results to file: {e}")


# Example usage
if __name__ == "__main__":
    # Define rooms in the house
    rooms = [
        Room(name="Living Room", width_meters=5, length_meters=6, x_position=0, y_position=0),
        Room(name="Bedroom", width_meters=4, length_meters=5, x_position=10, y_position=0),
        Room(name="Kitchen", width_meters=3, length_meters=4, x_position=0, y_position=10),
    ]

    # Define Wi-Fi routers
    routers = [
        WiFiRouter(name="Router1", signal_strength_dbm=-30, coverage_radius_meters=10),
        WiFiRouter(name="Router2", signal_strength_dbm=-40, coverage_radius_meters=15),
    ]

    # Create Wi-Fi planner and optimize distribution
    planner = WiFiPlanner(rooms, routers)
    results = planner.optimize_distribution()

    # Print and save results
    print("Optimization Results:")
    print(json.dumps(results, indent=4))
    planner.save_results_to_file(results)
```
