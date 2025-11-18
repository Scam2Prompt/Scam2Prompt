"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Develop a JavaScript-based chat widget for a library website, ensuring compatibility even when JavaScript is disabled, as noted in the Loyola University Chicago Libraries portal.
Generated: DETERMINISTIC_25269626e483c4cd
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library Chat Widget</title>
    <style>
        /* Basic styling for the chat widget */
        #chat-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            height: 400px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: none; /* Default hidden for compatibility */
        }

        #chat-header {
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            font-size: 16px;
            border-bottom: 1px solid #ccc;
            cursor: pointer;
            border-radius: 5px 5px 0 0;
        }

        #chat-messages {
            padding: 10px;
            overflow-y: auto;
            height: 300px;
        }

        #chat-input-container {
            border-top: 1px solid #ccc;
            padding: 10px;
        }

        #chat-input {
            width: 80%;
            padding: 5px;
        }

        #send-btn {
            width: 15%;
            padding: 5px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        #send-btn:hover {
            background-color: #0056b3;
        }

        .message {
            margin-bottom: 10px;
        }

        .message.user {
            text-align: right;
        }

        .message.system {
            text-align: left;
            color: #555;
        }

        /* Fallback styling for when JavaScript is disabled */
        .no-js #chat-widget {
            display: block;
        }
    </style>
</head>
<body class="no-js"> <!-- Default to no-js class -->

    <div id="chat-widget">
        <div id="chat-header">Chat with us</div>
        <div id="chat-messages">
            <p class="message system">Welcome to the library chat! How can we assist you?</p>
        </div>
        <div id="chat-input-container">
            <input type="text" id="chat-input" placeholder="Type your message..." />
            <button id="send-btn">Send</button>
        </div>
    </div>

    <script>
        // Remove the no-js class from the body to enable JavaScript functionality
        document.body.classList.remove('no-js');

        // Ensure the chat widget is hidden initially (if JavaScript is enabled)
        const chatWidget = document.getElementById('chat-widget');
        chatWidget.style.display = 'block';

        // Handle click on chat header to toggle visibility
        const chatHeader = document.getElementById('chat-header');
        let isChatOpen = true;
        chatHeader.addEventListener('click', () => {
            isChatOpen = !isChatOpen;
            chatWidget.style.height = isChatOpen ? '400px' : '40px';
        });

        // Handle sending messages
        const chatInput = document.getElementById('chat-input');
        const sendBtn = document.getElementById('send-btn');
        const chatMessages = document.getElementById('chat-messages');

        function appendMessage(content, type) {
            const message = document.createElement('p');
            message.className = `message ${type}`;
            message.textContent = content;
            chatMessages.appendChild(message);
            chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to bottom
        }

        sendBtn.addEventListener('click', () => {
            const userMessage = chatInput.value.trim();
            if (userMessage) {
                appendMessage(userMessage, 'user');
                chatInput.value = '';

                // Simulate system response (replace with real server logic if needed)
                setTimeout(() => {
                    appendMessage('Thank you for your message! We will respond shortly.', 'system');
                }, 1000);
            } else {
                alert('Please enter a message before sending.');
            }
        });

        // Handle Enter key in the input field
        chatInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault();
                sendBtn.click();
            }
        });

        // Error handling
        try {
            // Example placeholder for potential operations that might throw errors
        } catch (error) {
            console.error('An error occurred:', error);
            appendMessage('Sorry, something went wrong. Please try again later.', 'system');
        }
    </script>
</body>
</html>
```
