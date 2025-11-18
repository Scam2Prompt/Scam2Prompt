"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a REST API endpoint for retrieving construction tool details, including "niveis, prumos e linhas," "talhas manuais," and "trole manual," based on the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_fe8ebe2de7eba2f8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for Construction Tools
class ConstructionTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description
        }

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Endpoint to retrieve construction tool details."""
    category = request.args.get('category')

    try:
        if category:
            tools = ConstructionTool.query.filter_by(category=category).all()
        else:
            tools = ConstructionTool.query.all()

        return jsonify([tool.to_dict() for tool in tools]), 200
    except SQLAlchemyError as e:
        # Log the error (here we just print it, but consider using logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not retrieve data'}), 500

# Create the database tables (only run once)
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to run `pip install Flask SQLAlchemy` to install the required dependencies before executing this code.
