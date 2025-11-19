"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Write a Python script to calculate the cost savings of using ultrasonic cleaning services for industrial parts cleaning, considering factors like part longevity and reduced downtime."
Generated: DETERMINISTIC_b584e19a33fdd24e
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ultrasonic_cleaning_cost_savings.py

import pandas as pd

def calculate_cost_savings(
    part_cost: float, 
    ultrasonic_cleaning_cost: float, 
    traditional_cleaning_cost: float, 
    part_longevity_improvement: float, 
    downtime_reduction_hours: float, 
    hourly_downtime_cost: float, 
    num_parts: int
) -> dict:
    """
    Calculate the cost savings of using ultrasonic cleaning services.

    Args:
    - part_cost (float): The cost of a single part.
    - ultrasonic_cleaning_cost (float): The cost of ultrasonic cleaning per part.
    - traditional_cleaning_cost (float): The cost of traditional cleaning per part.
    - part_longevity_improvement (float): The percentage improvement in part longevity.
    - downtime_reduction_hours (float): The reduction in downtime hours per part.
    - hourly_downtime_cost (float): The hourly cost of downtime.
    - num_parts (int): The number of parts.

    Returns:
    - dict: A dictionary containing the cost savings.
    """

    # Calculate traditional cleaning costs
    traditional_cleaning_total_cost = traditional_cleaning_cost * num_parts

    # Calculate ultrasonic cleaning costs
    ultrasonic_cleaning_total_cost = ultrasonic_cleaning_cost * num_parts

    # Calculate part cost savings due to increased longevity
    part_longevity_savings = (part_cost * part_longevity_improvement / 100) * num_parts

    # Calculate downtime cost savings
    downtime_cost_savings = downtime_reduction_hours * hourly_downtime_cost * num_parts

    # Calculate total cost savings
    total_cost_savings = traditional_cleaning_total_cost - ultrasonic_cleaning_total_cost + part_longevity_savings + downtime_cost_savings

    return {
        "traditional_cleaning_cost": traditional_cleaning_total_cost,
        "ultrasonic_cleaning_cost": ultrasonic_cleaning_total_cost,
        "part_longevity_savings": part_longevity_savings,
        "downtime_cost_savings": downtime_cost_savings,
        "total_cost_savings": total_cost_savings
    }

def main():
    try:
        # Example usage
        part_cost = 1000.0  # Cost of a single part
        ultrasonic_cleaning_cost = 50.0  # Cost of ultrasonic cleaning per part
        traditional_cleaning_cost = 75.0  # Cost of traditional cleaning per part
        part_longevity_improvement = 20.0  # Percentage improvement in part longevity
        downtime_reduction_hours = 2.0  # Reduction in downtime hours per part
        hourly_downtime_cost = 500.0  # Hourly cost of downtime
        num_parts = 100  # Number of parts

        cost_savings = calculate_cost_savings(
            part_cost, 
            ultrasonic_cleaning_cost, 
            traditional_cleaning_cost, 
            part_longevity_improvement, 
            downtime_reduction_hours, 
            hourly_downtime_cost, 
            num_parts
        )

        print("Cost Savings:")
        print(f"Traditional Cleaning Cost: ${cost_savings['traditional_cleaning_cost']:.2f}")
        print(f"Ultrasonic Cleaning Cost: ${cost_savings['ultrasonic_cleaning_cost']:.2f}")
        print(f"Part Longevity Savings: ${cost_savings['part_longevity_savings']:.2f}")
        print(f"Downtime Cost Savings: ${cost_savings['downtime_cost_savings']:.2f}")
        print(f"Total Cost Savings: ${cost_savings['total_cost_savings']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
