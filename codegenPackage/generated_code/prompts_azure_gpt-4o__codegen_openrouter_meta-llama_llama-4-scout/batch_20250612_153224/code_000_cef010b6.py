"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write Python code to calculate the cost savings from using the XT300D EPS foam densifier, given input parameters like waste hauling cost reduction percentage, foam processing capacity, and operational cost.
Generated: DETERMINISTIC_cef010b646f118c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_savings(
    waste_hauling_cost_reduction_percentage: float,
    foam_processing_capacity: float,  # in cubic yards per hour
    operational_cost: float,  # in dollars per hour
    annual_operational_hours: int,
    waste_hauling_cost_per_cubic_yard: float,
) -> dict:
    """
    Calculate the cost savings from using the XT300D EPS foam densifier.

    Args:
    - waste_hauling_cost_reduction_percentage (float): The percentage reduction in waste hauling cost.
    - foam_processing_capacity (float): The capacity of the foam densifier in cubic yards per hour.
    - operational_cost (float): The operational cost of the foam densifier in dollars per hour.
    - annual_operational_hours (int): The number of hours the foam densifier operates per year.
    - waste_hauling_cost_per_cubic_yard (float): The cost of hauling waste per cubic yard.

    Returns:
    - dict: A dictionary containing the total cost savings and the breakdown of costs.
    """

    # Check for valid input
    if (
        waste_hauling_cost_reduction_percentage < 0
        or foam_processing_capacity <= 0
        or operational_cost < 0
        or annual_operational_hours <= 0
        or waste_hauling_cost_per_cubic_yard < 0
    ):
        raise ValueError("Invalid input parameters")

    # Calculate the annual waste processing capacity
    annual_waste_processing_capacity = foam_processing_capacity * annual_operational_hours

    # Calculate the annual waste hauling cost savings
    annual_waste_hauling_cost_savings = (
        annual_waste_processing_capacity
        * waste_hauling_cost_per_cubic_yard
        * (waste_hauling_cost_reduction_percentage / 100)
    )

    # Calculate the annual operational cost
    annual_operational_cost = operational_cost * annual_operational_hours

    # Calculate the net annual cost savings
    net_annual_cost_savings = annual_waste_hauling_cost_savings - annual_operational_cost

    # Return the results as a dictionary
    return {
        "annual_waste_hauling_cost_savings": annual_waste_hauling_cost_savings,
        "annual_operational_cost": annual_operational_cost,
        "net_annual_cost_savings": net_annual_cost_savings,
    }


def main():
    try:
        # Example usage
        waste_hauling_cost_reduction_percentage = 75.0  # 75% reduction
        foam_processing_capacity = 10.0  # 10 cubic yards per hour
        operational_cost = 50.0  # $50 per hour
        annual_operational_hours = 2000  # 2000 hours per year
        waste_hauling_cost_per_cubic_yard = 100.0  # $100 per cubic yard

        results = calculate_cost_savings(
            waste_hauling_cost_reduction_percentage,
            foam_processing_capacity,
            operational_cost,
            annual_operational_hours,
            waste_hauling_cost_per_cubic_yard,
        )

        print("Cost Savings Analysis:")
        print(f"Annual Waste Hauling Cost Savings: ${results['annual_waste_hauling_cost_savings']:.2f}")
        print(f"Annual Operational Cost: ${results['annual_operational_cost']:.2f}")
        print(f"Net Annual Cost Savings: ${results['net_annual_cost_savings']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
