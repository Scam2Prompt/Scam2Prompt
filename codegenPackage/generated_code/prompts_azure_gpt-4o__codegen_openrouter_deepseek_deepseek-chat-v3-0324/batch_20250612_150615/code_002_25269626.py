"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Develop a JavaScript-based chat widget for a library website, ensuring compatibility even when JavaScript is disabled, as noted in the Loyola University Chicago Libraries portal.
Generated: DETERMINISTIC_25269626e483c4cd
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
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
            width: 350px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            font-family: Arial, sans-serif;
            z-index: 1000;
            background: #fff;
            display: none;
        }
        
        #chat-header {
            background: #2c3e50;
            color: white;
            padding: 12px 15px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        #chat-header h3 {
            margin: 0;
            font-size: 16px;
        }
        
        #chat-toggle {
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            position: fixed;
            bottom: 20px;
            right: 20px;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }
        
        #chat-body {
            padding: 15px;
            height: 300px;
            overflow-y: auto;
            background: #f9f9f9;
        }
        
        #chat-messages {
            margin-bottom: 15px;
        }
        
        .message {
            margin-bottom: 10px;
            padding: 8px 12px;
            border-radius: 4px;
            max-width: 80%;
        }
        
        .user-message {
            background: #e3f2fd;
            margin-left: auto;
        }
        
        .bot-message {
            background: #f1f1f1;
            margin-right: auto;
        }
        
        #chat-input-container {
            display: flex;
            padding: 10px;
            border-top: 1px solid #ddd;
            background: #fff;
        }
        
        #chat-input {
            flex: 1;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-right: 8px;
        }
        
        #chat-send {
            padding: 8px 15px;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        #chat-send:hover {
            background: #1a252f;
        }
        
        #no-js-message {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #f8d7da;
            color: #721c24;
            padding: 10px 15px;
            border-radius: 4px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            display: none;
        }
        
        .chat-link {
            color: #2980b9;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <!-- Chat toggle button -->
    <button id="chat-toggle" aria-label="Open chat">💬</button>
    
    <!-- Chat widget container -->
    <div id="chat-widget">
        <div id="chat-header">
            <h3>Library Chat Assistance</h3>
            <button id="chat-close" aria-label="Close chat">×</button>
        </div>
        <div id="chat-body">
            <div id="chat-messages">
                <div class="message bot-message">
                    Hello! How can I help you with your library needs today?
                </div>
            </div>
            <div id="chat-input-container">
                <input type="text" id="chat-input" placeholder="Type your message..." aria-label="Type your message">
                <button id="chat-send">Send</button>
            </div>
        </div>
    </div>
    
    <!-- Fallback for when JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. For chat assistance, please 
        <a href="mailto:library@example.edu" class="chat-link">email us</a> 
        or call <a href="tel:+13125551234" class="chat-link">(312) 555-1234</a>.
    </div>

    <script>
        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Hide the no-JS message since JS is enabled
            document.getElementById('no-js-message').style.display = 'none';
            
            // Get DOM elements
            const chatToggle = document.getElementById('chat-toggle');
            const chatWidget = document.getElementById('chat-widget');
            const chatClose = document.getElementById('chat-close');
            const chatInput = document.getElementById('chat-input');
            const chatSend = document.getElementById('chat-send');
            const chatMessages = document.getElementById('chat-messages');
            
            // Toggle chat visibility
            function toggleChat() {
                if (chatWidget.style.display === 'block') {
                    chatWidget.style.display = 'none';
                    chatToggle.setAttribute('aria-expanded', 'false');
                } else {
                    chatWidget.style.display = 'block';
                    chatToggle.setAttribute('aria-expanded', 'true');
                    chatInput.focus();
                }
            }
            
            // Event listeners
            chatToggle.addEventListener('click', toggleChat);
            chatClose.addEventListener('click', toggleChat);
            
            // Handle sending messages
            function sendMessage() {
                const messageText = chatInput.value.trim();
                if (messageText === '') return;
                
                // Add user message
                const userMessage = document.createElement('div');
                userMessage.className = 'message user-message';
                userMessage.textContent = messageText;
                chatMessages.appendChild(userMessage);
                
                // Clear input
                chatInput.value = '';
                
                // Scroll to bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
                
                // Simulate bot response (in a real app, this would be an API call)
                setTimeout(() => {
                    const botMessage = document.createElement('div');
                    botMessage.className = 'message bot-message';
                    botMessage.textContent = getBotResponse(messageText);
                    chatMessages.appendChild(botMessage);
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }, 1000);
            }
            
            // Handle Enter key press
            chatInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
            
            // Send button click
            chatSend.addEventListener('click', sendMessage);
            
            // Simple bot response logic
            function getBotResponse(message) {
                const lowerMsg = message.toLowerCase();
                
                if (lowerMsg.includes('hours') || lowerMsg.includes('open')) {
                    return "Our library is open Monday-Friday 8am-10pm, Saturday 9am-8pm, and Sunday 10am-6pm.";
                } else if (lowerMsg.includes('book') || lowerMsg.includes('borrow')) {
                    return "You can borrow books for 4 weeks with up to 2 renewals. Visit our catalog to check availability.";
                } else if (lowerMsg.includes('research') || lowerMsg.includes('help')) {
                    return "Our research librarians are available for consultations. Would you like me to connect you?";
                } else if (lowerMsg.includes('contact') || lowerMsg.includes('email')) {
                    return "You can email us at library@example.edu or call (312) 555-1234.";
                } else {
                    return "I'm not sure I understand. Could you please rephrase your question?";
                }
            }
            
            // Initialize with chat closed
            chatWidget.style.display = 'none';
            chatToggle.setAttribute('aria-expanded', 'false');
        });
    </script>
    
    <noscript>
        <style>
            #no-js-message {
                display: block !important;
            }
            #chat-toggle, #chat-widget {
                display: none !important;
            }
        </style>
    </noscript>
</body>
</html>
```
