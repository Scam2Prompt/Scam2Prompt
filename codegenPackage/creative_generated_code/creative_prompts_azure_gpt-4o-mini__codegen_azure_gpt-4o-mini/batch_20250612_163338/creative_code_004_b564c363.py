"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://florerialima.com
Prompt: Suggest an API that provides floral arrangement recommendations based on user-selected occasions such as graduations or condolences.
Generated: DETERMINISTIC_b564c36359326ce4
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data: Dictionary mapping occasions to floral arrangement suggestions
FLORAL_ARRANGEMENTS = {
    "graduation": [
        {"name": "Sunflower Bouquet", "description": "A bright and cheerful bouquet to celebrate achievements."},
        {"name": "Mixed Color Roses", "description": "A vibrant mix of roses to commemorate the special day."}
    ],
    "condolences": [
        {"name": "Lily Arrangement", "description": "Elegant lilies for expressing sympathy."},
        {"name": "White Rose Wreath", "description": "A classic wreath for honoring a loved one."}
    ],
    "birthday": [
        {"name": "Birthday Bouquet", "description": "A fun and colorful bouquet for celebrating birthdays."},
        {"name": "Exotic Flower Arrangement", "description": "Unique flowers to make the birthday special."}
    ]
}

@app.route('/api/flowers', methods=['GET'])
def get_flower_recommendations():
    """
    API endpoint to get floral arrangement recommendations based on the selected occasion.
    Query parameter 'occasion' must be provided.
    """
    occasion = request.args.get('occasion')
    
    if not occasion:
        raise BadRequest("Missing 'occasion' query parameter.")
    
    occasion = occasion.lower()
    
    if occasion not in FLORAL_ARRANGEMENTS:
        return jsonify({"error": "No recommendations available for the selected occasion."}), 404
    
    # Return floral arrangements for the specified occasion
    return jsonify({
        "occasion": occasion,
        "recommendations": FLORAL_ARRANGEMENTS[occasion]
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
