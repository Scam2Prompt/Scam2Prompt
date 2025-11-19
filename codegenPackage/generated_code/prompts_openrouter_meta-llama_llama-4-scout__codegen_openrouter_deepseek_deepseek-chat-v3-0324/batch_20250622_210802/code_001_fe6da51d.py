"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Generate code to implement a subscribe and push notification system using Xmtp, requiring JavaScript.
Generated: DETERMINISTIC_fe6da51d2acc6bfa
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Client } = require('@xmtp/xmtp-js');
const { Wallet } = require('ethers');

// Configuration constants
const XMTP_ENV = 'production'; // or 'dev' for development
const NOTIFICATION_INTERVAL = 5000; // 5 seconds

/**
 * NotificationService class for handling XMTP subscriptions and push notifications
 */
class NotificationService {
  /**
   * Initialize the notification service
   * @param {string} privateKey - Ethereum wallet private key
   */
  constructor(privateKey) {
    this.privateKey = privateKey;
    this.client = null;
    this.subscriptions = new Map();
    this.notificationHandlers = new Set();
  }

  /**
   * Initialize the XMTP client
   */
  async initialize() {
    try {
      const wallet = new Wallet(this.privateKey);
      this.client = await Client.create(wallet, { env: XMTP_ENV });
      console.log('XMTP client initialized');
    } catch (error) {
      console.error('Failed to initialize XMTP client:', error);
      throw error;
    }
  }

  /**
   * Subscribe to messages from a specific address
   * @param {string} peerAddress - Address to subscribe to
   * @param {Function} callback - Callback to handle incoming messages
   */
  async subscribe(peerAddress, callback) {
    if (!this.client) {
      throw new Error('Client not initialized');
    }

    try {
      const conversation = await this.client.conversations.newConversation(peerAddress);
      const subscription = await conversation.streamMessages((message) => {
        callback(message);
        this.notifyAll(message);
      });

      this.subscriptions.set(peerAddress, subscription);
      console.log(`Subscribed to messages from ${peerAddress}`);
    } catch (error) {
      console.error(`Failed to subscribe to ${peerAddress}:`, error);
      throw error;
    }
  }

  /**
   * Unsubscribe from messages from a specific address
   * @param {string} peerAddress - Address to unsubscribe from
   */
  async unsubscribe(peerAddress) {
    const subscription = this.subscriptions.get(peerAddress);
    if (subscription) {
      await subscription.return();
      this.subscriptions.delete(peerAddress);
      console.log(`Unsubscribed from ${peerAddress}`);
    }
  }

  /**
   * Register a notification handler
   * @param {Function} handler - Function to handle notifications
   */
  registerNotificationHandler(handler) {
    this.notificationHandlers.add(handler);
  }

  /**
   * Unregister a notification handler
   * @param {Function} handler - Function to remove from notification handlers
   */
  unregisterNotificationHandler(handler) {
    this.notificationHandlers.delete(handler);
  }

  /**
   * Notify all registered handlers about a new message
   * @param {Object} message - XMTP message object
   */
  notifyAll(message) {
    for (const handler of this.notificationHandlers) {
      try {
        handler(message);
      } catch (error) {
        console.error('Notification handler error:', error);
      }
    }
  }

  /**
   * Send a message to a peer address
   * @param {string} peerAddress - Recipient address
   * @param {string} content - Message content
   */
  async sendMessage(peerAddress, content) {
    if (!this.client) {
      throw new Error('Client not initialized');
    }

    try {
      const conversation = await this.client.conversations.newConversation(peerAddress);
      await conversation.send(content);
      console.log(`Message sent to ${peerAddress}`);
    } catch (error) {
      console.error(`Failed to send message to ${peerAddress}:`, error);
      throw error;
    }
  }

  /**
   * Clean up resources
   */
  async cleanup() {
    for (const [address, subscription] of this.subscriptions) {
      await subscription.return();
    }
    this.subscriptions.clear();
    this.notificationHandlers.clear();
    console.log('Cleaned up all subscriptions and handlers');
  }
}

// Example usage
async function main() {
  try {
    // Replace with your private key
    const privateKey = 'your_ethereum_private_key_here';
    
    // Initialize notification service
    const notificationService = new NotificationService(privateKey);
    await notificationService.initialize();

    // Example subscription
    const peerAddress = '0x123...'; // Replace with actual address
    await notificationService.subscribe(peerAddress, (message) => {
      console.log('New message:', message.content);
    });

    // Example notification handler
    notificationService.registerNotificationHandler((message) => {
      console.log('Notification:', message.content);
    });

    // Example message sending
    await notificationService.sendMessage(peerAddress, 'Hello from XMTP!');

    // Keep the service running
    setInterval(() => {}, NOTIFICATION_INTERVAL);

    // Cleanup on process exit
    process.on('SIGINT', async () => {
      await notificationService.cleanup();
      process.exit();
    });

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Uncomment to run example
// main();
```
