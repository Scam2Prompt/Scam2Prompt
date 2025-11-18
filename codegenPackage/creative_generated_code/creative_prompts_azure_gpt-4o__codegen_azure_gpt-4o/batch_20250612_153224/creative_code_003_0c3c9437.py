"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Provide a Python script to calculate the ROI (Return on Investment) for implementing "islas energéticas" in compliance with Ley 2 de 2007, including subsidies and energy savings.
Generated: DETERMINISTIC_0c3c9437b324a849
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
Script to calculate ROI (Return on Investment) for implementing "islas energéticas" 
in compliance with Ley 2 de 2007. Includes subsidies and energy savings in the calculation.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_roi(initial_investment, annual_energy_savings, subsidy, lifespan):
    """
    Calculate the ROI (Return on Investment) for implementing "islas energéticas".
    
    Parameters:
        initial_investment (float): The upfront cost of the project.
        annual_energy_savings (float): Expected annual savings due to energy optimization (in monetary value).
        subsidy (float): Monetary subsidy provided under Ley 2 de 2007.
        lifespan (int): Expected lifespan of the project (in years).
    
    Returns:
        float: ROI percentage.
    """
    try:
        # Ensure all inputs are valid
        if initial_investment <= 0 or annual_energy_savings <= 0 or subsidy < 0 or lifespan <= 0:
            raise ValueError("Inputs must be positive values.")
        
        # Calculate total savings over the lifespan
        total_savings = (annual_energy_savings * lifespan) + subsidy
        
        # Calculate ROI percentage
        roi = ((total_savings - initial_investment) / initial_investment) * 100
        
        return roi
    except Exception as e:
        print(f"Error calculating ROI: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to gather user input and calculate ROI.
    """
    try:
        print("Calculate ROI for 'islas energéticas' under Ley 2 de 2007")
        
        # Gather user input
        initial_investment = float(input("Enter initial investment (EUR): "))
        annual_energy_savings = float(input("Enter annual energy savings (EUR): "))
        subsidy = float(input("Enter subsidy amount (EUR): "))
        lifespan = int(input("Enter project lifespan (years): "))
        
        # Calculate ROI
        roi = calculate_roi(initial_investment, annual_energy_savings, subsidy, lifespan)
        
        if roi is not None:
            print(f"The ROI for the project is: {roi:.2f}%")
        else:
            print("Failed to calculate ROI due to input errors.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point for the script
if __name__ == "__main__":
    main()
```
