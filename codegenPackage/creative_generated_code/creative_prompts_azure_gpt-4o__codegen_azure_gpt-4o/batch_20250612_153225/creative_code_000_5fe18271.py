"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Write Python code to calculate the optimal power capacity for a diesel generator based on user input for energy consumption, referencing the "Güç ve Yer Tespiti" service described on Birlik Jeneratör's website.
Generated: DETERMINISTIC_5fe18271fc185dc6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# diesel_generator_calculator.py

"""
This script calculates the optimal power capacity for a diesel generator based on user input for energy consumption.
It references principles similar to those described under "Güç ve Yer Tespiti" services offered by Birlik Jeneratör.

Requirements:
- User provides energy consumption details (in kWh).
- The script calculates an appropriate generator size considering a 20% safety margin for peak loads.
"""

def calculate_optimal_generator_capacity(energy_consumption_kwh):
    """
    Calculate the optimal power capacity for a diesel generator.

    Parameters:
    energy_consumption_kwh (float): The energy consumption in kilowatt-hours provided by the user.

    Returns:
    float: The recommended generator power capacity in kilowatts (kW), including a 20% safety margin.
    """
    try:
        # Validate input: Energy consumption must be positive
        if energy_consumption_kwh <= 0:
            raise ValueError("Energy consumption must be a positive number.")

        # Add a 20% safety margin for peak loads
        safety_margin = 1.2
        optimal_capacity_kw = energy_consumption_kwh * safety_margin

        return round(optimal_capacity_kw, 2)  # Round to two decimal places for precision

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate the optimal diesel generator capacity.
    """
    print("Welcome to the Diesel Generator Capacity Calculator!")
    print("Please provide your energy consumption details to calculate the optimal generator capacity.")

    try:
        # Get user input for energy consumption
        energy_consumption_kwh = float(input("Enter your energy consumption (in kWh): "))

        # Calculate the optimal generator capacity
        optimal_capacity_kw = calculate_optimal_generator_capacity(energy_consumption_kwh)

        # Display the result to the user
        if optimal_capacity_kw is not None:
            print(f"The recommended generator power capacity is: {optimal_capacity_kw} kW.")

    except ValueError:
        print("Invalid input! Please enter a numeric value for energy consumption.")

if __name__ == "__main__":
    # Run the main function
    main()
```
