"""
Generated Code Metadata:
========================
Original URL: https://simplife.life
Prompt: Develop a JavaScript function that displays a chat support feature for an e-commerce site, inspired by the 24-hour chat support mentioned on simplife.life.
Generated: DETERMINISTIC_99580eb84d26fcd9
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ChatSupportWidget - A 24/7 chat support widget for e-commerce sites
 * Features:
 * - Toggle chat window visibility
 * - Send messages
 * - Display chat history
 * - Simulate automated responses
 * - Local storage for chat history persistence
 */

class ChatSupportWidget {
  constructor() {
    this.isOpen = false;
    this.chatHistory = [];
    this.initialize();
    this.loadChatHistory();
  }

  /**
   * Initialize the widget DOM elements and event listeners
   */
  initialize() {
    // Create main container
    this.widgetContainer = document.createElement('div');
    this.widgetContainer.className = 'chat-support-widget';
    this.widgetContainer.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 1000;
      font-family: Arial, sans-serif;
    `;

    // Create toggle button
    this.toggleButton = document.createElement('button');
    this.toggleButton.className = 'chat-toggle';
    this.toggleButton.textContent = 'Need Help? Chat 24/7';
    this.toggleButton.style.cssText = `
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    `;
    this.toggleButton.addEventListener('click', () => this.toggleChat());

    // Create chat window
    this.chatWindow = document.createElement('div');
    this.chatWindow.className = 'chat-window';
    this.chatWindow.style.cssText = `
      display: none;
      width: 300px;
      height: 400px;
      background-color: white;
      border-radius: 5px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
      flex-direction: column;
    `;

    // Create chat header
    const chatHeader = document.createElement('div');
    chatHeader.style.cssText = `
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    `;
    chatHeader.innerHTML = `
      <h3 style="margin: 0; font-size: 16px;">24/7 Support</h3>
      <button class="close-chat" style="background: none; border: none; color: white; cursor: pointer; font-size: 16px;">×</button>
    `;
    chatHeader.querySelector('.close-chat').addEventListener('click', () => this.toggleChat());

    // Create chat messages container
    this.messagesContainer = document.createElement('div');
    this.messagesContainer.className = 'chat-messages';
    this.messagesContainer.style.cssText = `
      flex: 1;
      padding: 10px;
      overflow-y: auto;
    `;

    // Create input area
    const inputArea = document.createElement('div');
    inputArea.style.cssText = `
      display: flex;
      padding: 10px;
      border-top: 1px solid #eee;
    `;

    this.messageInput = document.createElement('input');
    this.messageInput.type = 'text';
    this.messageInput.placeholder = 'Type your message...';
    this.messageInput.style.cssText = `
      flex: 1;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-right: 5px;
    `;
    this.messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.sendMessage();
    });

    const sendButton = document.createElement('button');
    sendButton.textContent = 'Send';
    sendButton.style.cssText = `
      padding: 8px 15px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    `;
    sendButton.addEventListener('click', () => this.sendMessage());

    // Assemble components
    inputArea.appendChild(this.messageInput);
    inputArea.appendChild(sendButton);
    this.chatWindow.appendChild(chatHeader);
    this.chatWindow.appendChild(this.messagesContainer);
    this.chatWindow.appendChild(inputArea);
    this.widgetContainer.appendChild(this.toggleButton);
    this.widgetContainer.appendChild(this.chatWindow);
    document.body.appendChild(this.widgetContainer);

    // Add initial welcome message
    this.addSystemMessage("Welcome to our 24/7 support! How can we help you today?");
  }

  /**
   * Toggle chat window visibility
   */
  toggleChat() {
    this.isOpen = !this.isOpen;
    this.chatWindow.style.display = this.isOpen ? 'flex' : 'none';
    if (this.isOpen) {
      this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
  }

  /**
   * Send a message from the user
   */
  sendMessage() {
    const messageText = this.messageInput.value.trim();
    if (!messageText) return;

    // Add user message
    this.addMessage(messageText, 'user');
    this.messageInput.value = '';

    // Save to history
    this.chatHistory.push({
      sender: 'user',
      text: messageText,
      timestamp: new Date().toISOString()
    });
    this.saveChatHistory();

    // Simulate automated response
    setTimeout(() => {
      const response = this.generateResponse(messageText);
      this.addMessage(response, 'system');
      this.chatHistory.push({
        sender: 'system',
        text: response,
        timestamp: new Date().toISOString()
      });
      this.saveChatHistory();
    }, 1000);
  }

  /**
   * Add a message to the chat UI
   * @param {string} text - The message text
   * @param {string} sender - 'user' or 'system'
   */
  addMessage(text, sender) {
    const messageElement = document.createElement('div');
    messageElement.style.cssText = `
      margin-bottom: 10px;
      padding: 8px 12px;
      border-radius: 5px;
      max-width: 80%;
      word-wrap: break-word;
      align-self: ${sender === 'user' ? 'flex-end' : 'flex-start'};
      background-color: ${sender === 'user' ? '#e3f2fd' : '#f1f1f1'};
    `;
    messageElement.textContent = text;
    this.messagesContainer.appendChild(messageElement);
    this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
  }

  /**
   * Add a system message
   * @param {string} text - The message text
   */
  addSystemMessage(text) {
    this.addMessage(text, 'system');
    this.chatHistory.push({
      sender: 'system',
      text: text,
      timestamp: new Date().toISOString()
    });
    this.saveChatHistory();
  }

  /**
   * Generate a response to user message
   * @param {string} userMessage - The user's message
   * @returns {string} The generated response
   */
  generateResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    
    if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
      return "Hello! Thanks for reaching out. How can I assist you today?";
    } else if (lowerMessage.includes('order') || lowerMessage.includes('purchase')) {
      return "For order-related questions, please provide your order number and I'll check the status for you.";
    } else if (lowerMessage.includes('return') || lowerMessage.includes('refund')) {
      return "Our return policy allows returns within 30 days of purchase. Would you like help initiating a return?";
    } else if (lowerMessage.includes('shipping') || lowerMessage.includes('delivery')) {
      return "Standard shipping takes 3-5 business days. We also offer expedited options. What would you like to know?";
    } else if (lowerMessage.includes('thank') || lowerMessage.includes('thanks')) {
      return "You're welcome! Is there anything else I can help with?";
    } else {
      return "I understand you're asking about: " + userMessage + ". Let me connect you with a specialist who can help with this.";
    }
  }

  /**
   * Save chat history to local storage
   */
  saveChatHistory() {
    try {
      localStorage.setItem('chatSupportHistory', JSON.stringify(this.chatHistory));
    } catch (error) {
      console.error('Failed to save chat history:', error);
    }
  }

  /**
   * Load chat history from local storage
   */
  loadChatHistory() {
    try {
      const savedHistory = localStorage.getItem('chatSupportHistory');
      if (savedHistory) {
        this.chatHistory = JSON.parse(savedHistory);
        // Render loaded messages
        this.chatHistory
