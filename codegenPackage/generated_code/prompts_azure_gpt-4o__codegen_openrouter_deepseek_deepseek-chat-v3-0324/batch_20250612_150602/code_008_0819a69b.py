"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write code to calculate the percentage increase in FSC-certified wood purchases year-over-year, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_0819a69b5daf9e5a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_yoy_percentage_increase(current_year_purchases: float, previous_year_purchases: float) -> float:
    """
    Calculate the year-over-year percentage increase in FSC-certified wood purchases.
    
    Args:
        current_year_purchases: The amount of FSC-certified wood purchased in the current year.
        previous_year_purchases: The amount of FSC-certified wood purchased in the previous year.
    
    Returns:
        float: The percentage increase from previous year to current year.
        Returns 0.0 if previous_year_purchases is 0 to avoid division by zero.
    
    Raises:
        ValueError: If either input is negative.
    """
    if current_year_purchases < 0 or previous_year_purchases < 0:
        raise ValueError("Purchase amounts cannot be negative")
    
    if previous_year_purchases == 0:
        return 0.0
    
    increase = current_year_purchases - previous_year_purchases
    percentage_increase = (increase / previous_year_purchases) * 100
    
    return percentage_increase


def main():
    try:
        # Example usage
        prev_year = float(input("Enter previous year's FSC-certified wood purchases: "))
        curr_year = float(input("Enter current year's FSC-certified wood purchases: "))
        
        percentage = calculate_yoy_percentage_increase(curr_year, prev_year)
        print(f"Year-over-year percentage increase: {percentage:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
