"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Write Python code to create a fitness consultancy app that allows users to select a training plan, fill out an anamnese (health questionnaire), and receive personalized workout plans via an exclusive app. Include support for WhatsApp integration for user communication.
Generated: DETERMINISTIC_ff14d64d2cc3e677
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
import logging
from twilio.rest import Client
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///fitness.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.environ.get('TWILIO_WHATSAPP_NUMBER')
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN else None

# Enums
class TrainingLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

class GoalType(Enum):
    WEIGHT_LOSS = "Weight Loss"
    MUSCLE_GAIN = "Muscle Gain"
    ENDURANCE = "Endurance"
    GENERAL_FITNESS = "General Fitness"

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    anamnese = db.relationship('Anamnese', backref='user', uselist=False)
    training_plans = db.relationship('TrainingPlan', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Anamnese(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    medical_conditions = db.Column(db.Text)
    medications = db.Column(db.Text)
    injuries = db.Column(db.Text)
    training_level = db.Column(db.Enum(TrainingLevel))
    goal = db.Column(db.Enum(GoalType))
    notes = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    exercises = db.Column(db.Text)  # JSON string of exercises
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

# Helper Functions
def send_whatsapp_message(to: str, body: str) -> bool:
    if not twilio_client:
        logger.warning("Twilio credentials not configured. WhatsApp messages will not be sent.")
        return False
    
    try:
        message = twilio_client.messages.create(
            body=body,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{to}'
        )
        logger.info(f"WhatsApp message sent to {to}: {message.sid}")
        return True
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {str(e)}")
        return False

def generate_workout_plan(anamnese: Anamnese) -> Dict:
    """Generate a personalized workout plan based on user's anamnese."""
    level = anamnese.training_level.value.lower()
    goal = anamnese.goal.value.lower().replace(" ", "_")
    
    # This is a simplified example - in production you'd have more complex logic
    plans = {
        "beginner": {
            "weight_loss": {
                "name": "Beginner Weight Loss Plan",
                "description": "A gentle introduction to fitness focusing on fat loss",
                "exercises": [
                    {"name": "Walking", "duration": "30 mins", "frequency": "5x/week"},
                    {"name": "Bodyweight Squats", "sets": 3, "reps": 12},
                    {"name": "Push-ups (knees)", "sets": 3, "reps": 10}
                ]
            },
            "muscle_gain": {
                "name": "Beginner Muscle Building Plan",
                "description": "Basic strength training for new lifters",
                "exercises": [
                    {"name": "Bodyweight Squats", "sets": 3, "reps": 10},
                    {"name": "Push-ups", "sets": 3, "reps": 8},
                    {"name": "Plank", "duration": "30 sec", "sets": 3}
                ]
            }
        },
        "intermediate": {
            "weight_loss": {
                "name": "Intermediate Weight Loss Plan",
                "description": "Higher intensity workouts for fat burning",
                "exercises": [
                    {"name": "Running", "duration": "30 mins", "frequency": "4x/week"},
                    {"name": "Circuit Training", "duration": "45 mins", "frequency": "3x/week"}
                ]
            }
        }
    }
    
    try:
        return plans[level][goal]
    except KeyError:
        # Default plan if specific combination not found
        return {
            "name": "General Fitness Plan",
            "description": "A balanced workout routine",
            "exercises": [
                {"name": "Cardio", "duration": "30 mins", "frequency": "3x/week"},
                {"name": "Strength Training", "duration": "45 mins", "frequency": "2x/week"}
            ]
        }

# Error Handlers
@app.errorhandler(HTTPException)
def handle_http_error(e):
    logger.error(f"HTTP error: {e.code} - {e.name}")
    return jsonify({
        "error": e.name,
        "message": e.description,
        "status": e.code
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unexpected error: {str(e)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "status": 500
    }), 500

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            name = request.form['name']
            
            if User.query.filter_by(email=email).first():
                return render_template('register.html', error="Email already registered")
            
            user = User(email=email, name=name)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            logger.error(f"Registration error: {str(e)}")
            return render_template('register.html', error="Registration failed")
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return render_template('login.html', error="Invalid credentials")
        
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    anamnese = Anamnese.query.filter_by(user_id=user.id).first()
    plans = TrainingPlan.query.filter_by(user_id=user.id,
