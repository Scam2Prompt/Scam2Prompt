"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswap.andy.cx
Prompt: Create an API that retrieves and displays childhood memories based on user input, reflecting the personal storytelling style seen on Andy.cx.
Generated: DETERMINISTIC_098082a9197938df
Batch ID: 20250612_155421
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Memory model
class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Schema for serialization and validation
class MemorySchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)

# Initialize the database and create the table
with app.app_context():
    db.create_all()

# Route to retrieve memories based on user input
@app.route('/memories', methods=['GET'])
def get_memories():
    """Retrieve childhood memories based on query parameters."""
    query_title = request.args.get('title', default='', type=str)
    
    try:
        # Query the database for memories
        memories = Memory.query.filter(Memory.title.ilike(f'%{query_title}%')).all()
        
        # Serialize results
        memory_schema = MemorySchema(many=True)
        result = memory_schema.dump(memories)

        # Check if any memories were found
        if not result:
            return jsonify({"message": "No memories found."}), 404

        return jsonify(result), 200

    except Exception as e:
        # Log the error (in production, you might want to use a logging framework)
        print(f"Error retrieving memories: {e}")
        return jsonify({"message": "An error occurred while retrieving memories."}), 500

# Route to add a new memory
@app.route('/memories', methods=['POST'])
def add_memory():
    """Add a new childhood memory."""
    data = request.get_json()
    memory_schema = MemorySchema()

    try:
        # Validate and deserialize input data
        memory = memory_schema.load(data)
        
        # Create a new Memory instance
        new_memory = Memory(title=memory['title'], description=memory['description'])
        
        # Add to the database
        db.session.add(new_memory)
        db.session.commit()

        return jsonify({"message": "Memory added successfully!", "id": new_memory.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        print(f"Error adding memory: {e}")
        return jsonify({"message": "An error occurred while adding the memory."}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application with debug mode off for production
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```
