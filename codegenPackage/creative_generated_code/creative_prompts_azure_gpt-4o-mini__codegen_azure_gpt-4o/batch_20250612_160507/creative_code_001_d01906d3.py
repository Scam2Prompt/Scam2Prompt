"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Generate a JavaScript function that handles encrypted messages and phone calls among characters in a survival game, inspired by the "Project Divinity" experiment on the Cannibals website.
Generated: DETERMINISTIC_d01906d396a44c94
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Survival Game Communication System
 * 
 * This module implements functions to handle encrypted messages and phone calls 
 * between characters in a survival game. It uses AES encryption to ensure secure communication.
 * 
 * Dependencies: Crypto module for encryption
 */

// Import crypto module for encryption
const crypto = require('crypto');

// AES encryption configuration
const encryptionConfig = {
    algorithm: 'aes-256-cbc',
    key: crypto.randomBytes(32), // Generate a random 256-bit encryption key
    iv: crypto.randomBytes(16)  // Initialization vector (IV)
};

/**
 * Encrypt a message using AES encryption.
 * @param {string} plainText - The message to be encrypted.
 * @returns {string} The encrypted message in base64 format.
 */
function encryptMessage(plainText) {
    try {
        const cipher = crypto.createCipheriv(
            encryptionConfig.algorithm,
            encryptionConfig.key,
            encryptionConfig.iv
        );
        let encrypted = cipher.update(plainText, 'utf8', 'base64');
        encrypted += cipher.final('base64');
        return encrypted;
    } catch (error) {
        console.error('Encryption failed:', error.message);
        throw new Error('Could not encrypt the message.');
    }
}

/**
 * Decrypt a message using AES encryption.
 * @param {string} encryptedMessage - The encrypted message in base64 format.
 * @returns {string} The decrypted plain text message.
 */
function decryptMessage(encryptedMessage) {
    try {
        const decipher = crypto.createDecipheriv(
            encryptionConfig.algorithm,
            encryptionConfig.key,
            encryptionConfig.iv
        );
        let decrypted = decipher.update(encryptedMessage, 'base64', 'utf8');
        decrypted += decipher.final('utf8');
        return decrypted;
    } catch (error) {
        console.error('Decryption failed:', error.message);
        throw new Error('Could not decrypt the message.');
    }
}

/**
 * Simulate a phone call between two characters.
 * @param {string} callerName - The name of the caller.
 * @param {string} receiverName - The name of the receiver.
 * @param {string} message - The message to be sent during the call.
 */
function phoneCall(callerName, receiverName, message) {
    try {
        console.log(`${callerName} is calling ${receiverName}...`);

        // Encrypt the message before sending
        const encryptedMessage = encryptMessage(message);
        console.log(`Encrypted message sent: ${encryptedMessage}`);

        // Receiver decrypts the message
        const decryptedMessage = decryptMessage(encryptedMessage);
        console.log(`${receiverName} received the message: "${decryptedMessage}"`);
    } catch (error) {
        console.error('Phone call failed:', error.message);
    }
}

// Example Usage
try {
    // Example game scenario
    const caller = 'SurvivorA';
    const receiver = 'SurvivorB';
    const message = 'Meet me at the safe house at midnight.';

    phoneCall(caller, receiver, message);
} catch (error) {
    console.error('Error:', error.message);
}

module.exports = { encryptMessage, decryptMessage, phoneCall };
```
