"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Develop an API that allows users to search for automotive parts by vehicle model, year, and type, referencing the product categories and examples from paxosrew.com.
Generated: DETERMINISTIC_e876e3b5ba8b4740
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automotive_parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Automotive Parts
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    part_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Part {self.model} {self.year} {self.part_type}>"

# Create the database and the tables
with app.app_context():
    db.create_all()

@app.route('/api/parts', methods=['GET'])
def search_parts():
    """
    Search for automotive parts by vehicle model, year, and type.

    Query Parameters:
        - model: Vehicle model (string)
        - year: Vehicle year (integer)
        - part_type: Type of part (string)

    Returns:
        A JSON array of matching parts or an error message.
    """
    model = request.args.get('model')
    year = request.args.get('year', type=int)
    part_type = request.args.get('part_type')

    try:
        # Build the query based on provided parameters
        query = Part.query
        if model:
            query = query.filter(Part.model.ilike(f"%{model}%"))
        if year:
            query = query.filter(Part.year == year)
        if part_type:
            query = query.filter(Part.part_type.ilike(f"%{part_type}%"))

        # Execute the query and return results
        results = query.all()
        parts = [{"id": part.id, "model": part.model, "year": part.year, "type": part.part_type, "description": part.description} for part in results]

        return jsonify(parts), 200

    except SQLAlchemyError as e:
        # Handle SQL errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/parts', methods=['POST'])
def add_part():
    """
    Add a new automotive part to the database.

    Request Body:
        - model: Vehicle model (string)
        - year: Vehicle year (integer)
        - part_type: Type of part (string)
        - description: Part description (string)

    Returns:
        A success message or an error message.
    """
    data = request.json

    try:
        new_part = Part(
            model=data['model'],
            year=data['year'],
            part_type=data['part_type'],
            description=data.get('description')
        )
        db.session.add(new_part)
        db.session.commit()

        return jsonify({"message": "Part added successfully!"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Part already exists or invalid data."}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
