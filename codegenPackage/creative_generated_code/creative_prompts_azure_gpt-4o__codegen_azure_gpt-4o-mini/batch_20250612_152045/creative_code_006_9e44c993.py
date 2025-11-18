"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webogram.org
Prompt: Create a script to integrate Telegram Web functionality into a React application, including sending and receiving messages.
Generated: DETERMINISTIC_9e44c993e19e0d7c
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import TelegramWebApp from '@telegram-web-app/sdk';

// Main component for the Telegram Web integration
const TelegramIntegration = () => {
  // State to hold messages
  const [messages, setMessages] = useState([]);
  // State to hold the input text
  const [inputText, setInputText] = useState('');

  // Effect to initialize the Telegram Web App SDK
  useEffect(() => {
    // Initialize the Telegram Web App SDK
    TelegramWebApp.init();

    // Function to handle incoming messages
    const handleIncomingMessage = (event) => {
      // Check if the event is a message
      if (event.data && event.data.type === 'message') {
        // Update messages state with new message
        setMessages((prevMessages) => [
          ...prevMessages,
          event.data.message,
        ]);
      }
    };

    // Register event listener for incoming messages
    window.addEventListener('message', handleIncomingMessage);

    // Cleanup function to remove the event listener
    return () => {
      window.removeEventListener('message', handleIncomingMessage);
    };
  }, []);

  // Function to send a message
  const sendMessage = () => {
    if (inputText.trim()) {
      // Construct the message object
      const message = {
        text: inputText,
        timestamp: new Date().toISOString(),
      };

      // Send the message via Telegram Web App SDK
      TelegramWebApp.sendMessage(message)
        .then(() => {
          // Reset input field after sending
          setInputText('');
        })
        .catch((error) => {
          console.error('Error sending message:', error);
          alert('Failed to send message. Please try again.');
        });
    } else {
      alert('Please enter a message before sending.');
    }
  };

  return (
    <div className="telegram-integration">
      <h1>Telegram Web Integration</h1>
      
      <div className="message-list">
        {messages.map((msg, index) => (
          <div key={index} className="message">
            <strong>{msg.sender || 'You'}:</strong> {msg.text}
          </div>
        ))}
      </div>

      <div className="input-group">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

// Exporting the component for use in the application
export default TelegramIntegration;
```

### Notes:
- Ensure that you have the Telegram Web App SDK installed in your project before using this code.
- The `sendMessage` function may need to be adjusted according to the exact SDK methods available, as the current SDK may not directly support `sendMessage` as shown. Please check the SDK documentation for the correct usage.
- You may need to style the component and handle specific cases based on your application needs.
