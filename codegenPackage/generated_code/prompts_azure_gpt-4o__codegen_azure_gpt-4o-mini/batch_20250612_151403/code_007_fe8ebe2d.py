"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a REST API endpoint for retrieving construction tool details, including "niveis, prumos e linhas," "talhas manuais," and "trole manual," based on the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_fe8ebe2de7eba2f8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
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
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the Tool object to a dictionary."""
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """
    Retrieve construction tool details based on category.
    Query parameters:
        - category: The category of tools to retrieve (e.g., 'niveis', 'talhas manuais', 'trole manual').
    Returns:
        - JSON response with tool details or an error message.
    """
    category = request.args.get('category')

    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    try:
        # Query the database for tools in the specified category
        tools = Tool.query.filter_by(category=category).all()
        if not tools:
            return jsonify({'message': 'No tools found for the specified category.'}), 404

        # Convert tools to a list of dictionaries
        tools_list = [tool.to_dict() for tool in tools]
        return jsonify(tools_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
