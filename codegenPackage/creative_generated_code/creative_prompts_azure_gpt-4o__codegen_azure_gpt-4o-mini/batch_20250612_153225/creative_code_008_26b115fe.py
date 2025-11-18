"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write code to implement a pre-workshop module for parents of adolescents undergoing DBT therapy, as described in the FAQs section of the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_26b115fe76a3bcf3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mente_sana.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Parent(db.Model):
    """Model representing a parent in the DBT therapy program."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    adolescents = db.relationship('Adolescent', backref='parent', lazy=True)

class Adolescent(db.Model):
    """Model representing an adolescent undergoing DBT therapy."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_parent():
    """Endpoint to register a parent and their adolescent(s)."""
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'adolescents' not in data:
            raise BadRequest("Missing required fields: name, email or adolescents")
        
        parent = Parent(name=data['name'], email=data['email'])
        db.session.add(parent)
        db.session.commit()

        for adolescent in data['adolescents']:
            if 'name' not in adolescent or 'age' not in adolescent:
                raise BadRequest("Missing required fields for adolescent: name or age")
            new_adolescent = Adolescent(name=adolescent['name'], age=adolescent['age'], parent_id=parent.id)
            db.session.add(new_adolescent)

        db.session.commit()
        return jsonify({"message": "Parent and adolescents registered successfully."}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while registering. Please try again."}), 500

@app.route('/parents', methods=['GET'])
def get_parents():
    """Endpoint to retrieve all registered parents and their adolescents."""
    try:
        parents = Parent.query.all()
        result = []
        for parent in parents:
            adolescents = [{'id': a.id, 'name': a.name, 'age': a.age} for a in parent.adolescents]
            result.append({'id': parent.id, 'name': parent.name, 'email': parent.email, 'adolescents': adolescents})
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving parents. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
