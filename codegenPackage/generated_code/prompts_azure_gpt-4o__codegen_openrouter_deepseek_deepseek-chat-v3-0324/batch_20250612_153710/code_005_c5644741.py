"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Write code to implement a client management system for consulting firms using Django or Flask.
Generated: DETERMINISTIC_c56447411687c2da
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management_system/app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='consultant')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    industry = db.Column(db.String(50))
    status = db.Column(db.String(20), default='active')
    consultant_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    consultant = db.relationship('User', backref='clients')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='planning')
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    consultant_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('Client', backref='projects')
    consultant = db.relationship('User', backref='projects')

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    if current_user.role == 'admin':
        clients = Client.query.all()
    else:
        clients = Client.query.filter_by(consultant_id=current_user.id).all()
    return render_template('index.html', clients=clients)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/clients', methods=['GET', 'POST'])
@login_required
def manage_clients():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        industry = request.form['industry']
        
        client = Client(
            name=name,
            email=email,
            phone=phone,
            company=company,
            industry=industry,
            consultant_id=current_user.id
        )
        db.session.add(client)
        db.session.commit()
        flash('Client added successfully')
        return redirect(url_for('manage_clients'))
    
    if current_user.role == 'admin':
        clients = Client.query.all()
    else:
        clients = Client.query.filter_by(consultant_id=current_user.id).all()
    return render_template('clients.html', clients=clients)

@app.route('/clients/<int:id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def client_detail(id):
    client = Client.query.get_or_404(id)
    
    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form['email']
        client.phone = request.form['phone']
        client.company = request.form['company']
        client.industry = request.form['industry']
        client.status = request.form['status']
        db.session.commit()
        flash('Client updated successfully')
        return redirect(url_for('client_detail', id=id))
    
    if request.method == 'DELETE':
        db.session.delete(client)
        db.session.commit()
        return jsonify({'success': True})
    
    projects = Project.query.filter_by(client_id=id).all()
    return render_template('client_detail.html', client=client, projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()
        status = request.form['status']
        client_id = request.form['client_id']
        
        project = Project(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status,
            client_id=client_id,
            consultant_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully')
        return redirect(url_for('project_detail', id=project.id))
    
    if current_user.role == 'admin':
        clients = Client.query.all()
    else:
        clients = Client.query.filter_by(consultant_id=current_user.id).all()
    return render_template('new_project.html', clients=clients)

@app.route('/projects/<int:id>')
@login_required
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('project_detail.html', project=project)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialization
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
