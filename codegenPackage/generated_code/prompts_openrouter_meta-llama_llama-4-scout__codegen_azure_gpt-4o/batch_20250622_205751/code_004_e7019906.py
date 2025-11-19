"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Develop an API to fetch and display fact-checking data from a database, using keywords such as "COVID-19 vaccine" and "Ayodhya Buddha statues".
Generated: DETERMINISTIC_e7019906e091934e
Batch ID: 20250622_205751
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

# Initialize Flask app
app = Flask(__name__)

# Configure database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fact_checking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Fact model
class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(255), nullable=False)
    fact = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert Fact object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'keyword': self.keyword,
            'fact': self.fact
        }

# API endpoint to fetch fact-checking data based on keywords
@app.route('/api/facts', methods=['GET'])
def get_facts():
    """
    Fetch fact-checking data based on keywords provided as query parameters.
    Example: /api/facts?keywords=COVID-19 vaccine,Ayodhya Buddha statues
    """
    try:
        # Get keywords from query parameters
        keywords = request.args.get('keywords')
        if not keywords:
            return jsonify({'error': 'Keywords parameter is required'}), 400

        # Split keywords into a list
        keyword_list = [keyword.strip() for keyword in keywords.split(',')]

        # Query the database for matching facts
        facts = Fact.query.filter(Fact.keyword.in_(keyword_list)).all()

        # Return the results as JSON
        return jsonify({'facts': [fact.to_dict() for fact in facts]}), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the Flask app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the server
    app.run(debug=True)
```
