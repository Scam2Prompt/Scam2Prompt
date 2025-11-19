"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Develop an API endpoint that allows users to search for iPhone cases by series and style, reflecting the organization seen on Glisten's product pages.
Generated: DETERMINISTIC_e1fa2612549311c3
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iphone_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the iPhone case model
class iPhoneCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the iPhoneCase object to a dictionary for JSON serialization."""
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
    - series: The series of the iPhone (e.g., "iPhone 12").
    - style: The style of the case (e.g., "clear", "rugged").
    
    Returns:
    - JSON list of matching iPhone cases.
    """
    series = request.args.get('series')
    style = request.args.get('style')

    # Validate input
    if not series and not style:
        return jsonify({"error": "At least 'series' or 'style' must be provided."}), 400

    # Build query filters
    query_filters = {}
    if series:
        query_filters['series'] = series
    if style:
        query_filters['style'] = style

    try:
        # Query the database for matching cases
        cases = iPhoneCase.query.filter_by(**query_filters).all()
        return jsonify([case.to_dict() for case in cases]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Note
Ensure to set up the database with appropriate data for the API to return meaningful results. Use the SQLite database or modify the connection string based on your production database.
