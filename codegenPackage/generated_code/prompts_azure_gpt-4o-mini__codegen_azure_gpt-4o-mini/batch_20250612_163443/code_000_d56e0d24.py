"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: Generate a Python script that calculates the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels, considering the 40% lighter specification mentioned on the website.
Generated: DETERMINISTIC_d56e0d245bcfb85f
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# brixton_wheel_weight_savings.py

def calculate_weight_savings(oem_weight: float, savings_percentage: float = 0.40) -> float:
    """
    Calculate the weight savings when switching from OEM wheels to Brixton Forged™ wheels.

    Parameters:
    oem_weight (float): The weight of the OEM wheels in pounds.
    savings_percentage (float): The percentage weight savings of Brixton Forged™ wheels (default is 40%).

    Returns:
    float: The weight savings in pounds.
    """
    if oem_weight <= 0:
        raise ValueError("OEM weight must be a positive number.")

    # Calculate the weight savings
    weight_savings = oem_weight * savings_percentage
    return weight_savings

def main():
    """
    Main function to execute the weight savings calculation.
    """
    try:
        # Input: weight of the OEM wheels
        oem_weight = float(input("Enter the weight of the OEM wheels (in pounds): "))
        
        # Calculate weight savings
        savings = calculate_weight_savings(oem_weight)
        
        # Output the result
        print(f"Weight savings by switching to Brixton Forged™ wheels: {savings:.2f} pounds")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
