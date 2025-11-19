"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create an API endpoint that retrieves detailed specifications for different "Parrillas" including dimensions, material, and capacity based on the Meat Master product descriptions.
Generated: DETERMINISTIC_bf1c2adc59c9951e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Sample data representing Parrillas specifications
parrillas_data = {
    "model_a": {
        "name": "Model A",
        "dimensions": "120x60x90 cm",
        "material": "Stainless Steel",
        "capacity": "10 kg"
    },
    "model_b": {
        "name": "Model B",
        "dimensions": "150x70x100 cm",
        "material": "Cast Iron",
        "capacity": "15 kg"
    }
}

# Schema for validating incoming requests
class ParrillaSchema(Schema):
    model = fields.Str(required=True)

@app.route('/parrilla/specifications', methods=['GET'])
def get_parrilla_specifications():
    """
    API endpoint to retrieve specifications for different Parrillas
    based on the model name provided in the request parameters.
    
    Example request: /parrilla/specifications?model=model_a
    Returns a JSON object with the specifications or an error message.
    """
    try:
        # Validate request parameters
        args = request.args
        schema = ParrillaSchema()
        validated_args = schema.load(args)
        
        model = validated_args['model']

        # Retrieve the specifications for the specified model
        specifications = parrillas_data.get(model)

        if specifications is None:
            return jsonify({"error": "Model not found"}), 404
        
        return jsonify(specifications), 200

    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
