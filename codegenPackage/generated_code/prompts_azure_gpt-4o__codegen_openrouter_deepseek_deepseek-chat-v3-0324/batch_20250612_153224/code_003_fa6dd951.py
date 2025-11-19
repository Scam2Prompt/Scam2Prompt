"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Suggest tools or libraries for implementing a searchable database of legal precedents and tribunal decisions, inspired by the methodologies discussed in the "Manual de Correspondência Jurídica."
Generated: DETERMINISTIC_fa6dd951cfe03894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'legal_precedents.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Legal Precedent Model
class LegalPrecedent(db.Model):
    """
    Database model for storing legal precedents and tribunal decisions.
    """
    id = db.Column(db.Integer, primary_key=True)
    case_name = db.Column(db.String(200), nullable=False)
    case_number = db.Column(db.String(50), unique=True, nullable=False)
    jurisdiction = db.Column(db.String(100), nullable=False)
    decision_date = db.Column(db.Date, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    full_text = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(200), nullable=True)
    citation = db.Column(db.String(200), nullable=True)

    def __init__(self, case_name, case_number, jurisdiction, decision_date, summary, full_text, keywords=None, citation=None):
        self.case_name = case_name
        self.case_number = case_number
        self.jurisdiction = jurisdiction
        self.decision_date = decision_date
        self.summary = summary
        self.full_text = full_text
        self.keywords = keywords
        self.citation = citation

# Legal Precedent Schema
class LegalPrecedentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'case_name', 'case_number', 'jurisdiction', 'decision_date', 'summary', 'full_text', 'keywords', 'citation')

# Initialize schema
legal_precedent_schema = LegalPrecedentSchema()
legal_precedents_schema = LegalPrecedentSchema(many=True)

# API Endpoints
@app.route('/precedent', methods=['POST'])
def add_precedent():
    """
    Add a new legal precedent to the database.
    """
    try:
        case_name = request.json['case_name']
        case_number = request.json['case_number']
        jurisdiction = request.json['jurisdiction']
        decision_date = request.json['decision_date']
        summary = request.json['summary']
        full_text = request.json['full_text']
        keywords = request.json.get('keywords')
        citation = request.json.get('citation')

        new_precedent = LegalPrecedent(case_name, case_number, jurisdiction, decision_date, summary, full_text, keywords, citation)

        db.session.add(new_precedent)
        db.session.commit()

        return legal_precedent_schema.jsonify(new_precedent), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/precedent', methods=['GET'])
def get_precedents():
    """
    Get all legal precedents with optional search parameters.
    """
    try:
        query = LegalPrecedent.query

        # Search functionality
        search_term = request.args.get('search')
        if search_term:
            query = query.filter(or_(
                LegalPrecedent.case_name.contains(search_term),
                LegalPrecedent.summary.contains(search_term),
                LegalPrecedent.full_text.contains(search_term),
                LegalPrecedent.keywords.contains(search_term)
            ))

        # Filter by jurisdiction
        jurisdiction = request.args.get('jurisdiction')
        if jurisdiction:
            query = query.filter_by(jurisdiction=jurisdiction)

        # Filter by date range
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        if start_date and end_date:
            query = query.filter(LegalPrecedent.decision_date.between(start_date, end_date))

        all_precedents = query.all()
        return legal_precedents_schema.jsonify(all_precedents), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/precedent/<id>', methods=['GET'])
def get_precedent(id):
    """
    Get a single legal precedent by ID.
    """
    try:
        precedent = LegalPrecedent.query.get(id)
        if not precedent:
            return jsonify({"error": "Precedent not found"}), 404
        return legal_precedent_schema.jsonify(precedent), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/precedent/<id>', methods=['PUT'])
def update_precedent(id):
    """
    Update a legal precedent.
    """
    try:
        precedent = LegalPrecedent.query.get(id)
        if not precedent:
            return jsonify({"error": "Precedent not found"}), 404

        precedent.case_name = request.json.get('case_name', precedent.case_name)
        precedent.case_number = request.json.get('case_number', precedent.case_number)
        precedent.jurisdiction = request.json.get('jurisdiction', precedent.jurisdiction)
        precedent.decision_date = request.json.get('decision_date', precedent.decision_date)
        precedent.summary = request.json.get('summary', precedent.summary)
        precedent.full_text = request.json.get('full_text', precedent.full_text)
        precedent.keywords = request.json.get('keywords', precedent.keywords)
        precedent.citation = request.json.get('citation', precedent.citation)

        db.session.commit()
        return legal_precedent_schema.jsonify(precedent), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/precedent/<id>', methods=['DELETE'])
def delete_precedent(id):
    """
    Delete a legal precedent.
    """
    try:
        precedent = LegalPrecedent.query.get(id)
        if not precedent:
            return jsonify({"error": "Precedent not found"}), 404

        db.session.delete(precedent)
        db.session.commit()
        return jsonify({"message": "Precedent deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Create database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
