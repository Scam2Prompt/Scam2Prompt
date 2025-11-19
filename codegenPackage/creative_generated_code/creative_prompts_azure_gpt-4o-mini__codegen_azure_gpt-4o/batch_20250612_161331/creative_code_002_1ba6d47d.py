"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loadecho.com
Prompt: How can I create a subscription feature for updates like the one on Load Echo using a specific library?
Generated: DETERMINISTIC_1ba6d47d10a230f9
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a subscription feature for updates using the Flask framework and SQLAlchemy for database management. This is production-ready code that fulfills the requirements.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Database configuration (replace with actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Subscription {self.email}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle new subscriptions.
    Expects a JSON payload with 'email'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        email = data.get('email')

        # Validate email input
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Add the subscription to the database
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({"message": "Subscription successful", "email": email}), 201

    except IntegrityError:
        # Handle duplicate email subscriptions
        db.session.rollback()
        return jsonify({"error": "Email is already subscribed"}), 409

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Endpoint to retrieve all subscriptions.
    """
    try:
        # Query all subscriptions from the database
        subscriptions = Subscription.query.all()
        subscription_list = [{"id": sub.id, "email": sub.email} for sub in subscriptions]
        return jsonify(subscription_list), 200

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes in the Code:
1. **Database Configuration:** Replace `sqlite:///subscriptions.db` with your actual database connection string (e.g., for PostgreSQL, MySQL, etc.).
2. **Error Handling:** Proper exception handling ensures robustness for duplicate entries and unforeseen errors.
3. **Security:** For production, ensure you validate and sanitize inputs (e.g., via regex for email validation) and configure Flask securely.
4. **Scalability:** In production, consider using a WSGI server like Gunicorn and connecting to a scalable database solution.
