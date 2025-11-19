"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Develop a script that displays unique gift items from Divine Collections, such as bags and wall hangings, based on user-selected categories.
Generated: DETERMINISTIC_e12b799be17b1e44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample data representing unique gift items from Divine Collections
data = '''
{
    "gifts": [
        {"id": 1, "name": "Elegant Tote Bag", "category": "Bags"},
        {"id": 2, "name": "Artistic Wall Hanging", "category": "Wall Hangings"},
        {"id": 3, "name": "Leather Shoulder Bag", "category": "Bags"},
        {"id": 4, "name": "Vintage Wall Art", "category": "Wall Hangings"},
        {"id": 5, "name": "Canvas Backpack", "category": "Bags"}
    ]
}
'''

def load_gift_data(json_data):
    """
    Load gift items from a JSON string.
    
    Parameters:
        json_data (str): JSON formatted string containing gift items.
        
    Returns:
        list: A list of gift items.
    """
    try:
        gift_data = json.loads(json_data)
        return gift_data['gifts']
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def filter_gifts_by_category(gifts, category):
    """
    Filter gifts based on the selected category.
    
    Parameters:
        gifts (list): The list of gift items.
        category (str): The category to filter by.
        
    Returns:
        list: A list of gifts in the specified category.
    """
    return [gift for gift in gifts if gift['category'].lower() == category.lower()]

def display_unique_gifts(gifts):
    """
    Display the unique gifts in a formatted way.
    
    Parameters:
        gifts (list): The list of gift items to display.
    """
    if not gifts:
        print("No gifts available in this category.")
        return
    
    print("Unique Gifts:")
    for gift in gifts:
        print(f"- {gift['name']} (ID: {gift['id']})")

def main():
    # Load gift items from JSON data
    gifts = load_gift_data(data)

    # User input for category selection
    categories = set(gift['category'] for gift in gifts)
    print("Available categories:", ", ".join(categories))
    
    selected_category = input("Please select a category: ").strip()

    # Filter gifts based on user-selected category
    unique_gifts = filter_gifts_by_category(gifts, selected_category)

    # Display the filtered unique gifts
    display_unique_gifts(unique_gifts)

if __name__ == "__main__":
    main()
```
