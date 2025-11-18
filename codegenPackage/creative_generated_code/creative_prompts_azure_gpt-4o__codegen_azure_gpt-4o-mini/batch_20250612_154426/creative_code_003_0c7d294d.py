"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Develop a web application that integrates mortgage application workflows, inspired by Genesis Investment Credit Union's mortgage services.
Generated: DETERMINISTIC_0c7d294d86a7b12f
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mortgages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the Mortgage application model
class MortgageApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    income = db.Column(db.Float, nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Define schema for input validation
class MortgageApplicationSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    income = fields.Float(required=True, validate=validate.Range(min=0))
    loan_amount = fields.Float(required=True, validate=validate.Range(min=0))

# Initialize schema instance
application_schema = MortgageApplicationSchema()

@app.route('/')
def index():
    """Render the index page for the mortgage application."""
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    """Handle a new mortgage application."""
    try:
        # Validate input data
        data = request.get_json()
        application_schema.load(data)

        # Create a new mortgage application
        application = MortgageApplication(
            name=data['name'],
            email=data['email'],
            income=data['income'],
            loan_amount=data['loan_amount']
        )
        
        db.session.add(application)
        db.session.commit()

        return jsonify({'message': 'Application submitted successfully!', 'id': application.id}), 201
    
    except ValidationError as err:
        # Handle validation errors
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

@app.route('/applications', methods=['GET'])
def list_applications():
    """Retrieve and list all mortgage applications."""
    applications = MortgageApplication.query.all()
    result = [{'id': app.id, 'name': app.name, 'email': app.email, 'income': app.income, 
               'loan_amount': app.loan_amount, 'status': app.status} for app in applications]
    return jsonify(result), 200

# Create the database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mortgage Application</title>
</head>
<body>
    <h1>Mortgage Application Form</h1>
    <form id="mortgageForm">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="number" name="income" placeholder="Your Income" required>
        <input type="number" name="loan_amount" placeholder="Desired Loan Amount" required>
        <button type="submit">Submit Application</button>
    </form>
    <div id="response"></div>
    <script>
        document.getElementById('mortgageForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());
            const responseDiv = document.getElementById('response');

            try {
                const response = await fetch('/apply', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                responseDiv.textContent = result.message || result.errors;
            } catch (error) {
                responseDiv.textContent = 'An error occurred. Please try again later.';
            }
        });
    </script>
</body>
</html>
```

### Note:
- This code includes a simple Flask web application for mortgage applications.
- The application includes a model for mortgage applications, input validation with Marshmallow, and basic routes for applying and listing applications.
- The HTML form allows users to submit their applications using the frontend script. 
- Make sure to run this in an environment with Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow installed.
