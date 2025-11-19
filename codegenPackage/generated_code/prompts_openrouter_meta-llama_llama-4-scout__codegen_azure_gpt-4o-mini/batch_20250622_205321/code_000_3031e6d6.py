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
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class WiFiRouter:
    def __init__(self, position, signal_strength):
        """
        Initialize a WiFi router with a position and signal strength.
        
        :param position: Tuple (x, y) representing the router's position.
        :param signal_strength: The maximum signal strength of the router.
        """
        self.position = np.array(position)
        self.signal_strength = signal_strength

    def signal_at(self, point):
        """
        Calculate the signal strength at a given point based on the router's position.
        
        :param point: Tuple (x, y) representing the point to evaluate.
        :return: Signal strength at the given point.
        """
        distance = np.linalg.norm(self.position - np.array(point))
        if distance == 0:
            return self.signal_strength  # Full strength at the router's position
        return max(0, self.signal_strength - distance)

class HomeWiFiPlanner:
    def __init__(self, home_size, num_routers):
        """
        Initialize the home WiFi planner.
        
        :param home_size: Tuple (width, height) representing the dimensions of the home.
        :param num_routers: Number of routers to place in the home.
        """
        self.home_size = home_size
        self.num_routers = num_routers
        self.routers = []

    def optimize_router_positions(self):
        """
        Optimize the positions of the routers to maximize signal coverage in the home.
        """
        # Initial random positions for routers
        initial_positions = np.random.rand(self.num_routers, 2) * self.home_size
        
        # Optimize positions using a minimization function
        result = minimize(self._objective_function, initial_positions.flatten(), method='L-BFGS-B', bounds=[(0, self.home_size[0]), (0, self.home_size[1])] * self.num_routers)
        
        # Reshape the result back to router positions
        optimized_positions = result.x.reshape(self.num_routers, 2)
        self.routers = [WiFiRouter(position=pos, signal_strength=10) for pos in optimized_positions]

    def _objective_function(self, positions):
        """
        Objective function to minimize: negative total signal strength in the home.
        
        :param positions: Flattened array of router positions.
        :return: Negative total signal strength.
        """
        total_signal = 0
        for i in range(self.num_routers):
            router_pos = positions[i*2:i*2+2]
            router = WiFiRouter(position=router_pos, signal_strength=10)
            # Calculate signal strength across the home grid
            for x in range(int(self.home_size[0])):
                for y in range(int(self.home_size[1])):
                    total_signal += router.signal_at((x, y))
        return -total_signal  # We minimize the negative signal

    def plot_wifi_coverage(self):
        """
        Plot the WiFi coverage area based on the router positions.
        """
        x = np.linspace(0, self.home_size[0], 100)
        y = np.linspace(0, self.home_size[1], 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros(X.shape)

        for router in self.routers:
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    Z[i, j] += router.signal_at((X[i, j], Y[i, j]))

        plt.figure(figsize=(10, 8))
        plt.contourf(X, Y, Z, levels=50, cmap='viridis')
        plt.colorbar(label='Signal Strength')
        plt.scatter(*zip(*[router.position for router in self.routers]), color='red', label='Routers')
        plt.title('WiFi Signal Distribution')
        plt.xlabel('Home Width')
        plt.ylabel('Home Height')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    try:
        # Define home size and number of routers
        home_size = (20, 15)  # Width x Height in meters
        num_routers = 5

        # Create a home WiFi planner instance
        planner = HomeWiFiPlanner(home_size, num_routers)

        # Optimize router positions
        planner.optimize_router_positions()

        # Plot the WiFi coverage
        planner.plot_wifi_coverage()

    except Exception as e:
        print(f"An error occurred: {e}")
```
