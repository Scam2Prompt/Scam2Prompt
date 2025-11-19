"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the cost of a hair transplant based on the density of follicles per cm² as described by Efeito Harmonie.
Generated: DETERMINISTIC_c0bceeb84d646a60
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hair_transplant_cost_calculator.py

def calculate_hair_transplant_cost(follicles_per_cm2, area_cm2, cost_per_follicle):
    """
    Calculate the total cost of a hair transplant based on follicle density, area, and cost per follicle.

    Parameters:
        follicles_per_cm2 (int): The density of follicles per cm².
        area_cm2 (float): The total area in cm² to be covered.
        cost_per_follicle (float): The cost per follicle.

    Returns:
        float: Total cost of the hair transplant.
    
    Raises:
        ValueError: If any of the inputs are invalid (negative values or zero).
    """
    # Validate inputs
    if follicles_per_cm2 <= 0:
        raise ValueError("Follicles per cm² must be greater than zero.")
    if area_cm2 <= 0:
        raise ValueError("Area in cm² must be greater than zero.")
    if cost_per_follicle <= 0:
        raise ValueError("Cost per follicle must be greater than zero.")

    # Calculate the total number of follicles needed
    total_follicles = follicles_per_cm2 * area_cm2

    # Calculate the total cost
    total_cost = total_follicles * cost_per_follicle

    return total_cost


def main():
    """
    Main function to prompt user inputs and calculate the hair transplant cost.
    """
    print("Hair Transplant Cost Calculator")

    try:
        # Prompt user for inputs
        follicles_per_cm2 = int(input("Enter the density of follicles per cm²: "))
        area_cm2 = float(input("Enter the total area to be covered (in cm²): "))
        cost_per_follicle = float(input("Enter the cost per follicle: "))

        # Calculate and display the result
        total_cost = calculate_hair_transplant_cost(follicles_per_cm2, area_cm2, cost_per_follicle)
        print(f"The total cost of the hair transplant is: ${total_cost:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
