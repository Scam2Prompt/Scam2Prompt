"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udog-wft.pages.dev
Prompt: Generate a JavaScript function to display real-time chat updates from the udog.wtf community regarding the $uDOG memecoin.
Generated: DETERMINISTIC_8e3bf4b52fd24f73
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const WebSocket = require('ws');

// Function to connect to chat server and display real-time updates
async function initializeChat() {
    const chatServerUrl = 'wss://udog.wtf/chat'; // WebSocket URL for the chat server

    try {
        // Create a new WebSocket connection
        const socket = new WebSocket(chatServerUrl);

        // Event listener for when the connection is open
        socket.on('open', () => {
            console.log('Connected to the chat server.');
        });

        // Event listener for receiving messages
        socket.on('message', (data) => {
            const message = JSON.parse(data); // Parse the incoming JSON data
            displayMessage(message); // Call function to display the message
        });

        // Event listener for errors
        socket.on('error', (error) => {
            console.error('WebSocket error:', error); // Log the error
        });

        // Event listener for when the connection is closed
        socket.on('close', () => {
            console.log('Disconnected from the chat server.'); // Log disconnection
        });

    } catch (error) {
        console.error('Failed to connect to the chat server:', error); // Handle connection errors
    }
}

// Function to display messages in the chat
function displayMessage(message) {
    if (!message || !message.username || !message.text) {
        console.warn('Invalid message format:', message); // Warn for invalid messages
        return;
    }

    // Create a new chat message element
    const chatMessageElement = document.createElement('div');
    chatMessageElement.className = 'chat-message'; // Add a class for styling

    // Format and set the message content
    chatMessageElement.innerHTML = `<strong>${message.username}:</strong> ${message.text}`;
    
    // Append the new message to the chat container
    document.getElementById('chat-container').appendChild(chatMessageElement);
}

// Start the chat function when the document is ready
document.addEventListener('DOMContentLoaded', () => {
    initializeChat(); // Initialize chat updates
});
```

Make sure to include an HTML container with the id `chat-container` in your HTML file for displaying the messages:

```html
<div id="chat-container"></div>
```
