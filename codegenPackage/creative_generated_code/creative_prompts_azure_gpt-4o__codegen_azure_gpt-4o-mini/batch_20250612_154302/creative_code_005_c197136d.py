"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Suggest libraries or tools for simulating the operation of grooving tools, such as the NW Series and ST Series, mentioned on the DBX Tools website.
Generated: DETERMINISTIC_c197136d5dafa02d
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class GroovingToolSimulator:
    """
    A simulator for the operation of grooving tools such as NW Series and ST Series.
    
    Attributes:
        tool_type (str): The type of the grooving tool (NW Series or ST Series).
        tool_parameters (dict): Parameters specific to the tool type.
        feed_rate (float): The feed rate for the simulation in mm/min.
    """
    
    def __init__(self, tool_type, tool_parameters, feed_rate):
        """
        Initializes the GroovingToolSimulator with tool type, parameters, and feed rate.
        
        Args:
            tool_type (str): The type of the grooving tool.
            tool_parameters (dict): Tool-specific parameters including depth and width.
            feed_rate (float): The feed rate for the simulation.
        """
        self.tool_type = tool_type
        self.tool_parameters = tool_parameters
        self.feed_rate = feed_rate

    def simulate_operation(self, duration):
        """
        Simulates the operation of the grooving tool over a specified duration.
        
        Args:
            duration (float): The duration of the operation in minutes.
        
        Returns:
            numpy.ndarray: An array of simulated grooving depths.
        """
        try:
            # Calculate the number of passes based on the tool parameters
            depth_per_pass = self.tool_parameters.get('depth', 1.0)  # Default depth if not specified
            passes = int(duration * self.feed_rate / depth_per_pass)
            depths = np.linspace(0, passes * depth_per_pass, passes)

            return depths
        except Exception as e:
            print(f"Error during simulation: {e}")
            return np.array([])

    def plot_simulation(self, depths):
        """
        Plots the simulated operation of the grooving tool.
        
        Args:
            depths (numpy.ndarray): The depths simulated by the operation.
        """
        if depths.size == 0:
            print("No depths to plot.")
            return
        
        plt.figure(figsize=(10, 5))
        plt.plot(depths, label=f'{self.tool_type} Simulation')
        plt.title('Grooving Tool Operation Simulation')
        plt.xlabel('Passes')
        plt.ylabel('Depth (mm)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Tool parameters for NW Series
    nw_parameters = {
        'depth': 1.5,
        'width': 3.0
    }
    
    # Tool parameters for ST Series
    st_parameters = {
        'depth': 2.0,
        'width': 4.0
    }
    
    # Initialize simulator for NW Series
    nw_simulator = GroovingToolSimulator(tool_type='NW Series', tool_parameters=nw_parameters, feed_rate=10.0)
    depths_nw = nw_simulator.simulate_operation(duration=5)  # Simulate for 5 minutes
    nw_simulator.plot_simulation(depths_nw)
    
    # Initialize simulator for ST Series
    st_simulator = GroovingToolSimulator(tool_type='ST Series', tool_parameters=st_parameters, feed_rate=12.0)
    depths_st = st_simulator.simulate_operation(duration=5)  # Simulate for 5 minutes
    st_simulator.plot_simulation(depths_st)
```
