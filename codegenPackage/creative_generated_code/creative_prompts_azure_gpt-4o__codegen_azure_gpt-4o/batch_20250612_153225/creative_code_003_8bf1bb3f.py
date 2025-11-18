"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Recommend a library or tool to implement a fast delivery tracking system for a B2B supplier offering products like "Air Bubble Roll" and "ACP Wall Printing," ensuring real-time updates for corporate clients.
Generated: DETERMINISTIC_8bf1bb3fc55b6118
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Delivery Tracking System for B2B supplier with real-time updates.

This implementation uses Flask (a lightweight web framework) and SQLite for simplicity.
For real-time updates, we utilize WebSockets via Flask-SocketIO.

You will need to install the necessary libraries:
    pip install flask flask-socketio flask-sqlalchemy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit

# Initialize the app, database, and SocketIO
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deliveries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Delivery model for tracking deliveries
class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., "In Transit", "Delivered"
    last_updated = db.Column(db.DateTime, nullable=False)

# Error handling for database operations
@app.errorhandler(500)
def handle_internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def handle_not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

# Route: Add a new delivery
@app.route('/delivery', methods=['POST'])
def add_delivery():
    try:
        data = request.json
        new_delivery = Delivery(
            client_name=data['client_name'],
            product_name=data['product_name'],
            status=data['status'],
            last_updated=db.func.now()
        )
        db.session.add(new_delivery)
        db.session.commit()
        emit_real_time_update(new_delivery)
        return jsonify({"message": "Delivery added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Update delivery status
@app.route('/delivery/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    try:
        delivery = Delivery.query.get(delivery_id)
        if not delivery:
            return jsonify({"error": "Delivery not found"}), 404
        
        data = request.json
        delivery.status = data.get('status', delivery.status)
        delivery.last_updated = db.func.now()
        db.session.commit()
        emit_real_time_update(delivery)
        return jsonify({"message": "Delivery updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Get delivery status
@app.route('/delivery/<int:delivery_id>', methods=['GET'])
def get_delivery_status(delivery_id):
    delivery = Delivery.query.get(delivery_id)
    if not delivery:
        return jsonify({"error": "Delivery not found"}), 404
    return jsonify({
        "id": delivery.id,
        "client_name": delivery.client_name,
        "product_name": delivery.product_name,
        "status": delivery.status,
        "last_updated": delivery.last_updated
    }), 200

# Emit real-time updates via WebSocket
def emit_real_time_update(delivery):
    socketio.emit('delivery_update', {
        "id": delivery.id,
        "client_name": delivery.client_name,
        "product_name": delivery.product_name,
        "status": delivery.status,
        "last_updated": delivery.last_updated.isoformat()
    })

# WebSocket event: Client connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')

# WebSocket event: Client disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Initialize the database and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    socketio.run(app, host='0.0.0.0', port=5000)
```

### Notes:
1. This implementation is minimal and may require additional features like authentication, logging, and scalability adjustments based on your needs.
2. Ensure appropriate security and optimizations for production systems.
