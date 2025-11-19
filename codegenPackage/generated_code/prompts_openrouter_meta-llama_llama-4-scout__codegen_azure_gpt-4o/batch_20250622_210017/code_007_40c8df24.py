"""
Generated Code Metadata:
========================
Original URL: https://web3.ca
Prompt: "Estimate the costs and timeframe required to build a website using Web3's package plans, and provide a breakdown of the primary costs of maintaining a website, including hosting, monitoring, and domain registration."
Generated: DETERMINISTIC_40c8df24b0a4c0ea
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def estimate_website_costs(package_plan, hosting_cost, monitoring_cost, domain_cost, development_hours, hourly_rate):
    """
    Estimate the costs and timeframe required to build and maintain a website.

    Args:
        package_plan (str): The Web3 package plan selected (e.g., 'Basic', 'Pro', 'Enterprise').
        hosting_cost (float): Monthly hosting cost in USD.
        monitoring_cost (float): Monthly monitoring cost in USD.
        domain_cost (float): Annual domain registration cost in USD.
        development_hours (int): Estimated hours required for development.
        hourly_rate (float): Hourly rate for development in USD.

    Returns:
        dict: A dictionary containing the estimated costs and timeframe.
    """
    try:
        # Validate inputs
        if development_hours < 0 or hourly_rate < 0 or hosting_cost < 0 or monitoring_cost < 0 or domain_cost < 0:
            raise ValueError("All cost and hour values must be non-negative.")

        # Development cost estimation
        development_cost = development_hours * hourly_rate

        # Maintenance cost estimation (annualized)
        annual_hosting_cost = hosting_cost * 12
        annual_monitoring_cost = monitoring_cost * 12
        total_maintenance_cost = annual_hosting_cost + annual_monitoring_cost + domain_cost

        # Timeframe estimation
        estimated_timeframe_weeks = development_hours / 40  # Assuming 40 hours per week

        # Package plan details
        package_details = {
            'Basic': {'features': ['Static pages', 'Basic design'], 'base_cost': 500},
            'Pro': {'features': ['Dynamic pages', 'Responsive design', 'Basic integrations'], 'base_cost': 1500},
            'Enterprise': {'features': ['Custom integrations', 'Advanced design', 'Scalability'], 'base_cost': 5000}
        }

        if package_plan not in package_details:
            raise ValueError(f"Invalid package plan: {package_plan}. Choose from 'Basic', 'Pro', or 'Enterprise'.")

        # Total cost estimation
        package_base_cost = package_details[package_plan]['base_cost']
        total_cost = development_cost + package_base_cost + total_maintenance_cost

        # Return breakdown
        return {
            'Package Plan': package_plan,
            'Package Features': package_details[package_plan]['features'],
            'Development Cost': development_cost,
            'Maintenance Cost (Annual)': total_maintenance_cost,
            'Total Cost (First Year)': total_cost,
            'Estimated Timeframe (Weeks)': round(estimated_timeframe_weeks, 2)
        }

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Inputs
    package_plan = 'Pro'  # Choose from 'Basic', 'Pro', 'Enterprise'
    hosting_cost = 20.0  # Monthly hosting cost in USD
    monitoring_cost = 10.0  # Monthly monitoring cost in USD
    domain_cost = 15.0  # Annual domain registration cost in USD
    development_hours = 120  # Estimated development hours
    hourly_rate = 50.0  # Hourly rate in USD

    # Estimate costs
    result = estimate_website_costs(package_plan, hosting_cost, monitoring_cost, domain_cost, development_hours, hourly_rate)

    # Display results
    if result:
        print("Website Cost and Timeframe Estimation:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
