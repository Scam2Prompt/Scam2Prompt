"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icrossingappxyz.com
Prompt: Create a code snippet in JavaScript that encrypts personal data before sending it to the "Identitas Kependudukan Digital" app, ensuring compliance with the data security practices mentioned.
Generated: DETERMINISTIC_9a3b72e8254fdf71
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the crypto module for encryption
const crypto = require('crypto');

/**
 * Encrypts personal data using AES-256-CBC.
 * @param {string} plaintextData - The personal data to be encrypted.
 * @param {string} encryptionKey - A 32-character encryption key (256-bit).
 * @returns {string} - The encrypted data in Base64 format.
 * @throws {Error} - Throws an error if encryption fails.
 */
function encryptPersonalData(plaintextData, encryptionKey) {
    try {
        // Validate that the encryption key has the correct length (32 bytes / 256-bit)
        if (encryptionKey.length !== 32) {
            throw new Error("Encryption key must be exactly 32 characters long.");
        }

        // Generate a random initialization vector (IV) - 16 bytes for AES-256-CBC
        const iv = crypto.randomBytes(16);

        // Create a cipher instance using AES-256-CBC
        const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(encryptionKey), iv);

        // Encrypt the data
        let encryptedData = cipher.update(plaintextData, 'utf8', 'base64');
        encryptedData += cipher.final('base64');

        // Combine the IV and encrypted data for transmission
        const encryptedPayload = iv.toString('base64') + ':' + encryptedData;

        return encryptedPayload;
    } catch (error) {
        // Log the error to the console for debugging purposes
        console.error("Data encryption failed:", error.message);

        // Re-throw the error to be handled by the caller
        throw error;
    }
}

/**
 * Example usage of the encryptPersonalData function.
 */
try {
    // Define sensitive data to be encrypted
    const personalData = "John Doe, 123456789, johndoe@example.com";

    // Define a 32-character encryption key (make sure to securely store this key)
    const encryptionKey = "your_secure_32_character_key_here";

    // Encrypt the personal data before sending it
    const encryptedData = encryptPersonalData(personalData, encryptionKey);

    // Log the encrypted data (for demonstration purposes only)
    console.log("Encrypted Data:", encryptedData);

    // Transmit the encrypted data securely to the app (pseudo-code)
    // sendToApp("Identitas Kependudukan Digital", encryptedData);
} catch (error) {
    console.error("An error occurred during encryption:", error.message);
}
```
