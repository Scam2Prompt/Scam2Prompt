"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Suggest a Python library for generating and managing links for an online tool catalog, similar to the "Gerar link" feature mentioned on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_ae968def736391cd
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a solution for generating and managing links for an online tool catalog.
It uses Flask as the web framework and a SQLite database for storage. The system generates unique URLs
for each tool in the catalog, allowing users to share or access specific tools easily.
"""

import os
import uuid
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tool_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Define the Tool model for the catalog
class Tool(db.Model):
    __tablename__ = 'tools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    link_uuid = db.Column(db.String(36), unique=True, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.link_uuid = str(uuid.uuid4())  # Generate a unique identifier for the tool


# Endpoint to add a new tool to the catalog
@app.route('/add_tool', methods=['POST'])
def add_tool():
    try:
        # Get tool details from the request
        data = request.json
        name = data.get('name')
        description = data.get('description')

        # Validate input
        if not name or not description:
            return jsonify({"error": "Name and description are required"}), 400

        # Create and save the tool
        new_tool = Tool(name=name, description=description)
        db.session.add(new_tool)
        db.session.commit()

        # Generate and return the link for the tool
        return jsonify({
            "message": "Tool added successfully",
            "tool_link": url_for('get_tool_by_link', link_uuid=new_tool.link_uuid, _external=True)
        }), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve a tool by its unique link
@app.route('/tool/<link_uuid>', methods=['GET'])
def get_tool_by_link(link_uuid):
    try:
        # Query the tool by its UUID
        tool = Tool.query.filter_by(link_uuid=link_uuid).first()
        if not tool:
            return jsonify({"error": "Tool not found"}), 404

        # Return tool information
        return jsonify({
            "id": tool.id,
            "name": tool.name,
            "description": tool.description
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Endpoint to list all tools in the catalog (optional)
@app.route('/tools', methods=['GET'])
def list_tools():
    try:
        # Query all tools
        tools = Tool.query.all()
        return jsonify([{
            "id": tool.id,
            "name": tool.name,
            "description": tool.description,
            "tool_link": url_for('get_tool_by_link', link_uuid=tool.link_uuid, _external=True)
        } for tool in tools]), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


# Initialize the database (create tables)
@app.before_first_request
def setup_database():
    db.create_all()


# Run the application
if __name__ == '__main__':
    # Ensure the database exists
    if not os.path.exists('tool_catalog.db'):
        setup_database()
    app.run(debug=True)
```
