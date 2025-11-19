"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: "Design a Web3 startup competition platform using a suitable programming language and framework, incorporating AI-driven insights and evaluation tools like Pitch Scan LLM."
Generated: DETERMINISTIC_f955c19e076b6903
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Web3 Startup Competition Platform with AI Evaluation

```python
# web3_competition_platform/app.py
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os
from dotenv import load_dotenv
import openai
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Initialize database
db = SQLAlchemy(app)

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Models
class Competition(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    prize_pool = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    submissions = db.relationship('Submission', backref='competition', lazy=True)

class Submission(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    competition_id = db.Column(db.String(36), db.ForeignKey('competition.id'), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pitch_deck_url = db.Column(db.String(255))
    wallet_address = db.Column(db.String(42), nullable=False)  # Ethereum address
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    evaluations = db.relationship('Evaluation', backref='submission', lazy=True)

class Evaluation(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    submission_id = db.Column(db.String(36), db.ForeignKey('submission.id'), nullable=False)
    ai_score = db.Column(db.Float)
    ai_feedback = db.Column(db.Text)
    evaluator_address = db.Column(db.String(42))  # Evaluator's wallet address
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Helper Functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'ppt', 'pptx'}

def analyze_pitch_with_ai(pitch_text):
    """Use OpenAI to analyze the pitch and provide feedback"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a startup investment expert analyzing pitch decks. Provide detailed feedback on the business model, market potential, team, and technology. Rate the pitch from 1-10."},
                {"role": "user", "content": pitch_text}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        app.logger.error(f"AI analysis failed: {str(e)}")
        return None

def calculate_ai_score(feedback):
    """Extract numerical score from AI feedback"""
    try:
        # Simple implementation - in production you'd want more sophisticated parsing
        if "10/" in feedback or "10 /" in feedback:
            return 10.0
        elif "9/" in feedback or "9 /" in feedback:
            return 9.0
        # Continue for other scores...
        else:
            return 7.0  # Default score if parsing fails
    except Exception as e:
        app.logger.error(f"Score calculation failed: {str(e)}")
        return 5.0  # Minimum score if error occurs

# Routes
@app.route('/')
def index():
    competitions = Competition.query.filter(Competition.end_date >= datetime.utcnow()).all()
    return render_template('index.html', competitions=competitions)

@app.route('/competition/<competition_id>')
def competition_detail(competition_id):
    competition = Competition.query.get_or_404(competition_id)
    submissions = Submission.query.filter_by(competition_id=competition_id).all()
    return render_template('competition.html', competition=competition, submissions=submissions)

@app.route('/api/competitions', methods=['POST'])
def create_competition():
    try:
        data = request.get_json()
        new_competition = Competition(
            title=data['title'],
            description=data['description'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            prize_pool=data['prize_pool']
        )
        db.session.add(new_competition)
        db.session.commit()
        return jsonify({"message": "Competition created", "id": new_competition.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/submit', methods=['POST'])
def submit_project():
    try:
        # Validate wallet address
        wallet_address = request.form['wallet_address']
        if not w3.is_address(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400

        # Handle file upload
        if 'pitch_deck' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
            
        file = request.files['pitch_deck']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
        else:
            return jsonify({"error": "Invalid file type"}), 400

        # Create submission
        new_submission = Submission(
            competition_id=request.form['competition_id'],
            project_name=request.form['project_name'],
            description=request.form['description'],
            pitch_deck_url=unique_filename,
            wallet_address=wallet_address
        )
        db.session.add(new_submission)
        db.session.commit()

        # Trigger AI evaluation
        ai_feedback = analyze_pitch_with_ai(request.form['description'])
        ai_score = calculate_ai_score(ai_feedback) if ai_feedback else None

        if ai_feedback and ai_score:
            evaluation = Evaluation(
                submission_id=new_submission.id,
                ai_score=ai_score,
                ai_feedback=ai_feedback
            )
            db.session.add(evaluation)
            db.session.commit()

        return jsonify({
            "message": "Submission successful",
            "submission_id": new_submission.id,
            "ai_evaluation": bool(ai_feedback)
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/evaluate/<submission_id>', methods=['POST'])
def evaluate_submission(submission_id):
    try:
        submission = Submission.query.get_or_404(submission_id)
        evaluator_address = request.json.get('evaluator_address')
        
        if evaluator_address and not w3.is_address(evaluator_address):
            return jsonify({"error": "Invalid evaluator address"}), 400

        # Get existing evaluation or create new one
        evaluation = Evaluation.query.filter_by(submission_id=submission_id).first()
        if not evaluation:
            evaluation = Evaluation(submission_id=submission_id)

        # Update evaluation
        if 'ai_score' in request.json:
            evaluation.ai_score = request.json['ai_score']
        if 'ai_feedback' in request.json:
            evaluation.ai_feedback = request.json['ai_feedback']
        if evaluator_address:
            evaluation.evaluator_address = evaluator_address

        db.session.add(evaluation)
        db.session.commit()

        return jsonify({"message": "Evaluation updated", "evaluation_id": evaluation.id}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/submissions/<submission_id>')
def get_submission(submission_id):
    submission = Submission.query.get_or_404(submission_id)
    evaluations = Evaluation.query.filter_by(submission_id=submission_id).all()
    
    return jsonify({
        "submission":
