"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: How can I enable JavaScript to run the XmtpSubscribePushDemo application and utilize its features?
Generated: DETERMINISTIC_af85cacd556b8876
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready JavaScript implementation for an XMTP (Extensible Messaging Transport Protocol) subscription push demo application:

```javascript
// XmtpSubscribePushDemo.js
// A demo application for subscribing to XMTP push notifications

const { Client } = require('@xmtp/xmtp-js');
const { Wallet } = require('ethers');

class XmtpSubscribePushDemo {
  /**
   * Initialize the XMTP client
   * @param {string} privateKey - Ethereum private key for the wallet
   * @param {string} env - XMTP environment ('dev' or 'production')
   */
  constructor(privateKey, env = 'dev') {
    if (!privateKey) {
      throw new Error('Private key is required');
    }
    this.privateKey = privateKey;
    this.env = env;
    this.client = null;
    this.subscriptions = new Map();
  }

  /**
   * Initialize and connect the XMTP client
   */
  async init() {
    try {
      const wallet = new Wallet(this.privateKey);
      this.client = await Client.create(wallet, { env: this.env });
      console.log('XMTP client initialized with address:', wallet.address);
    } catch (error) {
      console.error('Failed to initialize XMTP client:', error);
      throw error;
    }
  }

  /**
   * Subscribe to messages from a specific address
   * @param {string} peerAddress - Ethereum address to subscribe to
   * @param {function} callback - Function to handle incoming messages
   */
  async subscribe(peerAddress, callback) {
    if (!this.client) {
      throw new Error('Client not initialized. Call init() first.');
    }

    if (!peerAddress || !callback) {
      throw new Error('peerAddress and callback are required');
    }

    try {
      const conversation = await this.client.conversations.newConversation(
        peerAddress
      );

      const subscription = await conversation.streamMessages((message) => {
        callback(message);
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
   * @param {string} peerAddress - Ethereum address to unsubscribe from
   */
  async unsubscribe(peerAddress) {
    if (!this.subscriptions.has(peerAddress)) {
      console.warn(`No active subscription for ${peerAddress}`);
      return;
    }

    try {
      const subscription = this.subscriptions.get(peerAddress);
      await subscription.return();
      this.subscriptions.delete(peerAddress);
      console.log(`Unsubscribed from ${peerAddress}`);
    } catch (error) {
      console.error(`Failed to unsubscribe from ${peerAddress}:`, error);
      throw error;
    }
  }

  /**
   * Send a message to a peer address
   * @param {string} peerAddress - Ethereum address to send message to
   * @param {string} content - Message content
   */
  async sendMessage(peerAddress, content) {
    if (!this.client) {
      throw new Error('Client not initialized. Call init() first.');
    }

    if (!peerAddress || !content) {
      throw new Error('peerAddress and content are required');
    }

    try {
      const conversation = await this.client.conversations.newConversation(
        peerAddress
      );
      await conversation.send(content);
      console.log(`Message sent to ${peerAddress}`);
    } catch (error) {
      console.error(`Failed to send message to ${peerAddress}:`, error);
      throw error;
    }
  }

  /**
   * Clean up all subscriptions and resources
   */
  async cleanup() {
    try {
      // Unsubscribe from all active subscriptions
      for (const [address, subscription] of this.subscriptions) {
        await subscription.return();
        this.subscriptions.delete(address);
      }

      if (this.client) {
        await this.client.close();
        this.client = null;
      }

      console.log('All resources cleaned up');
    } catch (error) {
      console.error('Error during cleanup:', error);
      throw error;
    }
  }
}

// Example usage:
/*
(async () => {
  try {
    const demo = new XmtpSubscribePushDemo('your-private-key-here');
    await demo.init();

    // Subscribe to messages from a peer
    await demo.subscribe('0xPeerAddressHere', (message) => {
      console.log('Received message:', message.content);
    });

    // Send a message
    await demo.sendMessage('0xPeerAddressHere', 'Hello from XMTP!');

    // Later, when done
    // await demo.cleanup();
  } catch (error) {
    console.error('Demo error:', error);
  }
})();
*/

module.exports = XmtpSubscribePushDemo;
```
