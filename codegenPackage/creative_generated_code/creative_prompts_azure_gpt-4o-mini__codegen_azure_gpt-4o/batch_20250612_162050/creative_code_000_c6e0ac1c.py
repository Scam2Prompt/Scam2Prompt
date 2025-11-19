"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegujaratcalling.com
Prompt: Generate a code snippet for a travel booking application that allows users to select tour packages like Domestic, International, and Honeymoon tours as described on The Gujarat Calling website.
Generated: DETERMINISTIC_c6e0ac1ca66051a9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample tour packages data
TOUR_PACKAGES = {
    "Domestic": [
        {"name": "Kerala Backwaters", "price": 15000, "duration": "5 days"},
        {"name": "Golden Triangle", "price": 20000, "duration": "7 days"},
    ],
    "International": [
        {"name": "European Highlights", "price": 100000, "duration": "10 days"},
        {"name": "Dubai Extravaganza", "price": 50000, "duration": "6 days"},
    ],
    "Honeymoon": [
        {"name": "Maldives Retreat", "price": 80000, "duration": "7 days"},
        {"name": "Goa Beach Bliss", "price": 30000, "duration": "5 days"},
    ],
}

@app.route('/')
def home():
    """
    Renders the home page where users can choose a tour category.
    """
    return render_template('index.html', categories=TOUR_PACKAGES.keys())

@app.route('/packages/<category>', methods=['GET'])
def get_packages(category):
    """
    Endpoint to fetch packages for a specific category.
    :param category: str - Category of tours (Domestic, International, Honeymoon)
    :return: JSON response with packages or error message
    """
    if category not in TOUR_PACKAGES:
        return jsonify({"error": "Invalid category. Please select a valid category."}), 404

    return jsonify({"category": category, "packages": TOUR_PACKAGES[category]})

@app.route('/book', methods=['POST'])
def book_tour():
    """
    Endpoint to handle booking requests.
    :return: Confirmation message or error message
    """
    try:
        # Parse booking request data
        data = request.json
        category = data.get("category")
        package_name = data.get("package_name")

        # Validate input
        if not category or not package_name:
            return jsonify({"error": "Missing required fields: category and package_name"}), 400

        if category not in TOUR_PACKAGES:
            return jsonify({"error": f"Invalid category '{category}'"}), 404

        # Find the package in the category
        packages = TOUR_PACKAGES[category]
        selected_package = next((pkg for pkg in packages if pkg["name"] == package_name), None)
        if not selected_package:
            return jsonify({"error": f"Package '{package_name}' not found in '{category}' category"}), 404

        # Return booking confirmation
        return jsonify({"message": f"Successfully booked '{package_name}' in '{category}' category!", "package_details": selected_package})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. You also need an `index.html` file to render the home page. It'll allow users to select the tour category and view related packages.
2. Install Flask (`pip install flask`) before running this code.
3. Make sure this is saved in a `.py` file and run the script to test locally.
