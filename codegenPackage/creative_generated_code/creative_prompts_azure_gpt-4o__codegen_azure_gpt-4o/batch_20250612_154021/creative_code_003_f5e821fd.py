"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Implement a feature to display and filter guilds by categories such as "featured" and "newest," inspired by the Guildhall website's guild exploration tools.
Generated: DETERMINISTIC_f5e821fdda9ae7e5
Batch ID: 20250612_154021
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

# Sample guild data
guilds = [
    {"id": 1, "name": "Knights of Valor", "category": "featured"},
    {"id": 2, "name": "Mystic Wanderers", "category": "newest"},
    {"id": 3, "name": "Shadow Assassins", "category": "featured"},
    {"id": 4, "name": "Eternal Guardians", "category": "newest"},
    {"id": 5, "name": "Dragon Tamers", "category": "featured"},
]

def filter_guilds_by_category(category):
    """
    Filters guilds based on the provided category.
    
    :param category: The category to filter guilds by.
    :return: List of guilds matching the category.
    """
    return [guild for guild in guilds if guild["category"] == category]

@app.route('/guilds', methods=['GET'])
def get_guilds():
    """
    Endpoint to get guilds filtered by category.
    
    Query Parameters:
      - category: The category to filter guilds by ("featured", "newest").
    
    :return: JSON response containing filtered guild data.
    """
    try:
        # Get the category parameter from the query string
        category = request.args.get('category')

        # If no category is provided, return all guilds
        if not category:
            return jsonify({"guilds": guilds}), 200

        # Validate the category parameter
        if category not in {"featured", "newest"}:
            return jsonify({"error": "Invalid category. Allowed categories are 'featured' and 'newest'."}), 400

        # Filter guilds based on the category
        filtered_guilds = filter_guilds_by_category(category)
        return jsonify({"guilds": filtered_guilds}), 200

    except Exception as e:
        # Catch any unexpected errors and return a 500 response
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
```
