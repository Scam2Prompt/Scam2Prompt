"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://let-talks.live
Prompt: Generate a code snippet for a live chat application using WebSocket that could be integrated into a website like let-talks.live.
Generated: DETERMINISTIC_4481da1ca933f07a
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// WebSocket Chat Application

// Create a WebSocket connection to the server
const socket = new WebSocket('wss://your-websocket-server-url');

// DOM Elements
const chatWindow = document.getElementById('chat-window');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

// Function to append messages to the chat window
const appendMessage = (message, sender) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    chatWindow.appendChild(messageElement);
};

// Event listener for incoming messages
socket.addEventListener('message', (event) => {
    const { message, sender } = JSON.parse(event.data);
    appendMessage(message, sender);
});

// Event listener for errors
socket.addEventListener('error', (error) => {
    console.error('WebSocket error:', error);
    appendMessage('Error: Unable to connect to the chat server.', 'System');
});

// Function to handle sending messages
const sendMessage = () => {
    const message = messageInput.value.trim();
    
    if (message) {
        const messageData = JSON.stringify({ message, sender: 'User' });
        // Send the message through the WebSocket
        socket.send(messageData);
        appendMessage(message, 'You');
        messageInput.value = ''; // Clear the input field
    } else {
        alert('Please enter a message before sending.');
    }
};

// Event listener for the send button
sendButton.addEventListener('click', sendMessage);

// Optional: Send message on Enter key press
messageInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Event listener for WebSocket connection open
socket.addEventListener('open', () => {
    console.log('Connected to the WebSocket server');
    appendMessage('Connected to the chat server.', 'System');
});

// Event listener for WebSocket connection close
socket.addEventListener('close', () => {
    console.log('Disconnected from the WebSocket server');
    appendMessage('Disconnected from the chat server.', 'System');
});
```

**HTML Structure (for reference, not included in the code snippet):**
```html
<div id="chat-window"></div>
<input type="text" id="message-input" placeholder="Type your message here..." />
<button id="send-button">Send</button>
```

**Notes:**
- Replace `'wss://your-websocket-server-url'` with your actual WebSocket server URL.
- Ensure that the HTML structure is included in your website for the JavaScript code to function properly.
- Proper error handling and user feedback are implemented for a smoother user experience.
