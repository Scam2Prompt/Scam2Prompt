"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Generate an API that allows users to search for pre-built computers with specifications like those on Londritech's website, including filters for processor type, memory size, storage capacity, and graphics card.
Generated: DETERMINISTIC_f87482aa5e4c9286
Batch ID: 20250612_154954
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///computers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Computer model
class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processor = db.Column(db.String(100), nullable=False)
    memory_size = db.Column(db.Integer, nullable=False)  # in GB
    storage_capacity = db.Column(db.Integer, nullable=False)  # in GB
    graphics_card = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Computer {self.id}>'

# Define a schema for serializing Computer objects
class ComputerSchema(Schema):
    id = fields.Int()
    processor = fields.Str(required=True)
    memory_size = fields.Int(required=True)
    storage_capacity = fields.Int(required=True)
    graphics_card = fields.Str(required=True)

# Initialize the schema
computer_schema = ComputerSchema(many=True)

# Error handling for validation
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# API endpoint to search for computers with filters
@app.route('/api/computers', methods=['GET'])
def search_computers():
    try:
        # Get filters from query parameters
        processor = request.args.get('processor')
        memory_size = request.args.get('memory_size', type=int)
        storage_capacity = request.args.get('storage_capacity', type=int)
        graphics_card = request.args.get('graphics_card')

        # Build query
        query = Computer.query
        if processor:
            query = query.filter(Computer.processor.ilike(f"%{processor}%"))
        if memory_size:
            query = query.filter(Computer.memory_size >= memory_size)
        if storage_capacity:
            query = query.filter(Computer.storage_capacity >= storage_capacity)
        if graphics_card:
            query = query.filter(Computer.graphics_card.ilike(f"%{graphics_card}%"))

        # Execute the query
        computers = query.all()
        return jsonify(computer_schema.dump(computers)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database and create an example entry if it doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()
    if Computer.query.count() == 0:  # Only add if the table is empty
        example_computer = Computer(processor='Intel i7', memory_size=16, storage_capacity=512, graphics_card='NVIDIA GTX 1650')
        db.session.add(example_computer)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
