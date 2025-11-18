"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-co.pages.dev
Prompt: Provide a solution for integrating gaming studio partnerships into a platform, allowing studios to drop gigs, careers, and incentives for users, as seen on Metacade.
Generated: DETERMINISTIC_7d6283e2c92daec5
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gaming_studios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Gaming Studio
class Studio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    gigs = db.relationship('Gig', backref='studio', lazy=True)

# Database model for Gigs
class Gig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    studio_id = db.Column(db.Integer, db.ForeignKey('studio.id'), nullable=False)

# Schema for Studio
class StudioSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# Schema for Gig
class GigSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    studio_id = fields.Int(required=True)

# Create database tables
db.create_all()

@app.route('/studios', methods=['POST'])
def create_studio():
    """Create a new gaming studio."""
    studio_schema = StudioSchema()
    try:
        studio_data = studio_schema.load(request.json)
        new_studio = Studio(name=studio_data['name'])
        db.session.add(new_studio)
        db.session.commit()
        return studio_schema.jsonify(new_studio), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Studio already exists."}), 409

@app.route('/studios/<int:studio_id>/gigs', methods=['POST'])
def create_gig(studio_id):
    """Create a new gig under a specific studio."""
    gig_schema = GigSchema()
    try:
        gig_data = gig_schema.load(request.json)
        new_gig = Gig(title=gig_data['title'], description=gig_data['description'], studio_id=studio_id)
        db.session.add(new_gig)
        db.session.commit()
        return gig_schema.jsonify(new_gig), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to create gig."}), 409

@app.route('/studios/<int:studio_id>/gigs', methods=['GET'])
def get_gigs(studio_id):
    """Retrieve all gigs for a specific studio."""
    gigs = Gig.query.filter_by(studio_id=studio_id).all()
    gig_schema = GigSchema(many=True)
    return gig_schema.jsonify(gigs), 200

@app.route('/studios', methods=['GET'])
def get_studios():
    """Retrieve all gaming studios."""
    studios = Studio.query.all()
    studio_schema = StudioSchema(many=True)
    return studio_schema.jsonify(studios), 200

if __name__ == '__main__':
    app.run(debug=True)
```
