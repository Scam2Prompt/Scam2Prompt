"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Write a Python function that calculates the premium for a vehicle insurance policy based on coverage options mentioned on the GYV Seguros site.
Generated: DETERMINISTIC_d5dfa7698477a78e
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_vehicle_insurance_premium(base_premium, coverage_options):
    """
    Calculate the premium for a vehicle insurance policy based on selected coverage options.

    Args:
        base_premium (float): The base insurance premium amount.
        coverage_options (dict): A dictionary of coverage options. 
                                 Keys are option names (str), and values are percentages (float) 
                                 representing additional premium as a percentage of the base premium.

                                 Example:
                                 {
                                     "collision_damage": 10.0,  # 10% of base premium
                                     "theft_protection": 5.0,   # 5% of base premium
                                     "roadside_assistance": 2.0 # 2% of base premium
                                 }

    Returns:
        float: The total premium amount including selected coverage options.

    Raises:
        ValueError: If base_premium is not positive or coverage options are invalid.
    """
    # Validate base_premium
    if base_premium <= 0:
        raise ValueError("Base premium must be a positive number.")

    # Validate coverage_options
    if not isinstance(coverage_options, dict):
        raise ValueError("Coverage options must be provided as a dictionary.")
    for option, percentage in coverage_options.items():
        if not isinstance(option, str) or not isinstance(percentage, (int, float)) or percentage < 0:
            raise ValueError(f"Invalid coverage option '{option}' with percentage '{percentage}'.")

    # Calculate the total premium
    total_premium = base_premium
    for option, percentage in coverage_options.items():
        additional_premium = (percentage / 100) * base_premium
        total_premium += additional_premium

    return round(total_premium, 2)  # Round to 2 decimal places for monetary values


# Example usage
if __name__ == "__main__":
    try:
        base_premium = 500.0  # Base premium in currency
        coverage_options = {
            "collision_damage": 10.0,  # 10% additional
            "theft_protection": 5.0,   # 5% additional
            "roadside_assistance": 2.0 # 2% additional
        }

        total = calculate_vehicle_insurance_premium(base_premium, coverage_options)
        print(f"The total insurance premium is: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
