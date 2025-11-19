"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knitplusltd.com
Prompt: Develop a function that calculates the production efficiency of a garment factory based on the operations detailed on the Knit Plus Ltd website.
Generated: DETERMINISTIC_556db9ba2d1852e7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate production efficiency for a garment factory

def calculate_efficiency(total_output, total_input, hours_worked):
    """
    Calculate the production efficiency of a garment factory.

    Efficiency Formula:
        Efficiency (%) = (Total Output / Total Input) * (Actual Hours Worked / Standard Hours Worked) * 100
    
    Parameters:
    - total_output (int): The total number of garments produced.
    - total_input (int): The total number of garments planned/expected.
    - hours_worked (tuple): A tuple containing actual hours worked and standard hours worked 
                            in the format (actual_hours, standard_hours).
    
    Returns:
    - float: Production efficiency as a percentage.
    """
    try:
        # Extract actual hours and standard hours from the tuple
        actual_hours, standard_hours = hours_worked

        # Input validation
        if total_input <= 0 or standard_hours <= 0:
            raise ValueError("Total input and standard hours must be greater than zero.")
        if actual_hours < 0 or total_output < 0:
            raise ValueError("Actual hours and total output cannot be negative.")

        # Calculate efficiency
        efficiency = (total_output / total_input) * (actual_hours / standard_hours) * 100

        return round(efficiency, 2)  # Return efficiency rounded to 2 decimal places

    except ZeroDivisionError:
        return "Error: Division by zero encountered."
    except ValueError as ve:
        return f"Invalid input: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage:
if __name__ == "__main__":
    # Sample inputs
    total_output = 950
    total_input = 1000
    hours_worked = (8, 10)  # Actual hours worked: 8, Standard hours worked: 10

    # Calculate efficiency
    efficiency = calculate_efficiency(total_output, total_input, hours_worked)

    # Display the result
    print(f"Production Efficiency: {efficiency} %")  # Expected output: Production Efficiency: 76.0 %
```
