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
# Flask web application for finding the best optical solutions based on user lifestyle and vision needs

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for optical solutions
optical_solutions = [
    {
        "id": 1,
        "name": "Comfort Fit Glasses",
        "description": "Ideal for daily wear with a lightweight design.",
        "lifestyles": ["daily wear", "office work"],
        "vision_needs": ["nearsighted", "normal"]
    },
    {
        "id": 2,
        "name": "Sports Contact Lenses",
        "description": "Perfect for active individuals and sports enthusiasts.",
        "lifestyles": ["sports", "outdoor"],
        "vision_needs": ["farsighted", "astigmatism"]
    },
    {
        "id": 3,
        "name": "Blue Light Filtering Glasses",
        "description": "Designed for extended screen time and digital device use.",
        "lifestyles": ["office work", "gaming"],
        "vision_needs": ["normal", "nearsighted"]
    }
]

@app.route('/')
def home():
    """
    Route for the homepage.
    Renders the main page where users can input their lifestyle and vision needs.
    """
    return render_template('index.html')

@app.route('/find-solutions', methods=['POST'])
def find_solutions():
    """
    API endpoint to find the best optical solutions based on user input.
    Expects 'lifestyle' and 'vision_need' from the request body.
    Returns matching optical solutions.
    """
    try:
        # Get user input from the request body
        user_lifestyle = request.form.get('lifestyle')
        user_vision_need = request.form.get('vision_need')

        # Validate input
        if not user_lifestyle or not user_vision_need:
            return jsonify({"error": "Lifestyle and vision needs are required."}), 400

        # Filter solutions based on user input
        matching_solutions = [
            solution for solution in optical_solutions
            if user_lifestyle in solution['lifestyles'] and user_vision_need in solution['vision_needs']
        ]

        # Return matching solutions
        return jsonify({"solutions": matching_solutions}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**Note:** This code assumes you have a corresponding `index.html` file in the `templates` directory for the homepage. It should include a form where users can input their lifestyle and vision needs.
