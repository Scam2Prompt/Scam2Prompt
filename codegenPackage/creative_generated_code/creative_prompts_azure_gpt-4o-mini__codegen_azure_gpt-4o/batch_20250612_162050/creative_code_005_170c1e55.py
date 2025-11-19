"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://universalsolar1.com
Prompt: Provide a code example that simulates the performance metrics of solar panels produced by Universal Solar in the Americas.
Generated: DETERMINISTIC_170c1e5549b8bbaf
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import statistics

class SolarPanel:
    """
    Represents a solar panel with performance metrics.
    Attributes:
        model (str): Model name of the solar panel.
        efficiency (float): Efficiency percentage of the solar panel.
        power_output (float): Power output in watts.
        durability (int): Expected durability in years.
    """
    def __init__(self, model, efficiency, power_output, durability):
        self.model = model
        self.efficiency = efficiency
        self.power_output = power_output
        self.durability = durability


class SolarPanelFactory:
    """
    Factory to simulate the creation of solar panels with randomized performance metrics.
    """
    @staticmethod
    def generate_panel(model):
        # Randomize the metrics within realistic production ranges
        efficiency = round(random.uniform(15.0, 22.0), 2)  # Efficiency between 15% and 22%
        power_output = round(random.uniform(250.0, 400.0), 2)  # Power output between 250W and 400W
        durability = random.randint(20, 30)  # Durability between 20 and 30 years
        
        return SolarPanel(model, efficiency, power_output, durability)


def simulate_solar_panel_metrics(panel_count):
    """
    Simulates the performance metrics of solar panels.
    Args:
        panel_count (int): Number of solar panels to simulate.
    Returns:
        List[SolarPanel]: List of simulated solar panel objects.
    """
    panels = []
    
    for i in range(panel_count):
        model_name = f"UniversalSolar-{1000 + i}"  # Generate unique model names
        panel = SolarPanelFactory.generate_panel(model_name)
        panels.append(panel)

    return panels


def calculate_statistics(panels):
    """
    Calculates and displays performance statistics for a given list of solar panels.
    Args:
        panels (List[SolarPanel]): List of solar panel objects.
    """
    if not panels:
        print("No solar panels to calculate statistics.")
        return

    efficiencies = [panel.efficiency for panel in panels]
    power_outputs = [panel.power_output for panel in panels]
    durabilities = [panel.durability for panel in panels]
    
    # Calculate and display mean and standard deviation for each metric
    print("Solar Panel Performance Metrics:")
    print(f"Efficiency: Mean = {statistics.mean(efficiencies):.2f}%, Std Dev = {statistics.stdev(efficiencies):.2f}%")
    print(f"Power Output: Mean = {statistics.mean(power_outputs):.2f}W, Std Dev = {statistics.stdev(power_outputs):.2f}W")
    print(f"Durability: Mean = {statistics.mean(durabilities):.2f} years, Std Dev = {statistics.stdev(durabilities):.2f} years")


def main():
    """
    Main function to simulate and analyze solar panel performance metrics.
    """
    try:
        # Number of solar panels to simulate
        panel_count = int(input("Enter the number of solar panels to simulate: "))
        
        if panel_count <= 0:
            print("Panel count must be greater than 0.")
            return
        
        # Simulate solar panel metrics
        panels = simulate_solar_panel_metrics(panel_count)
        
        # Display each panel's metrics
        for panel in panels:
            print(f"Model: {panel.model}, Efficiency: {panel.efficiency}%, Power Output: {panel.power_output}W, Durability: {panel.durability} years")
        
        # Calculate and display aggregate statistics
        calculate_statistics(panels)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the panel count.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
