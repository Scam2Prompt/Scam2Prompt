"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trattar.blogspot.com
Prompt: Generate a script that calculates the mechanical properties (e.g., resistance and density) of treated eucalyptus wood, as outlined by Trattar Madeiras.
Generated: DETERMINISTIC_8ca25746869db8a0
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_mechanical_properties(density, moisture_content, resistance_factor):
    """
    Calculate mechanical properties of treated eucalyptus wood.

    Parameters:
        density (float): Density of the wood in kg/m³.
        moisture_content (float): Moisture content of the wood as a percentage (0-100).
        resistance_factor (float): Resistance factor based on treatment type, typically provided by Trattar Madeiras.

    Returns:
        dict: A dictionary containing the calculated resistance and adjusted density.
    """
    try:
        # Validate input values
        if density <= 0:
            raise ValueError("Density must be a positive number.")
        if not (0 <= moisture_content <= 100):
            raise ValueError("Moisture content must be between 0 and 100.")
        if resistance_factor <= 0:
            raise ValueError("Resistance factor must be a positive number.")

        # Adjust density based on moisture content
        adjusted_density = density * (1 + (moisture_content / 100))

        # Calculate resistance
        resistance = resistance_factor * math.sqrt(adjusted_density)

        # Return results
        return {
            "adjusted_density": round(adjusted_density, 2),
            "resistance": round(resistance, 2)
        }

    except Exception as e:
        # Handle errors and provide meaningful feedback
        print(f"Error calculating mechanical properties: {e}")
        return None


def main():
    """
    Main function to prompt user input and calculate mechanical properties
    of treated eucalyptus wood.
    """
    print("Mechanical Properties Calculator for Treated Eucalyptus Wood")
    try:
        # Prompt user for inputs
        density = float(input("Enter the density of the wood (kg/m³): "))
        moisture_content = float(input("Enter the moisture content of the wood (%): "))
        resistance_factor = float(input("Enter the resistance factor based on treatment: "))

        # Calculate mechanical properties
        properties = calculate_mechanical_properties(density, moisture_content, resistance_factor)

        if properties:
            # Display results to the user
            print("\nCalculated Mechanical Properties:")
            print(f"Adjusted Density: {properties['adjusted_density']} kg/m³")
            print(f"Resistance: {properties['resistance']} units")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
