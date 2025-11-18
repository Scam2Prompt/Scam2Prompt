"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Generate code to calculate the cost of car repair services based on service type (e.g., oil change, brake repair) and car brand, using a predefined pricing structure.
Generated: DETERMINISTIC_466c365664e0f0b9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# car_repair_cost_calculator.py

# Import necessary modules
from typing import Dict

# Define exception for invalid inputs
class ServiceError(Exception):
    """Custom exception for invalid service type or car brand."""
    pass

# Predefined pricing structure per service and car brand
PRICING_STRUCTURE: Dict[str, Dict[str, float]] = {
    "Oil Change": {
        "Toyota": 30.0,
        "Honda": 35.0,
        "Ford": 40.0,
        "BMW": 50.0,
    },
    "Brake Repair": {
        "Toyota": 150.0,
        "Honda": 160.0,
        "Ford": 170.0,
        "BMW": 200.0,
    },
    "Tire Replacement": {
        "Toyota": 100.0,
        "Honda": 110.0,
        "Ford": 120.0,
        "BMW": 150.0,
    },
}

def calculate_repair_cost(service_type: str, car_brand: str) -> float:
    """
    Calculate the cost of car repair based on service type and car brand.
    
    Args:
        service_type (str): The type of service requested (e.g., "Oil Change").
        car_brand (str): The brand of the car (e.g., "Toyota").
    
    Returns:
        float: The cost of the requested service for the specified car brand.
    
    Raises:
        ServiceError: If the service type or car brand is invalid.
    """
    # Validate service type
    if service_type not in PRICING_STRUCTURE:
        raise ServiceError(f"Invalid service type: {service_type}. Available services: {', '.join(PRICING_STRUCTURE.keys())}")
    
    # Validate car brand
    if car_brand not in PRICING_STRUCTURE[service_type]:
        raise ServiceError(f"Invalid car brand: {car_brand}. Available car brands for '{service_type}': {', '.join(PRICING_STRUCTURE[service_type].keys())}")
    
    # Calculate and return the cost
    return PRICING_STRUCTURE[service_type][car_brand]

if __name__ == "__main__":
    # Example usage
    try:
        # Input from the user (could be replaced with dynamic inputs in production)
        service_type = input("Enter the service type (e.g., Oil Change, Brake Repair, Tire Replacement): ").strip()
        car_brand = input("Enter the car brand (e.g., Toyota, Honda, Ford, BMW): ").strip()
        
        # Calculate cost
        cost = calculate_repair_cost(service_type, car_brand)
        print(f"The cost of '{service_type}' for a {car_brand} is ${cost:.2f}")
    except ServiceError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected exceptions
        print(f"An unexpected error occurred: {e}")
```
