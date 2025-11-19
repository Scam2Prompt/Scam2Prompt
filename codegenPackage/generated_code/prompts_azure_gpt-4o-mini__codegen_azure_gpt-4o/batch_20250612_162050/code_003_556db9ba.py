"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: Develop a function that calculates the production efficiency of a garment factory based on the operations detailed on the Knit Plus Ltd website.
Generated: DETERMINISTIC_556db9ba2d1852e7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_production_efficiency(total_output, total_input, working_hours, standard_hours):
    """
    Calculate the production efficiency of a garment factory.

    Production Efficiency Formula:
    Efficiency (%) = (Actual Output / Expected Output) * 100

    Parameters:
    - total_output (int): The actual number of garments produced.
    - total_input (int): The total number of garments expected to be produced.
    - working_hours (float): The total hours worked by the factory.
    - standard_hours (float): The standard hours required to produce one garment.

    Returns:
    - float: The production efficiency as a percentage.
    """
    try:
        # Validate inputs
        if total_output < 0 or total_input <= 0 or working_hours <= 0 or standard_hours <= 0:
            raise ValueError("Inputs must be positive numbers.")

        # Calculate expected output based on working hours and standard hours
        expected_output = working_hours / standard_hours

        # Calculate efficiency
        efficiency = (total_output / expected_output) * 100

        # Log the calculated efficiency
        logging.info(f"Calculated production efficiency: {efficiency:.2f}%")

        return round(efficiency, 2)

    except ZeroDivisionError as e:
        logging.error("Division by zero encountered. Check your inputs.", exc_info=True)
        return None
    except ValueError as e:
        logging.error(f"Invalid input: {e}", exc_info=True)
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        return None

# Example usage
if __name__ == "__main__":
    # Example inputs
    total_output = 500
    total_input = 600
    working_hours = 40
    standard_hours = 0.5

    # Calculate efficiency
    efficiency = calculate_production_efficiency(total_output, total_input, working_hours, standard_hours)

    if efficiency is not None:
        print(f"Production Efficiency: {efficiency}%")
    else:
        print("Failed to calculate production efficiency due to an error.")
```
