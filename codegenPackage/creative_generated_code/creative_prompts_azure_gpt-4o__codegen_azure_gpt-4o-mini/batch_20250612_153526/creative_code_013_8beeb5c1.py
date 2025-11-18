"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Suggest an API to model the effect of wall thickness (WT) on the strength and flexibility of stainless steel pipes used in automotive engine systems.
Generated: DETERMINISTIC_8beeb5c14a240d6f
Batch ID: 20250612_153526
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

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Pipe
class Pipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wall_thickness = db.Column(db.Float, nullable=False)
    strength = db.Column(db.Float, nullable=False)
    flexibility = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pipe {self.id}: WT={self.wall_thickness}, Strength={self.strength}, Flexibility={self.flexibility}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/pipes', methods=['POST'])
def add_pipe():
    """
    Add a new pipe to the database.
    Expecting JSON input with wall_thickness, strength, and flexibility.
    """
    data = request.get_json()

    if not all(key in data for key in ('wall_thickness', 'strength', 'flexibility')):
        return jsonify({"error": "Missing data"}), 400

    try:
        # Create new pipe instance
        new_pipe = Pipe(
            wall_thickness=data['wall_thickness'],
            strength=data['strength'],
            flexibility=data['flexibility']
        )
        
        # Add and commit to the database
        db.session.add(new_pipe)
        db.session.commit()
        return jsonify({'message': 'Pipe added successfully', 'pipe_id': new_pipe.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity Error, please check your input"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pipes', methods=['GET'])
def get_pipes():
    """
    Retrieve all pipes from the database.
    Returns a list of pipes with their details.
    """
    pipes = Pipe.query.all()
    return jsonify([{'id': pipe.id, 'wall_thickness': pipe.wall_thickness, 
                     'strength': pipe.strength, 'flexibility': pipe.flexibility} for pipe in pipes]), 200

@app.route('/pipes/<int:pipe_id>', methods=['GET'])
def get_pipe(pipe_id):
    """
    Retrieve a specific pipe by its ID.
    """
    pipe = Pipe.query.get(pipe_id)
    if pipe is None:
        return jsonify({"error": "Pipe not found"}), 404
    
    return jsonify({'id': pipe.id, 
                    'wall_thickness': pipe.wall_thickness, 
                    'strength': pipe.strength, 
                    'flexibility': pipe.flexibility}), 200

@app.route('/pipes/<int:pipe_id>', methods=['PUT'])
def update_pipe(pipe_id):
    """
    Update an existing pipe's attributes.
    Expecting JSON input with optional wall_thickness, strength, and/or flexibility.
    """
    data = request.get_json()
    pipe = Pipe.query.get(pipe_id)

    if pipe is None:
        return jsonify({"error": "Pipe not found"}), 404

    if 'wall_thickness' in data:
        pipe.wall_thickness = data['wall_thickness']
    if 'strength' in data:
        pipe.strength = data['strength']
    if 'flexibility' in data:
        pipe.flexibility = data['flexibility']

    db.session.commit()
    return jsonify({'message': 'Pipe updated successfully'}), 200

@app.route('/pipes/<int:pipe_id>', methods=['DELETE'])
def delete_pipe(pipe_id):
    """
    Delete a pipe from the database by its ID.
    """
    pipe = Pipe.query.get(pipe_id)
    if pipe is None:
        return jsonify({"error": "Pipe not found"}), 404
    
    db.session.delete(pipe)
    db.session.commit()
    return jsonify({'message': 'Pipe deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
