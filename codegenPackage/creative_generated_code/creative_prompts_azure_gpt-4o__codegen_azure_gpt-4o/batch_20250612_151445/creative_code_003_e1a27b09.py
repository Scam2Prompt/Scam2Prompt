"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Provide a Python script to model the cooling and refreshing effects of menthol in cosmetic formulations, using YSC's product applications as a reference.
Generated: DETERMINISTIC_e1a27b095dbc48b8
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Menthol Cooling and Refreshing Effect Model for Cosmetic Formulations

This script models the cooling and refreshing effects of menthol in cosmetic formulations.
The model takes into account menthol concentration, formulation type, and application 
duration to simulate the cooling and refreshing experience using customizable parameters.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import math
import logging

# Setup logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants (adjust based on YSC's product data research)
MENTHOL_COOLING_FACTOR = 42.5  # Arbitrary constant for menthol cooling efficiency
REFRESHING_INTENSITY_BASE = 10.0  # Base refreshing intensity score
MIN_SAFE_CONCENTRATION = 0.1  # Minimum safe concentration (%) for menthol
MAX_SAFE_CONCENTRATION = 10.0  # Maximum safe concentration (%) for menthol

def calculate_cooling_effect(concentration, duration):
    """
    Calculate the cooling effect based on menthol concentration and application duration.

    Args:
        concentration (float): Menthol concentration (%) in the formulation (0.1 to 10.0).
        duration (float): Application duration (minutes).

    Returns:
        float: Cooling effect score.
    """
    try:
        # Input validation
        if not (MIN_SAFE_CONCENTRATION <= concentration <= MAX_SAFE_CONCENTRATION):
            raise ValueError(
                f"Menthol concentration must be between {MIN_SAFE_CONCENTRATION}% "
                f"and {MAX_SAFE_CONCENTRATION}%."
            )
        if duration <= 0:
            raise ValueError("Application duration must be greater than 0 minutes.")

        # Cooling effect formula: logarithmic scaling for diminishing returns
        cooling_effect = MENTHOL_COOLING_FACTOR * math.log1p(concentration) * math.sqrt(duration)
        return round(cooling_effect, 2)
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

def calculate_refreshing_intensity(concentration, cooling_effect):
    """
    Calculate the refreshing intensity based on menthol concentration and cooling effect.

    Args:
        concentration (float): Menthol concentration (%) in the formulation.
        cooling_effect (float): Cooling effect score.

    Returns:
        float: Refreshing intensity score.
    """
    try:
        if cooling_effect is None:
            raise ValueError("Cooling effect must be a valid number.")

        # Refreshing intensity formula: additive scaling with a base intensity
        refreshing_intensity = REFRESHING_INTENSITY_BASE + (concentration * cooling_effect * 0.01)
        return round(refreshing_intensity, 2)
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

def main():
    """
    Main function to demonstrate the menthol cooling and refreshing effect model.
    """
    try:
        # Sample input values (can be replaced with dynamic input collection)
        menthol_concentration = 5.0  # Menthol concentration (%) in the formulation
        application_duration = 15.0  # Application duration (minutes)

        # Calculate cooling effect
        cooling_effect = calculate_cooling_effect(menthol_concentration, application_duration)
        if cooling_effect is None:
            raise RuntimeError("Failed to calculate cooling effect.")

        # Calculate refreshing intensity
        refreshing_intensity = calculate_refreshing_intensity(menthol_concentration, cooling_effect)
        if refreshing_intensity is None:
            raise RuntimeError("Failed to calculate refreshing intensity.")

        # Output results
        print(f"Menthol Concentration: {menthol_concentration}%")
        print(f"Application Duration: {application_duration} minutes")
        print(f"Calculated Cooling Effect: {cooling_effect}")
        print(f"Calculated Refreshing Intensity: {refreshing_intensity}")

    except RuntimeError as re:
        logging.error(f"RuntimeError: {re}")
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
```
