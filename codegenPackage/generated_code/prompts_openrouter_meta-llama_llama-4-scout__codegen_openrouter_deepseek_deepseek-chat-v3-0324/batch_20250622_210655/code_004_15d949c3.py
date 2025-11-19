"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Create a RESTful API to manage translation projects, including features like real-time quoting, project tracking, and client feedback, inspired by the services provided by SOLID SRL.
Generated: DETERMINISTIC_15d949c3b2af4aa6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# translation_project_api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import datetime
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'translation.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    projects = db.relationship('Project', backref='client', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    source_language = db.Column(db.String(50), nullable=False)
    target_language = db.Column(db.String(50), nullable=False)
    word_count = db.Column(db.Integer, nullable=False)
    price_per_word = db.Column(db.Float, nullable=False)
    deadline = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='Pending')
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    feedbacks = db.relationship('Feedback', backref='project', lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Schemas
class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone')

class ProjectSchema(ma.Schema):
    client = fields.Nested(ClientSchema)
    class Meta:
        fields = ('id', 'title', 'description', 'source_language', 'target_language', 
                 'word_count', 'price_per_word', 'deadline', 'status', 'client_id', 'total_price')
    
    total_price = fields.Method("calculate_total_price")
    
    def calculate_total_price(self, obj):
        return obj.word_count * obj.price_per_word

class FeedbackSchema(ma.Schema):
    project = fields.Nested(ProjectSchema)
    class Meta:
        fields = ('id', 'rating', 'comment', 'project_id')

# Initialize schemas
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

# Routes
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json.get('phone', '')

        new_client = Client(name=name, email=email, phone=phone)
        db.session.add(new_client)
        db.session.commit()

        return client_schema.jsonify(new_client), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        all_clients = Client.query.all()
        return clients_schema.jsonify(all_clients), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    try:
        client = Client.query.get(id)
        if not client:
            return jsonify({'message': 'Client not found'}), 404
        return client_schema.jsonify(client), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects', methods=['POST'])
def add_project():
    try:
        title = request.json['title']
        description = request.json.get('description', '')
        source_language = request.json['source_language']
        target_language = request.json['target_language']
        word_count = request.json['word_count']
        price_per_word = request.json['price_per_word']
        deadline_str = request.json.get('deadline')
        client_id = request.json['client_id']

        deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d') if deadline_str else None

        new_project = Project(
            title=title,
            description=description,
            source_language=source_language,
            target_language=target_language,
            word_count=word_count,
            price_per_word=price_per_word,
            deadline=deadline,
            client_id=client_id
        )

        db.session.add(new_project)
        db.session.commit()

        return project_schema.jsonify(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        all_projects = Project.query.all()
        return projects_schema.jsonify(all_projects), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'message': 'Project not found'}), 404
        return project_schema.jsonify(project), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<id>/status', methods=['PUT'])
def update_project_status(id):
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'message': 'Project not found'}), 404
        
        status = request.json['status']
        if status not in ['Pending', 'In Progress', 'Completed', 'Delivered']:
            return jsonify({'message': 'Invalid status'}), 400
        
        project.status = status
        db.session.commit()
        
        return project_schema.jsonify(project), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<id>/quote', methods=['GET'])
def get_project_quote(id):
    try:
        project = Project.query.get(id)
        if not project:
            return jsonify({'message': 'Project not found'}), 404
        
        quote = {
            'word_count': project.word_count,
            'price_per_word': project.price_per_word,
            'total_price': project.word_count * project.price_per_word
        }
        
        return jsonify(quote), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedbacks', methods=['POST'])
def add_feedback():
    try:
        rating = request.json['rating']
        comment = request.json.get('comment', '')
        project_id = request.json['project_id']

        if rating < 1 or rating > 5:
            return jsonify({'message': 'Rating must be between 1 and 5'}), 400

        new_feedback = Feedback(rating=rating, comment=comment, project_id=project_id)
        db.session.add(new_feedback)
        db.session.commit()

        return feedback_schema.jsonify(new_feedback), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    try:
        all_feedbacks = Feedback.query.all()
        return feedbacks_schema.jsonify(all_feedbacks), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedbacks/project/<project_id>', methods=['GET'])
def get_project_feedbacks(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'message': 'Project not found'}), 404
            
        feedbacks = Feedback.query.filter_by(project_id=project_id).all()
        return feedbacks_schema.jsonify(feedbacks), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
