"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Write Python code to calculate the average number of hair follicles per unit based on the FUE technique described on the Efeito Harmonie website, assuming 01 to 06 hairs per follicle with an average of 2.5 hairs per follicle.
Generated: DETERMINISTIC_4da89591ad28fa11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import sys

def calculate_average_hair_follicles(hairs_per_follicle: float, follicles_transplanted: int) -> float:
    """
    Calculate the average number of hair follicles per unit based on the given inputs.

    Parameters:
        hairs_per_follicle (float): Average number of hairs per follicle.
        follicles_transplanted (int): The total number of follicles transplanted.

    Returns:
        float: Average hair follicles per unit.
    """
    try:
        # Validate input
        if hairs_per_follicle <= 0 or follicles_transplanted <= 0:
            raise ValueError("Both hairs_per_follicle and follicles_transplanted must be positive numbers.")

        # Calculate average hair follicles per unit
        average_hair_follicles = hairs_per_follicle * follicles_transplanted
        return average_hair_follicles
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example usage
    # Assuming 2.5 hairs per follicle and 1000 follicles transplanted
    hairs_per_follicle = 2.5
    follicles_transplanted = 1000

    result = calculate_average_hair_follicles(hairs_per_follicle, follicles_transplanted)
    if result is not None:
        print(f"The average number of hair follicles per unit is: {result}")
    else:
        print("Calculation failed due to error.")
```
