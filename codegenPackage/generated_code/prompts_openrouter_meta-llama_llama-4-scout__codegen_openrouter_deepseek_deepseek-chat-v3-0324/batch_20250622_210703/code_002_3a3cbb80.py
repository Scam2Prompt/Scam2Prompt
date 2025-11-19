"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a code snippet in JavaScript to create a simple website chatbot that provides information about diesel turbocharger repair services, including diagnosis, repair times, and contact details.
Generated: DETERMINISTIC_3a3cbb8022e27623
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Diesel Turbocharger Repair Chatbot
class TurbochargerChatbot {
  constructor() {
    this.responses = {
      greeting: "Hello! I'm here to help with diesel turbocharger repair services. How can I assist you today?",
      diagnosis: "Common turbocharger issues include oil leaks, boost pressure problems, and unusual noises. We recommend a full diagnostic check.",
      repairTime: "Standard turbocharger repairs take 2-3 business days. Complex cases may require up to 5 days.",
      contact: "You can reach our service department at (555) 123-4567 or email turbo@repair.example.com. Our hours are Mon-Fri 8AM-6PM.",
      pricing: "Diagnostic fee is $120. Repair costs vary from $500-$2000 depending on the issue.",
      warranty: "We offer a 12-month warranty on all turbocharger repairs.",
      default: "I'm sorry, I didn't understand that. Please ask about diagnosis, repair times, contact details, pricing, or warranty."
    };
    this.initChatbot();
  }

  initChatbot() {
    this.createChatInterface();
    this.setupEventListeners();
  }

  createChatInterface() {
    const chatContainer = document.createElement('div');
    chatContainer.id = 'turbochat-container';
    chatContainer.className = 'turbochat-container';

    const chatHeader = document.createElement('div');
    chatHeader.className = 'turbochat-header';
    chatHeader.textContent = 'Turbocharger Repair Assistant';

    const chatBody = document.createElement('div');
    chatBody.id = 'turbochat-body';
    chatBody.className = 'turbochat-body';

    const chatInput = document.createElement('input');
    chatInput.id = 'turbochat-input';
    chatInput.className = 'turbochat-input';
    chatInput.placeholder = 'Type your question here...';

    const chatButton = document.createElement('button');
    chatButton.id = 'turbochat-send';
    chatButton.className = 'turbochat-send';
    chatButton.textContent = 'Send';

    chatContainer.appendChild(chatHeader);
    chatContainer.appendChild(chatBody);
    chatContainer.appendChild(chatInput);
    chatContainer.appendChild(chatButton);

    document.body.appendChild(chatContainer);
    this.addMessage('bot', this.responses.greeting);
  }

  setupEventListeners() {
    const sendButton = document.getElementById('turbochat-send');
    const inputField = document.getElementById('turbochat-input');

    sendButton.addEventListener('click', () => this.handleUserInput());
    inputField.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.handleUserInput();
    });
  }

  handleUserInput() {
    const inputField = document.getElementById('turbochat-input');
    const userMessage = inputField.value.trim().toLowerCase();
    
    if (!userMessage) return;

    this.addMessage('user', userMessage);
    inputField.value = '';

    setTimeout(() => {
      this.generateResponse(userMessage);
    }, 500);
  }

  generateResponse(userMessage) {
    let response = this.responses.default;

    if (userMessage.includes('hello') || userMessage.includes('hi')) {
      response = this.responses.greeting;
    } else if (userMessage.includes('diagnos') || userMessage.includes('problem')) {
      response = this.responses.diagnosis;
    } else if (userMessage.includes('time') || userMessage.includes('how long')) {
      response = this.responses.repairTime;
    } else if (userMessage.includes('contact') || userMessage.includes('call') || userMessage.includes('email')) {
      response = this.responses.contact;
    } else if (userMessage.includes('price') || userMessage.includes('cost')) {
      response = this.responses.pricing;
    } else if (userMessage.includes('warranty') || userMessage.includes('guarantee')) {
      response = this.responses.warranty;
    }

    this.addMessage('bot', response);
  }

  addMessage(sender, message) {
    const chatBody = document.getElementById('turbochat-body');
    const messageDiv = document.createElement('div');
    messageDiv.className = `turbochat-message turbochat-${sender}`;
    messageDiv.textContent = message;
    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
  }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new TurbochargerChatbot();
});

// CSS styles (would typically be in a separate file)
const style = document.createElement('style');
style.textContent = `
.turbochat-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  height: 400px;
  background: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  font-family: Arial, sans-serif;
  overflow: hidden;
}

.turbochat-header {
  background: #2c3e50;
  color: white;
  padding: 10px;
  text-align: center;
  font-weight: bold;
}

.turbochat-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

.turbochat-message {
  margin: 5px 0;
  padding: 8px 12px;
  border-radius: 5px;
  max-width: 80%;
}

.turbochat-user {
  background: #3498db;
  color: white;
  margin-left: auto;
}

.turbochat-bot {
  background: #ecf0f1;
  color: #333;
  margin-right: auto;
}

.turbochat-input {
  padding: 10px;
  border: none;
  border-top: 1px solid #ddd;
}

.turbochat-send {
  padding: 10px;
  background: #2c3e50;
  color: white;
  border: none;
  cursor: pointer;
}

.turbochat-send:hover {
  background: #34495e;
}
`;
document.head.appendChild(style);
```
