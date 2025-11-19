"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write code to simulate a Wi-Fi signal distribution analysis for a home, considering factors like room size and router placement, as described in Maxnet Telecom's "Casa Conectada" service.
Generated: DETERMINISTIC_99e21bbb34f47471
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class Room:
    """
    A class to represent a room in the house for Wi-Fi signal analysis.
    
    Attributes:
        length (float): Length of the room in meters.
        width (float): Width of the room in meters.
        router_position (tuple): (x, y) coordinates of the router in the room.
    """
    
    def __init__(self, length, width, router_position):
        self.length = length
        self.width = width
        self.router_position = router_position

    def is_within_bounds(self, x, y):
        """Check if the given coordinates are within the room's bounds."""
        return 0 <= x <= self.length and 0 <= y <= self.width

class WifiSignal:
    """
    A class to simulate Wi-Fi signal distribution in a room.
    
    Attributes:
        room (Room): The room where the Wi-Fi signal is analyzed.
        signal_strength (float): The initial signal strength from the router.
    """
    
    def __init__(self, room, signal_strength=100):
        self.room = room
        self.signal_strength = signal_strength

    def calculate_signal_strength(self, x, y):
        """
        Calculate the Wi-Fi signal strength at a given (x, y) position.
        
        Args:
            x (float): The x-coordinate in the room.
            y (float): The y-coordinate in the room.
        
        Returns:
            float: The calculated signal strength at the given position.
        """
        if not self.room.is_within_bounds(x, y):
            return 0  # No signal outside the room
        
        # Calculate distance from the router
        distance = np.sqrt((x - self.room.router_position[0]) ** 2 + 
                           (y - self.room.router_position[1]) ** 2)
        
        # Signal strength decreases with distance (simple model)
        if distance == 0:
            return self.signal_strength  # Full strength at the router
        
        # Signal strength decreases inversely with distance squared
        return max(0, self.signal_strength / (distance ** 2))

    def generate_signal_map(self, resolution=0.1):
        """
        Generate a signal strength map for the room.
        
        Args:
            resolution (float): The step size for the grid.
        
        Returns:
            np.ndarray: A 2D array representing signal strength across the room.
        """
        x_values = np.arange(0, self.room.length, resolution)
        y_values = np.arange(0, self.room.width, resolution)
        signal_map = np.zeros((len(x_values), len(y_values)))

        for i, x in enumerate(x_values):
            for j, y in enumerate(y_values):
                signal_map[i, j] = self.calculate_signal_strength(x, y)

        return signal_map

    def plot_signal_map(self):
        """Plot the Wi-Fi signal strength distribution in the room."""
        signal_map = self.generate_signal_map()
        plt.imshow(signal_map, extent=(0, self.room.length, 0, self.room.width), origin='lower', cmap='hot')
        plt.colorbar(label='Signal Strength (arbitrary units)')
        plt.scatter(*self.room.router_position, color='blue', label='Router Position', marker='x', s=100)
        plt.title('Wi-Fi Signal Distribution')
        plt.xlabel('Room Length (m)')
        plt.ylabel('Room Width (m)')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Define room dimensions and router position
        room_length = 5.0  # meters
        room_width = 4.0   # meters
        router_position = (2.5, 2.0)  # center of the room

        # Create Room and WifiSignal instances
        room = Room(room_length, room_width, router_position)
        wifi_signal = WifiSignal(room)

        # Plot the Wi-Fi signal distribution
        wifi_signal.plot_signal_map()
    except Exception as e:
        print(f"An error occurred: {e}")
```
