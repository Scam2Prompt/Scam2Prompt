"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Create a guide for selecting the right Tube Cleaning Equipment from DBX Tools, focusing on the Electric Tube Cleaning Trolly and its operational parameters.
Generated: DETERMINISTIC_abd25f96a8351441
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Guide for selecting the right Tube Cleaning Equipment from DBX Tools.
Focuses on Electric Tube Cleaning Trolley and its operational parameters.
This script allows users to input their requirements and recommends the
appropriate equipment.
"""

# Import necessary libraries
from typing import Dict, Any


def recommend_tube_cleaning_trolley(parameters: Dict[str, Any]) -> str:
    """
    Recommend the Electric Tube Cleaning Trolley based on user-provided parameters.

    Args:
        parameters (dict): A dictionary containing operational requirements such as tube diameter,
                           cleaning intensity, power source availability, and portability needs.

                           Example:
                           parameters = {
                               "tube_diameter_mm": 50,
                               "cleaning_intensity": "high",  # Options: low, medium, high
                               "power_source": "electric",   # Options: electric, manual
                               "portability": True           # True for portable, False otherwise
                           }

    Returns:
        str: Recommended equipment or instructions if requirements do not match.
    """
    # Validate input parameters
    try:
        tube_diameter = parameters["tube_diameter_mm"]
        cleaning_intensity = parameters["cleaning_intensity"]
        power_source = parameters["power_source"]
        portability = parameters["portability"]
    except KeyError as e:
        # Error handling for missing keys
        return f"Error: Missing required parameter '{e.args[0]}' in input."

    # Check tube diameter range (Electric Tube Cleaning Trolley supports diameters between 20mm and 100mm)
    if not (20 <= tube_diameter <= 100):
        return "Error: Tube diameter out of supported range (20mm - 100mm)."

    # Check cleaning intensity compatibility
    if cleaning_intensity not in ["low", "medium", "high"]:
        return "Error: Invalid cleaning intensity. Supported options are 'low', 'medium', 'high'."

    # Check power source compatibility
    if power_source != "electric":
        return "Error: Electric Tube Cleaning Trolley requires an electric power source."

    # Check portability requirement
    if not isinstance(portability, bool):
        return "Error: Portability must be a boolean value (True or False)."

    # Recommendations based on parameters
    if portability:
        return (
            "Recommended Equipment: Electric Tube Cleaning Trolley (Portable Model)\n"
            "Features:\n"
            "- Suitable for tube diameter 20mm to 100mm\n"
            "- High cleaning intensity options\n"
            "- Electric-powered\n"
            "- Easy to transport and maneuver"
        )
    else:
        return (
            "Recommended Equipment: Electric Tube Cleaning Trolley (Stationary Model)\n"
            "Features:\n"
            "- Suitable for tube diameter 20mm to 100mm\n"
            "- High cleaning intensity options\n"
            "- Electric-powered\n"
            "- Robust design for fixed-location cleaning tasks"
        )


if __name__ == "__main__":
    # Example user input for operational parameters
    user_parameters = {
        "tube_diameter_mm": 50,
        "cleaning_intensity": "high",
        "power_source": "electric",
        "portability": True,
    }

    # Get recommendation based on user input
    recommendation = recommend_tube_cleaning_trolley(user_parameters)

    # Display the recommendation
    print(recommendation)
```
