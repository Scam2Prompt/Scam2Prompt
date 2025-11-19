"""
Generated Code Metadata:
========================
Original URL: https://availlabs.net
Prompt: Develop a solution for live chat integration to improve communication and support for swag management, similar to the dedicated support feature mentioned on Avail Labs' website.
Generated: DETERMINISTIC_b773268a8d04883b
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from typing import Dict, Optional, List
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for chat messages (replace with database in production)
chat_rooms: Dict[str, List[Dict]] = {}
active_support_agents: Dict[str, Dict] = {}

class ChatManager:
    """Manages chat rooms and messages"""
    
    @staticmethod
    def create_chat_room(room_id: str) -> None:
        """Initialize a new chat room"""
        if room_id not in chat_rooms:
            chat_rooms[room_id] = []
    
    @staticmethod
    def add_message(room_id: str, sender: str, message: str, is_support: bool = False) -> Dict:
        """Add a message to a chat room"""
        if room_id not in chat_rooms:
            ChatManager.create_chat_room(room_id)
            
        msg = {
            'sender': sender,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'is_support': is_support
        }
        chat_rooms[room_id].append(msg)
        return msg
    
    @staticmethod
    def get_messages(room_id: str) -> List[Dict]:
        """Retrieve all messages for a chat room"""
        return chat_rooms.get(room_id, [])

class SupportAgentManager:
    """Manages support agent availability"""
    
    @staticmethod
    def register_agent(agent_id: str, agent_info: Dict) -> None:
        """Register a support agent as available"""
        active_support_agents[agent_id] = {
            **agent_info,
            'last_active': datetime.now().isoformat(),
            'available': True
        }
    
    @staticmethod
    def unregister_agent(agent_id: str) -> None:
        """Remove a support agent from availability"""
        if agent_id in active_support_agents:
            del active_support_agents[agent_id]
    
    @staticmethod
    def get_available_agent() -> Optional[Dict]:
        """Get the first available support agent"""
        for agent_id, agent_info in active_support_agents.items():
            if agent_info.get('available', False):
                return agent_info
        return None

# REST API Endpoints
@app.route('/api/chat/<room_id>', methods=['GET'])
def get_chat_messages(room_id: str):
    """Get all messages for a chat room"""
    try:
        messages = ChatManager.get_messages(room_id)
        return jsonify({'status': 'success', 'messages': messages})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/chat/<room_id>/send', methods=['POST'])
def send_message(room_id: str):
    """Send a message to a chat room"""
    try:
        data = request.get_json()
        sender = data.get('sender')
        message = data.get('message')
        is_support = data.get('is_support', False)
        
        if not sender or not message:
            return jsonify({'status': 'error', 'message': 'Missing sender or message'}), 400
            
        msg = ChatManager.add_message(room_id, sender, message, is_support)
        socketio.emit('new_message', {'room_id': room_id, 'message': msg})
        return jsonify({'status': 'success', 'message': msg})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/support/agents', methods=['GET'])
def get_available_agents():
    """Get list of available support agents"""
    try:
        available_agents = [
            agent for agent in active_support_agents.values() 
            if agent.get('available', False)
        ]
        return jsonify({'status': 'success', 'agents': available_agents})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# WebSocket Handlers
@socketio.on('connect')
def handle_connect():
    """Handle new WebSocket connection"""
    emit('connection_response', {'status': 'connected'})

@socketio.on('join_room')
def handle_join_room(data):
    """Handle joining a chat room"""
    room_id = data.get('room_id')
    if room_id:
        socketio.enter_room(request.sid, room_id)
        emit('room_joined', {'room_id': room_id})

@socketio.on('leave_room')
def handle_leave_room(data):
    """Handle leaving a chat room"""
    room_id = data.get('room_id')
    if room_id:
        socketio.leave_room(request.sid, room_id)
        emit('room_left', {'room_id': room_id})

@socketio.on('register_agent')
def handle_register_agent(data):
    """Handle support agent registration"""
    agent_id = data.get('agent_id')
    if agent_id:
        SupportAgentManager.register_agent(agent_id, data)
        emit('agent_registered', {'status': 'success', 'agent_id': agent_id})

@socketio.on('unregister_agent')
def handle_unregister_agent(data):
    """Handle support agent unregistration"""
    agent_id = data.get('agent_id')
    if agent_id:
        SupportAgentManager.unregister_agent(agent_id)
        emit('agent_unregistered', {'status': 'success', 'agent_id': agent_id})

# Frontend Route
@app.route('/chat')
def chat_interface():
    """Render the chat interface"""
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
```
