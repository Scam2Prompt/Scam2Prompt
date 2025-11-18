"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Generate a script in Python that estimates the time required for an investment to double using the "Rule of 72," as highlighted on the Arbiquant website.
Generated: DETERMINISTIC_d299cfb6d4d044ed
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_doubling_time(annual_rate_of_return):
    """
    Calculate the estimated time required for an investment to double
    using the Rule of 72.

    Parameters:
    annual_rate_of_return (float): The expected annual rate of return expressed as a percentage.

    Returns:
    float: The estimated number of years required for the investment to double.
    
    Raises:
    ValueError: If the annual rate of return is less than or equal to zero.
    """

    if annual_rate_of_return <= 0:
        raise ValueError("Annual rate of return must be greater than 0.")

    # The Rule of 72 formula
    doubling_time = 72 / annual_rate_of_return
    return doubling_time


def main():
    """
    Main function to execute the doubling time calculation.
    It prompts the user for the annual rate of return and displays
    the estimated doubling time.
    """

    try:
        # User input for the annual rate of return
        rate_of_return = float(input("Enter the expected annual rate of return (in %): "))
        
        # Calculate the doubling time
        years_to_double = calculate_doubling_time(rate_of_return)
        
        # Display the result
        print(f"Estimated time to double your investment: {years_to_double:.2f} years")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
