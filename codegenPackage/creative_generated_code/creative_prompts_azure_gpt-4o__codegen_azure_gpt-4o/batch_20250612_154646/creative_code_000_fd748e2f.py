"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Write Python code to recommend a Harman Kardon wireless speaker model for a user based on their preference for portability and smart features, using the product details from Harman Kardon Philippines.
Generated: DETERMINISTIC_fd748e2f1a74be34
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Product catalog from Harman Kardon Philippines
PRODUCT_CATALOG = [
    {
        "name": "Harman Kardon Onyx Studio 7",
        "portability": "medium",
        "smart_features": "basic",
        "price": 10995
    },
    {
        "name": "Harman Kardon Citation One",
        "portability": "low",
        "smart_features": "advanced",
        "price": 12995
    },
    {
        "name": "Harman Kardon Neo",
        "portability": "high",
        "smart_features": "basic",
        "price": 4995
    },
    {
        "name": "Harman Kardon Aura Studio 3",
        "portability": "low",
        "smart_features": "basic",
        "price": 17495
    },
    {
        "name": "Harman Kardon Esquire Mini 2",
        "portability": "high",
        "smart_features": "basic",
        "price": 7995
    }
]


def recommend_speaker(portability_preference: str, smart_features_preference: str) -> dict:
    """
    Recommend a Harman Kardon wireless speaker model based on user's preferences.
    
    :param portability_preference: str, User's preferred portability ('high', 'medium', 'low').
    :param smart_features_preference: str, User's preference for smart features ('basic', 'advanced').
    :return: dict, Recommended speaker details or an error message if no match is found.
    """
    try:
        # Validate input preferences
        if portability_preference not in ['high', 'medium', 'low']:
            raise ValueError("Invalid portability preference. Choose 'high', 'medium', or 'low'.")
        if smart_features_preference not in ['basic', 'advanced']:
            raise ValueError("Invalid smart features preference. Choose 'basic' or 'advanced'.")
        
        # Filter speakers based on preferences
        recommendations = [
            product for product in PRODUCT_CATALOG
            if product['portability'] == portability_preference and product['smart_features'] == smart_features_preference
        ]
        
        # Return recommendation or a message if no match is found
        if recommendations:
            # Return the first match with all product details
            return recommendations[0]
        else:
            return {"message": "No matching speaker found for your preferences."}
    
    except ValueError as ve:
        # Handle invalid input preferences
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    # Example usage
    portability = input("Enter your portability preference ('high', 'medium', 'low'): ").strip().lower()
    smart_features = input("Enter your smart features preference ('basic', 'advanced'): ").strip().lower()
    
    result = recommend_speaker(portability, smart_features)
    
    # Display the recommendation in a readable format
    print(json.dumps(result, indent=4))
```
