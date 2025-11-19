"""
Generated Code Metadata:
========================
Original URL: https://seubolodecorado.com.br
Prompt: Illustrate how to implement a notification system in a web application that alerts users when their custom Bentô Cake order is ready for pickup.
Generated: DETERMINISTIC_4b89e377c4deffb0
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import datetime
import os
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///orders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and SocketIO
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Database models
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, preparing, ready, picked_up
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Error handling
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

# API Endpoints
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        user_id = data['user_id']
        
        new_order = Order(user_id=user_id)
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return handle_error(e)

@app.route('/orders/<int:order_id>/ready', methods=['PUT'])
def mark_order_ready(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        order.status = 'ready'
        db.session.commit()
        
        # Notify user via WebSocket
        socketio.emit('order_ready', {'order_id': order.id, 'user_id': order.user_id}, room=f'user_{order.user_id}')
        
        return jsonify(order.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return handle_error(e)

# WebSocket handlers
@socketio.on('connect')
def handle_connect():
    user_id = request.args.get('user_id')
    if user_id:
        socketio.server.enter_room(request.sid, f'user_{user_id}')
        emit('connection_success', {'message': f'Connected to notifications for user {user_id}'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    socketio.run(app, debug=True)
```

```javascript
// Frontend implementation (using JavaScript with Socket.IO)
document.addEventListener('DOMContentLoaded', function() {
    const userId = 123; // This would typically come from user session
    
    // Connect to WebSocket
    const socket = io({
        query: { user_id: userId }
    });
    
    // Handle connection success
    socket.on('connection_success', function(data) {
        console.log(data.message);
    });
    
    // Handle order ready notification
    socket.on('order_ready', function(data) {
        if (data.user_id === userId) {
            showNotification(`Your Bento Cake order #${data.order_id} is ready for pickup!`);
        }
    });
    
    // Function to display notification
    function showNotification(message) {
        if (!("Notification" in window)) {
            console.log("This browser does not support notifications");
            return;
        }
        
        if (Notification.permission === "granted") {
            new Notification(message);
        } else if (Notification.permission !== "denied") {
            Notification.requestPermission().then(function(permission) {
                if (permission === "granted") {
                    new Notification(message);
                }
            });
        }
    }
    
    // Example function to place an order (would be called from UI)
    function placeOrder() {
        fetch('/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId })
        })
        .then(response => response.json())
        .then(data => console.log('Order created:', data))
        .catch(error => console.error('Error:', error));
    }
});
```
