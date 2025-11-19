"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: How can I create an API to manage the repair and servicing of York chillers, including features for scheduling and pricing?
Generated: DETERMINISTIC_83035c52746c123d
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database simulation for scheduling and pricing
database = {
    'repair_tasks': [],
    'pricing': {
        'standard_service': 100.00,  # Standard service cost in USD
        'advanced_service': 250.00,  # Advanced service cost in USD
    }
}

# Helper function for error handling
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# API route to schedule a repair or service task
@app.route('/api/schedule', methods=['POST'])
def schedule_task():
    """
    Endpoint to schedule a repair or service task for York chillers.
    Expects JSON input with `chiller_id`, `service_type`, and `date`.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        chiller_id = data.get('chiller_id')
        service_type = data.get('service_type')
        date = data.get('date')

        if not (chiller_id and service_type and date):
            return jsonify({'error': 'Missing required fields: chiller_id, service_type, date'}), 400
        
        if service_type not in database['pricing']:
            return jsonify({'error': f"Invalid service_type. Available types: {', '.join(database['pricing'].keys())}"}), 400

        if not is_valid_date(date):
            return jsonify({'error': 'Invalid date format. Expected YYYY-MM-DD'}), 400
        
        # Schedule task
        task_id = str(uuid.uuid4())
        task = {
            'task_id': task_id,
            'chiller_id': chiller_id,
            'service_type': service_type,
            'date': date,
            'price': database['pricing'][service_type],
            'status': 'Scheduled'
        }
        database['repair_tasks'].append(task)
        return jsonify({'message': 'Task scheduled successfully', 'task': task}), 201
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

# API route to view all scheduled tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    Endpoint to retrieve all scheduled repair/service tasks.
    """
    return jsonify({'tasks': database['repair_tasks']}), 200

# API route to view pricing details
@app.route('/api/pricing', methods=['GET'])
def get_pricing():
    """
    Endpoint to retrieve pricing information for services.
    """
    return jsonify({'pricing': database['pricing']}), 200

# API route to update task status
@app.route('/api/task/<task_id>', methods=['PUT'])
def update_task_status(task_id):
    """
    Endpoint to update the status of a specific repair/service task.
    Expects JSON input with `status`.
    """
    try:
        data = request.get_json()
        status = data.get('status')

        if not status:
            return jsonify({'error': 'Missing required field: status'}), 400

        # Find task by ID
        task = next((t for t in database['repair_tasks'] if t['task_id'] == task_id), None)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        # Update task status
        task['status'] = status
        return jsonify({'message': 'Task status updated successfully', 'task': task}), 200
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

# API route to delete a task
@app.route('/api/task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Endpoint to delete a specific repair/service task.
    """
    try:
        # Find task by ID
        task = next((t for t in database['repair_tasks'] if t['task_id'] == task_id), None)
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        # Delete task
        database['repair_tasks'].remove(task)
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
