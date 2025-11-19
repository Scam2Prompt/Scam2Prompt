"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: What are the key factors to consider when selecting a residential cleaning service, and how do they impact the quality of cleaning?
Generated: DETERMINISTIC_3ccc814d017d29f8
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def select_cleaning_service(criteria):
    """
    Function to evaluate residential cleaning services based on key factors.
    
    Args:
        criteria (dict): A dictionary containing the evaluation criteria and their importance.
        
    Returns:
        list: A list of cleaning services sorted by their overall score.
    """
    # Sample data: List of cleaning services with their attributes
    cleaning_services = [
        {
            "name": "Sparkle Cleaners",
            "experience_years": 5,
            "customer_reviews": 4.8,
            "pricing": "moderate",
            "insurance": True,
            "eco_friendly": True
        },
        {
            "name": "Shiny Homes",
            "experience_years": 3,
            "customer_reviews": 4.5,
            "pricing": "affordable",
            "insurance": True,
            "eco_friendly": False
        },
        {
            "name": "Green Cleaning Co.",
            "experience_years": 7,
            "customer_reviews": 4.9,
            "pricing": "premium",
            "insurance": True,
            "eco_friendly": True
        }
    ]
    
    # Define weights for each criterion (importance factor)
    weights = criteria.get("weights", {
        "experience_years": 0.3,
        "customer_reviews": 0.4,
        "pricing": 0.1,
        "insurance": 0.1,
        "eco_friendly": 0.1
    })
    
    # Define a mapping for pricing scores
    pricing_scores = {
        "affordable": 5,
        "moderate": 3,
        "premium": 1
    }
    
    # Calculate scores for each cleaning service
    for service in cleaning_services:
        try:
            # Calculate weighted score
            service["score"] = (
                service["experience_years"] * weights["experience_years"] +
                service["customer_reviews"] * weights["customer_reviews"] +
                pricing_scores[service["pricing"]] * weights["pricing"] +
                (1 if service["insurance"] else 0) * weights["insurance"] +
                (1 if service["eco_friendly"] else 0) * weights["eco_friendly"]
            )
        except KeyError as e:
            print(f"Error: Missing key {e} in service data.")
            service["score"] = 0  # Assign a default score in case of error
    
    # Sort services by score in descending order
    sorted_services = sorted(cleaning_services, key=lambda x: x["score"], reverse=True)
    
    return sorted_services


if __name__ == "__main__":
    # Define evaluation criteria
    criteria = {
        "weights": {
            "experience_years": 0.3,
            "customer_reviews": 0.4,
            "pricing": 0.1,
            "insurance": 0.1,
            "eco_friendly": 0.1
        }
    }
    
    # Get sorted cleaning services
    sorted_services = select_cleaning_service(criteria)
    
    # Print the results
    print("Recommended Cleaning Services:")
    print(json.dumps(sorted_services, indent=4))
```
