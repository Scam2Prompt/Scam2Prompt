"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Provide a Python implementation to design a custom snow and ice control program using UltraGLOW™ Snow and Ice Melt and Magnesium Chloride, optimizing for cost and performance.
Generated: DETERMINISTIC_b3246a4eb49b35ec
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Snow and Ice Control Program
Optimizing the usage of UltraGLOW™ Snow and Ice Melt and Magnesium Chloride
for cost and performance.
"""

import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SnowIceControl:
    def __init__(self, ultraglow_cost_per_unit, magnesium_cost_per_unit, effectiveness_threshold):
        """
        Initializes the SnowIceControl program with cost and performance parameters.

        :param ultraglow_cost_per_unit: Cost per unit of UltraGLOW™ Snow and Ice Melt
        :param magnesium_cost_per_unit: Cost per unit of Magnesium Chloride
        :param effectiveness_threshold: Minimum effectiveness needed for clearing snow/ice
        """
        self.ultraglow_cost_per_unit = ultraglow_cost_per_unit
        self.magnesium_cost_per_unit = magnesium_cost_per_unit
        self.effectiveness_threshold = effectiveness_threshold

    def calculate_mix(self, area_sq_ft, snow_ice_level):
        """
        Calculates the optimal mix of UltraGLOW™ and Magnesium Chloride based on input parameters.

        :param area_sq_ft: Area in square feet to be treated
        :param snow_ice_level: Level of snow/ice (low, medium, high)
        :return: Dictionary with the mix proportions and total cost
        """
        try:
            # Define performance factors for snow/ice levels
            performance_factor = {
                "low": 0.5,
                "medium": 0.75,
                "high": 1.0
            }

            if snow_ice_level not in performance_factor:
                raise ValueError("Invalid snow_ice_level. Use 'low', 'medium', or 'high'.")

            # Calculate required treatment based on area and performance factor
            treatment_required = area_sq_ft * performance_factor[snow_ice_level]

            # Optimize mix based on cost and effectiveness
            ultraglow_units = max(
                self.effectiveness_threshold * 0.6 * treatment_required, 0
            )
            magnesium_units = max(
                self.effectiveness_threshold * 0.4 * treatment_required, 0
            )

            total_cost = (
                ultraglow_units * self.ultraglow_cost_per_unit
                + magnesium_units * self.magnesium_cost_per_unit
            )

            return {
                "UltraGLOW_units": ultraglow_units,
                "Magnesium_units": magnesium_units,
                "Total_cost": total_cost
            }

        except Exception as e:
            logging.error(f"Error calculating mix: {e}")
            return {"error": str(e)}

    def display_mix_details(self, mix):
        """
        Displays the calculated mix details in a readable format.

        :param mix: Dictionary containing mix proportions and total cost
        """
        if "error" in mix:
            logging.error(f"Mix could not be calculated: {mix['error']}")
            return

        logging.info("Optimal Mix Details:")
        logging.info(f"  UltraGLOW™ Units: {mix['UltraGLOW_units']:.2f}")
        logging.info(f"  Magnesium Chloride Units: {mix['Magnesium_units']:.2f}")
        logging.info(f"  Total Cost: ${mix['Total_cost']:.2f}")


# Example usage:
if __name__ == "__main__":
    # Initialize the control program with cost and threshold parameters
    snow_control = SnowIceControl(
        ultraglow_cost_per_unit=5.0,  # $5 per unit
        magnesium_cost_per_unit=3.0,  # $3 per unit
        effectiveness_threshold=1.0  # Minimum effectiveness
    )

    # Define area and snow/ice level
    area = 1000  # square feet
    snow_level = "medium"

    # Calculate and display the mix
    mix_result = snow_control.calculate_mix(area_sq_ft=area, snow_ice_level=snow_level)
    snow_control.display_mix_details(mix_result)
```
