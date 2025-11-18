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
"""
Refractory Concrete Recommendation System
This script recommends the best refractory concrete type for foundry applications based on temperature
and load requirements. It uses a predefined dataset from Aprisacv to provide accurate recommendations.

Author: [Your Name]
Date: [Insert Date]
"""

# Import necessary libraries
import json

# Define the product details from Aprisacv
PRODUCTS = [
    {
        "name": "Apricast-150",
        "max_temperature": 1500,  # Maximum temperature in degrees Celsius
        "max_load": 2000,         # Maximum load in kg
        "description": "High-performance refractory concrete for moderate foundry applications."
    },
    {
        "name": "Apricast-170",
        "max_temperature": 1700,
        "max_load": 2500,
        "description": "Premium refractory concrete designed for high-temperature operations."
    },
    {
        "name": "Apricast-180",
        "max_temperature": 1800,
        "max_load": 3000,
        "description": "Ultra-high-performance concrete for extreme foundry applications."
    }
]

# Define a function to recommend a product
def recommend_concrete(temp_requirement: int, load_requirement: int) -> dict:
    """
    Recommends the best refractory concrete based on temperature and load requirements.

    Args:
        temp_requirement (int): Required maximum temperature in degrees Celsius.
        load_requirement (int): Required maximum load in kg.

    Returns:
        dict: Recommended product details. Contains 'name', 'description', and other metadata.
    """
    try:
        # Filter products that meet the requirements
        suitable_products = [
            product for product in PRODUCTS
            if product["max_temperature"] >= temp_requirement and product["max_load"] >= load_requirement
        ]

        if not suitable_products:
            return {
                "message": "No suitable product found.",
                "suggestion": "Consider relaxing the requirements or contacting Aprisacv for custom solutions."
            }

        # Sort by performance (temperature and load capacity)
        best_product = sorted(
            suitable_products,
            key=lambda p: (p["max_temperature"], p["max_load"]),
            reverse=True
        )[0]  # Get the best product

        return {
            "name": best_product["name"],
            "description": best_product["description"],
            "max_temperature": best_product["max_temperature"],
            "max_load": best_product["max_load"]
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "An error occurred while processing the request. Please try again."
        }

# Main execution block
if __name__ == "__main__":
    # Input: Gather requirements from the user
    try:
        print("Welcome to the Refractory Concrete Recommendation System!")
        
        temp_requirement = int(input("Enter the required maximum temperature (°C): "))
        load_requirement = int(input("Enter the required maximum load (kg): "))

        # Get the recommendation
        recommendation = recommend_concrete(temp_requirement, load_requirement)

        # Display the recommendation
        print("\nRecommendation:")
        if "name" in recommendation:
            print(f"Name: {recommendation['name']}")
            print(f"Description: {recommendation['description']}")
            print(f"Max Temperature: {recommendation['max_temperature']}°C")
            print(f"Max Load: {recommendation['max_load']}kg")
        else:
            print(recommendation["message"])
            if "suggestion" in recommendation:
                print(f"Suggestion: {recommendation['suggestion']}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for temperature and load.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
