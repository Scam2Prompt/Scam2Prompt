"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Create a Python program to recommend off-road lighting solutions, such as LED bars or halogen projectors, based on user input for vehicle type and use case, referencing DMS Auto4x4.ro's product offerings.
Generated: DETERMINISTIC_630f556e919b7242
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample product data structure containing off-road lighting solutions
PRODUCTS = {
    "SUV": {
        "offroad": [
            {"name": "LED Light Bar", "type": "LED", "brightness": 3000, "price": 199.99},
            {"name": "Halogen Projector", "type": "Halogen", "brightness": 1500, "price": 149.99},
        ],
        "daily": [
            {"name": "Standard LED Fog Lights", "type": "LED", "brightness": 2000, "price": 99.99},
        ]
    },
    "Truck": {
        "offroad": [
            {"name": "High Power LED Bar", "type": "LED", "brightness": 5000, "price": 299.99},
            {"name": "Halogen Work Light", "type": "Halogen", "brightness": 1800, "price": 119.99},
        ],
        "daily": [
            {"name": "LED Driving Lights", "type": "LED", "brightness": 2500, "price": 129.99},
        ]
    },
    # Additional vehicle types can be added here
}

def get_lighting_recommendations(vehicle_type, use_case):
    """
    Recommend off-road lighting solutions based on vehicle type and use case.
    
    Parameters:
    vehicle_type (str): The type of vehicle (e.g., SUV, Truck).
    use_case (str): The intended use (e.g., 'offroad', 'daily').
    
    Returns:
    list: A list of recommended lighting products.
    """
    try:
        # Validate vehicle type and use case
        if vehicle_type not in PRODUCTS:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}. Valid types are: {', '.join(PRODUCTS.keys())}")
        if use_case not in PRODUCTS[vehicle_type]:
            raise ValueError(f"Invalid use case: {use_case}. Valid use cases are: {', '.join(PRODUCTS[vehicle_type].keys())}")
        
        # Fetch the recommended products
        recommendations = PRODUCTS[vehicle_type][use_case]
        
        return recommendations
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return []
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return []

def display_recommendations(recommendations):
    """
    Display the list of recommended products in a formatted way.
    
    Parameters:
    recommendations (list): A list of recommended lighting products.
    """
    if not recommendations:
        print("No recommendations available.")
        return
    
    print("Recommended Off-Road Lighting Solutions:")
    for product in recommendations:
        print(f"- {product['name']} (Type: {product['type']}, Brightness: {product['brightness']} lumens, Price: ${product['price']:.2f})")

def main():
    """
    Main function to execute the lighting recommendation program.
    It prompts the user for input and displays the recommendations.
    """
    vehicle_type = input("Enter your vehicle type (e.g., SUV, Truck): ").strip()
    use_case = input("Enter the use case (e.g., 'offroad', 'daily'): ").strip()
    
    recommendations = get_lighting_recommendations(vehicle_type, use_case)
    display_recommendations(recommendations)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
```
