"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Provide a code example for integrating virtual assistants into a smart home system, based on the insights from the "Asistentes Virtuales" section.
Generated: DETERMINISTIC_06592e41d3e8f442
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for storing device states
device_states = {
    'lights': False,
    'thermostat': 22,
    'door_locks': False
}

@app.route('/api/device/<device_name>', methods=['GET', 'POST', 'PUT'])
def manage_device(device_name):
    """
    Manage smart home devices via RESTful API.
    
    Args:
        device_name (str): The name of the device to manage.
    
    Returns:
        JSON response indicating the device state or an error message.
    """
    try:
        if request.method == 'GET':
            # Return the current state of the requested device
            if device_name in device_states:
                return jsonify({device_name: device_states[device_name]}), 200
            else:
                return jsonify({'error': 'Device not found'}), 404
        
        elif request.method == 'POST':
            # Turn on the device (if applicable)
            if device_name in device_states:
                if device_name == 'lights':
                    device_states[device_name] = True
                    return jsonify({'status': 'Lights turned on'}), 200
                else:
                    return jsonify({'error': 'Cannot turn on this device'}), 400

        elif request.method == 'PUT':
            # Update device state based on the provided data
            data = request.json
            if device_name == 'thermostat' and 'temperature' in data:
                device_states[device_name] = data['temperature']
                return jsonify({'status': 'Thermostat updated', 'temperature': device_states[device_name]}), 200
            elif device_name == 'door_locks':
                device_states[device_name] = data.get('lock', device_states[device_name])
                return jsonify({'status': 'Door lock status updated', 'locked': device_states[device_name]}), 200
            else:
                return jsonify({'error': 'Invalid data provided'}), 400

        return jsonify({'error': 'Method not allowed'}), 405

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
