"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atwg.xyz
Prompt: Create a REST API that facilitates seamless communication for a call center, inspired by ATWG LTD's customer support model.
Generated: DETERMINISTIC_3b0d0c6e6e273736
Batch ID: 20250612_161420
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///call_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Agent model
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Define the Request schema for validation
class AgentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)

# Create a schema instance
agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new agent
@app.route('/agents', methods=['POST'])
def add_agent():
    try:
        # Validate and deserialize input
        json_data = request.get_json()
        agent = agent_schema.load(json_data)
        
        new_agent = Agent(name=agent['name'], status=agent['status'])
        db.session.add(new_agent)
        db.session.commit()
        return agent_schema.dump(new_agent), 201
    except (ValidationError, IntegrityError) as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve all agents
@app.route('/agents', methods=['GET'])
def get_agents():
    agents = Agent.query.all()
    return agents_schema.dump(agents), 200

# Endpoint to update an agent's status
@app.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    try:
        json_data = request.get_json()
        agent = Agent.query.get_or_404(agent_id)

        if 'name' in json_data:
            agent.name = json_data['name']
        if 'status' in json_data:
            agent.status = json_data['status']
        
        db.session.commit()
        return agent_schema.dump(agent), 200
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while updating the agent."}), 500

# Endpoint to delete an agent
@app.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    db.session.delete(agent)
    db.session.commit()
    return jsonify({"message": "Agent deleted successfully."}), 204

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', True))  # Set debug mode based on environment variable
```
