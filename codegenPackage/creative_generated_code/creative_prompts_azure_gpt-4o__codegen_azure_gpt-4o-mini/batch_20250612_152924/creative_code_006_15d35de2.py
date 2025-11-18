"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueraygroup.com
Prompt: Suggest libraries to build a real-time notification system for shipment status updates, tailored for a logistics company like Blue Ray Logistic.
Generated: DETERMINISTIC_15d35de21072a446
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import json
import threading
from queue import Queue
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

# Initialize Flask application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# In-memory queue to hold shipment status updates
shipment_updates_queue = Queue()

# Sample data structure to hold shipment data
shipments = {
    1: {"status": "Pending", "location": "Warehouse A"},
    2: {"status": "In Transit", "location": "Warehouse B"},
}

def process_updates():
    """Background thread to process shipment updates."""
    while True:
        # Wait for an update from the queue
        shipment_id, new_status = shipment_updates_queue.get()
        if shipment_id is None:
            break  # Exit the thread if None is received
        # Update shipment status
        if shipment_id in shipments:
            shipments[shipment_id]['status'] = new_status
            # Emit the new status to all connected clients
            socketio.emit('shipment_update', {'id': shipment_id, 'status': new_status})
        shipment_updates_queue.task_done()

@app.route('/update_shipment', methods=['POST'])
def update_shipment():
    """
    Endpoint to update shipment status.
    Expects JSON data with shipment id and new status.
    """
    try:
        data = request.get_json()
        shipment_id = data['id']
        new_status = data['status']

        # Validate input data
        if shipment_id not in shipments:
            return jsonify({'error': 'Invalid shipment ID'}), 400

        # Enqueue the update for processing
        shipment_updates_queue.put((shipment_id, new_status))
        return jsonify({'message': 'Shipment status updated successfully'}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/shipments', methods=['GET'])
def get_shipments():
    """Endpoint to retrieve the current shipment statuses."""
    return jsonify(shipments), 200

if __name__ == '__main__':
    # Start the background thread for processing updates
    update_thread = threading.Thread(target=process_updates)
    update_thread.start()

    # Run the application
    socketio.run(app, host='0.0.0.0', port=5000)

    # Clean up the thread upon exit
    update_thread.join()
```
