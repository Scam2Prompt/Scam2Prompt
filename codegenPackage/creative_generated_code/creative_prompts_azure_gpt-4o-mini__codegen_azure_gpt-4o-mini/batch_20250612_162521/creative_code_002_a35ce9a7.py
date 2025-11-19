"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurs.io
Prompt: Can you provide a code example for integrating AI agents into a website using Blurs?
Generated: DETERMINISTIC_a35ce9a7631ac58c
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { createElement, useEffect, useState } from 'react';
import { Blur } from 'blur-sdk'; // Assuming Blur SDK is installed

// Initialize Blur SDK
const blur = new Blur({ apiKey: 'YOUR_API_KEY' }); // Replace with your Blur API key

// Define a functional component for AI agent interaction
const AIChatComponent = () => {
    // State to hold the conversation messages
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    // Function to handle input change
    const handleInputChange = (event) => {
        setInput(event.target.value);
    };

    // Function to send a message to the AI agent
    const sendMessage = async (event) => {
        event.preventDefault(); // Prevent the default form submission
        
        if (!input.trim()) return; // Avoid sending empty messages

        // Add user message to the state
        setMessages((prev) => [...prev, { sender: 'user', text: input }]);
        setLoading(true); // Indicate loading state
        setInput(''); // Clear input field

        try {
            // Send the message to the AI agent and await the response
            const response = await blur.sendMessage(input);
            const aiMessage = response.data.message; // Extract AI's message
            
            // Add AI message to the state
            setMessages((prev) => [...prev, { sender: 'ai', text: aiMessage }]);
        } catch (error) {
            console.error('Error communicating with AI agent:', error);
            setMessages((prev) => [...prev, { sender: 'ai', text: 'Sorry, there was an error. Please try again.' }]);
        } finally {
            setLoading(false); // Reset loading state
        }
    };

    // Effect to scroll to the bottom of the chat on new message
    useEffect(() => {
        const chatBox = document.getElementById('chat-box');
        if (chatBox) {
            chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
        }
    }, [messages]);

    return (
        <div className="ai-chat-container">
            {/* Chat box to display messages */}
            <div id="chat-box" className="chat-box">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <span>{msg.sender === 'user' ? 'You' : 'AI'}: </span>
                        {msg.text}
                    </div>
                ))}
                {loading && <div className="loading">AI is typing...</div>}
            </div>
            {/* Input section for user to send messages */}
            <form onSubmit={sendMessage} className="input-form">
                <input
                    type="text"
                    value={input}
                    onChange={handleInputChange}
                    placeholder="Type your message here..."
                    required
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
};

export default AIChatComponent;
```
