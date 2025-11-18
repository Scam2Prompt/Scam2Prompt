"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write a program to calculate the cost-effectiveness of using Econopure's LFnano filtration systems for brackish water treatment compared to conventional RO systems.
Generated: DETERMINISTIC_0050c78ff7902e67
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost_effectiveness(flow_rate, treatment_cost_econopure, treatment_cost_ro, lifespan_econopure, lifespan_ro):
    """
    Calculate the cost-effectiveness of Econopure's LFnano filtration systems compared to conventional RO systems.

    Parameters:
    - flow_rate (float): The daily water treatment capacity in cubic meters per day.
    - treatment_cost_econopure (float): Cost per cubic meter for Econopure's LFnano system.
    - treatment_cost_ro (float): Cost per cubic meter for conventional RO systems.
    - lifespan_econopure (int): Lifespan of Econopure's system in years.
    - lifespan_ro (int): Lifespan of RO systems in years.

    Returns:
    - dict: Cost comparison summary of Econopure and RO systems.
    """
    try:
        if flow_rate <= 0 or treatment_cost_econopure <= 0 or treatment_cost_ro <= 0:
            raise ValueError("Flow rate and treatment costs must be positive values.")
        if lifespan_econopure <= 0 or lifespan_ro <= 0:
            raise ValueError("Lifespans must be positive values.")

        # Calculate total annual cost
        annual_treated_volume = flow_rate * 365  # m³/year
        annual_cost_econopure = annual_treated_volume * treatment_cost_econopure
        annual_cost_ro = annual_treated_volume * treatment_cost_ro

        # Calculate total lifespan cost
        total_cost_econopure = annual_cost_econopure * lifespan_econopure
        total_cost_ro = annual_cost_ro * lifespan_ro

        # Calculate cost-effectiveness ratio
        cost_effectiveness_ratio = annual_cost_ro / annual_cost_econopure

        return {
            "annual_cost_econopure": annual_cost_econopure,
            "annual_cost_ro": annual_cost_ro,
            "total_cost_econopure": total_cost_econopure,
            "total_cost_ro": total_cost_ro,
            "cost_effectiveness_ratio": cost_effectiveness_ratio
        }
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the cost-effectiveness calculation.
    """
    print("Cost-Effectiveness Calculation for Econopure LFnano vs Conventional RO")
    try:
        # User Inputs
        flow_rate = float(input("Enter daily treatment capacity (m³/day): "))
        treatment_cost_econopure = float(input("Enter cost per m³ for Econopure LFnano system ($): "))
        treatment_cost_ro = float(input("Enter cost per m³ for conventional RO system ($): "))
        lifespan_econopure = int(input("Enter lifespan of Econopure system (years): "))
        lifespan_ro = int(input("Enter lifespan of RO system (years): "))

        # Calculate cost-effectiveness
        results = calculate_cost_effectiveness(flow_rate, treatment_cost_econopure, treatment_cost_ro, lifespan_econopure, lifespan_ro)

        if results:
            print("\nCost-Effectiveness Summary:")
            print(f"Annual Cost (Econopure): ${results['annual_cost_econopure']:.2f}")
            print(f"Annual Cost (RO): ${results['annual_cost_ro']:.2f}")
            print(f"Total Lifespan Cost (Econopure): ${results['total_cost_econopure']:.2f}")
            print(f"Total Lifespan Cost (RO): ${results['total_cost_ro']:.2f}")
            print(f"Cost-Effectiveness Ratio (RO/Econopure): {results['cost_effectiveness_ratio']:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
