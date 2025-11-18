"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter.graphy.com
Prompt: Write code to implement live video streaming with real-time chat functionality for an online learning platform, similar to the live learning sessions described on Jupiter Swap™.
Generated: DETERMINISTIC_1e360fe1ecba05b5
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, Response, request
import cv2
import threading
import socket
import json

# Initialize Flask app
app = Flask(__name__)

# Global variable to store the video frame
video_frame = None
clients = []

# Function to capture video from the webcam
def capture_video():
    global video_frame
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Encode the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        video_frame = buffer.tobytes()

    cap.release()

# Function to stream video frames
def generate_frames():
    global video_frame
    while True:
        if video_frame is not None:
            # Yield the video frame in a format suitable for the client
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + video_frame + b'\r\n')

# Route for the video streaming page
@app.route('/')
def index():
    return render_template('index.html')

# Route for streaming video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# WebSocket for real-time chat
@app.route('/chat', methods=['POST'])
def chat():
    message_data = request.json
    if not message_data or 'username' not in message_data or 'message' not in message_data:
        return {'error': 'Invalid message format'}, 400
    
    # Broadcast message to all connected clients
    for client in clients:
        client.send(json.dumps(message_data))
    
    return {'status': 'Message sent'}, 200

# Function to handle client connections for chat
def handle_client_connection(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                # Process incoming chat messages
                message_data = json.loads(message.decode('utf-8'))
                chat(message_data)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

# Start the video capture in a separate thread
video_thread = threading.Thread(target=capture_video)
video_thread.daemon = True
video_thread.start()

if __name__ == '__main__':
    try:
        # Start the Flask app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Streaming</title>
    <style>
        #video {
            width: 100%;
            max-width: 600px;
        }
    </style>
</head>
<body>
    <h1>Live Video Streaming</h1>
    <img id="video" src="{{ url_for('video_feed') }}" alt="Live Video Stream">

    <h2>Chat</h2>
    <div id="chat-box"></div>
    <input type="text" id="username" placeholder="Username">
    <input type="text" id="message" placeholder="Message">
    <button onclick="sendMessage()">Send</button>

    <script>
        const chatBox = document.getElementById('chat-box');

        function sendMessage() {
            const username = document.getElementById('username').value;
            const message = document.getElementById('message').value;
            
            if (!username || !message) {
                alert('Please enter both username and message.');
                return;
            }

            // Send message to server
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, message }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    appendMessage(username, message);
                }
            })
            .catch(error => console.error('Error:', error));
        }

        function appendMessage(username, message) {
            const msgElement = document.createElement('div');
            msgElement.textContent = `${username}: ${message}`;
            chatBox.appendChild(msgElement);
        }
    </script>
</body>
</html>
```

**Note:** Make sure to have Flask and OpenCV installed in your Python environment, and run the Flask application with proper testing. The chat feature in this simple implementation doesn't include WebSocket for real-time messaging, you'll need to implement that separately for true real-time chat functionality.
