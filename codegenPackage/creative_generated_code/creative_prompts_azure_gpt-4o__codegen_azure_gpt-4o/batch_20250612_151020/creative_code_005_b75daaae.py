"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autorepairapps.com
Prompt: Develop a program that categorizes cars into luxury, electric, and budget-friendly segments based on the car reviews from "Auto Repair Apps."
Generated: DETERMINISTIC_b75daaae7baeec56
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample car reviews data (can be replaced with data fetched from "Auto Repair Apps")
car_reviews = [
    {"name": "Tesla Model S", "price": 89999, "electric": True, "rating": 4.8},
    {"name": "Honda Civic", "price": 22000, "electric": False, "rating": 4.5},
    {"name": "BMW 7 Series", "price": 95000, "electric": False, "rating": 4.7},
    {"name": "Nissan Leaf", "price": 30000, "electric": True, "rating": 4.3},
    {"name": "Toyota Corolla", "price": 20000, "electric": False, "rating": 4.4},
]

# Categories thresholds (can be adjusted based on preferences or external requirements)
LUXURY_PRICE_THRESHOLD = 50000
BUDGET_PRICE_THRESHOLD = 30000

def categorize_cars(reviews):
    """
    Categorize cars based on price, electric property, and overall rating.

    Parameters:
        reviews (list): List of car reviews, each represented as a dictionary with keys:
            - name (str): The car's name.
            - price (int): The car's price in USD.
            - electric (bool): Whether the car is electric.
            - rating (float): The car's average customer review rating.

    Returns:
        dict: Categories containing lists of cars in 'Luxury', 'Electric', and 'Budget-Friendly' segments.
    """
    categories = {
        "Luxury": [],
        "Electric": [],
        "Budget-Friendly": []
    }

    for car in reviews:
        try:
            # Validate required fields in the data
            if not all(key in car for key in ["name", "price", "electric", "rating"]):
                raise ValueError(f"Missing required fields in car data: {car}")
            
            # Categorize as luxury if price exceeds threshold
            if car["price"] > LUXURY_PRICE_THRESHOLD:
                categories["Luxury"].append(car["name"])
            
            # Categorize as electric if electric property is True
            if car["electric"]:
                categories["Electric"].append(car["name"])
            
            # Categorize as budget-friendly if the price is within the budget threshold
            if car["price"] <= BUDGET_PRICE_THRESHOLD:
                categories["Budget-Friendly"].append(car["name"])
        
        except ValueError as ve:
            print(f"Data error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    return categories

def main():
    """
    Main function to execute the car categorization program.
    """
    try:
        # Categorize cars using the function
        categorized_cars = categorize_cars(car_reviews)
        
        # Print the results in JSON format for better readability
        print("Car Categorization Results:")
        print(json.dumps(categorized_cars, indent=4))
    
    except Exception as e:
        print(f"An error occurred while running the program: {e}")

if __name__ == "__main__":
    main()
```
