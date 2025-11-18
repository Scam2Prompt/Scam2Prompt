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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library Chat Widget</title>
    <style>
        /* Basic styles for chat widget */
        #chat-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            max-width: 90%;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            display: none; /* Hidden by default */
            background-color: white;
        }

        #chat-header {
            background-color: #007bff;
            color: white;
            padding: 10px;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }

        #chat-messages {
            height: 200px;
            overflow-y: auto;
            padding: 10px;
        }

        #chat-input {
            display: flex;
            padding: 10px;
        }

        #message {
            flex: 1;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        #send {
            margin-left: 5px;
            padding: 5px 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        #send:disabled {
            background-color: #ccc;
        }
    </style>
</head>
<body>

    <div id="chat-widget">
        <div id="chat-header">Library Chat</div>
        <div id="chat-messages"></div>
        <div id="chat-input">
            <input type="text" id="message" placeholder="Type your message..." required>
            <button id="send" disabled>Send</button>
        </div>
    </div>

    <noscript>
        <style>
            #chat-widget {
                display: none; /* Hide widget when JavaScript is disabled */
            }
        </style>
        <div>
            <p>JavaScript is disabled. Please use the chat link below:</p>
            <a href="mailto:library@example.com">Contact Library</a>
        </div>
    </noscript>

    <script>
        // Check if DOM is fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            const chatWidget = document.getElementById('chat-widget');
            const messageInput = document.getElementById('message');
            const sendButton = document.getElementById('send');
            const chatMessages = document.getElementById('chat-messages');

            // Show chat widget on page load
            chatWidget.style.display = 'block';

            // Enable send button if message input is not empty
            messageInput.addEventListener('input', () => {
                sendButton.disabled = messageInput.value.trim() === '';
            });

            // Handle send button click
            sendButton.addEventListener('click', () => {
                const messageText = messageInput.value.trim();
                if (messageText) {
                    // Append message to chat
                    const messageElement = document.createElement('div');
                    messageElement.textContent = `You: ${messageText}`;
                    chatMessages.appendChild(messageElement);
                    chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
                    messageInput.value = ''; // Clear input
                    sendButton.disabled = true; // Disable button until new message
                }
            });

            // Optional: simulate receiving a response after a delay
            const simulateResponse = () => {
                const responseElement = document.createElement('div');
                responseElement.textContent = 'Library Bot: How can I assist you?';
                chatMessages.appendChild(responseElement);
                chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
            };

            // Simulate a bot response after 2 seconds
            setTimeout(simulateResponse, 2000);
        });
    </script>
</body>
</html>
```
