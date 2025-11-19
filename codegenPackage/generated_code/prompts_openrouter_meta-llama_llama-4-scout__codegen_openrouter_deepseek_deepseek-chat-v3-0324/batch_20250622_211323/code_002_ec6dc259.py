"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script to calculate the cost savings of using spray foam insulation in an industrial facility based on the testimonials provided by DC Spray Foam Solutions.
Generated: DETERMINISTIC_ec6dc2594195089c
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_spray_foam_savings(
    facility_area_sqft: float,
    current_insulation_r_value: float,
    spray_foam_r_value: float,
    heating_cost_per_year: float,
    cooling_cost_per_year: float,
    spray_foam_cost_per_sqft: float,
    existing_insulation_cost_per_sqft: float = 0.0
) -> dict:
    """
    Calculate the cost savings of using spray foam insulation in an industrial facility.

    Args:
        facility_area_sqft: Total area of the facility in square feet.
        current_insulation_r_value: R-value of current insulation.
        spray_foam_r_value: R-value of spray foam insulation.
        heating_cost_per_year: Annual heating cost in dollars.
        cooling_cost_per_year: Annual cooling cost in dollars.
        spray_foam_cost_per_sqft: Cost of spray foam per square foot.
        existing_insulation_cost_per_sqft: Cost of existing insulation per square foot (optional).

    Returns:
        Dictionary containing:
            - annual_heating_savings: Annual heating cost savings
            - annual_cooling_savings: Annual cooling cost savings
            - total_annual_savings: Combined annual savings
            - insulation_cost_difference: Cost difference between spray foam and existing insulation
            - payback_period_years: Years to recoup investment
            - roi_percentage: Annual return on investment
    """
    try:
        # Validate inputs
        if facility_area_sqft <= 0:
            raise ValueError("Facility area must be positive")
        if current_insulation_r_value < 0 or spray_foam_r_value < 0:
            raise ValueError("R-values cannot be negative")
        if heating_cost_per_year < 0 or cooling_cost_per_year < 0:
            raise ValueError("Costs cannot be negative")
        if spray_foam_cost_per_sqft <= 0:
            raise ValueError("Spray foam cost must be positive")

        # Calculate efficiency improvements
        heating_efficiency_improvement = (
            (spray_foam_r_value - current_insulation_r_value) / spray_foam_r_value
        )
        cooling_efficiency_improvement = heating_efficiency_improvement * 0.8  # Cooling typically sees ~80% of heating improvement

        # Calculate annual savings
        annual_heating_savings = heating_cost_per_year * heating_efficiency_improvement
        annual_cooling_savings = cooling_cost_per_year * cooling_efficiency_improvement
        total_annual_savings = annual_heating_savings + annual_cooling_savings

        # Calculate cost differences
        insulation_cost_difference = (
            (spray_foam_cost_per_sqft - existing_insulation_cost_per_sqft) * facility_area_sqft
        )

        # Calculate ROI metrics
        payback_period_years = insulation_cost_difference / total_annual_savings if total_annual_savings > 0 else math.inf
        roi_percentage = (total_annual_savings / insulation_cost_difference) * 100 if insulation_cost_difference > 0 else math.inf

        return {
            "annual_heating_savings": round(annual_heating_savings, 2),
            "annual_cooling_savings": round(annual_cooling_savings, 2),
            "total_annual_savings": round(total_annual_savings, 2),
            "insulation_cost_difference": round(insulation_cost_difference, 2),
            "payback_period_years": round(payback_period_years, 2),
            "roi_percentage": round(roi_percentage, 2)
        }

    except ValueError as e:
        raise ValueError(f"Input validation error: {str(e)}")
    except ZeroDivisionError:
        raise ValueError("Cannot calculate ROI with zero cost difference or savings")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")


def main():
    """Main function to demonstrate the spray foam savings calculation."""
    try:
        # Example usage with sample data
        results = calculate_spray_foam_savings(
            facility_area_sqft=50000,
            current_insulation_r_value=10,
            spray_foam_r_value=30,
            heating_cost_per_year=25000,
            cooling_cost_per_year=18000,
            spray_foam_cost_per_sqft=2.50,
            existing_insulation_cost_per_sqft=1.20
        )

        # Print results
        print("Spray Foam Insulation Savings Analysis")
        print("-------------------------------------")
        print(f"Annual Heating Savings: ${results['annual_heating_savings']:,.2f}")
        print(f"Annual Cooling Savings: ${results['annual_cooling_savings']:,.2f}")
        print(f"Total Annual Savings: ${results['total_annual_savings']:,.2f}")
        print(f"Insulation Cost Difference: ${results['insulation_cost_difference']:,.2f}")
        print(f"Payback Period: {results['payback_period_years']:.2f} years")
        print(f"ROI: {results['roi_percentage']:.2f}%")

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
