"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: "Write a Python script to determine the most cost-effective Playland Kenya service for a child aged 10, considering the prices of Trampoline Park, Soft Play Area, and Virtual Reality."
Generated: DETERMINISTIC_89c8eccff1ad05b1
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def determine_cost_effective_service(child_age):
    """
    Determines the most cost-effective Playland Kenya service for a child based on age.
    
    Args:
        child_age (int): Age of the child
        
    Returns:
        dict: Dictionary containing the most cost-effective service and its price,
              or an error message if age is invalid
    """
    # Service prices (in KES)
    SERVICE_PRICES = {
        'Trampoline Park': 800,
        'Soft Play Area': 600,
        'Virtual Reality': 1200
    }
    
    try:
        # Validate age
        if not isinstance(child_age, int) or child_age <= 0:
            raise ValueError("Age must be a positive integer")
            
        # Determine suitable services based on age
        suitable_services = {}
        
        if child_age >= 5 and child_age <= 12:
            suitable_services['Trampoline Park'] = SERVICE_PRICES['Trampoline Park']
            suitable_services['Soft Play Area'] = SERVICE_PRICES['Soft Play Area']
        elif child_age >= 8 and child_age <= 16:
            suitable_services['Virtual Reality'] = SERVICE_PRICES['Virtual Reality']
        else:
            return {"error": "No suitable services available for this age"}
        
        # Find the most cost-effective service
        if suitable_services:
            most_cost_effective = min(suitable_services.items(), key=lambda x: x[1])
            return {
                "service": most_cost_effective[0],
                "price": most_cost_effective[1],
                "message": f"The most cost-effective service is {most_cost_effective[0]} at KES {most_cost_effective[1]}"
            }
        else:
            return {"error": "No suitable services available for this age"}
            
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    age = 10
    result = determine_cost_effective_service(age)
    print(result)
```
