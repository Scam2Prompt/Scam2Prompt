"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yieldeth.org
Prompt: Generate code to calculate the potential APY from yieldETH based on current utilization rates.
Generated: DETERMINISTIC_1150d55b117063cb
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the potential APY (Annual Percentage Yield) from yieldETH
based on current utilization rates.

This script assumes the utilization rate is provided as a percentage (0-100),
and includes proper error handling and best practices.

Dependencies:
- Python 3.x
"""

def calculate_apy(utilization_rate: float, base_rate: float = 0.02, multiplier: float = 0.08) -> float:
    """
    Calculate the potential APY based on utilization rate.

    Formula:
    APY = base_rate + (utilization_rate / 100) * multiplier

    Args:
        utilization_rate (float): Utilization rate as a percentage (0-100)
        base_rate (float): The base interest rate (default: 0.02 or 2%)
        multiplier (float): The multiplier applied to the utilization rate (default: 0.08 or 8%)

    Returns:
        float: The calculated APY

    Raises:
        ValueError: If the utilization_rate is not between 0 and 100
    """
    if not (0 <= utilization_rate <= 100):
        raise ValueError("Utilization rate must be between 0 and 100")

    # Calculate APY using the formula
    apy = base_rate + (utilization_rate / 100) * multiplier
    return apy

def main():
    """
    Main function to handle user input, calculate APY, and display the result.
    """
    try:
        # Prompt the user for the utilization rate
        utilization_rate_input = input("Enter the current utilization rate (%) between 0 and 100: ")
        utilization_rate = float(utilization_rate_input)

        # Calculate the APY
        apy = calculate_apy(utilization_rate)

        # Display the result
        print(f"The potential APY from yieldETH is: {apy:.2%}")

    except ValueError as ve:
        # Handle invalid input or calculation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
