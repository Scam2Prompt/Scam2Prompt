"""
Generated Code Metadata:
========================
Original URL: https://kaafmall.com
Prompt: Write code to create a WhatsApp-style chat interface using HTML, CSS, and JavaScript, including features like missed call notifications and multimedia placeholders as shown on the kaafmall.com webpage.
Generated: DETERMINISTIC_c751107984a67426
Batch ID: 20250612_152410
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://web.whatsapp.com/img/bg-chat-tile-light_a4be512e7195b6b733d9110b408f075d.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp-style Chat Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #e5ddd5;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .chat-container {
            width: 360px;
            height: 600px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .chat-header {
            background-color: #075e54;
            color: white;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-header h2 {
            font-size: 18px;
            font-weight: 500;
        }

        .chat-header-icons {
            display: flex;
            gap: 15px;
        }

        .chat-header-icons i {
            cursor: pointer;
        }

        .chat-messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            background-image: url('https://web.whatsapp.com/img/bg-chat-tile-light_a4be512e7195b6b733d9110b408f075d.png');
            background-repeat: repeat;
        }

        .message {
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
            max-width: 80%;
        }

        .message-sent {
            align-self: flex-end;
            align-items: flex-end;
        }

        .message-received {
            align-self: flex-start;
            align-items: flex-start;
        }

        .message-content {
            padding: 8px 12px;
            border-radius: 8px;
            margin-bottom: 5px;
            position: relative;
            word-wrap: break-word;
        }

        .message-sent .message-content {
            background-color: #dcf8c6;
            border-top-right-radius: 0;
        }

        .message-received .message-content {
            background-color: white;
            border-top-left-radius: 0;
        }

        .message-time {
            font-size: 11px;
            color: #666;
        }

        .message-sent .message-time {
            text-align: right;
        }

        .message-received .message-time {
            text-align: left;
        }

        .missed-call {
            background-color: #ffebee;
            padding: 8px 12px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 15px;
            align-self: center;
        }

        .missed-call i {
            color: #f44336;
        }

        .missed-call-text {
            font-size: 14px;
            color: #f44336;
        }

        .media-placeholder {
            width: 200px;
            height: 150px;
            background-color: #f5f5f5;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #666;
            font-size: 14px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .media-placeholder i {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .media-placeholder img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }

        .chat-input {
            display: flex;
            padding: 10px;
            background-color: #f0f0f0;
            align-items: center;
        }

        .chat-input input {
            flex: 1;
            padding: 10px 15px;
            border: none;
            border-radius: 20px;
            outline: none;
            font-size: 14px;
        }

        .chat-input-icons {
            display: flex;
            gap: 15px;
            margin-left: 10px;
        }

        .chat-input-icons i {
            cursor: pointer;
            color: #666;
        }

        .chat-input-icons i:hover {
            color: #075e54;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>Chat</h2>
            <div class="chat-header-icons">
                <i class="fas fa-search"></i>
                <i class="fas fa-ellipsis-v"></i>
            </div>
        </div>

        <div class="chat-messages" id="chatMessages">
            <!-- Messages will be added here dynamically -->
        </div>

        <div class="chat-input">
            <i class="far fa-smile"></i>
            <input type="text" placeholder="Type a message" id="messageInput">
            <div class="chat-input-icons">
                <i class="fas fa-paperclip"></i>
                <i class="fas fa-microphone"></i>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatMessages = document.getElementById('chatMessages');
            const messageInput = document.getElementById('messageInput');
            
            // Sample messages data
            const messages = [
                {
                    type: 'received',
                    content: 'Hey there! How are you?',
                    time: '10:30 AM'
                },
                {
                    type: 'sent',
                    content: 'I\'m good, thanks! How about you?',
                    time: '10:32 AM'
                },
                {
                    type: 'missed-call',
                    time: '10:35 AM'
                },
                {
                    type: 'received',
                    content: 'I\'m doing well. Can we meet tomorrow?',
                    time: '10:36 AM'
                },
                {
                    type: 'received',
                    media: 'image',
                    content: 'Check out this place!',
                    time: '10:37 AM'
                },
                {
                    type: 'sent',
                    content: 'Sure, that works for me!',
                    time: '10:40 AM'
                }
            ];

            // Render initial messages
            renderMessages();

            // Handle sending new messages
            messageInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && messageInput.value.trim() !== '') {
                    const newMessage = {
                        type: 'sent',
                        content: messageInput.value,
                        time: getCurrentTime()
                    };
                    
                    messages.push(newMessage);
                    renderMessages();
                    messageInput.value = '';
                    
                    // Scroll to bottom
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }
            });

            function renderMessages() {
                chatMessages.innerHTML = '';
                
                messages.forEach(message => {
                    if (message.type === 'missed-call') {
                        const missedCallElement = document.createElement('div');
                        missedCallElement.className = 'missed-call';
                        missedCallElement.innerHTML = `
                            <i class="fas fa-phone-slash"></i>
                            <span class="missed-call-text">Missed voice call</span>
                            <span class="message-time">${message.time}</span>
                        `;
                        chatMessages.appendChild(missedCallElement);
                    } else {
                        const messageElement = document.createElement('div');
                        messageElement.className = `message message-${message.type}`;
                        
                        if (message.media) {
                            const mediaElement = document.createElement('div');
                            mediaElement.className = 'media-placeholder';
                            mediaElement.innerHTML = `
                                <i class="fas fa-${message.media === 'image' ? 'image' : 'video'}"></i>
                                <span>${message.media === 'image' ? 'Photo' : 'Video'}</span>
                            `;
                            messageElement.appendChild(mediaElement);
                            
                            if (message.content) {
                                const contentElement = document.createElement('div');
                                contentElement.className = 'message-content';
                                contentElement.textContent = message.content;
                                messageElement.appendChild(contentElement);
                            }
                        } else {
                            const contentElement = document.createElement('div');
                            contentElement.className = 'message-content';
                            contentElement.textContent = message.content;
                            messageElement.appendChild(contentElement);
                        }
                        
                        const timeElement = document.createElement('div');
                        timeElement.className = 'message-time
