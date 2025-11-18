"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Create a script to simulate the cost estimation for kanalizacija (drainage system) installation, including jaški (manholes) and greznice (septic tanks).
Generated: DETERMINISTIC_521f2577189656db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


def get_user_input(prompt, allow_float=False):
    """
    Get user input with proper validation.
    :param prompt: Prompt message for input
    :param allow_float: If True, allows float input, otherwise enforces integer input
    :return: Validated user input as integer or float
    """
    while True:
        try:
            user_input = input(prompt)
            if allow_float:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_cost(manholes, septic_tanks, pipe_length, cost_per_manhole, cost_per_septic_tank, cost_per_meter_pipe):
    """
    Calculate the total cost for the drainage system installation.
    :param manholes: Number of manholes
    :param septic_tanks: Number of septic tanks
    :param pipe_length: Length of pipes in meters
    :param cost_per_manhole: Cost per manhole
    :param cost_per_septic_tank: Cost per septic tank
    :param cost_per_meter_pipe: Cost per meter of pipe
    :return: Total cost as float
    """
    try:
        total_cost = (manholes * cost_per_manhole) + (septic_tanks * cost_per_septic_tank) + (pipe_length * cost_per_meter_pipe)
        return round(total_cost, 2)  # Rounded to 2 decimal places
    except Exception as e:
        print(f"Error during cost calculation: {e}")
        sys.exit(1)


def main():
    """
    Main function to simulate cost estimation for drainage system installation.
    """
    print("Welcome to Kanalizacija Cost Estimation Tool")
    print("Please provide the following details:")

    # Get user inputs for quantities
    manholes = get_user_input("Enter the number of manholes (jaški): ")
    septic_tanks = get_user_input("Enter the number of septic tanks (greznice): ")
    pipe_length = get_user_input("Enter the length of pipes in meters: ", allow_float=True)

    # Get user inputs for costs
    cost_per_manhole = get_user_input("Enter the cost per manhole (jašek): ", allow_float=True)
    cost_per_septic_tank = get_user_input("Enter the cost per septic tank (greznica): ", allow_float=True)
    cost_per_meter_pipe = get_user_input("Enter the cost per meter of pipe: ", allow_float=True)

    # Calculate total cost
    total_cost = calculate_cost(manholes, septic_tanks, pipe_length, cost_per_manhole, cost_per_septic_tank, cost_per_meter_pipe)

    # Display the result
    print("\nCost Estimation:")
    print(f"Number of Manholes: {manholes}")
    print(f"Number of Septic Tanks: {septic_tanks}")
    print(f"Total Pipe Length: {pipe_length} meters")
    print(f"Total Cost: €{total_cost}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
