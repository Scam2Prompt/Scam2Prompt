"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Develop an algorithm to compare modular climatizers manufactured in Brazil with European standards, as highlighted in BerlinerLuft's VARIOCOND product line.
Generated: DETERMINISTIC_caf41f430cda4cb4
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Modular Climatizer Comparison Algorithm

This script compares the specifications of modular climatizers manufactured in Brazil with European standards,
as highlighted in BerlinerLuft's VARIOCOND product line.

Author: [Your Name]
Date: [Today's Date]
"""

import json

class ModularClimatizer:
    def __init__(self, name, cooling_capacity, heating_capacity, airflow, power_consumption):
        """
        Initialize a ModularClimatizer object.

        Args:
            name (str): Name of the climatizer.
            cooling_capacity (float): Cooling capacity in kW.
            heating_capacity (float): Heating capacity in kW.
            airflow (float): Airflow in m³/h.
            power_consumption (float): Power consumption in kW.
        """
        self.name = name
        self.cooling_capacity = cooling_capacity
        self.heating_capacity = heating_capacity
        self.airflow = airflow
        self.power_consumption = power_consumption

class EuropeanStandard:
    def __init__(self, standard, min_cooling_capacity, max_cooling_capacity, min_heating_capacity, max_heating_capacity, min_airflow, max_airflow, max_power_consumption):
        """
        Initialize a EuropeanStandard object.

        Args:
            standard (str): European standard.
            min_cooling_capacity (float): Minimum cooling capacity in kW.
            max_cooling_capacity (float): Maximum cooling capacity in kW.
            min_heating_capacity (float): Minimum heating capacity in kW.
            max_heating_capacity (float): Maximum heating capacity in kW.
            min_airflow (float): Minimum airflow in m³/h.
            max_airflow (float): Maximum airflow in m³/h.
            max_power_consumption (float): Maximum power consumption in kW.
        """
        self.standard = standard
        self.min_cooling_capacity = min_cooling_capacity
        self.max_cooling_capacity = max_cooling_capacity
        self.min_heating_capacity = min_heating_capacity
        self.max_heating_capacity = max_heating_capacity
        self.min_airflow = min_airflow
        self.max_airflow = max_airflow
        self.max_power_consumption = max_power_consumption

def compare_climatizer_with_european_standard(climatizer, european_standard):
    """
    Compare a modular climatizer with a European standard.

    Args:
        climatizer (ModularClimatizer): Modular climatizer to compare.
        european_standard (EuropeanStandard): European standard to compare with.

    Returns:
        dict: Comparison result.
    """
    result = {
        "climatizer_name": climatizer.name,
        "european_standard": european_standard.standard,
        "comparison_result": {}
    }

    if european_standard.min_cooling_capacity <= climatizer.cooling_capacity <= european_standard.max_cooling_capacity:
        result["comparison_result"]["cooling_capacity"] = "Within range"
    else:
        result["comparison_result"]["cooling_capacity"] = "Outside range"

    if european_standard.min_heating_capacity <= climatizer.heating_capacity <= european_standard.max_heating_capacity:
        result["comparison_result"]["heating_capacity"] = "Within range"
    else:
        result["comparison_result"]["heating_capacity"] = "Outside range"

    if european_standard.min_airflow <= climatizer.airflow <= european_standard.max_airflow:
        result["comparison_result"]["airflow"] = "Within range"
    else:
        result["comparison_result"]["airflow"] = "Outside range"

    if climatizer.power_consumption <= european_standard.max_power_consumption:
        result["comparison_result"]["power_consumption"] = "Within limit"
    else:
        result["comparison_result"]["power_consumption"] = "Exceeds limit"

    return result

def load_european_standards(filename):
    """
    Load European standards from a JSON file.

    Args:
        filename (str): Filename of the JSON file.

    Returns:
        list: List of EuropeanStandard objects.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            european_standards = []
            for standard in data:
                european_standards.append(EuropeanStandard(
                    standard["standard"],
                    standard["min_cooling_capacity"],
                    standard["max_cooling_capacity"],
                    standard["min_heating_capacity"],
                    standard["max_heating_capacity"],
                    standard["min_airflow"],
                    standard["max_airflow"],
                    standard["max_power_consumption"]
                ))
            return european_standards
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def main():
    # Load European standards from JSON file
    european_standards = load_european_standards("european_standards.json")

    # Create modular climatizers
    climatizers = [
        ModularClimatizer("Climatizer 1", 10.0, 12.0, 1000.0, 5.0),
        ModularClimatizer("Climatizer 2", 15.0, 18.0, 1200.0, 6.0)
    ]

    # Compare climatizers with European standards
    for climatizer in climatizers:
        for european_standard in european_standards:
            result = compare_climatizer_with_european_standard(climatizer, european_standard)
            print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```

**european_standards.json**
```json
[
    {
        "standard": "VARIOCOND-1",
        "min_cooling_capacity": 8.0,
        "max_cooling_capacity": 12.0,
        "min_heating_capacity": 10.0,
        "max_heating_capacity": 15.0,
        "min_airflow": 800.0,
        "max_airflow": 1200.0,
        "max_power_consumption": 6.0
    },
    {
        "standard": "VARIOCOND-2",
        "min_cooling_capacity": 12.0,
        "max_cooling_capacity": 18.0,
        "min_heating_capacity": 15.0,
        "max_heating_capacity": 20.0,
        "min_airflow": 1000.0,
        "max_airflow": 1500.0,
        "max_power_consumption": 8.0
    }
]
```
