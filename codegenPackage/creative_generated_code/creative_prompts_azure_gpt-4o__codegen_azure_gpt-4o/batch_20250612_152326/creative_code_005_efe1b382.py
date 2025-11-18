"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://receive-dmailapp.pages.dev
Prompt: Write a tutorial for developers on integrating Dmail's decentralized communication system into a dApp, focusing on encrypted messaging and unified notifications.
Generated: DETERMINISTIC_efe1b38295068f54
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Tutorial: Integrating Dmail's Decentralized Communication System into a dApp
 * Focus: Encrypted messaging and unified notifications
 * Language: JavaScript (Node.js with web3.js for Ethereum-based dApps)
 */

// Required dependencies
// Install these packages: npm install dotenv web3 axios crypto
require('dotenv').config(); // For environment variable management
const Web3 = require('web3'); // For blockchain interaction
const axios = require('axios'); // For API requests (Dmail SDK or endpoints)
const crypto = require('crypto'); // For encryption and decryption

// Load environment variables (Set your own in a .env file)
const INFURA_ENDPOINT = process.env.INFURA_ENDPOINT; // Ethereum Node URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the wallet
const DMAIL_API_URL = process.env.DMAIL_API_URL; // Dmail API endpoint
const DMAIL_API_KEY = process.env.DMAIL_API_KEY; // Dmail API key

// Web3 setup
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_ENDPOINT)); // Connect to Ethereum node

/**
 * Function to encrypt a message
 * @param {string} message - Plain text message to encrypt
 * @return {object} - Encrypted message and key
 */
function encryptMessage(message) {
    try {
        const key = crypto.randomBytes(32); // Generate a random encryption key
        const iv = crypto.randomBytes(16); // Generate a random initialization vector (IV)
        const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
        let encrypted = cipher.update(message, 'utf8', 'hex');
        encrypted += cipher.final('hex');
        
        return {
            encryptedMessage: encrypted,
            encryptionKey: key.toString('hex'),
            iv: iv.toString('hex')
        };
    } catch (error) {
        console.error('Error encrypting message:', error);
        throw new Error('Encryption failed');
    }
}

/**
 * Function to decrypt a message
 * @param {string} encryptedMessage - Encrypted message
 * @param {string} key - Encryption key
 * @param {string} iv - Initialization vector
 * @return {string} - Decrypted plain text message
 */
function decryptMessage(encryptedMessage, key, iv) {
    try {
        const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key, 'hex'), Buffer.from(iv, 'hex'));
        let decrypted = decipher.update(encryptedMessage, 'hex', 'utf8');
        decrypted += decipher.final('utf8');
        return decrypted;
    } catch (error) {
        console.error('Error decrypting message:', error);
        throw new Error('Decryption failed');
    }
}

/**
 * Function to send an encrypted message to Dmail API
 * @param {string} receiverAddress - Receiver's wallet address
 * @param {string} message - Plain text message to send
 */
async function sendEncryptedMessage(receiverAddress, message) {
    try {
        // Encrypt the message
        const { encryptedMessage, encryptionKey, iv } = encryptMessage(message);

        // Prepare payload for Dmail API
        const payload = {
            receiver: receiverAddress,
            encryptedMessage: encryptedMessage,
            encryptionKey: encryptionKey,
            iv: iv
        };

        // Send the message via Dmail API
        const response = await axios.post(`${DMAIL_API_URL}/sendMessage`, payload, {
            headers: {
                'Authorization': `Bearer ${DMAIL_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        console.log('Message sent successfully:', response.data);
    } catch (error) {
        console.error('Error sending encrypted message:', error);
        throw new Error('Failed to send message');
    }
}

/**
 * Function to fetch notifications from Dmail API
 */
async function fetchNotifications() {
    try {
        const response = await axios.get(`${DMAIL_API_URL}/notifications`, {
            headers: {
                'Authorization': `Bearer ${DMAIL_API_KEY}`
            }
        });

        console.log('Notifications fetched successfully:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error fetching notifications:', error);
        throw new Error('Failed to fetch notifications');
    }
}

/**
 * Example usage of the above functions
 */
(async () => {
    try {
        const receiverAddress = '0xReceiverWalletAddress'; // Replace with the receiver's Ethereum address
        const message = 'Hello, this is an encrypted test message';

        // Send an encrypted message
        await sendEncryptedMessage(receiverAddress, message);

        // Fetch unified notifications
        const notifications = await fetchNotifications();
        console.log('Notifications:', notifications);
    } catch (error) {
        console.error('Error in example usage:', error);
    }
})();
```

### Notes:
- Replace placeholder values (`process.env.*`) with actual values or set them in your `.env` file.
- Ensure your Ethereum wallet and private key are secure and not exposed.
- Install the required packages using `npm` before running the script.
- Test this code in a development environment before deploying to production.
