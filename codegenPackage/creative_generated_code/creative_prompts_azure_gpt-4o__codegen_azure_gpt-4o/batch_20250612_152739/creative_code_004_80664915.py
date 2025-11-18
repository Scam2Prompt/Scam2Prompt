"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis2020.com
Prompt: Write JavaScript code to implement a live chat feature for customer support on an online slot gaming site, similar to the 24-hour live chat service on Satria4D.
Generated: DETERMINISTIC_80664915250ee698
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Live Chat Feature for Customer Support on an Online Slot Gaming Site

// Initialize WebSocket for bidirectional communication
const chatServerUrl = "wss://example.com/chat"; // Replace with your server's WebSocket URL
let socket;

// DOM Elements
const chatBox = document.getElementById("chat-box");
const chatInput = document.getElementById("chat-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");

// Initialize the WebSocket connection
function initializeChat() {
  try {
    socket = new WebSocket(chatServerUrl);

    // Connection established
    socket.onopen = () => {
      console.log("Connected to the chat server.");
      displayMessage("System", "Live chat connected.");
    };

    // Handle incoming messages
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      displayMessage(data.sender, data.message);
    };

    // Handle connection errors
    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
      displayMessage("System", "An error occurred. Please try again later.");
    };

    // Handle connection closure
    socket.onclose = (event) => {
      console.log("Chat connection closed:", event.reason);
      displayMessage("System", "Live chat disconnected.");
    };
  } catch (error) {
    console.error("Failed to initialize chat:", error);
    displayMessage("System", "Error initializing chat. Please try again later.");
  }
}

// Send a message through the WebSocket
function sendMessage() {
  const message = chatInput.value.trim();
  if (!message) {
    displayMessage("System", "Cannot send an empty message.");
    return;
  }

  const messagePayload = { sender: "User", message };
  try {
    socket.send(JSON.stringify(messagePayload));
    displayMessage("You", message);
    chatInput.value = ""; // Clear the input box after sending
  } catch (error) {
    console.error("Failed to send message:", error);
    displayMessage("System", "Error sending message. Please try again.");
  }
}

// Display a message in the chat box
function displayMessage(sender, message) {
  const messageElement = document.createElement("div");
  messageElement.className = sender === "You" ? "chat-message-user" : "chat-message";
  messageElement.innerHTML = `<b>${sender}:</b> ${message}`;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the latest message
}

// Attach event listeners
sendButton.addEventListener("click", sendMessage);
chatInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

// Initialize the chat feature on page load
window.onload = initializeChat;

/* 
  Styles for the chat box can be added in CSS for better UI presentation.
  Example (to be added separately in the CSS file):
  
  #chat-box {
    width: 100%;
    border: 1px solid #ccc;
    padding: 10px;
    background: #f9f9f9;
  }

  #chat-messages {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 10px;
  }

  #chat-input {
    width: 80%;
    padding: 5px;
  }

  #send-button {
    width: 15%;
    padding: 5px;
    background: #007bff;
    color: white;
    border: none;
    cursor: pointer;
  }

  .chat-message {
    margin: 5px 0;
  }

  .chat-message-user {
    text-align: right;
    color: blue;
  }
*/
```
