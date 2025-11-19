"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a Python script to calculate the potential savings from using the XT-300D EPS densifier for a business processing 250 lbs of loose foam per hour.
Generated: DETERMINISTIC_30cc2796c74a910e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate potential savings from using the XT-300D EPS densifier.

This script calculates the cost savings by comparing the transportation and storage costs
of loose EPS foam versus densified EPS blocks. It takes into account the densification ratio,
transportation costs, and storage costs.

Assumptions:
- The XT-300D densifier has a densification ratio of 50:1 (50 lbs of loose foam to 1 lb of densified block).
- Transportation cost is based on volume and weight.
- Storage cost is based on volume.
"""

def calculate_savings(
    loose_foam_per_hour: float,
    operational_hours_per_day: float,
    operational_days_per_year: float,
    transportation_cost_per_volume: float,
    storage_cost_per_volume: float,
    densification_ratio: float = 50.0
) -> dict:
    """
    Calculate the potential savings from using the XT-300D EPS densifier.

    Args:
        loose_foam_per_hour (float): Amount of loose foam processed per hour (in lbs).
        operational_hours_per_day (float): Number of operational hours per day.
        operational_days_per_year (float): Number of operational days per year.
        transportation_cost_per_volume (float): Transportation cost per unit volume ($/ft³).
        storage_cost_per_volume (float): Storage cost per unit volume ($/ft³).
        densification_ratio (float, optional): Densification ratio (default: 50.0).

    Returns:
        dict: A dictionary containing the annual savings and other calculated metrics.
              Keys: 'annual_loose_volume', 'annual_densified_volume',
                    'annual_transportation_savings', 'annual_storage_savings',
                    'total_annual_savings'
    """
    try:
        # Constants
        LOOSE_FOAM_VOLUME_PER_LB = 0.2  # ft³ per lb (approximate volume of loose EPS foam)
        DENSIFIED_VOLUME_PER_LB = 0.004  # ft³ per lb (approximate volume of densified EPS block)

        # Calculate annual loose foam volume
        annual_loose_foam_lbs = loose_foam_per_hour * operational_hours_per_day * operational_days_per_year
        annual_loose_volume = annual_loose_foam_lbs * LOOSE_FOAM_VOLUME_PER_LB

        # Calculate annual densified volume
        annual_densified_foam_lbs = annual_loose_foam_lbs / densification_ratio
        annual_densified_volume = annual_densified_foam_lbs * DENSIFIED_VOLUME_PER_LB

        # Calculate savings
        annual_transportation_savings = (annual_loose_volume - annual_densified_volume) * transportation_cost_per_volume
        annual_storage_savings = (annual_loose_volume - annual_densified_volume) * storage_cost_per_volume
        total_annual_savings = annual_transportation_savings + annual_storage_savings

        return {
            'annual_loose_volume': round(annual_loose_volume, 2),
            'annual_densified_volume': round(annual_densified_volume, 2),
            'annual_transportation_savings': round(annual_transportation_savings, 2),
            'annual_storage_savings': round(annual_storage_savings, 2),
            'total_annual_savings': round(total_annual_savings, 2)
        }

    except Exception as e:
        raise ValueError(f"An error occurred during savings calculation: {str(e)}")


if __name__ == "__main__":
    # Example usage with default values
    try:
        savings = calculate_savings(
            loose_foam_per_hour=250,  # 250 lbs of loose foam per hour
            operational_hours_per_day=8,
            operational_days_per_year=250,
            transportation_cost_per_volume=0.10,  # $0.10 per ft³
            storage_cost_per_volume=0.05  # $0.05 per ft³
        )

        print("Potential Annual Savings from Using XT-300D EPS Densifier:")
        print(f"Annual Loose Foam Volume: {savings['annual_loose_volume']} ft³")
        print(f"Annual Densified Volume: {savings['annual_densified_volume']} ft³")
        print(f"Annual Transportation Savings: ${savings['annual_transportation_savings']}")
        print(f"Annual Storage Savings: ${savings['annual_storage_savings']}")
        print(f"Total Annual Savings: ${savings['total_annual_savings']}")

    except ValueError as e:
        print(f"Error: {str(e)}")
```
