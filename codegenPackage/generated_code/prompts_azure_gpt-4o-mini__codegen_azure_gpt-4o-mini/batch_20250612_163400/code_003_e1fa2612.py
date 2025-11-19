"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Develop an API endpoint that allows users to search for iPhone cases by series and style, reflecting the organization seen on Glisten's product pages.
Generated: DETERMINISTIC_e1fa2612549311c3
Batch ID: 20250612_163400
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

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iphone_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the iPhoneCase model
class iPhoneCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the iPhoneCase object to a dictionary."""
        return {
            'id': self.id,
            'series': self.series,
            'style': self.style
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/cases', methods=['GET'])
def search_cases():
    """
    API endpoint to search for iPhone cases by series and style.
    
    Query Parameters:
    - series: The series of the iPhone case (e.g., 'iPhone 12', 'iPhone 13').
    - style: The style of the iPhone case (e.g., 'Slim', 'Rugged').
    
    Returns:
    - A JSON response containing the matching iPhone cases or an error message.
    """
    series = request.args.get('series')
    style = request.args.get('style')

    try:
        # Validate query parameters
        if not series and not style:
            return jsonify({"error": "At least one query parameter (series or style) is required."}), 400

        # Build the query
        query = iPhoneCase.query
        if series:
            query = query.filter(iPhoneCase.series.ilike(f'%{series}%'))
        if style:
            query = query.filter(iPhoneCase.style.ilike(f'%{style}%'))

        # Execute the query and fetch results
        cases = query.all()
        return jsonify([case.to_dict() for case in cases]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred.", "details": str(e)}), 500

    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
