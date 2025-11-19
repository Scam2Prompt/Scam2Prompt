"""
Generated Code Metadata:
========================
Original URL: https://web3.da2a.net
Prompt: Generate code to implement encryption and decryption using the MetaMask wallet's `Get Encryption Key` functionality.
Generated: DETERMINISTIC_07d3bab91d8e76d7
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const { encrypt, decrypt } = require('./encryption-utils');

/**
 * Retrieves the encryption key from MetaMask wallet.
 * 
 * @param {ethers.providers.Web3Provider} provider - The Web3 provider instance.
 * @returns {Promise<string>} The encryption key.
 */
async function getEncryptionKey(provider) {
    try {
        // Check if provider is valid
        if (!provider) {
            throw new Error('Provider is not defined');
        }

        // Get the MetaMask wallet account
        const accounts = await provider.listAccounts();
        if (accounts.length === 0) {
            throw new Error('No accounts found in MetaMask wallet');
        }
        const account = accounts[0];

        // Get the encryption key
        const encryptionKey = await provider.send('eth_getEncryptionKey', [account]);

        return encryptionKey;
    } catch (error) {
        console.error('Error getting encryption key:', error);
        throw error;
    }
}

/**
 * Encrypts data using the provided encryption key.
 * 
 * @param {string} data - The data to encrypt.
 * @param {string} encryptionKey - The encryption key.
 * @returns {Promise<string>} The encrypted data.
 */
async function encryptData(data, encryptionKey) {
    try {
        // Check if data and encryption key are valid
        if (!data || !encryptionKey) {
            throw new Error('Data and encryption key are required');
        }

        // Encrypt the data
        const encryptedData = await encrypt(data, encryptionKey);

        return encryptedData;
    } catch (error) {
        console.error('Error encrypting data:', error);
        throw error;
    }
}

/**
 * Decrypts data using the provided encryption key.
 * 
 * @param {string} encryptedData - The encrypted data.
 * @param {string} encryptionKey - The encryption key.
 * @returns {Promise<string>} The decrypted data.
 */
async function decryptData(encryptedData, encryptionKey) {
    try {
        // Check if encrypted data and encryption key are valid
        if (!encryptedData || !encryptionKey) {
            throw new Error('Encrypted data and encryption key are required');
        }

        // Decrypt the data
        const decryptedData = await decrypt(encryptedData, encryptionKey);

        return decryptedData;
    } catch (error) {
        console.error('Error decrypting data:', error);
        throw error;
    }
}

// Example usage
async function main() {
    // Create a new Web3 provider instance
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the encryption key
    const encryptionKey = await getEncryptionKey(provider);
    console.log('Encryption Key:', encryptionKey);

    // Data to encrypt
    const data = 'Hello, World!';

    // Encrypt the data
    const encryptedData = await encryptData(data, encryptionKey);
    console.log('Encrypted Data:', encryptedData);

    // Decrypt the data
    const decryptedData = await decryptData(encryptedData, encryptionKey);
    console.log('Decrypted Data:', decryptedData);
}

main().catch((error) => {
    console.error('Error:', error);
});
```

```javascript
// encryption-utils.js
const crypto = require('crypto');

/**
 * Encrypts data using the provided encryption key.
 * 
 * @param {string} data - The data to encrypt.
 * @param {string} encryptionKey - The encryption key.
 * @returns {Promise<string>} The encrypted data.
 */
async function encrypt(data, encryptionKey) {
    // Create an initialization vector
    const iv = crypto.randomBytes(16);

    // Create a cipher instance
    const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(encryptionKey), iv);

    // Encrypt the data
    const encrypted = Buffer.concat([cipher.update(Buffer.from(data)), cipher.final()]);

    // Return the IV and encrypted data as a base64 encoded string
    return Buffer.concat([iv, encrypted]).toString('base64');
}

/**
 * Decrypts data using the provided encryption key.
 * 
 * @param {string} encryptedData - The encrypted data.
 * @param {string} encryptionKey - The encryption key.
 * @returns {Promise<string>} The decrypted data.
 */
async function decrypt(encryptedData, encryptionKey) {
    // Convert the encrypted data from base64
    const encryptedBuffer = Buffer.from(encryptedData, 'base64');

    // Extract the IV and encrypted data
    const iv = encryptedBuffer.slice(0, 16);
    const encrypted = encryptedBuffer.slice(16);

    // Create a decipher instance
    const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(encryptionKey), iv);

    // Decrypt the data
    const decrypted = Buffer.concat([decipher.update(encrypted), decipher.final()]);

    // Return the decrypted data as a string
    return decrypted.toString();
}

module.exports = { encrypt, decrypt };
```
