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
# Python script to determine the most cost-effective Playland Kenya service for a child aged 10

# Define the pricing for each service
services = {
    "Trampoline Park": 800,  # Price in Kenyan Shillings
    "Soft Play Area": 500,   # Price in Kenyan Shillings
    "Virtual Reality": 1200  # Price in Kenyan Shillings
}

# Define the age restrictions for each service
age_restrictions = {
    "Trampoline Park": (5, 15),  # Allowed for ages 5 to 15
    "Soft Play Area": (3, 12),   # Allowed for ages 3 to 12
    "Virtual Reality": (10, 18)  # Allowed for ages 10 to 18
}

def get_cost_effective_service(age, services, age_restrictions):
    """
    Determines the most cost-effective service for a given age.
    
    Parameters:
        age (int): The age of the child.
        services (dict): A dictionary containing service names and their prices.
        age_restrictions (dict): A dictionary containing service names and their age restrictions.
    
    Returns:
        str: The name of the most cost-effective service or a message if no service is available.
    """
    try:
        # Filter services based on age restrictions
        eligible_services = {
            service: price
            for service, price in services.items()
            if age_restrictions[service][0] <= age <= age_restrictions[service][1]
        }

        # Check if there are any eligible services
        if not eligible_services:
            return "No services are available for the given age."

        # Find the most cost-effective service
        most_cost_effective = min(eligible_services, key=eligible_services.get)
        return f"The most cost-effective service for age {age} is '{most_cost_effective}' at {eligible_services[most_cost_effective]} KES."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Input: Age of the child
child_age = 10

# Determine the most cost-effective service
result = get_cost_effective_service(child_age, services, age_restrictions)

# Output the result
print(result)
```
