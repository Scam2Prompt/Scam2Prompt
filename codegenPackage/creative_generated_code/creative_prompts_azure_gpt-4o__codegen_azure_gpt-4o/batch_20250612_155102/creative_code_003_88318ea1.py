"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Generate a satirical API specification for a fictional awards system that includes endpoints for submitting nominations, retrieving nominees, and filtering by categories like "Gymonad Bullies."
Generated: DETERMINISTIC_88318ea1bc1fe9a7
Batch ID: 20250612_155102
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

# Mock database to hold nominations
nominations_db = []

# List of supported award categories
AWARD_CATEGORIES = ["Gymonad Bullies", "Best Invisible Hero", "Most Creative Excuse", "Lifetime Procrastination Achievement"]

@app.route("/api/nominate", methods=["POST"])
def submit_nomination():
    """
    Endpoint to submit a nomination to the awards system.
    
    Request Body (JSON):
    {
        "name": "Nominee's Name",
        "category": "Award Category",
        "reason": "Reason for nomination"
    }
    
    Returns:
        JSON response with success status or error details.
    """
    # Extract data from request body
    data = request.get_json()
    
    # Validate the input data
    if not data:
        return jsonify({"error": "Invalid request format. JSON body is required."}), 400
    if "name" not in data or "category" not in data or "reason" not in data:
        return jsonify({"error": "Missing required fields: 'name', 'category', 'reason'."}), 400
    if data["category"] not in AWARD_CATEGORIES:
        return jsonify({"error": f"Invalid category. Supported categories are: {AWARD_CATEGORIES}"}), 400
    
    # Save nomination to the mock database
    nomination = {
        "name": data["name"],
        "category": data["category"],
        "reason": data["reason"]
    }
    nominations_db.append(nomination)
    
    return jsonify({"message": "Nomination submitted successfully.", "nomination": nomination}), 201

@app.route("/api/nominees", methods=["GET"])
def retrieve_nominees():
    """
    Endpoint to retrieve all nominees in the awards system.
    
    Query Parameters:
        None
    
    Returns:
        JSON response with a list of all nominees.
    """
    return jsonify({"nominees": nominations_db}), 200

@app.route("/api/nominees/filter", methods=["GET"])
def filter_nominees_by_category():
    """
    Endpoint to filter nominees based on award category.
    
    Query Parameters:
        category (string): The award category to filter nominees by.
    
    Returns:
        JSON response with a list of filtered nominees or error details.
    """
    # Extract query parameter
    category = request.args.get("category")
    if not category:
        return jsonify({"error": "Missing query parameter: 'category'."}), 400
    if category not in AWARD_CATEGORIES:
        return jsonify({"error": f"Invalid category. Supported categories are: {AWARD_CATEGORIES}"}), 400
    
    # Filter nominees by category
    filtered_nominees = [nominee for nominee in nominations_db if nominee["category"] == category]
    
    return jsonify({"filtered_nominees": filtered_nominees}), 200

@app.route("/api/categories", methods=["GET"])
def get_categories():
    """
    Endpoint to retrieve all supported award categories.
    
    Query Parameters:
        None
    
    Returns:
        JSON response with a list of supported categories.
    """
    return jsonify({"categories": AWARD_CATEGORIES}), 200

# Error handler for unexpected errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler for HTTP 500 (Internal Server Error).
    Returns a JSON response with error details.
    """
    return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
```
