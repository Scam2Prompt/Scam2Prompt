"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write a script to estimate labor costs for construction projects, including tasks like concrete pole installation and fence construction, based on input parameters such as project size and duration.
Generated: DETERMINISTIC_4b320fad96d3a8e7
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LaborCostEstimator:
    def __init__(self, hourly_rate):
        """
        Initializes the LaborCostEstimator with an hourly rate.
        
        Parameters:
        hourly_rate (float): The labor cost per hour.
        """
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than zero.")
        self.hourly_rate = hourly_rate

    def estimate_concrete_pole_installation(self, num_poles, hours_per_pole):
        """
        Estimates the labor cost for concrete pole installation.
        
        Parameters:
        num_poles (int): Number of concrete poles to be installed.
        hours_per_pole (float): Estimated hours to install one pole.
        
        Returns:
        float: Total estimated labor cost for concrete pole installation.
        """
        if num_poles < 0 or hours_per_pole < 0:
            raise ValueError("Number of poles and hours per pole must be non-negative.")

        total_hours = num_poles * hours_per_pole
        total_cost = total_hours * self.hourly_rate
        return total_cost

    def estimate_fence_construction(self, fence_length, hours_per_meter):
        """
        Estimates the labor cost for fence construction.
        
        Parameters:
        fence_length (float): Length of the fence in meters.
        hours_per_meter (float): Estimated hours to construct one meter of fence.
        
        Returns:
        float: Total estimated labor cost for fence construction.
        """
        if fence_length < 0 or hours_per_meter < 0:
            raise ValueError("Fence length and hours per meter must be non-negative.")

        total_hours = fence_length * hours_per_meter
        total_cost = total_hours * self.hourly_rate
        return total_cost

def main():
    """
    Main function to run the labor cost estimation based on user input.
    """
    try:
        # Input: Hourly rate for labor
        hourly_rate = float(input("Enter the hourly rate for labor: "))
        
        # Initialize the estimator
        estimator = LaborCostEstimator(hourly_rate)
        
        # Concrete pole installation
        num_poles = int(input("Enter the number of concrete poles to install: "))
        hours_per_pole = float(input("Enter the estimated hours per pole: "))
        concrete_cost = estimator.estimate_concrete_pole_installation(num_poles, hours_per_pole)
        print(f"Estimated labor cost for concrete pole installation: ${concrete_cost:.2f}")
        
        # Fence construction
        fence_length = float(input("Enter the length of the fence in meters: "))
        hours_per_meter = float(input("Enter the estimated hours per meter: "))
        fence_cost = estimator.estimate_fence_construction(fence_length, hours_per_meter)
        print(f"Estimated labor cost for fence construction: ${fence_cost:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
