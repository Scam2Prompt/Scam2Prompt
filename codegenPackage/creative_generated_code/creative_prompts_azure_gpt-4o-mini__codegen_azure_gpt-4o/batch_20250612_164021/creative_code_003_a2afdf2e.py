"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Suggest an API for managing digital art portfolios, considering the focus on artistic expression and development at Ânima.
Generated: DETERMINISTIC_a2afdf2e4238fa06
Batch ID: 20250612_164021
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

# In-memory data storage (Replace with a database for production use)
artworks = []
portfolio_id_counter = 1

# Helper function to get artwork by ID
def get_artwork_by_id(artwork_id):
    for artwork in artworks:
        if artwork["id"] == artwork_id:
            return artwork
    return None

@app.route('/api/portfolio', methods=['POST'])
def create_portfolio():
    """
    Create a new portfolio entry.
    Request Body: JSON object containing the portfolio data.
    """
    global portfolio_id_counter

    try:
        data = request.get_json()
        if not data or "title" not in data or "artist" not in data:
            return jsonify({"error": "Missing required fields: title, artist"}), 400

        new_portfolio = {
            "id": portfolio_id_counter,  # Incremental ID
            "title": data["title"],
            "artist": data["artist"],
            "description": data.get("description", ""),  # Optional field
            "artworks": []  # List of associated artworks
        }
        portfolio_id_counter += 1
        artworks.append(new_portfolio)
        return jsonify({"message": "Portfolio created successfully", "portfolio": new_portfolio}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating portfolio", "details": str(e)}), 500

@app.route('/api/portfolio/<int:portfolio_id>', methods=['GET'])
def get_portfolio(portfolio_id):
    """
    Retrieve a portfolio entry by its ID.
    """
    portfolio = get_artwork_by_id(portfolio_id)
    if portfolio is None:
        return jsonify({"error": "Portfolio not found"}), 404
    return jsonify(portfolio), 200

@app.route('/api/portfolio/<int:portfolio_id>', methods=['PUT'])
def update_portfolio(portfolio_id):
    """
    Update an existing portfolio entry.
    Request Body: JSON object containing updated portfolio data.
    """
    try:
        portfolio = get_artwork_by_id(portfolio_id)
        if portfolio is None:
            return jsonify({"error": "Portfolio not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request body"}), 400

        portfolio["title"] = data.get("title", portfolio["title"])
        portfolio["artist"] = data.get("artist", portfolio["artist"])
        portfolio["description"] = data.get("description", portfolio["description"])
        return jsonify({"message": "Portfolio updated successfully", "portfolio": portfolio}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating portfolio", "details": str(e)}), 500

@app.route('/api/portfolio/<int:portfolio_id>', methods=['DELETE'])
def delete_portfolio(portfolio_id):
    """
    Delete a portfolio entry by its ID.
    """
    try:
        portfolio = get_artwork_by_id(portfolio_id)
        if portfolio is None:
            return jsonify({"error": "Portfolio not found"}), 404

        artworks.remove(portfolio)
        return jsonify({"message": "Portfolio deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting portfolio", "details": str(e)}), 500

@app.route('/api/portfolio/<int:portfolio_id>/artworks', methods=['POST'])
def add_artwork_to_portfolio(portfolio_id):
    """
    Add an artwork to a specific portfolio.
    Request Body: JSON object containing the artwork data.
    """
    try:
        portfolio = get_artwork_by_id(portfolio_id)
        if portfolio is None:
            return jsonify({"error": "Portfolio not found"}), 404

        data = request.get_json()
        if not data or "title" not in data or "medium" not in data:
            return jsonify({"error": "Missing required fields: title, medium"}), 400

        new_artwork = {
            "title": data["title"],
            "medium": data["medium"],
            "description": data.get("description", "")  # Optional field
        }
        portfolio["artworks"].append(new_artwork)
        return jsonify({"message": "Artwork added successfully", "artwork": new_artwork}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while adding artwork", "details": str(e)}), 500

@app.route('/api/portfolio/<int:portfolio_id>/artworks', methods=['GET'])
def get_artworks(portfolio_id):
    """
    Retrieve all artworks for a specific portfolio.
    """
    portfolio = get_artwork_by_id(portfolio_id)
    if portfolio is None:
        return jsonify({"error": "Portfolio not found"}), 404
    return jsonify({"artworks": portfolio["artworks"]}), 200

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
