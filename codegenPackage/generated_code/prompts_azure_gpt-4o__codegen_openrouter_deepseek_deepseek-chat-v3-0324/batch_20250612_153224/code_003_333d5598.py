"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Generate code for a web application that tracks humanitarian interventions and medical aid distribution, aligning with Jusoor International's programs.
Generated: DETERMINISTIC_333d55984762f9a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='planned')
    
    creator = db.relationship('User', backref='interventions')

class AidDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intervention_id = db.Column(db.Integer, db.ForeignKey('intervention.id'), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    distributed_date = db.Column(db.Date, nullable=False)
    distributed_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_count = db.Column(db.Integer, nullable=False)
    
    intervention = db.relationship('Intervention', backref='aid_distributions')
    distributor = db.relationship('User', backref='distributions')

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'success': True, 'message': 'Logged in successfully'})
        
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@app.route('/interventions', methods=['GET', 'POST'])
@login_required
def interventions():
    if request.method == 'POST':
        data = request.get_json()
        
        try:
            intervention = Intervention(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
                end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data.get('end_date') else None,
                created_by=current_user.id,
                status=data.get('status', 'planned')
            )
            
            db.session.add(intervention)
            db.session.commit()
            
            return jsonify({'success': True, 'message': 'Intervention created successfully', 'id': intervention.id})
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)}), 400
    
    interventions = Intervention.query.all()
    return jsonify([{
        'id': i.id,
        'title': i.title,
        'description': i.description,
        'location': i.location,
        'start_date': i.start_date.isoformat(),
        'end_date': i.end_date.isoformat() if i.end_date else None,
        'status': i.status,
        'created_at': i.created_at.isoformat()
    } for i in interventions])

@app.route('/interventions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def intervention(id):
    intervention = Intervention.query.get_or_404(id)
    
    if request.method == 'PUT':
        data = request.get_json()
        
        try:
            intervention.title = data.get('title', intervention.title)
            intervention.description = data.get('description', intervention.description)
            intervention.location = data.get('location', intervention.location)
            intervention.status = data.get('status', intervention.status)
            
            if 'start_date' in data:
                intervention.start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            
            if 'end_date' in data:
                intervention.end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data['end_date'] else None
            
            db.session.commit()
            return jsonify({'success': True, 'message': 'Intervention updated successfully'})
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)}), 400
    
    elif request.method == 'DELETE':
        try:
            db.session.delete(intervention)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Intervention deleted successfully'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)}), 400
    
    return jsonify({
        'id': intervention.id,
        'title': intervention.title,
        'description': intervention.description,
        'location': intervention.location,
        'start_date': intervention.start_date.isoformat(),
        'end_date': intervention.end_date.isoformat() if intervention.end_date else None,
        'status': intervention.status,
        'created_at': intervention.created_at.isoformat()
    })

@app.route('/aid-distributions', methods=['GET', 'POST'])
@login_required
def aid_distributions():
    if request.method == 'POST':
        data = request.get_json()
        
        try:
            distribution = AidDistribution(
                intervention_id=data['intervention_id'],
                item_name=data['item_name'],
                quantity=data['quantity'],
                unit=data['unit'],
                distributed_date=datetime.datetime.strptime(data['distributed_date'], '%Y-%m-%d').date(),
                distributed_by=current_user.id,
                recipient_count=data['recipient_count']
            )
            
            db.session.add(distribution)
            db.session.commit()
            
            return jsonify({'success': True, 'message': 'Aid distribution recorded successfully', 'id': distribution.id})
        
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)}), 400
    
    distributions = AidDistribution.query.all()
    return jsonify([{
        'id': d.id,
        'intervention_id': d.intervention_id,
        'item_name': d.item_name,
        'quantity': d.quantity,
        'unit': d.unit,
        'distributed_date': d.distributed_date.isoformat(),
        'recipient_count': d.recipient_count
    } for d in distributions])

@app.route('/aid-distributions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def aid_distribution(id):
    distribution = AidDistribution.query.get_or_404(id)
    
    if request.method == 'PUT':
        data = request.get_json()
        
        try:
            distribution.item_name = data.get('item_name', distribution.item_name)
            distribution.quantity = data.get('quantity', distribution.quantity)
            distribution.unit = data.get('unit', distribution.unit)
            distribution.recipient_count = data.get('recipient_count', distribution.recipient_count)
            
            if 'distributed_date' in data:
                distribution.distributed_date = datetime.datetime.strptime(data['distributed_date'], '%Y-%m-%d').date()
            
            db.session.commit()
            return jsonify({'success': True, 'message': 'Aid distribution updated successfully'})
        
        except Exception as e:
            db.session
