"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Suggest a REST API for a plumbing service that includes endpoints for pipe cleaning, leak detection, and asbestos removal, reflecting the services offered by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_47ae2951587d3a17
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data store for services
services = {
    'pipe_cleaning': [],
    'leak_detection': [],
    'asbestos_removal': []
}

# Error response helper
def error_response(message, code):
    return jsonify({'error': message}), code

@app.route('/services/pipe_cleaning', methods=['GET', 'POST'])
def pipe_cleaning():
    # GET all pipe cleaning requests
    if request.method == 'GET':
        return jsonify(services['pipe_cleaning'])

    # POST a new pipe cleaning request
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'description' not in data:
            return error_response("Invalid data. 'description' is required.", 400)
        services['pipe_cleaning'].append(data)
        return jsonify(data), 201

@app.route('/services/leak_detection', methods=['GET', 'POST'])
def leak_detection():
    # GET all leak detection requests
    if request.method == 'GET':
        return jsonify(services['leak_detection'])

    # POST a new leak detection request
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'location' not in data:
            return error_response("Invalid data. 'location' is required.", 400)
        services['leak_detection'].append(data)
        return jsonify(data), 201

@app.route('/services/asbestos_removal', methods=['GET', 'POST'])
def asbestos_removal():
    # GET all asbestos removal requests
    if request.method == 'GET':
        return jsonify(services['asbestos_removal'])

    # POST a new asbestos removal request
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'area' not in data:
            return error_response("Invalid data. 'area' is required.", 400)
        services['asbestos_removal'].append(data)
        return jsonify(data), 201

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
