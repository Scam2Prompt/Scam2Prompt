"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Write a script to create a decentralized, privacy-preserving AI platform using Tendermint-based consensus and secure enclave storage, as described in PrivateAI's approach.
Generated: DETERMINISTIC_9bb517fc66077a85
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import subprocess
import json

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///privateai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing AI models in the database
class AIModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    model_data = db.Column(db.LargeBinary, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to run Tendermint node
def run_tendermint():
    try:
        # Start the Tendermint node
        subprocess.Popen(['tendermint', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(f"Error starting Tendermint node: {e}")

# Endpoint to upload AI model
@app.route('/upload_model', methods=['POST'])
def upload_model():
    """
    Endpoint to upload AI models.
    Expects a JSON payload with 'model_name' and 'model_data' (base64 encoded).
    """
    try:
        data = request.json
        model_name = data['model_name']
        model_data = data['model_data']

        # Decode the model data from base64
        model_data_decoded = json.loads(model_data)

        # Store model in database
        new_model = AIModel(model_name=model_name, model_data=model_data_decoded)
        db.session.add(new_model)
        db.session.commit()

        return jsonify({'message': 'Model uploaded successfully!'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to list AI models
@app.route('/models', methods=['GET'])
def list_models():
    """
    Endpoint to list all AI models stored in the database.
    """
    try:
        models = AIModel.query.all()
        return jsonify([{'id': model.id, 'model_name': model.model_name} for model in models]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Tendermint node on startup
run_tendermint()

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

Please make sure to have all dependencies installed and the Tendermint binary available in your system path for the code to run properly.
