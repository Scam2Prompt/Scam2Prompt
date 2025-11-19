"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oliveiragomesadv.com.br
Prompt: Create a REST API that provides legal advice for family law cases, incorporating the specialized areas mentioned by Oliveira Gomes Advogados.
Generated: DETERMINISTIC_9277b6184a5d7c8d
Batch ID: 20250612_161700
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
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///family_law_advice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the model for legal advice
class LegalAdvice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_of_law = db.Column(db.String(100), nullable=False)
    advice_text = db.Column(db.Text, nullable=False)

    def __init__(self, area_of_law, advice_text):
        self.area_of_law = area_of_law
        self.advice_text = advice_text

# Define the schema for serializing legal advice
class LegalAdviceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LegalAdvice

# Initialize the database and create the table
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all legal advice
@app.route('/api/advice', methods=['GET'])
def get_all_advice():
    try:
        advice_list = LegalAdvice.query.all()
        advice_schema = LegalAdviceSchema(many=True)
        return jsonify(advice_schema.dump(advice_list)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get advice by area of law
@app.route('/api/advice/<string:area>', methods=['GET'])
def get_advice_by_area(area):
    try:
        advice = LegalAdvice.query.filter_by(area_of_law=area).first()
        if advice is None:
            return jsonify({'message': 'Advice not found'}), 404
        advice_schema = LegalAdviceSchema()
        return jsonify(advice_schema.dump(advice)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add new legal advice
@app.route('/api/advice', methods=['POST'])
def add_advice():
    try:
        area_of_law = request.json['area_of_law']
        advice_text = request.json['advice_text']
        
        new_advice = LegalAdvice(area_of_law, advice_text)
        db.session.add(new_advice)
        db.session.commit()

        advice_schema = LegalAdviceSchema()
        return jsonify(advice_schema.dump(new_advice)), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update existing legal advice
@app.route('/api/advice/<int:id>', methods=['PUT'])
def update_advice(id):
    try:
        advice = LegalAdvice.query.get(id)
        if advice is None:
            return jsonify({'message': 'Advice not found'}), 404

        area_of_law = request.json.get('area_of_law', advice.area_of_law)
        advice_text = request.json.get('advice_text', advice.advice_text)

        advice.area_of_law = area_of_law
        advice.advice_text = advice_text
        db.session.commit()

        advice_schema = LegalAdviceSchema()
        return jsonify(advice_schema.dump(advice)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete legal advice
@app.route('/api/advice/<int:id>', methods=['DELETE'])
def delete_advice(id):
    try:
        advice = LegalAdvice.query.get(id)
        if advice is None:
            return jsonify({'message': 'Advice not found'}), 404
        
        db.session.delete(advice)
        db.session.commit()
        
        return jsonify({'message': 'Advice deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required libraries before running the code:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Flask-CORS
```
