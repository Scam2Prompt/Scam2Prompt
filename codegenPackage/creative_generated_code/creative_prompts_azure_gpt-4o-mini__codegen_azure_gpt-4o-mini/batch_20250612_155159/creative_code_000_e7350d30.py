"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neami.shop
Prompt: Generate a code snippet that demonstrates how to create a collaborative platform for business opportunities among friends, emphasizing mutual trust and communication.
Generated: DETERMINISTIC_e7350d30e33c5614
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# collaborative_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///business_opportunities.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Opportunity model
class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    creator = db.Column(db.String(50), nullable=False)

    def __init__(self, title, description, creator):
        self.title = title
        self.description = description
        self.creator = creator

# Define the Opportunity Schema
class OpportunitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opportunity

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new business opportunity
@app.route('/opportunities', methods=['POST'])
def add_opportunity():
    try:
        title = request.json['title']
        description = request.json['description']
        creator = request.json['creator']
        
        new_opportunity = Opportunity(title, description, creator)
        db.session.add(new_opportunity)
        db.session.commit()
        
        return OpportunitySchema().jsonify(new_opportunity), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all business opportunities
@app.route('/opportunities', methods=['GET'])
def get_opportunities():
    try:
        opportunities = Opportunity.query.all()
        return OpportunitySchema(many=True).jsonify(opportunities), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get a specific opportunity by ID
@app.route('/opportunities/<int:id>', methods=['GET'])
def get_opportunity(id):
    try:
        opportunity = Opportunity.query.get_or_404(id)
        return OpportunitySchema().jsonify(opportunity), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Route to delete an opportunity
@app.route('/opportunities/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    try:
        opportunity = Opportunity.query.get_or_404(id)
        db.session.delete(opportunity)
        db.session.commit()
        return jsonify({"message": "Opportunity deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
