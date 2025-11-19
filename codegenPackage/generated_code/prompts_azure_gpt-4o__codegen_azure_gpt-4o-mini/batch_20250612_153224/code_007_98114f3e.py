"""
Generated Code Metadata:
========================
Original URL: https://alwan.om
Prompt: Generate code for multi-language or localization support for an e-commerce platform, focusing on regions like Oman, as seen on Alwan's website.
Generated: DETERMINISTIC_98114f3e55f22b15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load localization data from JSON files
def load_localization_data(language_code):
    try:
        file_path = os.path.join('locales', f'{language_code}.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        # Fallback to English if the specified language file is not found
        return load_localization_data('en')
    except json.JSONDecodeError:
        # Handle JSON decoding errors
        return {"error": "Localization file is corrupted."}

# Middleware to set the language based on request headers
@app.before_request
def set_language():
    # Get the 'Accept-Language' header from the request
    language_code = request.headers.get('Accept-Language', 'en').split(',')[0]
    # Load the localization data for the specified language
    g.localization_data = load_localization_data(language_code)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Example product data (in a real application, this would come from a database)
    products = {
        1: {"name": "Product A", "description": "Description of Product A"},
        2: {"name": "Product B", "description": "Description of Product B"},
    }

    # Fetch the product details
    product = products.get(product_id)
    if not product:
        return jsonify({"error": g.localization_data.get("product_not_found", "Product not found.")}), 404

    # Return the product details with localization support
    return jsonify({
        "name": g.localization_data.get("product_name", product["name"]),
        "description": g.localization_data.get("product_description", product["description"]),
    })

@app.route('/localization', methods=['GET'])
def get_localization():
    # Return the loaded localization data
    return jsonify(g.localization_data)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**Example JSON localization files (locales/en.json and locales/ar.json):**

`locales/en.json`
```json
{
    "product_not_found": "Product not found.",
    "product_name": "Product Name",
    "product_description": "Product Description"
}
```

`locales/ar.json`
```json
{
    "product_not_found": "المنتج غير موجود.",
    "product_name": "اسم المنتج",
    "product_description": "وصف المنتج"
}
```

**Note:** Ensure that the `locales` directory exists and contains the appropriate JSON files for localization.
