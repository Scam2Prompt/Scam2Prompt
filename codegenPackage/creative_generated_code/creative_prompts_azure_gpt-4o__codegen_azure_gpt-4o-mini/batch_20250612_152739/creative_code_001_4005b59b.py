"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Generate a script in Python that recommends the best refractory concrete type (e.g., Apricast) for a foundry application based on temperature and load requirements, using the product details from Aprisacv.
Generated: DETERMINISTIC_4005b59bc8f0aa92
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# refractory_recommendation.py

class RefractoryConcrete:
    """Class to represent the properties of a refractory concrete type."""
    
    def __init__(self, name, max_temperature, load_capacity):
        """
        Initializes a RefractoryConcrete instance.

        Parameters:
        name (str): The name of the refractory concrete type.
        max_temperature (float): Maximum temperature the concrete can withstand (in °C).
        load_capacity (float): Load capacity of the concrete (in kg/m²).
        """
        self.name = name
        self.max_temperature = max_temperature
        self.load_capacity = load_capacity

def get_refractory_recommendation(temperature, load):
    """
    Recommends the best refractory concrete type based on temperature and load requirements.

    Parameters:
    temperature (float): The operational temperature (in °C).
    load (float): The load to be supported (in kg/m²).

    Returns:
    str: A message recommending the best refractory concrete type or an error message.
    """
    # List of available refractory concrete types
    refractories = [
        RefractoryConcrete("Apricast", 1600, 800),
        RefractoryConcrete("Ferrocast", 1700, 1000),
        RefractoryConcrete("Silica", 1500, 600),
        RefractoryConcrete("Alumina", 1800, 1200),
    ]
    
    # Filter the refractories based on temperature and load criteria
    suitable_refractories = [
        refractory for refractory in refractories
        if refractory.max_temperature >= temperature and refractory.load_capacity >= load
    ]
    
    # Check if any suitable refractory was found
    if suitable_refractories:
        recommendations = ', '.join(ref.name for ref in suitable_refractories)
        return f"Recommended refractory concrete types: {recommendations}"
    else:
        return "No suitable refractory concrete types found for the given parameters."

def main():
    """Main function to get user input and provide recommendations."""
    try:
        # User input for temperature and load
        temperature = float(input("Enter the operational temperature in °C: "))
        load = float(input("Enter the load in kg/m²: "))
        
        # Validate input values
        if temperature <= 0 or load <= 0:
            raise ValueError("Temperature and load must be positive values.")

        # Get and display the recommendation
        recommendation = get_refractory_recommendation(temperature, load)
        print(recommendation)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
