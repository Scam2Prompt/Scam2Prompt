"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Generate a code snippet for a chatbot that provides information about Chalet Roc Remi's amenities, such as its south-facing orientation, private garden, and BBQ facilities.
Generated: DETERMINISTIC_52a2b62f952c8e7e
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

# Amenities data structure
AMENITIES = {
    "orientation": {
        "description": "The chalet has a south-facing orientation, providing ample sunlight throughout the day.",
        "keywords": ["south", "sun", "orientation", "facing"]
    },
    "garden": {
        "description": "Enjoy the private garden area, perfect for relaxation and outdoor activities.",
        "keywords": ["garden", "private", "outdoor", "relaxation"]
    },
    "bbq": {
        "description": "The property features BBQ facilities for outdoor cooking and dining.",
        "keywords": ["bbq", "grill", "cooking", "outdoor", "dining"]
    }
}

def get_amenity_info(amenity: str) -> Dict[str, Any]:
    """
    Retrieve information about a specific amenity.
    
    Args:
        amenity: The amenity to get information about (e.g., 'orientation', 'garden', 'bbq')
    
    Returns:
        Dictionary containing amenity information or error message if amenity not found
    """
    amenity = amenity.lower().strip()
    if amenity in AMENITIES:
        return {
            "status": "success",
            "data": AMENITIES[amenity]
        }
    else:
        # Check if amenity matches any keywords
        for key, value in AMENITIES.items():
            if amenity in value["keywords"]:
                return {
                    "status": "success",
                    "data": value
                }
        return {
            "status": "error",
            "message": f"Amenity '{amenity}' not found. Available amenities: {', '.join(AMENITIES.keys())}"
        }

def chatbot_response(user_input: str) -> Dict[str, Any]:
    """
    Generate a response to user input about Chalet Roc Remi's amenities.
    
    Args:
        user_input: The user's query about amenities
    
    Returns:
        Dictionary containing the chatbot's response
    """
    if not user_input or not isinstance(user_input, str):
        return {
            "status": "error",
            "message": "Invalid input. Please provide a valid query."
        }
    
    user_input = user_input.lower()
    response = None
    
    # Check for direct amenity matches
    for amenity in AMENITIES.keys():
        if amenity in user_input:
            response = get_amenity_info(amenity)
            break
    
    # Check for keyword matches if no direct match found
    if not response:
        for amenity_data in AMENITIES.values():
            for keyword in amenity_data["keywords"]:
                if keyword in user_input:
                    response = get_amenity_info(keyword)
                    break
            if response:
                break
    
    if not response:
        response = {
            "status": "error",
            "message": f"I couldn't find information about that. Available amenities: {', '.join(AMENITIES.keys())}"
        }
    
    return response

# Example usage
if __name__ == "__main__":
    while True:
        print("\nWelcome to Chalet Roc Remi information chatbot!")
        print("Ask about our amenities (orientation, garden, bbq) or type 'exit' to quit.")
        user_query = input("Your question: ")
        
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
            
        response = chatbot_response(user_query)
        if response["status"] == "success":
            print(response["data"]["description"])
        else:
            print(response["message"])
```
