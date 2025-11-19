"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Create an API endpoint for listing automotive tools and tires with pricing and installment options, as seen on the Itamarati Online website.
Generated: DETERMINISTIC_edcfac9d5a7f04d0
Batch ID: 20250612_163406
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

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automotive_tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for AutomotiveTools
class AutomotiveTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    installment_options = db.Column(db.String(255), nullable=True)

# Schema for serializing AutomotiveTool objects
class AutomotiveToolSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    installment_options = fields.Str()

# Initialize schema
tool_schema = AutomotiveToolSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": str(error)}), 400

# API endpoint to list automotive tools
@app.route('/api/tools', methods=['GET'])
def list_tools():
    try:
        # Query all tools from the database
        tools = AutomotiveTool.query.all()
        # Serialize the tools using the schema
        result = tool_schema.dump(tools)
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# API endpoint to add a new automotive tool
@app.route('/api/tools', methods=['POST'])
def add_tool():
    try:
        # Validate and deserialize request data
        data = request.get_json()
        new_tool = tool_schema.load(data)
        # Create a new AutomotiveTool instance
        tool = AutomotiveTool(**new_tool)
        db.session.add(tool)
        db.session.commit()
        # Serialize the newly created tool
        result = tool_schema.dump(tool)
        return jsonify(result), 201
    except ValidationError as ve:
        return handle_validation_error(ve)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database and create tables if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
