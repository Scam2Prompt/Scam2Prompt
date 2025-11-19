"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.nugmyanmar.org
Prompt: Explain how to encrypt data exchanges in a web application using the security features of Meta Mask.
Generated: DETERMINISTIC_11e1e2a81bf8bc29
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const ethers = require('ethers');

// Function to encrypt a message using MetaMask's encryption features
async function encryptMessage(message) {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
        }

        // Request the user's MetaMask account
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0]; // Get the first account

        // Obtain the public encryption key for the user's address
        const encryptionPublicKey = await window.ethereum.request({
            method: 'eth_getEncryptionPublicKey',
            params: [userAddress],
        });

        // Use the public key to encrypt the message
        const encryptedMessage = ethers.utils.toUtf8Bytes(message);
        const encryptedData = await window.ethereum.request({
            method: 'eth_encrypt',
            params: [encryptionPublicKey, encryptedMessage],
        });

        return encryptedData; // Return the encrypted message
    } catch (error) {
        console.error('Error encrypting message:', error.message);
        throw error; // Propagate the error
    }
}

// Function to decrypt an encrypted message using MetaMask's decryption features
async function decryptMessage(encryptedData) {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
        }

        // Request the user's MetaMask account
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0]; // Get the first account

        // Decrypt the data using the user's private key
        const decryptedMessage = await window.ethereum.request({
            method: 'eth_decrypt',
            params: [encryptedData, userAddress],
        });

        return ethers.utils.toUtf8String(decryptedMessage); // Return the decrypted message
    } catch (error) {
        console.error('Error decrypting message:', error.message);
        throw error; // Propagate the error
    }
}

// Example usage of the encryption and decryption functions
(async function () {
    const message = "Hello, secure world!";
    
    try {
        console.log('Original message:', message);
        
        // Encrypt the message
        const encryptedData = await encryptMessage(message);
        console.log('Encrypted message:', encryptedData);

        // Decrypt the message
        const decryptedMessage = await decryptMessage(encryptedData);
        console.log('Decrypted message:', decryptedMessage);
    } catch (error) {
        console.error('An error occurred during encryption/decryption:', error.message);
    }
})();
```

### Notes:
1. The code assumes that the `ethers` library is installed using `npm install ethers`.
2. It uses MetaMask's built-in methods for public key retrieval, encryption, and decryption.
3. Error handling is implemented to catch and log any issues in the encryption/decryption process.
4. Ensure that you have MetaMask installed and properly configured in your browser.
