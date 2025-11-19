"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Generate a code snippet for an e-commerce website that lists various salon equipment like "صندلی آرایشگاهی" and "ترولی آرایشگاهی" with options for filtering by category.
Generated: DETERMINISTIC_a7313ca89595f302
Batch ID: 20250612_162325
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

# Sample data: List of salon equipment with categories
salon_equipment = [
    {"id": 1, "name": "صندلی آرایشگاهی", "category": "صندلی"},
    {"id": 2, "name": "ترولی آرایشگاهی", "category": "تجهیزات"},
    {"id": 3, "name": "آینه آرایشگاهی", "category": "آینه"},
    {"id": 4, "name": "کابینت آرایشگاهی", "category": "کابینت"},
    {"id": 5, "name": "دستگاه بخور", "category": "تجهیزات"},
]

@app.route('/equipment', methods=['GET'])
def get_equipment():
    """
    Retrieve a list of salon equipment with optional filtering by category.
    
    Query Parameters:
    - category: Optional filter to narrow down results by equipment category.
    
    Returns:
    - A JSON response containing the filtered list of salon equipment.
    """
    category = request.args.get('category')
    
    try:
        # Filter by category if provided
        if category:
            filtered_equipment = [item for item in salon_equipment if item['category'] == category]
        else:
            filtered_equipment = salon_equipment
        
        # Return the filtered equipment list
        return jsonify(filtered_equipment), 200
    
    except Exception as e:
        # Catch and log any exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
