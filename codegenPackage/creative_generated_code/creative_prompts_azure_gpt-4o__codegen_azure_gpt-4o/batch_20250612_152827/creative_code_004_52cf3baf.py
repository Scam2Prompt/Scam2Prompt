"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Write code to simulate the color calibration process for printing packaging boxes, ensuring minimal color deviation, as described in Metis's emphasis on accurate color reproduction.
Generated: DETERMINISTIC_52cf3bafd82dd96f
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class ColorCalibration:
    """
    A class to simulate the color calibration process for printing packaging boxes.
    Ensures minimal color deviation by comparing target and printed colors.
    """
    
    def __init__(self, target_colors, tolerance=0.01):
        """
        Initializes the ColorCalibration instance.

        :param target_colors: A dictionary of target colors (e.g., {'Red': (255, 0, 0), 'Blue': (0, 0, 255)}).
        :param tolerance: Maximum acceptable deviation in color values (default: 0.01).
        """
        self.target_colors = target_colors
        self.tolerance = tolerance

    def calculate_color_deviation(self, printed_color, target_color):
        """
        Calculates the color deviation using Euclidean distance in RGB space.

        :param printed_color: A tuple representing the RGB values of a printed color (e.g., (250, 5, 0)).
        :param target_color: A tuple representing the RGB values of the target color (e.g., (255, 0, 0)).
        :return: The deviation between the printed color and the target color.
        """
        deviation = np.sqrt(sum((p - t) ** 2 for p, t in zip(printed_color, target_color)))
        return deviation

    def calibrate_colors(self, printed_colors):
        """
        Simulates the calibration process by checking and adjusting printed colors.

        :param printed_colors: A dictionary of printed colors (e.g., {'Red': (250, 5, 0), 'Blue': (0, 0, 240)}).
        :return: A dictionary of calibrated colors and their deviations.
        """
        calibrated_colors = {}
        
        for color_name, target_color in self.target_colors.items():
            printed_color = printed_colors.get(color_name)
            if not printed_color:
                raise ValueError(f"Printed color for '{color_name}' is missing.")
            
            deviation = self.calculate_color_deviation(printed_color, target_color)
            calibrated_colors[color_name] = {
                "printed_color": printed_color,
                "target_color": target_color,
                "deviation": deviation,
                "calibration_needed": deviation > self.tolerance
            }
            
        return calibrated_colors

    def print_report(self, calibration_results):
        """
        Prints a detailed report of the calibration results.

        :param calibration_results: A dictionary containing calibration results.
        """
        print("Color Calibration Report:")
        for color_name, result in calibration_results.items():
            print(f"- {color_name}:")
            print(f"  Printed Color: {result['printed_color']}")
            print(f"  Target Color: {result['target_color']}")
            print(f"  Deviation: {result['deviation']:.4f}")
            print(f"  Calibration Needed: {'Yes' if result['calibration_needed'] else 'No'}")
            print()

# Example usage:
if __name__ == "__main__":
    # Define target colors and printed colors
    target_colors = {
        "Red": (255, 0, 0),
        "Blue": (0, 0, 255),
        "Green": (0, 255, 0)
    }
    printed_colors = {
        "Red": (250, 5, 0),
        "Blue": (0, 0, 240),
        "Green": (0, 250, 10)
    }

    # Initialize the calibration process
    calibrator = ColorCalibration(target_colors, tolerance=5.0)

    try:
        # Calibrate colors and generate the report
        calibration_results = calibrator.calibrate_colors(printed_colors)
        calibrator.print_report(calibration_results)
    except ValueError as e:
        print(f"Error: {e}")
```
