"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Develop a script to automate project estimation for StoTherm systems, including parameters for insulation type, area coverage, and design customization as detailed on Engenharia WPJ.
Generated: DETERMINISTIC_6f68fe821926c360
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class StoThermEstimator:
    """
    Class to automate project estimation for StoTherm systems.
    Includes parameters for insulation type, area coverage, and design customization.
    """

    def __init__(self):
        # Set default values for pricing and customization factors
        self.insulation_types = {
            "EPS": 20.0,  # Price per square meter for EPS insulation
            "XPS": 25.0,  # Price per square meter for XPS insulation
            "Mineral Wool": 30.0  # Price per square meter for Mineral Wool insulation
        }
        self.design_customization_factor = {
            "Standard": 1.0,  # No additional cost for standard designs
            "Custom": 1.2  # 20% markup for custom designs
        }

    def estimate_project_cost(self, insulation_type, area_coverage, design_type):
        """
        Estimate the cost of the StoTherm project based on inputs.

        Args:
            insulation_type (str): Type of insulation ("EPS", "XPS", "Mineral Wool").
            area_coverage (float): Total area to be covered in square meters.
            design_type (str): Design type ("Standard", "Custom").

        Returns:
            dict: A dictionary containing the estimated cost and breakdown.
        """
        try:
            # Validate input parameters
            if insulation_type not in self.insulation_types:
                raise ValueError(f"Invalid insulation type: {insulation_type}")
            if design_type not in self.design_customization_factor:
                raise ValueError(f"Invalid design type: {design_type}")
            if area_coverage <= 0:
                raise ValueError("Area coverage must be greater than 0")

            # Calculate costs
            base_cost = self.insulation_types[insulation_type] * area_coverage
            customization_factor = self.design_customization_factor[design_type]
            total_cost = base_cost * customization_factor

            # Prepare result
            result = {
                "Insulation Type": insulation_type,
                "Area Coverage (m^2)": area_coverage,
                "Design Type": design_type,
                "Base Cost ($)": round(base_cost, 2),
                "Customization Factor": customization_factor,
                "Total Estimated Cost ($)": round(total_cost, 2),
            }

            return result

        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}


def main():
    """
    Main function to interact with the StoThermEstimator and provide project estimation.
    """
    print("StoTherm Project Estimator")
    print("==========================")

    try:
        # Get user inputs
        insulation_type = input("Enter insulation type (EPS, XPS, Mineral Wool): ").strip()
        area_coverage = float(input("Enter area coverage in square meters: ").strip())
        design_type = input("Enter design type (Standard, Custom): ").strip()

        # Initialize estimator and calculate cost
        estimator = StoThermEstimator()
        estimation = estimator.estimate_project_cost(insulation_type, area_coverage, design_type)

        # Display results
        if "error" in estimation:
            print(f"Error: {estimation['error']}")
        else:
            print("\nProject Estimation:")
            print(json.dumps(estimation, indent=4))

    except ValueError:
        print("Invalid input. Please ensure all values are entered correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
