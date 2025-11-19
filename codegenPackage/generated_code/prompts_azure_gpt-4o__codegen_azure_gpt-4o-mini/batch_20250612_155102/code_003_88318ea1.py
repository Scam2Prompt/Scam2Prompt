"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Generate a satirical API specification for a fictional awards system that includes endpoints for submitting nominations, retrieving nominees, and filtering by categories like "Gymonad Bullies."
Generated: DETERMINISTIC_88318ea1bc1fe9a7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for nominations
nominations = []

# Define a simple Nomination class
class Nomination:
    def __init__(self, nominee_name, category):
        self.nominee_name = nominee_name
        self.category = category

# Endpoint to submit a nomination
@app.route('/nominations', methods=['POST'])
def submit_nomination():
    """
    Submit a nomination for an award.
    Expects a JSON payload with 'nominee_name' and 'category'.
    """
    try:
        data = request.get_json()
        nominee_name = data['nominee_name']
        category = data['category']

        # Validate input
        if not nominee_name or not category:
            raise BadRequest("Both 'nominee_name' and 'category' are required.")

        # Create a new nomination and add it to the list
        nomination = Nomination(nominee_name, category)
        nominations.append(nomination)

        return jsonify({"message": "Nomination submitted successfully!"}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to retrieve all nominees
@app.route('/nominations', methods=['GET'])
def get_nominations():
    """
    Retrieve all nominations.
    Optionally filter by category using a query parameter.
    """
    category_filter = request.args.get('category')
    filtered_nominations = nominations

    if category_filter:
        filtered_nominations = [n for n in nominations if n.category == category_filter]

    return jsonify([{"nominee_name": n.nominee_name, "category": n.category} for n in filtered_nominations]), 200

# Endpoint to filter nominations by category
@app.route('/nominations/categories/<string:category>', methods=['GET'])
def get_nominations_by_category(category):
    """
    Retrieve nominations filtered by a specific category.
    """
    filtered_nominations = [n for n in nominations if n.category == category]

    if not filtered_nominations:
        return jsonify({"message": "No nominations found for this category."}), 404

    return jsonify([{"nominee_name": n.nominee_name, "category": n.category} for n in filtered_nominations]), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
