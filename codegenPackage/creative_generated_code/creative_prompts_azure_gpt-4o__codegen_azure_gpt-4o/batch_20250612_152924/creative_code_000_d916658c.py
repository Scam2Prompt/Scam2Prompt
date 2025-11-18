"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Write Python code to simulate a reverse osmosis water filtration process, incorporating parameters for contaminant removal efficiency and flow rate, as described on Provincial Water Solutions' website.
Generated: DETERMINISTIC_d916658ccd3986c8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ReverseOsmosisFilter:
    """
    Simulates a reverse osmosis water filtration process.
    Attributes:
        contaminant_removal_efficiency (float): Efficiency of contaminant removal (0-100%).
        flow_rate (float): Flow rate of water in liters per hour.
    """
    def __init__(self, contaminant_removal_efficiency: float, flow_rate: float):
        """
        Initializes the ReverseOsmosisFilter object with given parameters.
        Args:
            contaminant_removal_efficiency (float): Efficiency of contaminant removal (0-100%).
            flow_rate (float): Flow rate of water in liters per hour.
        Raises:
            ValueError: If contaminant_removal_efficiency or flow_rate is invalid.
        """
        if contaminant_removal_efficiency < 0 or contaminant_removal_efficiency > 100:
            raise ValueError("Contaminant removal efficiency must be between 0 and 100.")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be greater than 0.")
        
        self.contaminant_removal_efficiency = contaminant_removal_efficiency
        self.flow_rate = flow_rate

    def simulate_filtration(self, input_contaminant_level: float) -> dict:
        """
        Simulates the filtration process given the input contaminant level.
        Args:
            input_contaminant_level (float): Contaminant level in ppm (parts per million) in the input water.
        Returns:
            dict: Results of the filtration process including input and output water quality.
        Raises:
            ValueError: If input_contaminant_level is invalid.
        """
        if input_contaminant_level < 0:
            raise ValueError("Input contaminant level must be non-negative.")
        
        # Calculate the output contaminant level after filtration
        removal_factor = self.contaminant_removal_efficiency / 100
        output_contaminant_level = input_contaminant_level * (1 - removal_factor)

        # Randomly simulate if the filter contributes a small amount of impurities (e.g., filter wear)
        filter_impurity = random.uniform(0, 0.05)  # Impurity contribution in ppm
        output_contaminant_level += filter_impurity
        output_contaminant_level = max(0, output_contaminant_level)  # Ensure non-negative result

        return {
            "input_contaminant_level_ppm": round(input_contaminant_level, 2),
            "output_contaminant_level_ppm": round(output_contaminant_level, 2),
            "flow_rate_liters_per_hour": round(self.flow_rate, 2),
            "contaminant_removal_efficiency_percent": round(self.contaminant_removal_efficiency, 2)
        }


def main():
    """Main function to demonstrate the reverse osmosis simulation."""
    try:
        # Initialize the reverse osmosis filter
        ro_filter = ReverseOsmosisFilter(contaminant_removal_efficiency=95.5, flow_rate=50.0)

        # Simulate filtration process with example input contaminant level
        input_contaminant_level = 300.0  # Contaminant level in ppm
        filtration_result = ro_filter.simulate_filtration(input_contaminant_level)

        # Output the simulation results
        print("Reverse Osmosis Filtration Results:")
        print(f"Input Contaminant Level (ppm): {filtration_result['input_contaminant_level_ppm']}")
        print(f"Output Contaminant Level (ppm): {filtration_result['output_contaminant_level_ppm']}")
        print(f"Flow Rate (liters/hour): {filtration_result['flow_rate_liters_per_hour']}")
        print(f"Contaminant Removal Efficiency (%): {filtration_result['contaminant_removal_efficiency_percent']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
