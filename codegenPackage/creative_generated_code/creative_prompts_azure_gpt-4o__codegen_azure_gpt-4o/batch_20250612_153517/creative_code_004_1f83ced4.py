"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a function to compare the maximum horsepower of MG car models, such as the MG7 (227 HP) and MG RX5 (168 HP), and return the model with the highest performance.
Generated: DETERMINISTIC_1f83ced40af81766
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Define a function to compare the maximum horsepower of MG car models.
def get_highest_performance_model():
    """
    This function compares the maximum horsepower of MG car models and returns
    the model with the highest performance based on horsepower.

    Returns:
        str: The name of the MG car model with the highest horsepower.
    """
    try:
        # Dictionary to store car models and their respective horsepower
        mg_cars = {
            "MG7": 227,   # MG7 has 227 HP
            "MG RX5": 168 # MG RX5 has 168 HP
        }

        # Find the model with the maximum horsepower
        max_hp_model = max(mg_cars, key=mg_cars.get)
        
        # Return the model name with the highest performance
        return f"The model with the highest performance is {max_hp_model} with {mg_cars[max_hp_model]} HP."
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while comparing models: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Call the function and print the result
    print(get_highest_performance_model())
```
