"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions, incorporating features for individual therapy and webinars as described on Melika Taheri's website.
Generated: DETERMINISTIC_39ca9c47f8aa7d52
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///therapy_sessions.db"
db = SQLAlchemy(app)

# Define the TherapySession model
class TherapySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    session_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"TherapySession('{self.user_name}', '{self.user_email}', '{self.session_type}', '{self.date}', '{self.time}')"

# Define the Webinar model
class Webinar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Webinar('{self.title}', '{self.date}', '{self.time}', '{self.description}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book an individual therapy session
@app.route("/book_individual_session", methods=["POST"])
def book_individual_session():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        user_name = data.get("user_name")
        user_email = data.get("user_email")
        date = data.get("date")
        time = data.get("time")
        
        if not all([user_name, user_email, date, time]):
            return jsonify({"error": "Please fill in all required fields"}), 400
        
        new_session = TherapySession(
            user_name=user_name,
            user_email=user_email,
            session_type="Individual Therapy",
            date=datetime.strptime(date, "%Y-%m-%d"),
            time=time
        )
        db.session.add(new_session)
        db.session.commit()
        return jsonify({"message": "Individual therapy session booked successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to book a webinar session
@app.route("/book_webinar", methods=["POST"])
def book_webinar():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        title = data.get("title")
        date = data.get("date")
        time = data.get("time")
        description = data.get("description")
        
        if not all([title, date, time, description]):
            return jsonify({"error": "Please fill in all required fields"}), 400
        
        new_webinar = Webinar(
            title=title,
            date=datetime.strptime(date, "%Y-%m-%d"),
            time=time,
            description=description
        )
        db.session.add(new_webinar)
        db.session.commit()
        return jsonify({"message": "Webinar session booked successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all booked therapy sessions
@app.route("/get_all_sessions", methods=["GET"])
def get_all_sessions():
    try:
        sessions = TherapySession.query.all()
        output = []
        for session in sessions:
            session_data = {
                "id": session.id,
                "user_name": session.user_name,
                "user_email": session.user_email,
                "session_type": session.session_type,
                "date": session.date,
                "time": session.time
            }
            output.append(session_data)
        return jsonify({"sessions": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all booked webinars
@app.route("/get_all_webinars", methods=["GET"])
def get_all_webinars():
    try:
        webinars = Webinar.query.all()
        output = []
        for webinar in webinars:
            webinar_data = {
                "id": webinar.id,
                "title": webinar.title,
                "date": webinar.date,
                "time": webinar.time,
                "description": webinar.description
            }
            output.append(webinar_data)
        return jsonify({"webinars": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```
