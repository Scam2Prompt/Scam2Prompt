"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Provide a step-by-step guide to creating a cloud-based platform for educational institutions, similar to the "CloudCampus" platform described on the Del Sol Montessori website.
Generated: DETERMINISTIC_0bb8399b7ca312f9
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CloudCampus Platform - Backend Service
# This is a Flask-based backend for an educational cloud platform

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "cloudcampus.db")}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Configure logging
handler = RotatingFileHandler('cloudcampus.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # student, teacher, admin
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    domain = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref='institution', lazy=True)
    courses = db.relationship('Course', backref='institution', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)
    materials = db.relationship('Material', backref='course', lazy=True)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, server_default=db.func.now())
    role = db.Column(db.String(20), nullable=False)  # student, teacher, ta

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, server_default=db.func.now())
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Marshmallow Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)

class InstitutionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Institution

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Institution

class MaterialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Material

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
institution_schema = InstitutionSchema()
institutions_schema = InstitutionSchema(many=True)
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
material_schema = MaterialSchema()
materials_schema = MaterialSchema(many=True)

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# API Routes
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ['username', 'email', 'password', 'role', 'institution_id']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists'}), 400
            
        new_user = User(
            username=data['username'],
            email=data['email'],
            role=data['role'],
            institution_id=data['institution_id']
        )
        new_user.set_password(data['password'])
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        app.logger.error(f'Registration error: {str(e)}')
        return jsonify({'error': 'Registration failed'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ['username', 'password']):
            return jsonify({'error': 'Missing username or password'}), 400
        
        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        app.logger.error(f'Login error: {str(e)}')
        return jsonify({'error': 'Login failed'}), 500

@app.route('/api/institutions', methods=['GET'])
@jwt_required()
def get_institutions():
    try:
        institutions = Institution.query.all()
        return institutions_schema.jsonify(institutions), 200
    except Exception as e:
        app.logger.error(f'Get institutions error: {str(e)}')
        return jsonify({'error': 'Failed to retrieve institutions'}), 500

@app.route('/api/courses', methods=['GET'])
@jwt_required()
def get_courses():
    try:
        institution_id = request.args.get('institution_id')
        if institution_id:
            courses = Course.query.filter_by(institution_id=institution_id).all()
        else:
            courses = Course.query.all()
        return courses_schema.jsonify(courses), 200
    except Exception as e:
        app.logger.error(f'Get courses error: {str(e)}')
        return jsonify({'error': 'Failed to retrieve courses'}), 500

@app.route('/api/materials', methods=['GET'])
@jwt_required()
def get_materials():
    try:
        course_id = request.args.get('course_id')
        if not course_id:
            return jsonify({'error': 'Course ID required'}), 400
            
        materials = Material.query.filter_by(course_id=course_id).all()
        return materials_schema.jsonify(materials), 200
    except Exception as e:
        app.logger.error(f'Get materials error: {str(e)}')
        return jsonify({'error': 'Failed to retrieve materials'}), 500

# Main function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

```python
# CloudCampus Platform - Frontend Service (React)
# This is a React frontend for the educational cloud platform

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { Container, Navbar, Nav, Button, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css
