"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to upload a model JSON file and generate a model card as described on the Lineage AI website.
Generated: DETERMINISTIC_f5106fbba813f8b3
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path where model files will be stored
MODEL_UPLOAD_FOLDER = 'uploaded_models'
os.makedirs(MODEL_UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload_model', methods=['POST'])
def upload_model():
    """Endpoint to upload a JSON model file and generate a model card."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith('.json'):
        return jsonify({"error": "File must be a JSON file"}), 400

    # Save the uploaded file
    file_path = os.path.join(MODEL_UPLOAD_FOLDER, file.filename)
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"File saving failed: {str(e)}"}), 500

    # Generate model card
    try:
        model_card = generate_model_card(file_path)
    except Exception as e:
        return jsonify({"error": f"Model card generation failed: {str(e)}"}), 500

    return jsonify({"message": "Model uploaded successfully", "model_card": model_card}), 200

def generate_model_card(file_path):
    """Generate a model card based on the uploaded JSON model file."""
    with open(file_path, 'r') as model_file:
        model_data = json.load(model_file)
    
    # Validate model data structure (example validation, adjust as needed)
    if not isinstance(model_data, dict) or 'name' not in model_data:
        raise ValueError("Invalid model data structure")

    # Create a simple model card
    model_card = {
        "model_name": model_data['name'],
        "description": model_data.get('description', 'No description provided'),
        "version": model_data.get('version', '1.0'),
        "author": model_data.get('author', 'Unknown'),
    }
    
    return model_card

if __name__ == '__main__':
    app.run(debug=True)
```
