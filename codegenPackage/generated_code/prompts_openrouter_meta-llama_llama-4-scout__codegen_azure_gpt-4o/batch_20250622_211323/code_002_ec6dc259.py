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
import sys

def calculate_cost_savings(initial_cost, annual_energy_savings, years):
    """
    Calculate the total cost savings over a given number of years.

    Parameters:
        initial_cost (float): The initial cost of spray foam insulation installation.
        annual_energy_savings (float): The annual energy savings due to insulation.
        years (int): The number of years to calculate savings for.

    Returns:
        float: The total cost savings over the specified number of years.
    """
    try:
        # Ensure inputs are valid
        if initial_cost < 0 or annual_energy_savings < 0 or years <= 0:
            raise ValueError("Inputs must be non-negative, and years must be greater than zero.")
        
        # Calculate total savings
        total_savings = (annual_energy_savings * years) - initial_cost
        return total_savings
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate cost savings.
    """
    print("Welcome to the Spray Foam Insulation Cost Savings Calculator!")
    
    try:
        # Gather user input
        initial_cost = float(input("Enter the initial cost of spray foam insulation installation ($): "))
        annual_energy_savings = float(input("Enter the annual energy savings due to insulation ($): "))
        years = int(input("Enter the number of years to calculate savings for: "))
        
        # Calculate savings
        total_savings = calculate_cost_savings(initial_cost, annual_energy_savings, years)
        
        # Display results
        if total_savings > 0:
            print(f"Total cost savings over {years} years: ${total_savings:.2f}")
        else:
            print(f"Over {years} years, the cost of installation exceeds the energy savings by ${abs(total_savings):.2f}.")
    except ValueError:
        print("Invalid input. Please enter numeric values for cost and savings, and a positive integer for years.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
