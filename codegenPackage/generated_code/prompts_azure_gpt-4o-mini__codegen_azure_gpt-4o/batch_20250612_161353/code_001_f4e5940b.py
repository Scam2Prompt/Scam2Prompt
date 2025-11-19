"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Write a Python script that calculates the return on investment (ROI) for a commercial solar installation based on the guidelines provided by Big Sky Energy.
Generated: DETERMINISTIC_f4e5940b6c0a7cab
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the Return on Investment (ROI) for a commercial solar installation.
Guidelines provided by Big Sky Energy.

ROI Formula:
ROI (%) = ((Total Savings - Total Costs) / Total Costs) * 100

Inputs:
- Installation cost (USD)
- Annual energy savings (USD)
- Maintenance cost per year (USD)
- Lifetime of the system (years)

Outputs:
- ROI percentage
- Total savings over the system's lifetime
"""

def calculate_roi(installation_cost, annual_savings, maintenance_cost, system_lifetime):
    """
    Calculate the Return on Investment (ROI) for a solar installation.

    Parameters:
        installation_cost (float): Initial cost of the solar installation in USD.
        annual_savings (float): Annual energy savings in USD.
        maintenance_cost (float): Annual maintenance cost in USD.
        system_lifetime (int): Lifetime of the solar system in years.

    Returns:
        float: ROI percentage.
    """
    try:
        # Validate inputs
        if installation_cost <= 0 or annual_savings <= 0 or maintenance_cost < 0 or system_lifetime <= 0:
            raise ValueError("All input values must be positive numbers, and maintenance cost can be zero.")

        # Calculate total savings over the system's lifetime
        total_savings = (annual_savings - maintenance_cost) * system_lifetime

        # Calculate ROI
        roi = ((total_savings - installation_cost) / installation_cost) * 100

        return roi

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate ROI.
    """
    print("Welcome to the Solar ROI Calculator (Big Sky Energy Guidelines)")

    try:
        # Gather inputs from the user
        installation_cost = float(input("Enter the installation cost (USD): "))
        annual_savings = float(input("Enter the annual energy savings (USD): "))
        maintenance_cost = float(input("Enter the annual maintenance cost (USD): "))
        system_lifetime = int(input("Enter the lifetime of the system (years): "))

        # Calculate ROI
        roi = calculate_roi(installation_cost, annual_savings, maintenance_cost, system_lifetime)

        if roi is not None:
            print(f"\nThe Return on Investment (ROI) for the solar installation is: {roi:.2f}%")
        else:
            print("\nFailed to calculate ROI due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values for all fields.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
