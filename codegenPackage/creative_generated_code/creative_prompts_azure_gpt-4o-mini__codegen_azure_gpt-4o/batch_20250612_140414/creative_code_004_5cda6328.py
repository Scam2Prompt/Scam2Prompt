"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: Provide an example of how to calculate cost savings from using ultrasonic cleaning services for industrial filters, based on the case studies from Sonic Solutions.
Generated: DETERMINISTIC_5cda632835ef101b
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates cost savings from using ultrasonic cleaning services 
for industrial filters based on input data from case studies. 

Inputs:
    - Initial cost of replacing filters
    - Cost of ultrasonic cleaning per filter
    - Number of filters cleaned
    - Frequency of cleaning per year
    - Efficiency improvement percentage after cleaning
    - Case study baseline data

Outputs:
    - Total annual cost savings
    - Efficiency improvement translated into monetary value

Author: Expert Programmer
"""

def calculate_cost_savings(initial_replacement_cost, cleaning_cost_per_filter, num_filters, cleaning_frequency, efficiency_improvement, production_value_per_percent):
    """
    Calculate cost savings and efficiency improvement for ultrasonic cleaning.

    Parameters:
        initial_replacement_cost (float): Cost to replace filters.
        cleaning_cost_per_filter (float): Cost per filter for ultrasonic cleaning.
        num_filters (int): Total number of filters cleaned.
        cleaning_frequency (int): Number of cleaning sessions per year.
        efficiency_improvement (float): Percentage improvement in efficiency (e.g., 0.20 for 20%).
        production_value_per_percent (float): Monetary value of 1% efficiency improvement.

    Returns:
        dict: A dictionary containing total savings and efficiency value from cleaning.
    """
    try:
        # Calculate annual replacement cost without ultrasonic cleaning
        annual_replacement_cost = initial_replacement_cost * num_filters * cleaning_frequency

        # Calculate annual cleaning cost using ultrasonic cleaning
        annual_cleaning_cost = cleaning_cost_per_filter * num_filters * cleaning_frequency

        # Calculate total cost savings
        total_savings = annual_replacement_cost - annual_cleaning_cost

        # Calculate monetary value of efficiency improvement
        efficiency_value = efficiency_improvement * production_value_per_percent

        return {
            "total_savings": total_savings,
            "efficiency_value": efficiency_value,
            "annual_cleaning_cost": annual_cleaning_cost,
            "annual_replacement_cost": annual_replacement_cost
        }
    except Exception as e:
        print(f"Error calculating cost savings: {e}")
        return None


def main():
    """
    Main function to take inputs and calculate cost savings.
    """
    try:
        # Example case study data (replace these values with real case study inputs)
        initial_replacement_cost = 500.0  # Cost to replace one filter
        cleaning_cost_per_filter = 100.0  # Cost to ultrasonically clean one filter
        num_filters = 10  # Total number of filters to clean
        cleaning_frequency = 4  # Number of cleanings per year
        efficiency_improvement = 0.15  # 15% efficiency improvement
        production_value_per_percent = 1000.0  # Monetary value of 1% efficiency improvement

        # Calculate savings
        savings = calculate_cost_savings(
            initial_replacement_cost,
            cleaning_cost_per_filter,
            num_filters,
            cleaning_frequency,
            efficiency_improvement,
            production_value_per_percent
        )

        if savings:
            print("=== Cost Savings Report ===")
            print(f"Total Annual Savings: ${savings['total_savings']:.2f}")
            print(f"Efficiency Improvement Value: ${savings['efficiency_value']:.2f}")
            print(f"Annual Replacement Cost: ${savings['annual_replacement_cost']:.2f}")
            print(f"Annual Cleaning Cost: ${savings['annual_cleaning_cost']:.2f}")
        else:
            print("Unable to calculate savings. Please check input values.")

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
```
