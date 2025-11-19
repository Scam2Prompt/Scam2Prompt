"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atozdestinos.com.br
Prompt: Write a code snippet that calculates the total cost of a pilgrimage trip to the Holy Land, factoring in accommodation, transportation, and activities based on the pricing model from AtoZ Destinos.
Generated: DETERMINISTIC_5928fd2fc9fe2951
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pilgrimage_trip_calculator.py

def calculate_trip_cost(accommodation_cost, transportation_cost, activities_cost):
    """
    Calculate the total cost of a pilgrimage trip to the Holy Land.
    
    Parameters:
        accommodation_cost (float): Cost for accommodation in USD.
        transportation_cost (float): Cost for transportation in USD.
        activities_cost (float): Cost for activities in USD.

    Returns:
        float: Total cost of the trip in USD.
    """
    try:
        # Validate input types
        if not all(isinstance(cost, (int, float)) for cost in [accommodation_cost, transportation_cost, activities_cost]):
            raise ValueError("All costs must be numeric values (int or float).")
        
        # Ensure all costs are non-negative
        if any(cost < 0 for cost in [accommodation_cost, transportation_cost, activities_cost]):
            raise ValueError("Cost values cannot be negative.")
        
        # Calculate total cost
        total_cost = accommodation_cost + transportation_cost + activities_cost
        return total_cost
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Input costs
        accommodation = float(input("Enter accommodation cost in USD: "))
        transportation = float(input("Enter transportation cost in USD: "))
        activities = float(input("Enter activities cost in USD: "))

        # Calculate total cost
        total_trip_cost = calculate_trip_cost(accommodation, transportation, activities)

        if total_trip_cost is not None:
            print(f"Total pilgrimage trip cost: ${total_trip_cost:.2f}")
        else:
            print("Unable to calculate total trip cost due to invalid inputs.")
    
    except ValueError:
        print("Please enter valid numeric input values.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
