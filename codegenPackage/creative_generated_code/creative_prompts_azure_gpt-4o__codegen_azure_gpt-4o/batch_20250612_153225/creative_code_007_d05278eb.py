"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Provide an example of integrating the Fannie AI chatbot tool into a single-page application using JavaScript frameworks like React or Angular.
Generated: DETERMINISTIC_d05278eb9cae2875
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of integrating the Fannie AI chatbot tool into a single-page application using React:

```javascript
// Import necessary modules and dependencies
import React, { useEffect, useState } from 'react';

// Fannie AI SDK (assuming it's installed as a dependency)
import FannieAI from 'fannie-ai-sdk'; // Replace with actual SDK import path

// Chatbot component
const Chatbot = () => {
  const [chatbot, setChatbot] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    // Initialize Fannie AI chatbot
    const initializeChatbot = async () => {
      try {
        const bot = await FannieAI.init({
          apiKey: process.env.REACT_APP_FANNIE_AI_API_KEY, // Use environment variables for sensitive data
          botId: 'your-bot-id',
        });
        setChatbot(bot);
      } catch (err) {
        console.error('Failed to initialize chatbot:', err);
        setError('Failed to initialize chatbot. Please try again later.');
      }
    };

    initializeChatbot();

    // Clean up resources when component unmounts
    return () => {
      if (chatbot) {
        chatbot.destroy();
      }
    };
  }, []);

  // Handle sending messages to the chatbot
  const sendMessage = async () => {
    if (!chatbot || !input.trim()) {
      return;
    }

    try {
      const userMessage = { sender: 'user', text: input.trim() };
      const botResponse = await chatbot.sendMessage(input.trim());

      // Update the chat messages
      setMessages((prevMessages) => [
        ...prevMessages,
        userMessage,
        { sender: 'bot', text: botResponse },
      ]);

      // Clear input field
      setInput('');
    } catch (err) {
      console.error('Failed to send message:', err);
      setError('Failed to send message. Please try again.');
    }
  };

  // Render chatbot UI
  return (
    <div style={{ maxWidth: '400px', margin: 'auto', border: '1px solid #ccc', padding: '20px' }}>
      <h1>Chat with Fannie AI</h1>
      
      {/* Error display */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Chat messages */}
      <div style={{ marginBottom: '20px', height: '300px', overflowY: 'auto', border: '1px solid #ddd', padding: '10px' }}>
        {messages.map((message, index) => (
          <div key={index} style={{ textAlign: message.sender === 'user' ? 'right' : 'left' }}>
            <p style={{ margin: 0 }}>
              <strong>{message.sender === 'user' ? 'You' : 'Fannie AI'}:</strong> {message.text}
            </p>
          </div>
        ))}
      </div>

      {/* Message input */}
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ flex: 1, padding: '10px', border: '1px solid #ccc', borderRadius: '4px' }}
        />
        <button onClick={sendMessage} style={{ marginLeft: '10px', padding: '10px 20px', backgroundColor: '#007BFF', color: '#fff', border: 'none', borderRadius: '4px' }}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;

// Notes:
// 1. Ensure you have installed the Fannie AI SDK and configured environment variables properly.
// 2. Replace `your-bot-id` with the actual bot ID.
// 3. Error handling is included to catch initialization and message-sending issues.
// 4. Styling is kept minimal; adjust as needed for production use.
```

Make sure you configure the environment variable `REACT_APP_FANNIE_AI_API_KEY` in your `.env` file to store the API key securely.
