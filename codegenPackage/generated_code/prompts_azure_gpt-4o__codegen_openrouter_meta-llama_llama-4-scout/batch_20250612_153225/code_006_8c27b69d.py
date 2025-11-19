"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Recommend tools or libraries for implementing video consultations for nutritionists, similar to the "Video Reception 'Top 5'" service offered by Olga Stepanova.
Generated: DETERMINISTIC_8c27b69dee2a9413
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Video Consultation Platform for Nutritionists**
=====================================================

### Dependencies

* `flask` for the web application
* `twilio` for video conferencing
* `sqlalchemy` for database operations
* `python-dotenv` for environment variable management

### Installation

```bash
pip install flask twilio sqlalchemy python-dotenv
```

### Code

```python
# app.py

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.video import Room, Participant
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Twilio client
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_client = Client(twilio_account_sid, twilio_auth_token)

# Initialize database
engine = create_engine(os.getenv('DATABASE_URL'))
Base = declarative_base()

class Nutritionist(Base):
    __tablename__ = 'nutritionists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new room for video consultation
@app.route('/create-room', methods=['POST'])
def create_room():
    try:
        nutritionist_id = request.json['nutritionist_id']
        patient_id = request.json['patient_id']
        room_name = f"consultation-{nutritionist_id}-{patient_id}"

        # Create a new room
        room = twilio_client.video.rooms.create(
            unique_name=room_name,
            type='video'
        )

        # Create a new video consultation record
        consultation = VideoConsultation(
            nutritionist_id=nutritionist_id,
            patient_id=patient_id,
            room_sid=room.sid
        )
        session.add(consultation)
        session.commit()

        return jsonify({'room_url': room.url}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Join a video consultation room
@app.route('/join-room', methods=['POST'])
def join_room():
    try:
        room_sid = request.json['room_sid']
        participant_name = request.json['participant_name']

        # Get the room
        room = twilio_client.video.rooms(room_sid).fetch()

        # Create a new participant
        participant = room.participants.create(
            name=participant_name
        )

        return jsonify({'participant_sid': participant.sid}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# End a video consultation
@app.route('/end-consultation', methods=['POST'])
def end_consultation():
    try:
        room_sid = request.json['room_sid']

        # Get the room
        room = twilio_client.video.rooms(room_sid).fetch()

        # End the room
        room.status = 'completed'
        room.update()

        # Update the video consultation record
        consultation = session.query(VideoConsultation).filter_by(room_sid=room_sid).first()
        consultation.status = 'completed'
        session.commit()

        return jsonify({'message': 'Consultation ended'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VideoConsultation(Base):
    __tablename__ = 'video_consultations'
    id = Column(Integer, primary_key=True)
    nutritionist_id = Column(Integer)
    patient_id = Column(Integer)
    room_sid = Column(String)
    status = Column(String, default='pending')
```

```python
# .env

TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
DATABASE_URL=your_database_url
```

### API Endpoints

* `POST /create-room`: Create a new room for video consultation
	+ Request Body: `nutritionist_id`, `patient_id`
	+ Response: `room_url`
* `POST /join-room`: Join a video consultation room
	+ Request Body: `room_sid`, `participant_name`
	+ Response: `participant_sid`
* `POST /end-consultation`: End a video consultation
	+ Request Body: `room_sid`
	+ Response: `message`
