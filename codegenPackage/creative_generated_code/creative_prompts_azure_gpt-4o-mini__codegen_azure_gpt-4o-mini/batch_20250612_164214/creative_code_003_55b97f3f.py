"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Develop an API endpoint that retrieves the list of beneficiaries under the integrated stipend program mentioned on the Govt. Shah Sultan College website.
Generated: DETERMINISTIC_55b97f3feca30b55
Batch ID: 20250612_164214
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

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beneficiaries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Beneficiary model
class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    program = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'program': self.program
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/beneficiaries', methods=['GET'])
def get_beneficiaries():
    """
    Retrieve the list of beneficiaries under the integrated stipend program.
    
    Returns:
        JSON response containing a list of beneficiaries or an error message.
    """
    try:
        # Query all beneficiaries from the database
        beneficiaries = Beneficiary.query.all()
        # Convert the result to a list of dictionaries
        beneficiaries_list = [beneficiary.to_dict() for beneficiary in beneficiaries]
        return jsonify(beneficiaries_list), 200
    except SQLAlchemyError as e:
        # Handle any SQLAlchemy errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
