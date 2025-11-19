"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Generate a list of shoe categories for a new e-commerce website inspired by Calini Sapatos em Geral's product offerings.
Generated: DETERMINISTIC_673a7b8c8c866b4c
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shoe_categories.py
# List of shoe categories for an e-commerce website inspired by Calini Sapatos em Geral

def get_shoe_categories():
    """
    Returns a list of shoe categories with their subcategories.
    Each category is a dictionary with 'name' and 'subcategories' keys.
    """
    categories = [
        {
            'name': 'Women\'s Shoes',
            'subcategories': [
                'High Heels',
                'Flats',
                'Sandals',
                'Boots',
                'Sneakers',
                'Wedges',
                'Pumps',
                'Loafers',
                'Espadrilles',
                'Mules'
            ]
        },
        {
            'name': 'Men\'s Shoes',
            'subcategories': [
                'Dress Shoes',
                'Loafers',
                'Sneakers',
                'Boots',
                'Sandals',
                'Oxfords',
                'Derby Shoes',
                'Monk Straps',
                'Boat Shoes',
                'Slip-ons'
            ]
        },
        {
            'name': 'Kids\' Shoes',
            'subcategories': [
                'School Shoes',
                'Sneakers',
                'Sandals',
                'Boots',
                'Mary Janes',
                'Ballet Flats',
                'Velcro Shoes',
                'Rain Boots',
                'Athletic Shoes',
                'Slip-ons'
            ]
        },
        {
            'name': 'Athletic Shoes',
            'subcategories': [
                'Running Shoes',
                'Basketball Shoes',
                'Tennis Shoes',
                'Training Shoes',
                'Walking Shoes',
                'Hiking Shoes',
                'Soccer Cleats',
                'Golf Shoes',
                'Cross-Trainers',
                'Skate Shoes'
            ]
        },
        {
            'name': 'Specialty Shoes',
            'subcategories': [
                'Dance Shoes',
                'Work Shoes',
                'Safety Shoes',
                'Orthopedic Shoes',
                'Wide Width Shoes',
                'Narrow Width Shoes',
                'Vegan Shoes',
                'Eco-Friendly Shoes',
                'Custom Made Shoes',
                'Limited Edition'
            ]
        }
    ]
    
    return categories


if __name__ == '__main__':
    # Example usage
    categories = get_shoe_categories()
    for category in categories:
        print(f"\n{category['name']}:")
        for subcategory in category['subcategories']:
            print(f" - {subcategory}")
```
