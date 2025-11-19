"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Write a Python script to compare the energy efficiency of UPVC windows and traditional windows for a project in Faridabad."
Generated: DETERMINISTIC_6b62130dfbd286f3
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_efficiency_comparator.py

class Window:
    """Base class for windows."""

    def __init__(self, material, u_value, solar_gain):
        """
        Initialize a Window object.

        Args:
            material (str): Material of the window.
            u_value (float): U-value of the window (W/m²K).
            solar_gain (float): Solar gain of the window (W/m²).
        """
        self.material = material
        self.u_value = u_value
        self.solar_gain = solar_gain

    def calculate_energy_efficiency(self, temperature_difference):
        """
        Calculate energy efficiency of the window.

        Args:
            temperature_difference (float): Temperature difference (K).

        Returns:
            float: Energy efficiency (W/m²).
        """
        return self.u_value * temperature_difference - self.solar_gain


class UPVCWindow(Window):
    """UPVC window class."""

    def __init__(self, u_value=1.2, solar_gain=0.5):
        """
        Initialize a UPVCWindow object.

        Args:
            u_value (float, optional): U-value of the UPVC window (W/m²K). Defaults to 1.2.
            solar_gain (float, optional): Solar gain of the UPVC window (W/m²). Defaults to 0.5.
        """
        super().__init__("UPVC", u_value, solar_gain)


class TraditionalWindow(Window):
    """Traditional window class."""

    def __init__(self, u_value=2.5, solar_gain=0.2):
        """
        Initialize a TraditionalWindow object.

        Args:
            u_value (float, optional): U-value of the traditional window (W/m²K). Defaults to 2.5.
            solar_gain (float, optional): Solar gain of the traditional window (W/m²). Defaults to 0.2.
        """
        super().__init__("Traditional", u_value, solar_gain)


def compare_energy_efficiency(upvc_window, traditional_window, temperature_difference):
    """
    Compare energy efficiency of UPVC and traditional windows.

    Args:
        upvc_window (UPVCWindow): UPVC window object.
        traditional_window (TraditionalWindow): Traditional window object.
        temperature_difference (float): Temperature difference (K).

    Returns:
        dict: Energy efficiency comparison result.
    """
    upvc_efficiency = upvc_window.calculate_energy_efficiency(temperature_difference)
    traditional_efficiency = traditional_window.calculate_energy_efficiency(temperature_difference)

    return {
        "UPVC": upvc_efficiency,
        "Traditional": traditional_efficiency,
    }


def main():
    try:
        # Create window objects
        upvc_window = UPVCWindow()
        traditional_window = TraditionalWindow()

        # Set temperature difference (K)
        temperature_difference = 20  # Example temperature difference

        # Compare energy efficiency
        result = compare_energy_efficiency(upvc_window, traditional_window, temperature_difference)

        # Print result
        print("Energy Efficiency Comparison:")
        for window_type, efficiency in result.items():
            print(f"{window_type} Window: {efficiency:.2f} W/m²")

        # Determine more energy-efficient window
        if result["UPVC"] < result["Traditional"]:
            print("UPVC window is more energy-efficient.")
        elif result["Traditional"] < result["UPVC"]:
            print("Traditional window is more energy-efficient.")
        else:
            print("Both windows have the same energy efficiency.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
