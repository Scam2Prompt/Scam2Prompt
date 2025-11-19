"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Suggest libraries or frameworks for building a one-stop shop platform for personal, family, and business solutions, including features for client management, tax preparation, and accounting.
Generated: DETERMINISTIC_ca7e83b8ba0d242e
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Core backend framework
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Database and ORM
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# Authentication and security
import bcrypt
import jwt
from datetime import datetime, timedelta

# Financial calculations
import decimal
from decimal import Decimal

# PDF generation for reports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Excel handling
import openpyxl
from openpyxl import Workbook

# Email functionality
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Date/time handling
from datetime import datetime, date

# API clients
import requests

# Environment variables
import os
from dotenv import load_dotenv

# Logging
import logging
from logging.handlers import RotatingFileHandler

# Testing
import pytest
from unittest.mock import patch

# Frontend frameworks (for reference)
"""
Frontend options:
- React.js with Material-UI or Ant Design
- Vue.js with Vuetify or Element UI
- Angular with Angular Material
"""

# Initialize Flask application
app = Flask(__name__)
load_dotenv()

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False)  # 'admin', 'client', 'accountant'
    created_at = Column(DateTime, default=datetime.utcnow)
    clients = relationship('Client', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class Client(db.Model):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    tax_id = Column(String(50))
    business_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    documents = relationship('Document', backref='client', lazy=True)
    transactions = relationship('Transaction', backref='client', lazy=True)

class Document(db.Model):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    name = Column(String(100), nullable=False)
    file_path = Column(String(200), nullable=False)
    document_type = Column(String(50), nullable=False)  # 'tax', 'invoice', 'contract'
    uploaded_at = Column(DateTime, default=datetime.utcnow)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    amount = Column(sqlalchemy.Numeric(10, 2), nullable=False)
    description = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)  # 'income', 'expense', 'tax'
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Utility functions
def generate_pdf_report(client_id, output_path):
    client = Client.query.get(client_id)
    if not client:
        raise ValueError("Client not found")
    
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # PDF generation logic
    c.drawString(100, height - 100, f"Financial Report for {client.name}")
    # Add more content as needed
    
    c.save()

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_FROM')
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
        server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
        server.send_message(msg)

# API Routes
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    user = User(
        email=data['email'],
        first_name=data.get('first_name', ''),
        last_name=data.get('last_name', ''),
        role=data.get('role', 'client')
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    access_token = jwt.create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/api/clients', methods=['GET'])
@jwt_required()
def get_clients():
    current_user = get_jwt_identity()
    clients = Client.query.filter_by(user_id=current_user).all()
    return jsonify([{
        'id': client.id,
        'name': client.name,
        'email': client.email,
        'phone': client.phone
    } for client in clients]), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Configure logging
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
