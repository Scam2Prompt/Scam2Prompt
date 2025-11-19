"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infusionperu.com
Prompt: Develop a function that recommends an Infusion Peru drink based on user preferences for flavors and health benefits, such as stress relief or immune support.
Generated: DETERMINISTIC_588a0eac26329781
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# infusion_recommendation.py

def recommend_infusion(flavor_preference, health_benefit):
    """
    Recommends an Infusion Peru drink based on user preferences.
    
    Parameters:
        flavor_preference (str): The user's preferred flavor (e.g., 'sweet', 'citrus', 'herbal').
        health_benefit (str): The desired health benefit (e.g., 'stress relief', 'immune support').
    
    Returns:
        str: The recommended Infusion Peru drink.
    """
    # List of Infusion Peru drinks with flavor and health benefit pairing
    infusions = [
        {"name": "Chamomile Infusion", "flavor": "herbal", "benefit": "stress relief"},
        {"name": "Lemon Verbena Infusion", "flavor": "citrus", "benefit": "stress relief"},
        {"name": "Eucalyptus Infusion", "flavor": "herbal", "benefit": "immune support"},
        {"name": "Hibiscus Infusion", "flavor": "sweet", "benefit": "immune support"},
        {"name": "Mint Infusion", "flavor": "herbal", "benefit": "digestive health"},
        {"name": "Ginger Infusion", "flavor": "spicy", "benefit": "digestive health"}
    ]

    try:
        # Filter infusions matching both flavor and health benefit
        matching_infusions = [
            infusion["name"] for infusion in infusions
            if infusion["flavor"] == flavor_preference.lower() and infusion["benefit"] == health_benefit.lower()
        ]

        # Return recommendation based on matches
        if matching_infusions:
            return f"Based on your preferences, we recommend: {', '.join(matching_infusions)}."
        else:
            return "Sorry, no matching Infusion Peru drinks found for your preferences."
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while processing your request: {str(e)}"


# Example usage
if __name__ == "__main__":
    # User preferences
    user_flavor = input("Enter your preferred flavor (e.g., sweet, citrus, herbal): ")
    user_benefit = input("Enter desired health benefit (e.g., stress relief, immune support): ")
    
    # Get recommendation
    result = recommend_infusion(user_flavor, user_benefit)
    print(result)
```
