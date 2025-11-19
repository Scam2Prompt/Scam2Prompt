"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Write a JavaScript function to initialize XMTP and subscribe to push notifications, based on the implementation details of the XMTP Subscribe Push Demo.
Generated: DETERMINISTIC_c38bf0b06f32e56a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Client } from '@xmtp/xmtp-js'; // Ensure you have the XMTP library installed

/**
 * Initializes the XMTP client and subscribes to push notifications.
 * @param {string} walletAddress - The wallet address of the user.
 * @param {string} privateKey - The private key for the user's wallet.
 * @returns {Promise<void>} - A promise that resolves when the subscription is successful.
 */
async function initializeXmtpAndSubscribe(walletAddress, privateKey) {
    try {
        // Create an instance of the XMTP client
        const xmtpClient = await Client.create(walletAddress, { privateKey });

        // Check if the client is initialized
        if (!xmtpClient) {
            throw new Error('Failed to initialize XMTP client.');
        }

        console.log('XMTP client initialized successfully.');

        // Subscribe to push notifications
        xmtpClient.onMessage(async (message) => {
            // Handle incoming messages
            console.log('New message received:', message);
            // You can add further processing of the message here
        });

        console.log('Subscribed to push notifications successfully.');

    } catch (error) {
        // Handle errors gracefully
        console.error('Error initializing XMTP or subscribing to notifications:', error);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Example usage (ensure to replace with actual wallet address and private key)
// initializeXmtpAndSubscribe('your_wallet_address', 'your_private_key');
```

Make sure to replace `'your_wallet_address'` and `'your_private_key'` with actual values when calling the function.
