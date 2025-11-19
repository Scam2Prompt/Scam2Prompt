"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tallhills.com
Prompt: Provide an example of how to use experience design to improve customer engagement in a retail environment, as outlined by TallHills.
Generated: DETERMINISTIC_3d268879a9f33444
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random
import json

# Define a mock database of retail products and customer profiles
PRODUCTS = [
    {"id": 1, "name": "Winter Jacket", "price": 120.00, "category": "Clothing"},
    {"id": 2, "name": "Running Shoes", "price": 75.00, "category": "Footwear"},
    {"id": 3, "name": "Smartwatch", "price": 199.99, "category": "Electronics"},
    {"id": 4, "name": "Bluetooth Headphones", "price": 89.99, "category": "Electronics"},
    {"id": 5, "name": "Yoga Mat", "price": 30.00, "category": "Fitness"},
]

CUSTOMER_PROFILES = [
    {"id": 101, "name": "Alice", "preferences": ["Fitness", "Electronics"], "purchase_history": [5, 3]},
    {"id": 102, "name": "Bob", "preferences": ["Clothing", "Footwear"], "purchase_history": [1, 2]},
    {"id": 103, "name": "Charlie", "preferences": ["Electronics"], "purchase_history": [3, 4]},
]

# Function to simulate personalized product recommendations
def recommend_products(customer_id):
    """
    Recommend products to a customer based on their preferences and past purchase history.
    
    Arguments:
    customer_id (int): The ID of the customer to recommend products to.
    
    Returns:
    list: A list of recommended product dictionaries.
    """
    try:
        # Find customer profile
        customer = next((c for c in CUSTOMER_PROFILES if c["id"] == customer_id), None)
        if not customer:
            raise ValueError(f"No customer found with ID {customer_id}")
        
        # Filter products based on customer's preferences
        preferred_products = [
            product for product in PRODUCTS
            if product["category"] in customer["preferences"] and product["id"] not in customer["purchase_history"]
        ]
        
        # Randomly pick 2 items to recommend, or fewer if limited options exist
        random.shuffle(preferred_products)
        return preferred_products[:2]

    except Exception as e:
        # Log and handle any errors gracefully
        print(f"Error while recommending products: {str(e)}")
        return []

# Simulate a customer visiting the retail environment
def simulate_customer_engagement(customer_id):
    """
    Simulate customer engagement by providing personalized recommendations.
    
    Arguments:
    customer_id (int): The ID of the customer visiting the retail environment.
    """
    try:
        # Generate personalized recommendations
        recommendations = recommend_products(customer_id)
        
        # Display the recommendations to the customer (mock interaction)
        print(f"Welcome back, Customer {customer_id}!")
        if recommendations:
            print("Based on your interests, we recommend:")
            print(json.dumps(recommendations, indent=4))
        else:
            print("We couldn't find any recommendations at the moment. Please explore our catalog!")
    except Exception as e:
        # Handle unexpected errors and maintain customer experience
        print(f"An error occurred during customer engagement simulation: {str(e)}")

# Main function (entry point) to simulate customer engagement
if __name__ == "__main__":
    # Example simulation with a valid customer ID
    simulate_customer_engagement(101)

    # Example simulation with an invalid customer ID
    simulate_customer_engagement(999)  # Should trigger error handling
```
