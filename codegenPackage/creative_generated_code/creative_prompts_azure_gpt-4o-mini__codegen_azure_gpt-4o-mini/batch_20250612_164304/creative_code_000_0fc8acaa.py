"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Generate a code snippet for a web application that allows users to find the best optical solutions based on their lifestyle and vision needs, similar to the services offered by Optic Alizé.
Generated: DETERMINISTIC_0fc8acaad5c26260
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Sample data for different optical solutions based on lifestyle
optical_solutions = {
    "active": [
        {"type": "Sports Glasses", "description": "Lightweight, impact-resistant glasses."},
        {"type": "Contact Lenses", "description": "Convenient and flexible for active lifestyles."}
    ],
    "office": [
        {"type": "Blue Light Glasses", "description": "Reduces eye strain from screens."},
        {"type": "Progressive Lenses", "description": "Seamless transition between different viewing distances."}
    ],
    "fashion": [
        {"type": "Designer Frames", "description": "Stylish glasses that make a statement."},
        {"type": "Sunglasses", "description": "Protective eyewear with UV protection."}
    ]
}

@app.route('/find_optical_solutions', methods=['POST'])
def find_optical_solutions():
    """Endpoint to find optical solutions based on user lifestyle and vision needs."""
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'lifestyle' not in data:
            return jsonify({"error": "Invalid input, please provide a lifestyle."}), 400

        lifestyle = data['lifestyle'].lower()

        # Get the appropriate solutions based on lifestyle
        solutions = optical_solutions.get(lifestyle)

        if solutions is None:
            return jsonify({"error": "No solutions found for the provided lifestyle."}), 404

        return jsonify({"lifestyle": lifestyle, "solutions": solutions}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format."}), 400
    except Exception as e:
        # Log the exception (logging mechanism can be integrated)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Note:** Ensure you have Flask installed in your Python environment (`pip install Flask`) to run this application.
