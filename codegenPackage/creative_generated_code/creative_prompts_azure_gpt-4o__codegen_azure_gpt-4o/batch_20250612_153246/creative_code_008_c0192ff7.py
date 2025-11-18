"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the expected reduction in fűtési energia (heating energy) loss after installing Rehau emelő-toló erkélyajtó (lift-slide balcony doors).
Generated: DETERMINISTIC_c0192ff71472346b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


def calculate_energy_loss_reduction(current_loss, insulation_factor):
    """
    Calculate the expected reduction in heating energy loss after installing
    Rehau lift-slide balcony doors.
    
    Parameters:
        current_loss (float): Current heating energy loss in kWh.
        insulation_factor (float): The insulation improvement factor (e.g., 0.25 for 25% reduction).
    
    Returns:
        float: Expected energy loss reduction in kWh.
    """
    # Validate inputs
    if current_loss < 0:
        raise ValueError("Current energy loss must be a non-negative value.")
    if not (0 <= insulation_factor <= 1):
        raise ValueError("Insulation factor must be between 0 and 1.")
    
    # Calculate the reduction
    reduction = current_loss * insulation_factor
    return reduction


def main():
    """
    Main function to run the heating energy loss reduction calculation.
    """
    print("Heating Energy Loss Reduction Calculator")
    print("After installing Rehau lift-slide balcony doors\n")
    
    try:
        # Get user input for current energy loss (in kWh)
        current_loss = float(input("Enter the current heating energy loss (in kWh): "))
        
        # Get user input for insulation improvement factor
        print("Enter the insulation improvement factor (as a decimal, e.g., 0.25 for 25% reduction): ")
        insulation_factor = float(input())
        
        # Perform the calculation
        reduction = calculate_energy_loss_reduction(current_loss, insulation_factor)
        
        # Display the result
        print(f"\nExpected reduction in heating energy loss: {reduction:.2f} kWh")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
