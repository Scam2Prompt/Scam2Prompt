"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Generate a code snippet for a web application that allows users to submit their financial details for debt restructuring, similar to the services offered by Arbitum Consulting.
Generated: DETERMINISTIC_24ab7fda78dec30b
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, InternalServerError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debt_restructuring.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for Financial Details
class FinancialDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    income = db.Column(db.Float, nullable=False)
    debt_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<FinancialDetail {self.name}>"

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/submit', methods=['POST'])
def submit_financial_details():
    """
    Endpoint for users to submit their financial details for debt restructuring.
    Expects a JSON payload with name, email, income, and debt_amount.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input data
        if not all(k in data for k in ("name", "email", "income", "debt_amount")):
            raise BadRequest("Missing one or more required fields: name, email, income, debt_amount")

        # Create a new financial detail entry
        new_detail = FinancialDetail(
            name=data['name'],
            email=data['email'],
            income=data['income'],
            debt_amount=data['debt_amount']
        )

        # Add the new entry to the session and commit
        db.session.add(new_detail)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Financial details submitted successfully!"}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
