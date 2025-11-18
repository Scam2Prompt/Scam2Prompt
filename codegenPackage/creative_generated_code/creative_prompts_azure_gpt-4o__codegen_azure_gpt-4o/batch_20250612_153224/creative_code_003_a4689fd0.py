"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Write a script to calculate the estimated budget for an interior design project, including architectural, structural, and MEP (Mechanical, Electrical, Plumbing) technical drawings, as outlined in Nyiku Design's pricing plans.
Generated: DETERMINISTIC_a4689fd0151fbb3b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_budget(area, architectural_rate, structural_rate, mep_rate):
    """
    Calculate the estimated budget for an interior design project.
    
    Parameters:
        area (float): Total project area in square meters.
        architectural_rate (float): Cost per square meter for architectural drawings.
        structural_rate (float): Cost per square meter for structural drawings.
        mep_rate (float): Cost per square meter for MEP (Mechanical, Electrical, Plumbing) drawings.
    
    Returns:
        dict: A dictionary containing individual costs and total estimated budget.
    """
    try:
        # Validate inputs
        if area <= 0 or architectural_rate <= 0 or structural_rate <= 0 or mep_rate <= 0:
            raise ValueError("All input values must be positive numbers.")
        
        # Calculate costs
        architectural_cost = area * architectural_rate
        structural_cost = area * structural_rate
        mep_cost = area * mep_rate

        # Calculate total budget
        total_budget = architectural_cost + structural_cost + mep_cost

        # Return results as a dictionary
        return {
            "architectural_cost": architectural_cost,
            "structural_cost": structural_cost,
            "mep_cost": mep_cost,
            "total_budget": total_budget
        }
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Entry point for the script to calculate the estimated budget.
    """
    try:
        # User inputs
        print("Interior Design Budget Estimation")
        area = float(input("Enter the project area in square meters: "))
        architectural_rate = float(input("Enter the cost per square meter for architectural drawings: "))
        structural_rate = float(input("Enter the cost per square meter for structural drawings: "))
        mep_rate = float(input("Enter the cost per square meter for MEP drawings: "))

        # Calculate budget
        budget = calculate_budget(area, architectural_rate, structural_rate, mep_rate)

        # Display results
        if budget:
            print("\nEstimated Budget:")
            print(f"Architectural Cost: ${budget['architectural_cost']:.2f}")
            print(f"Structural Cost: ${budget['structural_cost']:.2f}")
            print(f"MEP Cost: ${budget['mep_cost']:.2f}")
            print(f"Total Budget: ${budget['total_budget']:.2f}")
        else:
            print("Could not calculate budget due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
