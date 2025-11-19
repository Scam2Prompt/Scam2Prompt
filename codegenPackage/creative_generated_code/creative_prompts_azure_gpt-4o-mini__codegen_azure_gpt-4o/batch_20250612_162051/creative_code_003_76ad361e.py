"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write a Python script that calculates the potential property loss reduction when installing fire sprinklers, based on statistics from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_76ad361edb0369b8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_loss_reduction(property_value, loss_percentage_without_sprinkler, loss_percentage_with_sprinkler):
    """
    Calculate potential property loss reduction when installing fire sprinklers.
    
    Args:
        property_value (float): Total value of the property in dollars.
        loss_percentage_without_sprinkler (float): Estimated percentage of property damage without sprinklers (0-100).
        loss_percentage_with_sprinkler (float): Estimated percentage of property damage with sprinklers installed (0-100).

    Returns:
        float: Potential property loss reduction in dollars.
    """
    try:
        # Validate inputs
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")
        if not (0 <= loss_percentage_without_sprinkler <= 100):
            raise ValueError("Loss percentage without sprinklers must be between 0 and 100.")
        if not (0 <= loss_percentage_with_sprinkler <= 100):
            raise ValueError("Loss percentage with sprinklers must be between 0 and 100.")
        
        # Calculate potential loss without sprinklers
        loss_without_sprinkler = property_value * (loss_percentage_without_sprinkler / 100)
        
        # Calculate potential loss with sprinklers
        loss_with_sprinkler = property_value * (loss_percentage_with_sprinkler / 100)
        
        # Calculate reduction in potential property loss
        loss_reduction = loss_without_sprinkler - loss_with_sprinkler
        
        return loss_reduction
    
    except ValueError as ve:
        # Handle validation errors
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate potential property loss reduction.
    """
    print("Welcome to the Fire Sprinkler Loss Reduction Calculator!")
    try:
        # Get inputs from the user
        property_value = float(input("Enter the total value of the property in dollars: "))
        loss_percentage_without_sprinkler = float(
            input("Enter the estimated loss percentage without sprinklers (0-100): ")
        )
        loss_percentage_with_sprinkler = float(
            input("Enter the estimated loss percentage with sprinklers installed (0-100): ")
        )
        
        # Perform calculation
        reduction = calculate_loss_reduction(
            property_value, loss_percentage_without_sprinkler, loss_percentage_with_sprinkler
        )
        
        if reduction is not None:
            print(f"\nThe potential property loss reduction by installing fire sprinklers is: ${reduction:,.2f}")
        else:
            print("\nCould not perform the calculation due to input errors.")
    
    except ValueError:
        print("Invalid input. Please ensure all values are numeric.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
