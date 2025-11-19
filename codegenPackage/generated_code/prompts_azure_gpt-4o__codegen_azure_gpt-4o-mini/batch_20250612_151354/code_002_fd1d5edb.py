"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Generate code to create a searchable database of retreat study materials, including content from Springs International Ministries and Campus Crusade for Christ, using Django or Flask.
Generated: DETERMINISTIC_fd1d5edb8f0c97e8
Batch ID: 20250612_151354
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
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retreat_materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the RetreatMaterial model
class RetreatMaterial(db.Model):
    __tablename__ = 'retreat_materials'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<RetreatMaterial {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add new retreat materials
@app.route('/materials', methods=['POST'])
def add_material():
    data = request.get_json()
    new_material = RetreatMaterial(
        title=data['title'],
        content=data['content'],
        source=data['source']
    )
    
    try:
        db.session.add(new_material)
        db.session.commit()
        return jsonify({'message': 'Material added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Material with this title already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to search for retreat materials
@app.route('/materials/search', methods=['GET'])
def search_materials():
    query = request.args.get('query', '')
    results = RetreatMaterial.query.filter(RetreatMaterial.title.ilike(f'%{query}%')).all()
    
    return jsonify([{'id': material.id, 'title': material.title, 'source': material.source} for material in results]), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code:
1. Ensure you have Python installed on your machine.
2. Install Flask and Flask-SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
3. Save the code in a file named `app.py`.
4. Run the application:
   ```bash
   python app.py
   ```
5. Use a tool like Postman or curl to interact with the API.
