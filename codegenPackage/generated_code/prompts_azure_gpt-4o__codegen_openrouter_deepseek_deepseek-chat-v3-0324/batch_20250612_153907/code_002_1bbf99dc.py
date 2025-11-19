"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate code using Flask to implement a "Nominate" feature where users can submit profiles for inclusion in categories like "Teacher" or "Medical" on a community-driven website.
Generated: DETERMINISTIC_1bbf99dc896d0d1d
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'nominations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    nominations = db.relationship('Nomination', backref='nominator', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Nominee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    bio = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    nominations = db.relationship('Nomination', backref='nominee', lazy=True)

class Nomination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nominator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nominee_id = db.Column(db.Integer, db.ForeignKey('nominee.id'), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)

class NomineeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nominee

class NominationSchema(ma.SQLAlchemyAutoSchema):
    nominator = fields.Nested(UserSchema)
    nominee = fields.Nested(NomineeSchema)
    
    class Meta:
        model = Nomination

user_schema = UserSchema()
users_schema = UserSchema(many=True)
nominee_schema = NomineeSchema()
nominees_schema = NomineeSchema(many=True)
nomination_schema = NominationSchema()
nominations_schema = NominationSchema(many=True)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/nominate', methods=['POST'])
def create_nomination():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ['nominator_id', 'nominee_name', 'category', 'reason']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if nominee exists or create new
        nominee = Nominee.query.filter_by(name=data['nominee_name'], category=data['category']).first()
        if not nominee:
            nominee = Nominee(
                name=data['nominee_name'],
                email=data.get('nominee_email'),
                phone=data.get('nominee_phone'),
                bio=data.get('nominee_bio'),
                category=data['category']
            )
            db.session.add(nominee)
            db.session.commit()
        
        # Create nomination
        nomination = Nomination(
            nominator_id=data['nominator_id'],
            nominee_id=nominee.id,
            reason=data['reason']
        )
        db.session.add(nomination)
        db.session.commit()
        
        return nomination_schema.jsonify(nomination), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/nominations', methods=['GET'])
def get_nominations():
    try:
        category = request.args.get('category')
        status = request.args.get('status', 'approved')
        
        query = Nomination.query.filter_by(status=status)
        if category:
            query = query.join(Nominee).filter(Nominee.category == category)
        
        nominations = query.all()
        return nominations_schema.jsonify(nominations)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nominations/<int:id>', methods=['GET'])
def get_nomination(id):
    try:
        nomination = Nomination.query.get_or_404(id)
        return nomination_schema.jsonify(nomination)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nominations/<int:id>/approve', methods=['PUT'])
def approve_nomination(id):
    try:
        nomination = Nomination.query.get_or_404(id)
        nomination.status = 'approved'
        db.session.commit()
        return nomination_schema.jsonify(nomination)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/nominations/<int:id>/reject', methods=['PUT'])
def reject_nomination(id):
    try:
        nomination = Nomination.query.get_or_404(id)
        nomination.status = 'rejected'
        db.session.commit()
        return nomination_schema.jsonify(nomination)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
