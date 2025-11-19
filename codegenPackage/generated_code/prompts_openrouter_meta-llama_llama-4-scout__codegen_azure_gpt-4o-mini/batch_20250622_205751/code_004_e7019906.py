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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fact_checking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FactCheck model
class FactCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(255), nullable=False)
    fact = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the FactCheck object to a dictionary."""
        return {
            'id': self.id,
            'keyword': self.keyword,
            'fact': self.fact
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/fact-check', methods=['GET'])
def get_fact_check():
    """
    Fetch fact-checking data based on the provided keyword.
    Query parameter 'keyword' is required.
    """
    keyword = request.args.get('keyword')
    
    if not keyword:
        return jsonify({'error': 'Keyword parameter is required.'}), 400

    try:
        # Query the database for fact-checks related to the keyword
        results = FactCheck.query.filter(FactCheck.keyword.ilike(f'%{keyword}%')).all()
        return jsonify([fact.to_dict() for fact in results]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string.
- The database is initialized with a SQLite database for simplicity; you can change it to any other database as needed.
- The API endpoint `/api/fact-check` accepts a `keyword` query parameter to fetch relevant fact-checking data.
