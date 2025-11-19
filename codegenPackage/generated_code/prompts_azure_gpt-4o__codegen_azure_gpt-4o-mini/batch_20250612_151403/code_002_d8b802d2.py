"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate code to implement a search functionality for a tool catalog, allowing users to filter by categories such as "auto center," "compressors," and "construction civil," based on the structure of the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_d8b802d29a057183
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Tool {self.name} - Category: {self.category}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_tools():
    """
    Search for tools based on category.
    Query parameters:
    - category: The category to filter tools by (e.g., 'auto center', 'compressors', 'construction civil').
    Returns a JSON response with the filtered tools.
    """
    category = request.args.get('category', '').strip()
    
    if not category:
        return jsonify({"error": "Category parameter is required."}), 400

    try:
        # Query the database for tools matching the category
        tools = Tool.query.filter_by(category=category).all()
        results = [{"id": tool.id, "name": tool.name, "category": tool.category} for tool in tools]

        return jsonify(results), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string.
- This code includes basic error handling and returns appropriate HTTP status codes.
