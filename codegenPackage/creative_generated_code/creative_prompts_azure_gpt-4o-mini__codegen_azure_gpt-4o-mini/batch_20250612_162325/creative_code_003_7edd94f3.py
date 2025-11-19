"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Develop a RESTful API that supports psychosocial counseling services for children in distress, reflecting the goals of Child Nepal.
Generated: DETERMINISTIC_7edd94f3866c7f19
Batch ID: 20250612_162325
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counseling_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Counseling Service model
class CounselingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, service_name, description):
        self.service_name = service_name
        self.description = description

# Define the Counseling Service schema
class CounselingServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CounselingService

# Initialize the schema
service_schema = CounselingServiceSchema()
services_schema = CounselingServiceSchema(many=True)

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description})
    response.content_type = "application/json"
    return response

# Endpoint to create a new counseling service
@app.route('/services', methods=['POST'])
def add_service():
    try:
        service_name = request.json['service_name']
        description = request.json['description']
        new_service = CounselingService(service_name, description)
        db.session.add(new_service)
        db.session.commit()
        return service_schema.jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve all counseling services
@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = CounselingService.query.all()
        return services_schema.jsonify(services), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a counseling service by ID
@app.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    try:
        service = CounselingService.query.get_or_404(id)
        return service_schema.jsonify(service), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Endpoint to update a counseling service
@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    try:
        service = CounselingService.query.get_or_404(id)
        service.service_name = request.json.get('service_name', service.service_name)
        service.description = request.json.get('description', service.description)
        db.session.commit()
        return service_schema.jsonify(service), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to delete a counseling service
@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    try:
        service = CounselingService.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "Service deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Create the database tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
