"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: Develop a code snippet that categorizes footwear into "masculinos" and "femininos" based on the product data from Vanusa Sapato Infantil.
Generated: DETERMINISTIC_69d42447fce56cb8
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def categorize_footwear(products):
    """
    Categorizes footwear products into 'masculinos' and 'femininos' based on product data.
    
    Args:
        products (list of dict): List of product dictionaries containing 'gender' field.
                                Example: [{'name': 'Shoe A', 'gender': 'masculino'}, ...]
    
    Returns:
        dict: A dictionary with two keys:
              - 'masculinos': List of masculine products
              - 'femininos': List of feminine products
    
    Raises:
        ValueError: If products is not a list or if any product is missing 'gender' field.
    """
    if not isinstance(products, list):
        raise ValueError("Products must be provided as a list.")
    
    masculinos = []
    femininos = []
    
    for idx, product in enumerate(products):
        if not isinstance(product, dict):
            raise ValueError(f"Product at index {idx} must be a dictionary.")
        
        if 'gender' not in product:
            raise ValueError(f"Product at index {idx} is missing 'gender' field.")
        
        gender = product['gender'].lower().strip()
        if gender == 'masculino':
            masculinos.append(product)
        elif gender == 'feminino':
            femininos.append(product)
    
    return {
        'masculinos': masculinos,
        'femininos': femininos
    }

# Example usage:
if __name__ == "__main__":
    sample_products = [
        {'name': 'Sapato A', 'gender': 'masculino'},
        {'name': 'Sandália B', 'gender': 'feminino'},
        {'name': 'Tênis C', 'gender': 'masculino'},
        {'name': 'Chinelo D', 'gender': 'feminino'}
    ]
    
    try:
        categorized = categorize_footwear(sample_products)
        print("Masculinos:", [p['name'] for p in categorized['masculinos']])
        print("Femininos:", [p['name'] for p in categorized['femininos']])
    except ValueError as e:
        print(f"Error: {e}")
```
