"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Generate a Python script that automates the process of selecting the right type of air compressor (e.g., piston, screw, scroll) based on user-defined criteria, referencing the product categories from Só Compressores e Bombas.
Generated: DETERMINISTIC_ffd0d8b324912239
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Dictionary to hold compressor types and their characteristics
COMPRESSORS = {
    "piston": {
        "applications": ["nail guns", "spray painting", "small tools"],
        "pressure_range": (30, 150),  # in PSI
        "cost": "low",
        "maintenance": "high"
    },
    "screw": {
        "applications": ["industrial operations", "continuous use"],
        "pressure_range": (100, 200),  # in PSI
        "cost": "high",
        "maintenance": "low"
    },
    "scroll": {
        "applications": ["HVAC", "medical applications"],
        "pressure_range": (50, 150),  # in PSI
        "cost": "medium",
        "maintenance": "medium"
    }
}

def select_compressor(application, desired_pressure):
    """
    Selects the appropriate air compressor type based on the application and desired pressure.

    :param application: str - The application for which the compressor is needed.
    :param desired_pressure: float - The desired pressure output in PSI.
    :return: str - Recommendation of the compressor type or an error message.
    """
    try:
        for compressor_type, specs in COMPRESSORS.items():
            # Check if the application is suitable
            if application.lower() in specs["applications"]:
                # Check if the desired pressure is within the range
                if specs["pressure_range"][0] <= desired_pressure <= specs["pressure_range"][1]:
                    return f"Recommended Compressor Type: {compressor_type.capitalize()}"
        
        # If no suitable compressor is found
        return "No suitable compressor found for the given criteria."

    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to run the compressor selection script.
    """
    print("Welcome to the Air Compressor Selector!")
    
    # User input for application and pressure
    application = input("Enter the application (e.g. nail guns, industrial operations, HVAC): ")
    pressure_input = input("Enter the desired pressure (in PSI): ")
    
    try:
        # Convert input pressure to float
        desired_pressure = float(pressure_input)
        
        # Get the recommended compressor type
        result = select_compressor(application, desired_pressure)
        print(result)
    
    except ValueError:
        print("Invalid input for pressure. Please enter a numeric value.")

if __name__ == "__main__":
    main()
```
