"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Implement a search feature that allows users to find "Parrillas" based on specific criteria like capacity and material, as highlighted on the Meat Master webpage.
Generated: DETERMINISTIC_5efc48a6b1a66937
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Sample data representing parrillas from the Meat Master webpage
# In a real-world application, this data would likely come from a database or API
parrillas_data = [
    {"id": 1, "name": "Classic Grill", "capacity": 4, "material": "Steel"},
    {"id": 2, "name": "Premium BBQ", "capacity": 6, "material": "Cast Iron"},
    {"id": 3, "name": "Family Grill", "capacity": 8, "material": "Aluminum"},
    {"id": 4, "name": "Compact Grill", "capacity": 2, "material": "Steel"},
    {"id": 5, "name": "Outdoor Master", "capacity": 10, "material": "Cast Iron"},
]

def search_parrillas(criteria):
    """
    Searches parrillas based on the provided criteria.
    
    Args:
        criteria (dict): Dictionary containing the search criteria.
                         Supported keys are 'capacity' and 'material'.
                         Example: {"capacity": 6, "material": "Cast Iron"}
    
    Returns:
        list: List of parrillas matching the criteria.
    """
    try:
        # Validate criteria
        if not isinstance(criteria, dict):
            raise ValueError("Search criteria must be a dictionary.")

        # Filter parrillas based on criteria
        filtered_parrillas = [
            parrilla for parrilla in parrillas_data
            if all(parrilla.get(key) == value for key, value in criteria.items() if value is not None)
        ]
        
        return filtered_parrillas
    except Exception as e:
        # Log or handle exceptions gracefully
        print(f"Error while searching parrillas: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Define search criteria (can be dynamic based on user input in production)
    search_criteria = {
        "capacity": 6,       # Capacity to filter (set to None to ignore this filter)
        "material": "Cast Iron"  # Material to filter (set to None to ignore this filter)
    }
    
    # Perform search
    result = search_parrillas(search_criteria)
    
    # Output results in JSON format
    print(json.dumps(result, indent=4))
```
