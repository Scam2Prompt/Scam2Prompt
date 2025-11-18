"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Provide a code example for integrating a live chat feature into a home services website, similar to the "Open chat" functionality on شركة انجاز's webpage.
Generated: DETERMINISTIC_a433ae3d0c41e4e6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Services Live Chat</title>
    <!-- Include external CSS for styling -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="chat-container" class="chat-container">
        <div id="chat-header" class="chat-header" onclick="toggleChat()">
            <h4>Live Chat</h4>
        </div>
        <div id="chat-messages" class="chat-messages"></div>
        <input type="text" id="chat-input" class="chat-input" placeholder="Type your message..." onkeypress="handleKeyPress(event)" />
    </div>

    <!-- Include external JavaScript for functionality -->
    <script src="chat.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

/* Chat container styles */
.chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    background-color: #fff;
    border-radius: 5px;
    display: none; /* Hidden by default */
    flex-direction: column;
}

/* Chat header styles */
.chat-header {
    background-color: #007bff;
    color: white;
    padding: 10px;
    cursor: pointer;
}

/* Chat messages styles */
.chat-messages {
    padding: 10px;
    height: 200px;
    overflow-y: auto;
}

/* Input box styles */
.chat-input {
    border: none;
    padding: 10px;
    border-top: 1px solid #ccc;
}
```

```javascript
// chat.js

// Select DOM elements
const chatContainer = document.getElementById('chat-container');
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');

// Function to toggle the visibility of the chat container
function toggleChat() {
    if (chatContainer.style.display === "none" || chatContainer.style.display === "") {
        chatContainer.style.display = "flex";
    } else {
        chatContainer.style.display = "none";
    }
}

// Function to handle key presses in the input field
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission
        const message = chatInput.value.trim();
        if (message) {
            sendMessage(message);
            chatInput.value = ''; // Clear the input field
        }
    }
}

// Function to send a message and update the chat display
function sendMessage(message) {
    try {
        // Create a new message element
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-message';
        messageElement.textContent = message;

        // Append message to the chat messages container
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the bottom
    } catch (error) {
        console.error("Error sending message:", error);
        alert("There was an issue sending your message. Please try again.");
    }
}
```

### Note:
- This code creates a simple live chat interface. For a production-ready chat system, consider integrating it with a backend service for message persistence, user authentication, and real-time communication using WebSocket or similar technology.
