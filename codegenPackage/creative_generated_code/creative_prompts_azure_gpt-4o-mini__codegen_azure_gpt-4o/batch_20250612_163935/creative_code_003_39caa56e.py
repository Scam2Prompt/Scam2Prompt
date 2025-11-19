"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a library function that filters sports equipment by type, such as "Acessórios" or "Fardamentos", as described on the sports blog page.
Generated: DETERMINISTIC_39caa56e3fdaa809
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sports_filter.py

"""
This library provides functionality to filter sports equipment by type.
User can specify the type of equipment such as 'Acessórios' or 'Fardamentos'.
"""

def filter_sports_equipment(equipment_list, filter_type):
    """
    Filters a list of sports equipment based on the specified type.
    
    Args:
        equipment_list (list of dict): A list of dictionaries representing sports equipment. 
                                       Each dictionary must have a 'type' key.
        filter_type (str): The type of equipment to filter ('Acessórios', 'Fardamentos', etc.)
    
    Returns:
        list of dict: A list of dictionaries containing equipment that matches the filter type.
    
    Raises:
        ValueError: If equipment_list is not a list or filter_type is not a string.
    """
    # Error handling for invalid input types
    if not isinstance(equipment_list, list):
        raise ValueError("equipment_list must be a list of dictionaries.")
    if not isinstance(filter_type, str):
        raise ValueError("filter_type must be a string.")

    # Filter the equipment based on the specified type
    filtered_equipment = [
        equipment for equipment in equipment_list 
        if 'type' in equipment and equipment['type'] == filter_type
    ]
    
    return filtered_equipment


if __name__ == "__main__":
    # Example usage of the filter_sports_equipment function
    sports_equipment = [
        {"name": "Soccer Ball", "type": "Acessórios"},
        {"name": "Uniform", "type": "Fardamentos"},
        {"name": "Helmet", "type": "Acessórios"},
        {"name": "Jersey", "type": "Fardamentos"},
    ]
    
    # Filter by type 'Acessórios'
    try:
        accessories = filter_sports_equipment(sports_equipment, "Acessórios")
        print("Filtered Acessórios:", accessories)
        
        # Filter by type 'Fardamentos'
        uniforms = filter_sports_equipment(sports_equipment, "Fardamentos")
        print("Filtered Fardamentos:", uniforms)
    except ValueError as e:
        print(f"Error: {e}")
```
