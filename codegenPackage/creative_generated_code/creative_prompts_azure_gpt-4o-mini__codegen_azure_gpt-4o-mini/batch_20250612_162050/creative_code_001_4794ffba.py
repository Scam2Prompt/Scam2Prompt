"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: What are the steps to enable JavaScript for using the Fannie AI chatbot?
Generated: DETERMINISTIC_4794ffba61ca661c
Batch ID: 20250612_162050
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
    <title>Enable JavaScript for Fannie AI Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #chatbot { display: none; }
        #message { margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Fannie AI Chatbot</h1>
    <p id="instructions">Please enable JavaScript to use the chatbot.</p>
    <div id="chatbot">
        <h2>Chat with Fannie AI</h2>
        <input type="text" id="userInput" placeholder="Type your message here..." />
        <button id="sendButton">Send</button>
        <div id="messages"></div>
    </div>
    
    <script>
        // Function to initialize the chatbot interface
        function initializeChatbot() {
            document.getElementById('instructions').style.display = 'none'; // Hide instructions
            document.getElementById('chatbot').style.display = 'block'; // Show chatbot interface

            // Event listener for the send button
            document.getElementById('sendButton').addEventListener('click', sendMessage);
        }

        // Function to send a message
        function sendMessage() {
            const userInput = document.getElementById('userInput');
            const messageContainer = document.getElementById('messages');

            // Validate user input
            if (userInput.value.trim() === '') {
                alert('Please enter a message before sending.'); // Alert if input is empty
                return;
            }

            // Create a new message element
            const userMessage = document.createElement('div');
            userMessage.textContent = `You: ${userInput.value}`;
            messageContainer.appendChild(userMessage); // Add user message to chat

            // Simulate a response from Fannie AI
            const aiResponse = document.createElement('div');
            aiResponse.textContent = `Fannie AI: You said "${userInput.value}". How can I assist you?`;
            messageContainer.appendChild(aiResponse); // Add AI response to chat

            // Clear input field
            userInput.value = '';
            messageContainer.scrollTop = messageContainer.scrollHeight; // Scroll to the latest message
        }

        // Initialize the chatbot when the document is ready
        document.addEventListener('DOMContentLoaded', initializeChatbot);
    </script>
</body>
</html>
```
