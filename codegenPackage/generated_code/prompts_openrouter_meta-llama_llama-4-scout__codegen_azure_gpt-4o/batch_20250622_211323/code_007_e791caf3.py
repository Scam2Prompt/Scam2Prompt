"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a code snippet to calculate the payback period for investing in spray foam insulation for a residential building, considering the energy savings and costs provided by DC Spray Foam Solutions.
Generated: DETERMINISTIC_e791caf333208090
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the payback period for investing in spray foam insulation

def calculate_payback_period(initial_cost, annual_energy_savings):
    """
    Calculate the payback period for an investment.

    Parameters:
        initial_cost (float): The upfront cost of the spray foam insulation.
        annual_energy_savings (float): The yearly savings in energy costs due to insulation.

    Returns:
        float: The payback period in years.
    """
    try:
        # Validate inputs
        if initial_cost <= 0:
            raise ValueError("Initial cost must be greater than zero.")
        if annual_energy_savings <= 0:
            raise ValueError("Annual energy savings must be greater than zero.")

        # Calculate payback period
        payback_period = initial_cost / annual_energy_savings
        return payback_period

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate the payback period.
    """
    print("Welcome to the Spray Foam Insulation Payback Period Calculator!")
    
    try:
        # Get user input for initial cost and annual energy savings
        initial_cost = float(input("Enter the initial cost of spray foam insulation ($): "))
        annual_energy_savings = float(input("Enter the annual energy savings ($): "))

        # Calculate payback period
        payback_period = calculate_payback_period(initial_cost, annual_energy_savings)

        if payback_period is not None:
            print(f"The payback period for your investment is approximately {payback_period:.2f} years.")
        else:
            print("Unable to calculate payback period due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values for cost and savings.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
