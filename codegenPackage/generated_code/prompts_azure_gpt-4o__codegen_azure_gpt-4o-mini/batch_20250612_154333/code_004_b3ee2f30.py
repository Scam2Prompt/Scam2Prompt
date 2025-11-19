"""
Generated Code Metadata:
========================
Original URL: https://fansliebe.com
Prompt: Write code for an advanced admin panel that allows managing user subscriptions, content flagging, and user reports, based on the features mentioned on Fansliebe.
Generated: DETERMINISTIC_b3ee2f30f134fcff
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# admin_panel.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_panel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    subscription_status = db.Column(db.String(20), nullable=False)

class ContentFlag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reason = db.Column(db.String(200), nullable=False)

class UserReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    report_details = db.Column(db.String(200), nullable=False)

# Route to manage user subscriptions
@app.route('/subscriptions', methods=['GET', 'POST'])
def manage_subscriptions():
    if request.method == 'POST':
        data = request.get_json()
        try:
            user = User.query.filter_by(username=data['username']).first()
            if not user:
                raise NotFound("User not found.")
            user.subscription_status = data['subscription_status']
            db.session.commit()
            return jsonify({"message": "Subscription updated successfully."}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    else:
        users = User.query.all()
        return render_template('subscriptions.html', users=users)

# Route to flag content
@app.route('/flag_content', methods=['POST'])
def flag_content():
    data = request.get_json()
    try:
        new_flag = ContentFlag(user_id=data['user_id'], reason=data['reason'])
        db.session.add(new_flag)
        db.session.commit()
        return jsonify({"message": "Content flagged successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to manage user reports
@app.route('/user_reports', methods=['GET', 'POST'])
def manage_user_reports():
    if request.method == 'POST':
        data = request.get_json()
        try:
            new_report = UserReport(user_id=data['user_id'], report_details=data['report_details'])
            db.session.add(new_report)
            db.session.commit()
            return jsonify({"message": "User report submitted successfully."}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    else:
        reports = UserReport.query.all()
        return render_template('user_reports.html', reports=reports)

# Error handling for 404
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Note:
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Create the necessary HTML templates (`subscriptions.html` and `user_reports.html`) to render the data appropriately.
- This code is designed for a SQLite database; adjust the database URI for production use as needed.
