"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dggg-7er.pages.dev
Prompt: Write a code example for integrating Dmail's messaging protocol into a Web3 application to send unified notifications across 16 supported networks.
Generated: DETERMINISTIC_43878beba808deb2
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { DMailClient } from 'dmail-sdk';
import { ethers } from 'ethers';

// Define constants
const DMAIL_API_KEY = 'your-dmail-api-key'; // Replace with your actual Dmail API key
const SUPPORTED_NETWORKS = [
    'Ethereum',
    'Polygon',
    'Binance Smart Chain',
    'Avalanche',
    'Fantom',
    'Harmony',
    'Arbitrum',
    'Optimism',
    'Celo',
    'Tezos',
    'Algorand',
    'Cardano',
    'Solana',
    'EOS',
    'Polkadot',
    'Near'
];

// Initialize DMail client
const dmailClient = new DMailClient(DMAIL_API_KEY);

// Function to send a notification
async function sendNotification(recipientAddress, message) {
    try {
        // Validate recipient address
        if (!ethers.utils.isAddress(recipientAddress)) {
            throw new Error('Invalid recipient address');
        }

        // Validate message length
        if (message.length === 0 || message.length > 256) {
            throw new Error('Message must be between 1 and 256 characters');
        }

        // Prepare the notification payload
        const notificationPayload = {
            recipient: recipientAddress,
            message: message,
            timestamp: new Date().toISOString(),
            networks: SUPPORTED_NETWORKS
        };

        // Send notification using DMail client
        const response = await dmailClient.sendMessage(notificationPayload);

        // Log the response
        console.log('Notification sent successfully:', response);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error sending notification:', error.message);
    }
}

// Example usage of the sendNotification function
(async () => {
    const recipient = '0xYourRecipientAddress'; // Replace with the actual recipient address
    const message = 'Hello from our Web3 application!';

    // Send the notification
    await sendNotification(recipient, message);
})();
```
