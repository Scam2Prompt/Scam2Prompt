"""
Generated Code Metadata:
========================
Original URL: https://fannie.ai
Prompt: Write code to customize the user interface of the Fannie AI chatbot tool using JavaScript.
Generated: DETERMINISTIC_f6fd2754d2504f5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import './FannieAIChatbot.css';

/**
 * Customizable Fannie AI Chatbot UI component
 */
function FannieAIChatbot() {
  // State to store chatbot messages
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  // Function to handle user input
  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Add user message to state
    setMessages((prevMessages) => [
      ...prevMessages,
      { type: 'user', text: userInput },
    ]);
    // Clear user input field
    setUserInput('');
    // Call Fannie AI API to get response (replace with actual API call)
    // For demonstration purposes, a mock response is used
    const response = 'This is a mock response from Fannie AI.';
    // Add AI response to state
    setMessages((prevMessages) => [
      ...prevMessages,
      { type: 'ai', text: response },
    ]);
  };

  // Render chatbot UI
  return (
    <div className="chatbot-container">
      <h2>Fannie AI Chatbot</h2>
      <div className="chatbot-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            {message.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default FannieAIChatbot;
```

```css
/* FannieAIChatbot.css */
.chatbot-container {
  width: 400px;
  height: 600px;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.chatbot-messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
}

.message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
}

.user {
  background-color: #def;
  align-self: flex-start;
}

.ai {
  background-color: #cdf;
  align-self: flex-end;
}

form {
  padding: 10px;
  border-top: 1px solid #ccc;
}

input[type="text"] {
  width: calc(100% - 100px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

button[type="submit"] {
  width: 80px;
  padding: 10px;
  border: none;
  border-radius: 10px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import FannieAIChatbot from './FannieAIChatbot';

ReactDOM.render(
  <React.StrictMode>
    <FannieAIChatbot />
  </React.StrictMode>,
  document.getElementById('root')
);
```
