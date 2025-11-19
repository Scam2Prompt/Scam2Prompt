"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a code snippet for a web application that allows users to create their own cosmetic brand using the full-service project model described by Fabricare Cosméticos.
Generated: DETERMINISTIC_92f6e558e446265f
Batch ID: 20250612_162325
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# In-memory storage for cosmetic brand data (for demonstration purposes)
cosmetic_brands = []

@app.route('/create-brand', methods=['POST'])
def create_brand():
    """
    Endpoint to create a cosmetic brand.
    Users can provide brand details which will be stored in-memory.
    """
    try:
        # Parse request data
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['brand_name', 'owner_name', 'product_types', 'contact_email']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create brand object
        brand = {
            "id": len(cosmetic_brands) + 1,  # Simple ID generation
            "brand_name": data['brand_name'],
            "owner_name": data['owner_name'],
            "product_types": data['product_types'],  # List of product types
            "contact_email": data['contact_email']
        }
        
        # Save the brand to in-memory storage
        cosmetic_brands.append(brand)

        return jsonify({"message": "Cosmetic brand created successfully!", "brand": brand}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while creating the brand.", "details": str(e)}), 500

@app.route('/brands', methods=['GET'])
def get_brands():
    """
    Endpoint to retrieve all created cosmetic brands.
    """
    return jsonify({"brands": cosmetic_brands}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```

### Notes
- **Dependencies**: Make sure Flask is installed (`pip install flask`) before running the code.
- **Execution**: Save this code in a file named `app.py` and run it using `python app.py`. The application will start on `http://127.0.0.1:5000`.
- **Endpoints**:
  - `POST /create-brand`: Accepts a JSON payload to create a cosmetic brand (e.g., `{"brand_name": "Glow Cosmetics", "owner_name": "Jane Doe", "product_types": ["skincare", "makeup"], "contact_email": "jane.doe@example.com"}`).
  - `GET /brands`: Returns all created brands.
