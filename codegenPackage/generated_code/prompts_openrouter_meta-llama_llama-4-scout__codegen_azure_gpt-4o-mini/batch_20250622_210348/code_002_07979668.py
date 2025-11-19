"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Generate a code snippet to implement a network of publishers and creators for a children's literature platform, allowing them to share their work and connect with audiences.
Generated: DETERMINISTIC_0797966806a80729
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///literature_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Publishers
class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    works = db.relationship('Work', backref='publisher', lazy=True)

# Database model for Works
class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)

# Schema for validating Publisher input
class PublisherSchema(Schema):
    name = fields.Str(required=True)

# Schema for validating Work input
class WorkSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    publisher_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new publisher
@app.route('/publishers', methods=['POST'])
def add_publisher():
    try:
        data = request.get_json()
        PublisherSchema().load(data)  # Validate input
        new_publisher = Publisher(name=data['name'])
        db.session.add(new_publisher)
        db.session.commit()
        return jsonify({"id": new_publisher.id, "name": new_publisher.name}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to create a new work
@app.route('/works', methods=['POST'])
def add_work():
    try:
        data = request.get_json()
        WorkSchema().load(data)  # Validate input
        new_work = Work(title=data['title'], content=data['content'], publisher_id=data['publisher_id'])
        db.session.add(new_work)
        db.session.commit()
        return jsonify({"id": new_work.id, "title": new_work.title}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all publishers
@app.route('/publishers', methods=['GET'])
def get_publishers():
    publishers = Publisher.query.all()
    return jsonify([{"id": pub.id, "name": pub.name} for pub in publishers]), 200

# Route to get all works
@app.route('/works', methods=['GET'])
def get_works():
    works = Work.query.all()
    return jsonify([{"id": work.id, "title": work.title, "publisher_id": work.publisher_id} for work in works]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
