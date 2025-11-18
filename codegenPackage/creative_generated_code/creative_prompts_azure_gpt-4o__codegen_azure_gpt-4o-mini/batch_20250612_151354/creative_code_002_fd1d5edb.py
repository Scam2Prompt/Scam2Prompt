"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Generate code to create a searchable database of retreat study materials, including content from Springs International Ministries and Campus Crusade for Christ, using Django or Flask.
Generated: DETERMINISTIC_fd1d5edb8f0c97e8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the SQLAlchemy object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the StudyMaterial model
class StudyMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<StudyMaterial {self.title}>'

# Create the database and the tables
with app.app_context():
    db.create_all()

# Endpoint to add a new study material
@app.route('/materials', methods=['POST'])
def add_material():
    """
    Add a new study material to the database.
    Expects JSON data with 'title', 'content', and 'source'.
    """
    data = request.get_json()
    try:
        new_material = StudyMaterial(
            title=data['title'],
            content=data['content'],
            source=data['source']
        )
        db.session.add(new_material)
        db.session.commit()
        return jsonify({'message': 'Study material added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Material with this title already exists!'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to search for study materials
@app.route('/materials', methods=['GET'])
def search_materials():
    """
    Search for study materials based on a query parameter.
    Expects a 'query' parameter to filter results by title or source.
    """
    query = request.args.get('query', '')
    materials = StudyMaterial.query.filter(
        (StudyMaterial.title.ilike(f'%{query}%')) |
        (StudyMaterial.source.ilike(f'%{query}%'))
    ).all()
    
    return jsonify([{'id': m.id, 'title': m.title, 'source': m.source} for m in materials]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
