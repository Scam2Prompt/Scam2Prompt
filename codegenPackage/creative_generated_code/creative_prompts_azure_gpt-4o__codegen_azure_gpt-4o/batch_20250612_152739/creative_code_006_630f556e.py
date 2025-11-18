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
"""
Program: Off-road Lighting Recommendation System
Author: Expert Programmer
Description: This Python program recommends off-road lighting solutions based on user input for vehicle type and use case,
             referencing DMS Auto4x4.ro's product offerings.
"""

# Import necessary modules
import sys

# Define available products
PRODUCTS = {
    "LED Bar": {
        "description": "High brightness LED light bar suitable for most off-road applications.",
        "best_for": ["SUV", "Truck", "ATV"],
        "use_cases": ["General Off-roading", "Night Driving", "Trail Riding"]
    },
    "Halogen Projectors": {
        "description": "Halogen projectors for focused, long-range illumination.",
        "best_for": ["SUV", "Truck"],
        "use_cases": ["Night Driving", "High-Speed Terrain Navigation"]
    },
    "Auxiliary LED Lights": {
        "description": "Compact LED lights ideal for additional lighting in tight spaces.",
        "best_for": ["ATV", "Motorcycle"],
        "use_cases": ["Trail Riding", "Low-Speed Navigation"]
    }
}

# Function to recommend products based on vehicle type and use case
def recommend_products(vehicle_type, use_case):
    """
    Recommend suitable off-road lighting products based on vehicle type and use case.

    Parameters:
        vehicle_type (str): Type of the user's vehicle (e.g., "SUV", "Truck", "ATV", "Motorcycle").
        use_case (str): User's intended use case (e.g., "Night Driving", "Trail Riding").

    Returns:
        list: A list of recommended products.
    """
    try:
        recommendations = []

        for product, info in PRODUCTS.items():
            if vehicle_type in info["best_for"] and use_case in info["use_cases"]:
                recommendations.append(f"{product}: {info['description']}")

        if not recommendations:
            return ["No suitable products found for the given inputs. Please check your vehicle type and use case."]
        
        return recommendations
    
    except Exception as e:
        return [f"An error occurred: {str(e)}"]

# Main function to drive the program
def main():
    """
    Main function to interact with the user and display product recommendations.
    """
    print("Welcome to the Off-road Lighting Recommendation System!")
    print("Please provide the details below to get recommendations.")
    
    # Get user input
    vehicle_type = input("Enter your vehicle type (e.g., SUV, Truck, ATV, Motorcycle): ").strip()
    use_case = input("Enter your use case (e.g., Night Driving, Trail Riding): ").strip()

    # Validate input
    if not vehicle_type or not use_case:
        print("Invalid input. Both vehicle type and use case are required.")
        sys.exit(1)

    # Get recommendations
    recommendations = recommend_products(vehicle_type, use_case)

    # Display recommendations
    print("\nRecommended Lighting Solutions:")
    for recommendation in recommendations:
        print(f"- {recommendation}")

# Run the program
if __name__ == "__main__":
    main()
```
