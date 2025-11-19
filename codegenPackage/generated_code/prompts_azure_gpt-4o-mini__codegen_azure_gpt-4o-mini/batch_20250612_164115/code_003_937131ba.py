"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Develop a REST API endpoint that allows users to submit their architectural plans for a cabinetry quote, integrating with United Cabinetry's existing systems.
Generated: DETERMINISTIC_937131bab7f4af2b
Batch ID: 20250612_164115
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
from werkzeug.exceptions import BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cabinetry.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for storing cabinetry quotes
class CabinetryQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    architectural_plan = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<CabinetryQuote {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/quotes', methods=['POST'])
def submit_quote():
    """
    Endpoint to submit architectural plans for cabinetry quotes.
    Expects a JSON payload with user_email and architectural_plan.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()

        # Validate the input data
        if not data or 'user_email' not in data or 'architectural_plan' not in data:
            raise BadRequest("Invalid input: 'user_email' and 'architectural_plan' are required.")

        user_email = data['user_email']
        architectural_plan = data['architectural_plan']

        # Create a new cabinetry quote entry
        new_quote = CabinetryQuote(user_email=user_email, architectural_plan=architectural_plan)
        db.session.add(new_quote)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Quote submitted successfully.", "quote_id": new_quote.id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
