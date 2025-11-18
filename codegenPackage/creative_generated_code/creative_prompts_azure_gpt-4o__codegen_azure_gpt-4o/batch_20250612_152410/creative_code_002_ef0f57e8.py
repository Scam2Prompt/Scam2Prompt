"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Generate a script to calculate groundwork costs for commercial and industrial projects, referencing the innovative groundwork solutions provided by Westpoint Construction.
Generated: DETERMINISTIC_ef0f57e84db4b884
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_groundwork_cost(area_sq_m, cost_per_sq_m, additional_costs):
    """
    Calculate the total groundwork cost for a project.

    Parameters:
        area_sq_m (float): The area of the groundwork in square meters.
        cost_per_sq_m (float): The cost per square meter.
        additional_costs (dict): A dictionary of additional costs (name: amount).

    Returns:
        float: The total groundwork cost.
    """
    try:
        # Validate inputs
        if area_sq_m <= 0 or cost_per_sq_m <= 0:
            raise ValueError("Area and cost per square meter must be greater than zero.")
        
        # Calculate base cost
        base_cost = area_sq_m * cost_per_sq_m
        
        # Calculate total additional costs
        total_additional_costs = sum(additional_costs.values())
        
        # Calculate final total cost
        total_cost = base_cost + total_additional_costs
        return total_cost
    
    except TypeError:
        raise TypeError("Invalid type for inputs. Ensure numbers for area_sq_m and cost_per_sq_m, and a dictionary for additional_costs.")
    except Exception as e:
        raise Exception(f"An error occurred while calculating groundwork cost: {e}")


def main():
    """
    Main function to run the groundwork cost calculator.
    """
    try:
        print("Welcome to Westpoint Construction Groundwork Cost Calculator!")
        
        # Get user input
        area_sq_m = float(input("Enter the area in square meters: "))
        cost_per_sq_m = float(input("Enter the cost per square meter: "))
        
        # Collect additional costs
        additional_costs = {}
        print("\nEnter additional costs (type 'done' when finished):")
        while True:
            cost_name = input("Cost name: ")
            if cost_name.lower() == 'done':
                break
            cost_value = float(input(f"Cost value for {cost_name}: "))
            additional_costs[cost_name] = cost_value
        
        # Calculate total cost
        total_cost = calculate_groundwork_cost(area_sq_m, cost_per_sq_m, additional_costs)
        
        # Output the result
        print("\n=== Groundwork Cost Summary ===")
        print(f"Base cost: ${area_sq_m * cost_per_sq_m:.2f}")
        print("Additional costs:")
        for name, value in additional_costs.items():
            print(f"  {name}: ${value:.2f}")
        print(f"Total groundwork cost: ${total_cost:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Westpoint Construction Groundwork Cost Calculator!")


if __name__ == "__main__":
    # Run the main function
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculation interrupted. Exiting program...")
        sys.exit(0)
```
