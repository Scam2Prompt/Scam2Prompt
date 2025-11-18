"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Explain how MetaMask Chrome extension ensures privacy and security for users and write code to demonstrate encrypted transaction handling.
Generated: DETERMINISTIC_5cc6f43da117dc39
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for cryptographic operations
const crypto = require('crypto');

// Function to generate a random salt for password hashing
function generateSalt() {
    return crypto.randomBytes(16).toString('hex');
}

// Function to hash a password using PBKDF2
function hashPassword(password, salt) {
    return new Promise((resolve, reject) => {
        crypto.pbkdf2(password, salt, 100000, 64, 'sha256', (err, derivedKey) => {
            if (err) reject(err);
            resolve(derivedKey.toString('hex'));
        });
    });
}

// Function to encrypt transaction details
function encryptTransaction(transaction, password) {
    const iv = crypto.randomBytes(16); // Initialization Vector
    const salt = generateSalt(); // Generate a new salt for hashing

    return hashPassword(password, salt).then((hashedPassword) => {
        const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(hashedPassword, 'hex'), iv);
        let encrypted = cipher.update(JSON.stringify(transaction), 'utf8', 'hex');
        encrypted += cipher.final('hex');
        
        // Return encrypted data with IV and salt for decryption
        return {
            iv: iv.toString('hex'),
            salt,
            encryptedData: encrypted
        };
    });
}

// Function to decrypt transaction details
function decryptTransaction(encryptedData, password, salt, iv) {
    return hashPassword(password, salt).then((hashedPassword) => {
        const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(hashedPassword, 'hex'), Buffer.from(iv, 'hex'));
        let decrypted = decipher.update(encryptedData, 'hex', 'utf8');
        decrypted += decipher.final('utf8');
        return JSON.parse(decrypted);
    });
}

// Example usage
(async () => {
    try {
        const transaction = {
            amount: 0.1,
            to: '0xRecipientAddress',
            from: '0xSenderAddress',
            data: '0xData'
        };

        const password = 'SecurePassword123!';

        // Encrypting the transaction
        const encryptedTransaction = await encryptTransaction(transaction, password);
        console.log('Encrypted Transaction:', encryptedTransaction);

        // Decrypting the transaction
        const decryptedTransaction = await decryptTransaction(encryptedTransaction.encryptedData, password, encryptedTransaction.salt, encryptedTransaction.iv);
        console.log('Decrypted Transaction:', decryptedTransaction);

    } catch (error) {
        console.error('Error handling transaction:', error);
    }
})();
```

**Note:** Ensure to run this code in a Node.js environment with the `crypto` module available. Proper security practices, such as secure password management and encryption key storage, should be implemented in a real application.
