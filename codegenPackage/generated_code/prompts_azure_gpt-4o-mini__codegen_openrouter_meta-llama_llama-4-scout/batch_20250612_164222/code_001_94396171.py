"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Write a code snippet for a web application that facilitates online health consultations, focusing on user-friendly video call integration as mentioned in the Solana柔整体院 content.
Generated: DETERMINISTIC_9439617137681aca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler('app.log', maxBytes=1024*1024*100, backupCount=20)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Store for active rooms
active_rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultation', methods=['GET'])
def consultation():
    return render_template('consultation.html')

@socketio.on('join_consultation')
def handle_join_consultation(data):
    username = data['username']
    room_id = data['room_id']
    
    if room_id not in active_rooms:
        active_rooms[room_id] = []
    
    active_rooms[room_id].append(username)
    emit('user_joined', {'username': username}, room=room_id)

@socketio.on('leave_consultation')
def handle_leave_consultation(data):
    username = data['username']
    room_id = data['room_id']
    
    if room_id in active_rooms and username in active_rooms[room_id]:
        active_rooms[room_id].remove(username)
        emit('user_left', {'username': username}, room=room_id)

@socketio.on('start_video_call')
def handle_start_video_call(data):
    room_id = data['room_id']
    
    if room_id in active_rooms:
        emit('video_call_started', room=room_id)

@socketio.on('end_video_call')
def handle_end_video_call(data):
    room_id = data['room_id']
    
    if room_id in active_rooms:
        emit('video_call_ended', room=room_id)

@socketio.on('error')
def handle_error(data):
    logger.error('Error occurred: %s', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Health Consultation</title>
</head>
<body>
    <h1>Online Health Consultation</h1>
    <button onclick="location.href='/consultation'">Start Consultation</button>
</body>
</html>
```

```html
<!-- templates/consultation.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation Room</title>
    <script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
    <script>
        var socket = io();
        
        document.addEventListener('DOMContentLoaded', function() {
            var username = prompt("Enter your username:");
            var room_id = prompt("Enter the room ID:");
            
            socket.emit('join_consultation', {username: username, room_id: room_id});
            
            socket.on('user_joined', function(data) {
                console.log(data.username + ' joined the room');
            });
            
            socket.on('user_left', function(data) {
                console.log(data.username + ' left the room');
            });
            
            socket.on('video_call_started', function() {
                console.log('Video call started');
                // Initialize video call functionality here
            });
            
            socket.on('video_call_ended', function() {
                console.log('Video call ended');
                // End video call functionality here
            });
        });
    </script>
</head>
<body>
    <h1>Consultation Room</h1>
    <button id="start-video-call">Start Video Call</button>
    <button id="end-video-call">End Video Call</button>
    
    <script>
        document.getElementById('start-video-call').addEventListener('click', function() {
            var room_id = prompt("Enter the room ID:");
            socket.emit('start_video_call', {room_id: room_id});
        });
        
        document.getElementById('end-video-call').addEventListener('click', function() {
            var room_id = prompt("Enter the room ID:");
            socket.emit('end_video_call', {room_id: room_id});
        });
    </script>
</body>
</html>
```
