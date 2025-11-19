"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: Generate code using JavaScript to implement a live chat feature for customer support on an online gambling site, similar to the one mentioned on PANSOS4D.
Generated: DETERMINISTIC_f53cd2c565274e27
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Live Chat Feature for Customer Support
class LiveChat {
  constructor(options) {
    // Configuration options
    this.socketUrl = options.socketUrl || 'wss://your-websocket-server.com';
    this.maxMessages = options.maxMessages || 100;
    this.autoConnect = options.autoConnect !== false;
    this.chatContainerId = options.chatContainerId || 'live-chat-container';
    this.userId = options.userId || this.generateUserId();
    this.username = options.username || 'Guest';
    this.isOperator = options.isOperator || false;

    // State
    this.messages = [];
    this.socket = null;
    this.connected = false;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;

    // DOM Elements
    this.chatContainer = null;
    this.messageInput = null;
    this.sendButton = null;
    this.messagesContainer = null;

    // Initialize
    this.initDOM();
    if (this.autoConnect) {
      this.connect();
    }
  }

  // Generate a random user ID
  generateUserId() {
    return 'user-' + Math.random().toString(36).substr(2, 9);
  }

  // Initialize DOM elements
  initDOM() {
    this.chatContainer = document.getElementById(this.chatContainerId);
    if (!this.chatContainer) {
      console.error('Chat container not found');
      return;
    }

    // Create chat UI
    this.chatContainer.innerHTML = `
      <div class="chat-header">
        <h3>Customer Support</h3>
        <div class="status-indicator ${this.connected ? 'connected' : 'disconnected'}"></div>
      </div>
      <div class="chat-messages"></div>
      <div class="chat-input">
        <input type="text" placeholder="Type your message..." class="message-input" ${this.connected ? '' : 'disabled'}>
        <button class="send-button" ${this.connected ? '' : 'disabled'}>Send</button>
      </div>
    `;

    this.messagesContainer = this.chatContainer.querySelector('.chat-messages');
    this.messageInput = this.chatContainer.querySelector('.message-input');
    this.sendButton = this.chatContainer.querySelector('.send-button');

    // Event listeners
    this.sendButton.addEventListener('click', () => this.sendMessage());
    this.messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.sendMessage();
    });
  }

  // Connect to WebSocket server
  connect() {
    if (this.connected) return;

    this.socket = new WebSocket(this.socketUrl);

    this.socket.onopen = () => {
      this.connected = true;
      this.reconnectAttempts = 0;
      this.updateUIStatus();
      this.sendSystemMessage('Connected to support');
      this.sendUserInfo();
    };

    this.socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      this.handleIncomingMessage(message);
    };

    this.socket.onclose = () => {
      this.connected = false;
      this.updateUIStatus();
      this.sendSystemMessage('Disconnected from support');
      this.attemptReconnect();
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  }

  // Attempt to reconnect with exponential backoff
  attemptReconnect() {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      this.sendSystemMessage('Failed to reconnect. Please refresh the page.');
      return;
    }

    const delay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), 30000);
    this.reconnectAttempts++;

    setTimeout(() => {
      this.sendSystemMessage(`Attempting to reconnect (${this.reconnectAttempts}/${this.maxReconnectAttempts})...`);
      this.connect();
    }, delay);
  }

  // Update UI connection status
  updateUIStatus() {
    const indicator = this.chatContainer.querySelector('.status-indicator');
    if (indicator) {
      indicator.className = `status-indicator ${this.connected ? 'connected' : 'disconnected'}`;
    }
    this.messageInput.disabled = !this.connected;
    this.sendButton.disabled = !this.connected;
  }

  // Send user information to server
  sendUserInfo() {
    if (!this.connected) return;

    const userInfo = {
      type: 'user_info',
      userId: this.userId,
      username: this.username,
      isOperator: this.isOperator,
      timestamp: Date.now()
    };

    this.socket.send(JSON.stringify(userInfo));
  }

  // Handle incoming messages
  handleIncomingMessage(message) {
    if (!message || !message.type) return;

    switch (message.type) {
      case 'chat_message':
        this.addMessage(message);
        break;
      case 'system_message':
        this.addSystemMessage(message.content);
        break;
      case 'operator_joined':
        this.addSystemMessage(`${message.username} has joined the chat`);
        break;
      case 'operator_left':
        this.addSystemMessage(`${message.username} has left the chat`);
        break;
      default:
        console.log('Unknown message type:', message.type);
    }
  }

  // Send a chat message
  sendMessage() {
    if (!this.connected) return;

    const content = this.messageInput.value.trim();
    if (!content) return;

    const message = {
      type: 'chat_message',
      userId: this.userId,
      username: this.username,
      content: content,
      timestamp: Date.now(),
      isOperator: this.isOperator
    };

    this.socket.send(JSON.stringify(message));
    this.messageInput.value = '';
    this.addMessage(message); // Add to local UI immediately
  }

  // Add a message to the UI
  addMessage(message) {
    if (this.messages.length >= this.maxMessages) {
      this.messages.shift();
      this.messagesContainer.removeChild(this.messagesContainer.firstChild);
    }

    this.messages.push(message);
    const messageElement = document.createElement('div');
    messageElement.className = `message ${message.isOperator ? 'operator-message' : 'user-message'}`;
    messageElement.innerHTML = `
      <div class="message-header">
        <span class="username">${message.username}</span>
        <span class="timestamp">${new Date(message.timestamp).toLocaleTimeString()}</span>
      </div>
      <div class="message-content">${this.escapeHtml(message.content)}</div>
    `;
    this.messagesContainer.appendChild(messageElement);
    this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
  }

  // Add a system message to the UI
  addSystemMessage(content) {
    const message = {
      type: 'system_message',
      content: content,
      timestamp: Date.now()
    };

    const messageElement = document.createElement('div');
    messageElement.className = 'system-message';
    messageElement.innerHTML = `
      <div class="message-content">${this.escapeHtml(content)}</div>
    `;
    this.messagesContainer.appendChild(messageElement);
    this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
  }

  // Escape HTML to prevent XSS
  escapeHtml(unsafe) {
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Disconnect from server
  disconnect() {
    if (this.socket) {
      this.socket.close();
    }
    this.connected = false;
    this.updateUIStatus();
  }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  const chat = new LiveChat({
    socketUrl: 'wss://your-websocket-server.com',
    chatContainerId: 'live-chat-container',
    username: 'Player123',
    autoConnect: true
  });

  // Expose chat instance for debugging
  window.chat = chat;
});

// CSS should be added separately, but here's a minimal example:
const style = document.createElement('style');
style.textContent = `
  #live-chat-container {
    width: 350px;
    height: 500px;
    border: 1px solid #ccc;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    font-family: Arial, sans-serif;
    background: #f9f9f9;
  }
  .chat-header {
    padding: 10px;
    background: #2c3e50;
    color: white;
    border-radius: 8px 8px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .status-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
  .status-indicator.connected {
    background: #2ecc71
