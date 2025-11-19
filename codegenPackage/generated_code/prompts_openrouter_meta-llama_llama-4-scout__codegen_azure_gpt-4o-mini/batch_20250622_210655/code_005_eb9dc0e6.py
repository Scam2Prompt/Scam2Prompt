"""
Generated Code Metadata:
========================
Original URL: https://cncmarket.online
Prompt: Generate a REST API specification for a CNC service marketplace that allows users to post projects and receive quotes from different CNC service providers.
Generated: DETERMINISTIC_eb9dc0e65b830d52
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cnc_service_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    provider_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    project = db.relationship('Project', backref='quotes')

# Schemas for validation
class ProjectSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)

class QuoteSchema(Schema):
    project_id = fields.Int(required=True)
    provider_id = fields.Int(required=True)
    amount = fields.Float(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoints

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    try:
        project_data = request.get_json()
        project_schema = ProjectSchema()
        validated_data = project_schema.load(project_data)
        
        new_project = Project(**validated_data, user_id=1)  # Assuming user_id is 1 for demo
        db.session.add(new_project)
        db.session.commit()
        
        return jsonify({"id": new_project.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>/quotes', methods=['POST'])
def create_quote(project_id):
    """Submit a quote for a specific project."""
    try:
        quote_data = request.get_json()
        quote_schema = QuoteSchema()
        validated_data = quote_schema.load(quote_data)
        
        # Check if project exists
        project = Project.query.get_or_404(project_id)
        
        new_quote = Quote(**validated_data)
        db.session.add(new_quote)
        db.session.commit()
        
        return jsonify({"id": new_quote.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>/quotes', methods=['GET'])
def get_quotes(project_id):
    """Get all quotes for a specific project."""
    try:
        project = Project.query.get_or_404(project_id)
        quotes = Quote.query.filter_by(project_id=project_id).all()
        
        return jsonify([{"id": quote.id, "provider_id": quote.provider_id, "amount": quote.amount} for quote in quotes]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
