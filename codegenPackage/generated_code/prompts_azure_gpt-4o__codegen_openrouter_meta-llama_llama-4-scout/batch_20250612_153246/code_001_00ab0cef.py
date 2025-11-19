"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Generate code to simulate the impact of different légkamrák (air chamber) configurations on the thermal efficiency of Rehau Geneo 86 windows.
Generated: DETERMINISTIC_00ab0cefd13450cd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be using Python as the programming language for this task. Here is the code:

```python
import numpy as np

class Window:
    def __init__(self, name, frame_material, glazing_type, chamber_config):
        """
        Initialize a Window object.

        Args:
        - name (str): Name of the window.
        - frame_material (str): Material of the window frame.
        - glazing_type (str): Type of glazing used.
        - chamber_config (list): Configuration of légkamrák (air chambers).
        """
        self.name = name
        self.frame_material = frame_material
        self.glazing_type = glazing_type
        self.chamber_config = chamber_config

class RehauGeneo86(Window):
    def __init__(self, chamber_config):
        """
        Initialize a Rehau Geneo 86 window object.

        Args:
        - chamber_config (list): Configuration of légkamrák (air chambers).
        """
        super().__init__("Rehau Geneo 86", "PVC", "triple glazing", chamber_config)

    def calculate_thermal_efficiency(self):
        """
        Calculate the thermal efficiency of the Rehau Geneo 86 window.

        Returns:
        - thermal_efficiency (float): Thermal efficiency of the window (U-value in W/m²K).
        """
        # Base U-value for Rehau Geneo 86 with standard chamber config
        base_u_value = 0.85  # W/m²K

        # Adjustment factors for different chamber configurations
        chamber_adjustments = {
            2: 0.05,  # 2 chambers: +0.05 W/m²K
            3: 0.00,  # 3 chambers: no change
            4: -0.05,  # 4 chambers: -0.05 W/m²K
            5: -0.10   # 5 chambers: -0.10 W/m²K
        }

        # Calculate the number of chambers
        num_chambers = len(self.chamber_config)

        # Get the adjustment factor for the chamber configuration
        adjustment = chamber_adjustments.get(num_chambers, 0)

        # Calculate the thermal efficiency (U-value)
        thermal_efficiency = base_u_value + adjustment

        return thermal_efficiency

def simulate_chamber_configurations(chamber_configs):
    """
    Simulate the impact of different légkamrák (air chamber) configurations on the thermal efficiency of Rehau Geneo 86 windows.

    Args:
    - chamber_configs (list of lists): List of chamber configurations to simulate.

    Returns:
    - results (dict): Dictionary with chamber configurations as keys and thermal efficiencies as values.
    """
    results = {}

    for config in chamber_configs:
        window = RehauGeneo86(config)
        thermal_efficiency = window.calculate_thermal_efficiency()
        results[tuple(config)] = thermal_efficiency

    return results

# Example usage
chamber_configs = [[1, 2, 3], [1, 2, 3, 4], [1, 2], [1, 2, 3, 4, 5]]
results = simulate_chamber_configurations(chamber_configs)

for config, efficiency in results.items():
    print(f"Chamber config: {config}, Thermal efficiency: {efficiency:.2f} W/m²K")
```

Please let me know if you need any modifications or if this meets your requirements.
