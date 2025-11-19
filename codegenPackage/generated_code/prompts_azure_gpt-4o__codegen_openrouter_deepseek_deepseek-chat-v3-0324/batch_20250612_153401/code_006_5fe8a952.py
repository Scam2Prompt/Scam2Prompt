"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Generate code to configure XMTP in a JavaScript app for subscribing to notifications, referencing the XMTP Subscribe Push Demo example.
Generated: DETERMINISTIC_5fe8a9526e643b9d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required XMTP libraries
import { Client } from '@xmtp/xmtp-js';
import { Notifications } from '@xmtp/xmtp-js/dist/types/src/notifications';

// Configuration for XMTP client
const XMTP_CONFIG = {
  env: 'production', // or 'dev' for development
  appVersion: '1.0.0', // your app version
};

/**
 * Initialize XMTP client with wallet
 * @param {Object} wallet - Ethereum wallet with signer capability
 * @returns {Promise<Client>} Initialized XMTP client
 */
async function initXMTPClient(wallet) {
  try {
    if (!wallet) {
      throw new Error('Wallet is required');
    }

    const client = await Client.create(wallet, {
      env: XMTP_CONFIG.env,
      appVersion: XMTP_CONFIG.appVersion,
    });

    return client;
  } catch (error) {
    console.error('Failed to initialize XMTP client:', error);
    throw error;
  }
}

/**
 * Subscribe to push notifications
 * @param {Client} xmtpClient - Initialized XMTP client
 * @param {string} topic - Topic to subscribe to
 * @param {Function} callback - Callback for new notifications
 * @returns {Promise<void>}
 */
async function subscribeToNotifications(xmtpClient, topic, callback) {
  try {
    if (!xmtpClient) {
      throw new Error('XMTP client is required');
    }
    if (!topic) {
      throw new Error('Topic is required');
    }
    if (!callback || typeof callback !== 'function') {
      throw new Error('Valid callback function is required');
    }

    const notifications = await Notifications.create(xmtpClient);
    await notifications.subscribe([topic]);

    // Set up stream for notifications
    const stream = await notifications.stream(topic);
    for await (const notification of stream) {
      callback(notification);
    }
  } catch (error) {
    console.error('Failed to subscribe to notifications:', error);
    throw error;
  }
}

/**
 * Unsubscribe from notifications
 * @param {Client} xmtpClient - Initialized XMTP client
 * @param {string} topic - Topic to unsubscribe from
 * @returns {Promise<void>}
 */
async function unsubscribeFromNotifications(xmtpClient, topic) {
  try {
    if (!xmtpClient) {
      throw new Error('XMTP client is required');
    }
    if (!topic) {
      throw new Error('Topic is required');
    }

    const notifications = await Notifications.create(xmtpClient);
    await notifications.unsubscribe([topic]);
  } catch (error) {
    console.error('Failed to unsubscribe from notifications:', error);
    throw error;
  }
}

export {
  initXMTPClient,
  subscribeToNotifications,
  unsubscribeFromNotifications,
  XMTP_CONFIG,
};
```
