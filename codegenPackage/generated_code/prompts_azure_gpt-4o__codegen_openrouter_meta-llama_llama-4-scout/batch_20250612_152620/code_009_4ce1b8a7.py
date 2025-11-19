"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Suggest a cloud-based solution for managing large-scale events with up to 5,000 participants, inspired by DCITY Events' capacity and technological infrastructure.
Generated: DETERMINISTIC_4ce1b8a780e19082
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Event Management System**
==========================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* AWS SDK for Python (Boto3) 1.26+

### Code

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import boto3
from botocore.exceptions import ClientError
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

# Initialize AWS services
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

class Event(db.Model):
    """Event model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Event('{self.name}', '{self.date}', {self.capacity})"

class Participant(db.Model):
    """Participant model"""
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Participant('{self.name}', '{self.email}')"

@app.route("/events", methods=["POST"])
def create_event():
    """Create a new event"""
    try:
        data = request.get_json()
        event = Event(name=data["name"], date=data["date"], capacity=data["capacity"])
        db.session.add(event)
        db.session.commit()
        return jsonify({"message": "Event created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

@app.route("/events/<int:event_id>/participants", methods=["POST"])
def add_participant(event_id):
    """Add a participant to an event"""
    try:
        event = Event.query.get(event_id)
        if event is None:
            return jsonify({"message": "Event not found"}), 404
        if event.capacity <= len(event.participants):
            return jsonify({"message": "Event is fully booked"}), 400
        data = request.get_json()
        participant = Participant(event_id=event_id, name=data["name"], email=data["email"])
        db.session.add(participant)
        db.session.commit()
        return jsonify({"message": "Participant added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

@app.route("/events/<int:event_id>/participants", methods=["GET"])
def get_participants(event_id):
    """Get all participants for an event"""
    try:
        event = Event.query.get(event_id)
        if event is None:
            return jsonify({"message": "Event not found"}), 404
        participants = Participant.query.filter_by(event_id=event_id).all()
        return jsonify([{"name": p.name, "email": p.email} for p in participants]), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """Delete an event"""
    try:
        event = Event.query.get(event_id)
        if event is None:
            return jsonify({"message": "Event not found"}), 404
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# requirements.txt

Flask==2.0.3
Flask-SQLAlchemy==2.5.1
boto3==1.26.27
```

```python
# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
```

```yml
# docker-compose.yml

version: "3"
services:
  app:
    build: .
    environment:
      - DATABASE_URL=sqlite:///events.db
    ports:
      - "5000:5000"
    depends_on:
      - db
    restart: always

  db:
    image: postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=events
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

```bash
# deploy.sh

#!/bin/bash

# Build and deploy to AWS Elastic Beanstalk
eb init -p python-3.9 events-app
eb create events-env
eb deploy
```
