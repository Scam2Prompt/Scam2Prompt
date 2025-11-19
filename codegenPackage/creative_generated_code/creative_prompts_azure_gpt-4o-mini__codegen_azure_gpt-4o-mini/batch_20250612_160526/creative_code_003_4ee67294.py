"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zentocosmetic.com
Prompt: Create an API endpoint that retrieves information about Zento's hair care products, including their ingredients and benefits, focusing on the moisturizing and volumizing properties.
Generated: DETERMINISTIC_4ee67294f85f1bb1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing Zento's hair care products
HAIR_CARE_PRODUCTS = [
    {
        "id": 1,
        "name": "Moisturizing Shampoo",
        "ingredients": ["Aloe Vera", "Coconut Oil", "Shea Butter"],
        "benefits": ["Deeply moisturizes", "Prevents dryness", "Enhances shine"],
        "properties": ["Moisturizing"]
    },
    {
        "id": 2,
        "name": "Volumizing Conditioner",
        "ingredients": ["Rice Protein", "Jojoba Oil", "Panthenol"],
        "benefits": ["Adds volume", "Strengthens hair", "Improves manageability"],
        "properties": ["Volumizing"]
    },
    {
        "id": 3,
        "name": "Hydrating Hair Mask",
        "ingredients": ["Argan Oil", "Honey", "Vitamin E"],
        "benefits": ["Intense hydration", "Repairs damage", "Softens hair"],
        "properties": ["Moisturizing"]
    },
    {
        "id": 4,
        "name": "Lift & Volume Spray",
        "ingredients": ["Seaweed Extract", "Glycerin", "Amino Acids"],
        "benefits": ["Boosts volume", "Provides lift", "Non-greasy finish"],
        "properties": ["Volumizing"]
    },
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieves hair care products focusing on moisturizing and volumizing properties.

    Query parameters:
    - property: Filter products by specific properties (moisturizing/volumizing).

    Returns:
    - JSON response containing a list of products matching the criteria.
    """
    try:
        # Get property filter from query parameters
        property_filter = request.args.get('property', None)

        # Filter products based on the provided property
        if property_filter:
            filtered_products = [
                product for product in HAIR_CARE_PRODUCTS
                if property_filter.lower() in (prop.lower() for prop in product['properties'])
            ]
        else:
            filtered_products = HAIR_CARE_PRODUCTS

        # Return the filtered list of products as JSON
        return jsonify(filtered_products), 200

    except Exception as e:
        # Log the exception for debugging purposes (in production, you might log this to a file)
        print(f"Error retrieving products: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving products."}), 500

if __name__ == '__main__':
    # Run the application on the specified port
    app.run(debug=True, port=5000)
```
