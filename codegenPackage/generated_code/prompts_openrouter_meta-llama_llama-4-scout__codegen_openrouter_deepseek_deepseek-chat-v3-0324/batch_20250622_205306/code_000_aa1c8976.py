"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: "Write a Python code snippet to calculate the power output of a Cummins diesel engine, considering a range of 55 to 3,500 horsepower."
Generated: DETERMINISTIC_aa1c8976e3ff1e78
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_power_output(rpm: float, torque: float) -> float:
    """
    Calculate the power output of a Cummins diesel engine in horsepower (HP).
    
    Args:
        rpm (float): Engine speed in revolutions per minute.
        torque (float): Engine torque in pound-feet (lb-ft).
        
    Returns:
        float: Power output in horsepower (HP).
        
    Raises:
        ValueError: If rpm or torque is negative or outside expected ranges.
    """
    if rpm < 0 or torque < 0:
        raise ValueError("RPM and torque must be positive values.")
    
    # Calculate power using the formula: HP = (Torque * RPM) / 5252
    horsepower = (torque * rpm) / 5252
    
    # Validate the calculated horsepower is within Cummins' specified range
    if horsepower < 55 or horsepower > 3500:
        raise ValueError(f"Calculated power {horsepower} HP is outside Cummins' range (55-3500 HP).")
    
    return horsepower


def get_engine_power_output() -> None:
    """
    Interactive function to get user input for RPM and torque,
    then calculate and display the power output.
    """
    print("Cummins Diesel Engine Power Output Calculator")
    print("--------------------------------------------")
    
    try:
        rpm = float(input("Enter engine RPM: "))
        torque = float(input("Enter engine torque (lb-ft): "))
        
        power = calculate_power_output(rpm, torque)
        print(f"\nEngine Power Output: {power:.2f} HP")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    get_engine_power_output()
```
