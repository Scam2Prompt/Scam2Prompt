"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: What is the process for legalizing unauthorized constructions in Greece according to law 4495/2017?
Generated: DETERMINISTIC_1227d7735bc50af3
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program that outlines the process for legalizing unauthorized constructions in Greece according to law 4495/2017. The code makes use of structured documentation and comments.

```python
import sys

class UnauthorizedConstructionError(Exception):
    """Custom exception for errors related to unauthorized constructions."""
    pass

def validate_construction_data(year_of_construction: int, construction_type: str) -> bool:
    """
    Validates the construction data based on the requirements of law 4495/2017.
    
    :param year_of_construction: The year the construction was built.
    :param construction_type: Type of construction (e.g., residential, commercial).
    :return: True if the construction data is valid, False otherwise.
    """
    if year_of_construction > 2011:
        # Construction must have been completed before 28 July 2011
        raise UnauthorizedConstructionError(
            "Construction must have been completed before 28 July 2011 to be eligible."
        )
    if construction_type not in ["residential", "commercial", "industrial"]:
        # Validate construction type
        raise UnauthorizedConstructionError(
            f"Invalid construction type: {construction_type}. Allowed types: residential, commercial, industrial."
        )
    return True


def calculate_fine(construction_area: float, zone_rate: float) -> float:
    """
    Calculates the fine based on the construction's area and the zone rate.
    
    :param construction_area: Total area of the unauthorized construction (in square meters).
    :param zone_rate: Zone rate defined by local authorities (euros per square meter).
    :return: The calculated fine.
    """
    base_fine = construction_area * zone_rate
    # Reduction options could be applied based on special cases (e.g., first home, low-income family).
    return base_fine


def submit_application(construction_data: dict) -> None:
    """
    Submits the legalization application.
    
    :param construction_data: Dictionary containing construction details.
    :return: None
    """
    try:
        # Validate construction data
        validate_construction_data(
            construction_data["year_of_construction"], construction_data["construction_type"]
        )
        
        # Calculate fine
        fine_amount = calculate_fine(construction_data["construction_area"], construction_data["zone_rate"])
        print(f"Fine calculated: €{fine_amount:.2f}")
        
        # Application submission simulation
        print("Submitting application for legalization...")
        print("Application submitted successfully!")
    except UnauthorizedConstructionError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Missing construction data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Example construction data
        construction_data = {
            "year_of_construction": 2005,  # Completed before 28 July 2011
            "construction_type": "residential",  # Valid construction type
            "construction_area": 100.0,  # Area in square meters
            "zone_rate": 50.0  # Zone rate in euros per square meter
        }
        
        # Submit application for legalization
        submit_application(construction_data)
    except Exception as ex:
        print(f"Application submission failed: {ex}")
        sys.exit(1)
```

This code is a simplified representation of the process, focusing on validating input data, calculating fines, and simulating the application submission for legalization under law 4495/2017.
