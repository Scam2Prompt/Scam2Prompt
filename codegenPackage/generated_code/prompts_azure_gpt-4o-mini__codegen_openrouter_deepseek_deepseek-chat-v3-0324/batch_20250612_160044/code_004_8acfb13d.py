"""
Generated Code Metadata:
========================
Original URL: https://tante4dx40.com
Prompt: What are the best practices for implementing a live chat support feature on a gaming website like TANTE4D?
Generated: DETERMINISTIC_8acfb13df9d5924d
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
import time
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
from typing import Dict, List, Optional
import uuid
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure logging
log_handler = RotatingFileHandler('chat.log', maxBytes=1000000, backupCount=5)
log_handler.setLevel(logging.INFO)
app.logger.addHandler(log_handler)

# In-memory storage for demo purposes (replace with database in production)
active_users: Dict[str, Dict] = {}
chat_rooms: Dict[str, Dict] = {}
support_agents: Dict[str, Dict] = {}
message_history: Dict[str, List[Dict]] = {}

class ChatManager:
    @staticmethod
    def create_chat_room(user_id: str) -> str:
        """Create a new chat room for user support"""
        room_id = str(uuid.uuid4())
        chat_rooms[room_id] = {
            'user_id': user_id,
            'agent_id': None,
            'created_at': datetime.utcnow().isoformat(),
            'status': 'waiting'
        }
        message_history[room_id] = []
        return room_id

    @staticmethod
    def assign_agent(room_id: str, agent_id: str) -> bool:
        """Assign a support agent to a chat room"""
        if room_id not in chat_rooms:
            return False
        
        chat_rooms[room_id]['agent_id'] = agent_id
        chat_rooms[room_id]['status'] = 'active'
        return True

    @staticmethod
    def add_message(room_id: str, sender_id: str, message: str, sender_type: str) -> bool:
        """Add a message to the chat history"""
        if room_id not in message_history:
            return False
        
        message_data = {
            'id': str(uuid.uuid4()),
            'sender_id': sender_id,
            'sender_type': sender_type,
            'message': message,
            'timestamp': datetime.utcnow().isoformat()
        }
        message_history[room_id].append(message_data)
        return True

    @staticmethod
    def close_chat_room(room_id: str) -> bool:
        """Close a chat room"""
        if room_id not in chat_rooms:
            return False
        
        chat_rooms[room_id]['status'] = 'closed'
        chat_rooms[room_id]['closed_at'] = datetime.utcnow().isoformat()
        return True

# WebSocket event handlers
@socketio.on('connect')
def handle_connect():
    app.logger.info(f"Client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    app.logger.info(f"Client disconnected: {request.sid}")
    # Clean up user data on disconnect
    for user_id, data in active_users.items():
        if data['socket_id'] == request.sid:
            del active_users[user_id]
            break

@socketio.on('join_chat')
def handle_join_chat(data):
    try:
        user_id = data['user_id']
        user_type = data['user_type']
        
        active_users[user_id] = {
            'socket_id': request.sid,
            'user_type': user_type,
            'joined_at': datetime.utcnow().isoformat()
        }
        
        if user_type == 'user':
            room_id = ChatManager.create_chat_room(user_id)
            join_room(room_id)
            emit('room_created', {'room_id': room_id, 'status': 'waiting'})
        elif user_type == 'agent':
            emit('agent_ready', {'message': 'You are now available for chat support'})
        
    except Exception as e:
        app.logger.error(f"Error in join_chat: {str(e)}")
        emit('error', {'message': 'Failed to join chat'})

@socketio.on('send_message')
def handle_send_message(data):
    try:
        room_id = data['room_id']
        sender_id = data['sender_id']
        message = data['message']
        sender_type = data['sender_type']
        
        if not ChatManager.add_message(room_id, sender_id, message, sender_type):
            emit('error', {'message': 'Failed to send message'})
            return
        
        emit('new_message', {
            'sender_id': sender_id,
            'sender_type': sender_type,
            'message': message,
            'timestamp': datetime.utcnow().isoformat()
        }, room=room_id)
        
    except Exception as e:
        app.logger.error(f"Error in send_message: {str(e)}")
        emit('error', {'message': 'Failed to send message'})

@socketio.on('agent_join')
def handle_agent_join(data):
    try:
        room_id = data['room_id']
        agent_id = data['agent_id']
        
        if not ChatManager.assign_agent(room_id, agent_id):
            emit('error', {'message': 'Failed to join chat room'})
            return
        
        join_room(room_id)
        emit('agent_joined', {'agent_id': agent_id}, room=room_id)
        
    except Exception as e:
        app.logger.error(f"Error in agent_join: {str(e)}")
        emit('error', {'message': 'Failed to join chat room'})

@socketio.on('end_chat')
def handle_end_chat(data):
    try:
        room_id = data['room_id']
        
        if not ChatManager.close_chat_room(room_id):
            emit('error', {'message': 'Failed to close chat room'})
            return
        
        emit('chat_ended', {'message': 'Chat session has ended'}, room=room_id)
        leave_room(room_id)
        
    except Exception as e:
        app.logger.error(f"Error in end_chat: {str(e)}")
        emit('error', {'message': 'Failed to end chat'})

# HTTP endpoints
@app.route('/chat/history/<room_id>', methods=['GET'])
def get_chat_history(room_id):
    try:
        if room_id not in message_history:
            return jsonify({'error': 'Room not found'}), 404
        
        return jsonify({
            'status': 'success',
            'messages': message_history[room_id]
        })
    except Exception as e:
        app.logger.error(f"Error in get_chat_history: {str(e)}")
        return jsonify({'error': 'Failed to retrieve chat history'}), 500

@app.route('/chat/status/<user_id>', methods=['GET'])
def get_chat_status(user_id):
    try:
        for room_id, room_data in chat_rooms.items():
            if room_data['user_id'] == user_id:
                return jsonify({
                    'status': 'success',
                    'room_id': room_id,
                    'chat_status': room_data['status']
                })
        
        return jsonify({'status': 'not_found'})
    except Exception as e:
        app.logger.error(f"Error in get_chat_status: {str(e)}")
        return jsonify({'error': 'Failed to check chat status'}), 500

@app.route('/chat/available_agents', methods=['GET'])
def get_available_agents():
    try:
        available = [agent_id for agent_id, data in support_agents.items() if data['is_available']]
        return jsonify({
            'status': 'success',
            'available_agents': available
        })
    except Exception as e:
        app.logger.error(f"Error in get_available_agents: {str(e)}")
        return jsonify({'error': 'Failed to retrieve available agents'}), 500

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
```
