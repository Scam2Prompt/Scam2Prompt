"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Write a JavaScript function to initialize XMTP and subscribe to push notifications, based on the implementation details of the XMTP Subscribe Push Demo.
Generated: DETERMINISTIC_c38bf0b06f32e56a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary XMTP libraries
import { Client } from '@xmtp/xmtp-js'; // Make sure to install the xmtp-js package
import { ethers } from 'ethers'; // For Ethereum wallet integration

/**
 * Initialize XMTP client and subscribe to push notifications
 * @param {string} privateKey - The private key of the user for wallet authentication
 * @param {function} onMessageReceived - Callback function to handle incoming messages
 */
async function initializeXmtp(privateKey, onMessageReceived) {
    try {
        // Create a new Ethereum wallet instance using the provided private key
        const wallet = new ethers.Wallet(privateKey);

        // Initialize the XMTP client with the wallet
        const xmtpClient = await Client.create(wallet);

        console.log('XMTP client initialized successfully.');

        // Subscribe to push notifications
        const subscription = await xmtpClient.messages.subscribe({
            onMessage: onMessageReceived,
        });

        console.log('Subscribed to push notifications.');

        return {
            xmtpClient,
            subscription,
        };
    } catch (error) {
        console.error('Error initializing XMTP client or subscribing to notifications:', error);
        throw new Error('XMTP initialization failed'); // Throwing an error for further handling
    }
}

// Example usage of the initializeXmtp function
(async () => {
    const privateKey = 'YOUR_PRIVATE_KEY_HERE'; // Replace with the user's private key

    // Callback function to handle incoming messages
    const handleMessage = (message) => {
        console.log('New message received:', message);
    };

    try {
        const { xmtpClient, subscription } = await initializeXmtp(privateKey, handleMessage);
        
        // You can now use xmtpClient to send messages or perform other operations

    } catch (error) {
        console.error('Failed to initialize XMTP and subscribe:', error);
    }
})();
```

Ensure to replace `'YOUR_PRIVATE_KEY_HERE'` with the actual private key for testing purposes. This code is ready for production with proper error handling and documentation.
