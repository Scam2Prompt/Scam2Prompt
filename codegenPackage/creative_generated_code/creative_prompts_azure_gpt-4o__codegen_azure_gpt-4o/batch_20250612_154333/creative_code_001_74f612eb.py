"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Generate a script that calculates the optimal depth for using an earth auger drill, incorporating details about its applications in construction and forestry as outlined on the PT. Fuji Metal Teknik webpage.
Generated: DETERMINISTIC_74f612eb400c1718
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the optimal depth for using an earth auger drill.

This script takes input parameters such as soil type, intended application (construction or forestry),
and auger specifications, and calculates the optimal drilling depth based on the PT. Fuji Metal Teknik 
guidelines and general practices.

Dependencies: None
Author: [Your Name]
Date: [Insert Date]
"""

def get_optimal_depth(soil_type, application, auger_diameter):
    """
    Calculate the optimal depth for using an earth auger drill.

    Args:
        soil_type (str): Type of soil (e.g., "clay", "sand", "rocky").
        application (str): Intended application ("construction" or "forestry").
        auger_diameter (float): Diameter of the auger drill in centimeters.

    Returns:
        float: Optimal depth in meters.
    """
    try:
        # Base depth settings based on soil type
        soil_depth_factor = {
            "clay": 1.5,
            "sand": 2.0,
            "rocky": 0.8
        }

        if soil_type not in soil_depth_factor:
            raise ValueError("Invalid soil type. Choose from 'clay', 'sand', or 'rocky'.")

        # Application adjustment factor
        application_factor = {
            "construction": 1.2,
            "forestry": 1.0
        }

        if application not in application_factor:
            raise ValueError("Invalid application. Choose from 'construction' or 'forestry'.")

        # Adjust depth based on auger diameter
        auger_diameter_factor = auger_diameter / 50  # Assume reference diameter is 50 cm

        # Calculate optimal depth
        optimal_depth = soil_depth_factor[soil_type] * application_factor[application] * auger_diameter_factor

        return round(optimal_depth, 2)  # Return depth rounded to 2 decimal places

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to interact with the user and calculate the optimal depth.
    """
    print("Earth Auger Drill Optimal Depth Calculator")
    print("-----------------------------------------")

    try:
        # Get user inputs
        soil_type = input("Enter soil type (clay, sand, rocky): ").strip().lower()
        application = input("Enter application (construction, forestry): ").strip().lower()
        auger_diameter = float(input("Enter auger diameter (in cm): ").strip())

        # Calculate optimal depth
        optimal_depth = get_optimal_depth(soil_type, application, auger_diameter)

        if optimal_depth is not None:
            print(f"The optimal depth for the earth auger drill is: {optimal_depth} meters.")

    except ValueError:
        print("Invalid input. Please enter the correct values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
