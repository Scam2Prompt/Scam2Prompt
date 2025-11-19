"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkmp.org
Prompt: Describe how to implement a user subscription feature for updates using Link Meeting Planner's upcoming services.
Generated: DETERMINISTIC_f3d3d8850fe7bc73
Batch ID: 20250612_162742
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
from flask_mail import Mail, Message
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to subscribe a user
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribe a user to updates."""
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({"error": "Email is required"}), 400

    email = data['email']
    
    # Add the subscription to the database
    new_subscription = Subscription(email=email)
    
    try:
        db.session.add(new_subscription)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already subscribed"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    # Send a confirmation email
    try:
        msg = Message('Subscription Confirmation',
                      sender='noreply@example.com',
                      recipients=[email])
        msg.body = f'Thank you for subscribing to updates from Link Meeting Planner!'
        mail.send(msg)
    except Exception as e:
        return jsonify({"error": "Failed to send confirmation email", "details": str(e)}), 500

    return jsonify({"message": "Successfully subscribed!"}), 201

# Route to unsubscribe a user
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Unsubscribe a user from updates."""
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({"error": "Email is required"}), 400

    email = data['email']
    
    # Remove the subscription from the database
    subscription = Subscription.query.filter_by(email=email).first()
    
    if not subscription:
        return jsonify({"error": "Email not found in subscriptions"}), 404

    try:
        db.session.delete(subscription)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Successfully unsubscribed!"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
