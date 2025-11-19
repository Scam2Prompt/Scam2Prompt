"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Write a code snippet to create a web panel for scheduling and editing property inspections, inspired by the functionalities of the BeSoft app.
Generated: DETERMINISTIC_7737b86c2f2068a6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for property inspections (for demonstration purposes)
inspections = {}

# Helper function to validate date format
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

@app.route('/')
def home():
    # Render a simple HTML page for scheduling and editing inspections
    return render_template('index.html')

@app.route('/inspections', methods=['GET'])
def get_inspections():
    """
    Endpoint to retrieve all scheduled inspections.
    """
    return jsonify(list(inspections.values())), 200

@app.route('/inspections', methods=['POST'])
def create_inspection():
    """
    Endpoint to schedule a new property inspection.
    """
    data = request.json
    try:
        # Validate required fields
        property_id = data.get('property_id')
        inspector_name = data.get('inspector_name')
        scheduled_time = data.get('scheduled_time')

        if not property_id or not inspector_name or not scheduled_time:
            return jsonify({'error': 'Missing required fields'}), 400

        if not validate_date(scheduled_time):
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS'}), 400

        # Create a new inspection
        inspection_id = str(uuid.uuid4())
        inspections[inspection_id] = {
            'id': inspection_id,
            'property_id': property_id,
            'inspector_name': inspector_name,
            'scheduled_time': scheduled_time,
            'status': 'Scheduled'
        }

        return jsonify(inspections[inspection_id]), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inspections/<inspection_id>', methods=['PUT'])
def update_inspection(inspection_id):
    """
    Endpoint to edit an existing property inspection.
    """
    if inspection_id not in inspections:
        return jsonify({'error': 'Inspection not found'}), 404

    data = request.json
    try:
        # Update fields if provided
        if 'property_id' in data:
            inspections[inspection_id]['property_id'] = data['property_id']
        if 'inspector_name' in data:
            inspections[inspection_id]['inspector_name'] = data['inspector_name']
        if 'scheduled_time' in data:
            if not validate_date(data['scheduled_time']):
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS'}), 400
            inspections[inspection_id]['scheduled_time'] = data['scheduled_time']
        if 'status' in data:
            inspections[inspection_id]['status'] = data['status']

        return jsonify(inspections[inspection_id]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inspections/<inspection_id>', methods=['DELETE'])
def delete_inspection(inspection_id):
    """
    Endpoint to delete a property inspection.
    """
    if inspection_id not in inspections:
        return jsonify({'error': 'Inspection not found'}), 404

    try:
        del inspections[inspection_id]
        return jsonify({'message': 'Inspection deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Note:** To make this code fully functional, you need to create an `index.html` file in a `templates` directory for the web panel UI. The file can include a simple form and JavaScript to interact with the API endpoints.
