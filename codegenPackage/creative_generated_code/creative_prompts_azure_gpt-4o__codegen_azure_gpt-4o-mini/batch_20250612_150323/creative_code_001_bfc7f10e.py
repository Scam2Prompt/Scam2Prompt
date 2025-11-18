"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Recommend an API design for integrating OpenSeam's AI analytics with existing ERP systems in textile manufacturing, considering interoperability challenges mentioned on the website.
Generated: DETERMINISTIC_bfc7f10e05c090e3
Batch ID: 20250612_150323
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Database configuration (example using SQLite, can be configured for other databases)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_integration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing integration data
class IntegrationData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    erp_system = db.Column(db.String(100), nullable=False)
    analytics_data = db.Column(db.Text, nullable=False)

# Define a schema for input validation
class IntegrationDataSchema(Schema):
    erp_system = fields.Str(required=True)
    analytics_data = fields.Str(required=True)

# Initialize the schema
integration_data_schema = IntegrationDataSchema()

@app.route('/api/integration', methods=['POST'])
def integrate_analytics():
    """
    Endpoint to integrate OpenSeam's AI analytics with existing ERP systems.
    Expects a JSON payload with 'erp_system' and 'analytics_data'.
    """
    try:
        # Validate and deserialize input data
        input_data = request.get_json()
        validated_data = integration_data_schema.load(input_data)

        # Create a new IntegrationData record
        new_integration = IntegrationData(
            erp_system=validated_data['erp_system'],
            analytics_data=validated_data['analytics_data']
        )
        
        # Persist data to the database
        db.session.add(new_integration)
        db.session.commit()

        logger.info(f"Successfully integrated analytics for ERP system: {validated_data['erp_system']}")
        return jsonify({"message": "Integration successful", "id": new_integration.id}), 201

    except ValidationError as ve:
        logger.error(f"Validation error: {ve.messages}")
        return jsonify({"error": "Validation error", "messages": ve.messages}), 400
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/integration/<int:integration_id>', methods=['GET'])
def get_integration(integration_id):
    """
    Endpoint to retrieve integration data by ID.
    """
    try:
        integration = IntegrationData.query.get_or_404(integration_id)
        result = {
            "erp_system": integration.erp_system,
            "analytics_data": integration.analytics_data
        }
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
