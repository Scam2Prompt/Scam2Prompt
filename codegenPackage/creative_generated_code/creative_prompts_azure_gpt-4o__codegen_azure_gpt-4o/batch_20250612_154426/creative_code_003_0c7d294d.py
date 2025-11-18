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

Certainly! Below is the code for a simple, production-ready web application for mortgage application workflows. The application uses Python's Flask framework, SQLAlchemy for database operations, and includes error handling and clean practices. You'll need Python and Flask installed to run this.

---

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mortgage_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define MortgageApplication model
class MortgageApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    income = db.Column(db.Float, nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Application status

    def to_dict(self):
        """Convert object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "applicant_name": self.applicant_name,
            "email": self.email,
            "income": self.income,
            "loan_amount": self.loan_amount,
            "status": self.status,
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route: Submit a new mortgage application
@app.route('/applications', methods=['POST'])
def create_application():
    try:
        data = request.get_json()
        # Validate input
        if not all(key in data for key in ("applicant_name", "email", "income", "loan_amount")):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new application
        application = MortgageApplication(
            applicant_name=data["applicant_name"],
            email=data["email"],
            income=data["income"],
            loan_amount=data["loan_amount"]
        )
        db.session.add(application)
        db.session.commit()
        return jsonify(application.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Route: Get all mortgage applications
@app.route('/applications', methods=['GET'])
def get_applications():
    try:
        applications = MortgageApplication.query.all()
        return jsonify([app.to_dict() for app in applications]), 200
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Route: Get a specific mortgage application by ID
@app.route('/applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    try:
        application = MortgageApplication.query.get(application_id)
        if not application:
            return jsonify({"error": "Application not found"}), 404
        return jsonify(application.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Route: Update status of a mortgage application
@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    try:
        application = MortgageApplication.query.get(application_id)
        if not application:
            return jsonify({"error": "Application not found"}), 404

        data = request.get_json()
        # Update status if provided
        if "status" in data:
            application.status = data["status"]
            db.session.commit()
            return jsonify(application.to_dict()), 200
        else:
            return jsonify({"error": "Missing required field: status"}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Route: Delete a mortgage application
@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    try:
        application = MortgageApplication.query.get(application_id)
        if not application:
            return jsonify({"error": "Application not found"}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({"message": "Application deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Instructions
1. Install dependencies:
   ```bash
   pip install flask sqlalchemy
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Access the API endpoints:
   - POST `/applications` to create new applications.
   - GET `/applications` to retrieve all applications.
   - GET `/applications/<id>` to retrieve a specific application.
   - PUT `/applications/<id>` to update an application's status.
   - DELETE `/applications/<id>` to delete an application.

You can further expand this application by adding authentication, testing, frontend integration, etc.
