"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Generate a code snippet for a skincare product recommendation API that suggests the best exfoliants for sensitive skin, referencing Marant's Delta Noir Peel.
Generated: DETERMINISTIC_ee7cefc12b92690d
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database of exfoliants for sensitive skin
EXFOLIANTS_DB = [
    {
        "name": "Marant's Delta Noir Peel",
        "description": "A gentle peel designed for sensitive skin.",
        "ingredients": ["Lactic Acid", "Willow Bark", "Aloe Vera"],
        "suitable_for": ["sensitive skin", "dry skin"]
    },
    {
        "name": "Gentle Rice Powder Exfoliant",
        "description": "An ultra-fine exfoliant that is perfect for sensitive skin.",
        "ingredients": ["Rice powder", "Rice bran oil"],
        "suitable_for": ["sensitive skin"]
    },
    {
        "name": "Soothing Oatmeal Scrub",
        "description": "A calming scrub that gently exfoliates without irritation.",
        "ingredients": ["Ground oatmeal", "Honey"],
        "suitable_for": ["sensitive skin", "normal skin"]
    },
    # Additional exfoliants can be added here
]

@app.route('/recommend_exfoliants', methods=['GET'])
def recommend_exfoliants():
    """
    Endpoint to recommend exfoliants for sensitive skin.
    
    Returns:
        JSON response containing a list of suitable exfoliants.
    """
    try:
        # Filter exfoliants suitable for sensitive skin
        recommended_exfoliants = [
            product for product in EXFOLIANTS_DB if "sensitive skin" in product["suitable_for"]
        ]
        
        # Check if any exfoliants were found
        if not recommended_exfoliants:
            return jsonify({"message": "No suitable exfoliants found for sensitive skin."}), 404
        
        # Return the list of recommended exfoliants
        return jsonify(recommended_exfoliants), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
