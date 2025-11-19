"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3.da2a.net
Prompt: Explain how to encrypt and decrypt data using the encryption key obtained from MetaMask.
Generated: DETERMINISTIC_96861bed8bc73c4a
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const crypto = require('crypto');

/**
 * Encrypts data using a specified encryption key.
 *
 * @param {string} key - The encryption key obtained from MetaMask.
 * @param {string} data - The plain text data to be encrypted.
 * @returns {string} - The encrypted data as a Base64 string.
 */
function encryptData(key, data) {
    try {
        // Generate a random initialization vector
        const iv = crypto.randomBytes(16);
        
        // Create a cipher object using the AES-256-CBC algorithm
        const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key, 'hex'), iv);

        // Encrypt the data
        let encrypted = cipher.update(data, 'utf8', 'base64');
        encrypted += cipher.final('base64');

        // Return the IV and the encrypted data concatenated together
        return iv.toString('base64') + ':' + encrypted;
    } catch (error) {
        console.error("Encryption error:", error);
        throw new Error("Failed to encrypt data.");
    }
}

/**
 * Decrypts data using a specified encryption key.
 *
 * @param {string} key - The encryption key obtained from MetaMask.
 * @param {string} encryptedData - The encrypted data to decrypt, including the IV.
 * @returns {string} - The decrypted plain text data.
 */
function decryptData(key, encryptedData) {
    try {
        // Split the IV and the encrypted data
        const [ivBase64, encryptedText] = encryptedData.split(':');
        const iv = Buffer.from(ivBase64, 'base64');

        // Create a decipher object using the AES-256-CBC algorithm
        const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key, 'hex'), iv);

        // Decrypt the data
        let decrypted = decipher.update(encryptedText, 'base64', 'utf8');
        decrypted += decipher.final('utf8');

        return decrypted;
    } catch (error) {
        console.error("Decryption error:", error);
        throw new Error("Failed to decrypt data.");
    }
}

// Example usage
const metaMaskKey = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'; // Replace with your actual key
const plaintext = 'Hello, World!';

// Encrypt the data
const encrypted = encryptData(metaMaskKey, plaintext);
console.log('Encrypted Data:', encrypted);

// Decrypt the data
const decrypted = decryptData(metaMaskKey, encrypted);
console.log('Decrypted Data:', decrypted);
```

### Important Notes:
- Ensure the encryption key is securely generated and handled.
- The example uses an AES-256-CBC algorithm; make sure your key is 32 bytes long (64 hex characters).
- The code assumes that the key is provided in hexadecimal format. Adjust accordingly if needed.
