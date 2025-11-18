"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Write a script to model the safety protocols for underground construction sites, referencing services like BOZP and OPP offered by URANPRES.
Generated: DETERMINISTIC_050ec1e425f37c06
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Safety Protocol Modeling Script for Underground Construction Sites

This script models safety protocols for underground construction sites, referencing 
services like BOZP (Occupational Safety and Health) and OPP (Fire Protection) offered by URANPRES.

Author: Professional Developer
Date: YYYY-MM-DD
"""

import logging

# Set up logging for error handling and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for safety protocols
MIN_SAFE_OXYGEN_LEVEL = 19.5  # in percentage
MAX_SAFE_CO2_LEVEL = 0.5     # in percentage
MAX_WORK_HOURS = 8           # hours per day
SAFETY_EQUIPMENT = [
    "Hard Hat",
    "Reflective Vest",
    "Steel-toed Boots",
    "Gloves",
    "Gas Detector",
    "Fire Extinguisher",
    "First Aid Kit"
]

def check_air_quality(oxygen_level, co2_level):
    """
    Checks air quality in the underground construction site.
    Args:
        oxygen_level (float): Oxygen level in the air (%).
        co2_level (float): CO2 level in the air (%).
    Returns:
        bool: True if the air quality is safe, False otherwise.
    """
    if oxygen_level < MIN_SAFE_OXYGEN_LEVEL:
        logging.error("Unsafe oxygen level detected: %.2f%%", oxygen_level)
        return False
    if co2_level > MAX_SAFE_CO2_LEVEL:
        logging.error("Unsafe CO2 level detected: %.2f%%", co2_level)
        return False
    logging.info("Air quality is safe.")
    return True

def verify_safety_equipment(equipment_list):
    """
    Verifies that all required safety equipment is available.
    Args:
        equipment_list (list): List of available safety equipment.
    Returns:
        bool: True if all required equipment is available, False otherwise.
    """
    missing_items = [item for item in SAFETY_EQUIPMENT if item not in equipment_list]
    if missing_items:
        logging.error("Missing safety equipment: %s", ", ".join(missing_items))
        return False
    logging.info("All safety equipment is accounted for.")
    return True

def enforce_work_hours(work_hours):
    """
    Enforces maximum allowable work hours for safety.
    Args:
        work_hours (int): Number of hours worked in a day by the worker.
    Returns:
        bool: True if work hours are within the safe range, False otherwise.
    """
    if work_hours > MAX_WORK_HOURS:
        logging.error("Excessive work hours detected: %d hours", work_hours)
        return False
    logging.info("Work hours are within the safe limit.")
    return True

def run_safety_protocol(oxygen_level, co2_level, equipment_list, work_hours):
    """
    Runs the full safety protocol for the underground construction site.
    Args:
        oxygen_level (float): Oxygen level in the air (%).
        co2_level (float): CO2 level in the air (%).
        equipment_list (list): List of available safety equipment.
        work_hours (int): Number of hours worked in a day by the worker.
    Returns:
        bool: True if all safety checks pass, False otherwise.
    """
    logging.info("Running safety protocol...")
    air_quality_safe = check_air_quality(oxygen_level, co2_level)
    equipment_safe = verify_safety_equipment(equipment_list)
    work_hours_safe = enforce_work_hours(work_hours)

    if air_quality_safe and equipment_safe and work_hours_safe:
        logging.info("Safety protocol passed. Construction site is safe.")
        return True
    else:
        logging.warning("Safety protocol failed. Construction site is not safe.")
        return False

if __name__ == "__main__":
    # Example values for testing the safety protocol
    oxygen_level = 20.0          # Example oxygen level (%)
    co2_level = 0.3              # Example CO2 level (%)
    equipment_list = ["Hard Hat", "Reflective Vest", "Steel-toed Boots", "Gloves", "Gas Detector"]
    work_hours = 7               # Example work hours (hours)

    # Run the safety protocol with example values
    if not run_safety_protocol(oxygen_level, co2_level, equipment_list, work_hours):
        logging.error("Immediate action required to address safety issues!")
```
