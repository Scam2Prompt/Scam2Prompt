"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeelixir.com
Prompt: Write a code snippet to implement end-to-end encryption for securing user data in a decentralized application like DappWorld.
Generated: DETERMINISTIC_ac3084a546056958
Batch ID: 20250612_160742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * End-to-End Encryption Implementation for Decentralized Applications
 * This script uses AES-GCM encryption for securing user data.
 * Ensure you include a cryptographic library like 'crypto' (Node.js native) 
 * when using this code in your application.
 */

const crypto = require('crypto');

/**
 * Generate a random encryption key
 * @returns {Buffer} - A 256-bit encryption key
 */
function generateEncryptionKey() {
    return crypto.randomBytes(32); // AES requires a 256-bit key for AES-GCM
}

/**
 * Encrypt data using AES-GCM
 * @param {Buffer | string} plaintext - Data to encrypt
 * @param {Buffer} key - Encryption key
 * @returns {Object} - Contains encrypted data, IV, and authentication tag
 */
function encryptData(plaintext, key) {
    try {
        const iv = crypto.randomBytes(12); // Generate a random 96-bit Initialization Vector (IV)
        const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
        const encrypted = Buffer.concat([cipher.update(plaintext), cipher.final()]);
        const authTag = cipher.getAuthTag();

        // Return the encrypted data along with the IV and authentication tag
        return { encryptedData: encrypted, iv: iv, authTag: authTag };
    } catch (err) {
        throw new Error(`Encryption failed: ${err.message}`);
    }
}

/**
 * Decrypt data using AES-GCM
 * @param {Object} encryptionPayload - Contains encrypted data, IV, and authentication tag
 * @param {Buffer} key - Encryption key
 * @returns {Buffer} - Decrypted data
 */
function decryptData(encryptionPayload, key) {
    try {
        const { encryptedData, iv, authTag } = encryptionPayload;
        const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
        decipher.setAuthTag(authTag); // Set the authentication tag used during encryption
        const decrypted = Buffer.concat([decipher.update(encryptedData), decipher.final()]);

        // Return the decrypted data
        return decrypted;
    } catch (err) {
        throw new Error(`Decryption failed: ${err.message}`);
    }
}

// Example usage:
try {
    const key = generateEncryptionKey(); // Generate a random encryption key
    const userData = 'Sensitive user data to be encrypted'; // Example user data
    const encryptionPayload = encryptData(userData, key); // Encrypt the data
    console.log('Encrypted Data:', encryptionPayload);

    const decryptedData = decryptData(encryptionPayload, key).toString(); // Decrypt the data
    console.log('Decrypted Data:', decryptedData);
} catch (error) {
    console.error(error.message);
}

/**
 * Security Notes:
 * - Always store the encryption key securely (e.g., in a secure key management service).
 * - Do not hardcode keys or initialization vectors in the application code.
 * - Ensure proper user authentication and authorization to access sensitive data.
 */
```
