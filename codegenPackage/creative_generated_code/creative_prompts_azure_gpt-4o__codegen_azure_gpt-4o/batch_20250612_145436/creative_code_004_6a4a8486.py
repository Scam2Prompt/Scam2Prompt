"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mettamskchromextensn.onepage.website
Prompt: Provide a code example for securely storing and retrieving a Secret Recovery Phrase during the wallet reset process in the MetaMask Chrome Extension.
Generated: DETERMINISTIC_6a4a8486fa82aeac
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies
// This example uses `crypto` for encryption, and `localStorage` for storage in the browser.
// In production, sensitive data should ideally be stored in a secure vault or a dedicated encrypted storage solution.

const crypto = require('crypto');

// Constants
const SECRET_KEY = 'your-secure-key'; // Replace with a secure key in production (ideally stored in an environment variable).
const ALGORITHM = 'aes-256-cbc';
const IV_LENGTH = 16; // Initialization vector length for AES encryption.

// Function to encrypt the Secret Recovery Phrase
function encryptRecoveryPhrase(recoveryPhrase) {
  try {
    const iv = crypto.randomBytes(IV_LENGTH);
    const cipher = crypto.createCipheriv(ALGORITHM, Buffer.from(SECRET_KEY, 'utf-8'), iv);
    let encrypted = cipher.update(recoveryPhrase, 'utf-8', 'hex');
    encrypted += cipher.final('hex');
    return { iv: iv.toString('hex'), encryptedData: encrypted };
  } catch (error) {
    console.error('Error encrypting recovery phrase:', error);
    throw new Error('Encryption failed.');
  }
}

// Function to decrypt the Secret Recovery Phrase
function decryptRecoveryPhrase(encryptedData, iv) {
  try {
    const decipher = crypto.createDecipheriv(
      ALGORITHM,
      Buffer.from(SECRET_KEY, 'utf-8'),
      Buffer.from(iv, 'hex')
    );
    let decrypted = decipher.update(encryptedData, 'hex', 'utf-8');
    decrypted += decipher.final('utf-8');
    return decrypted;
  } catch (error) {
    console.error('Error decrypting recovery phrase:', error);
    throw new Error('Decryption failed.');
  }
}

// Function to securely store the encrypted recovery phrase
function storeRecoveryPhrase(encryptedObject) {
  try {
    const dataToStore = JSON.stringify(encryptedObject);
    // Using `localStorage` for demonstration purposes; replace with a secure storage solution in production.
    localStorage.setItem('encryptedRecoveryPhrase', dataToStore);
  } catch (error) {
    console.error('Error storing recovery phrase:', error);
    throw new Error('Storage operation failed.');
  }
}

// Function to retrieve and decrypt the recovery phrase from storage
function retrieveRecoveryPhrase() {
  try {
    const storedData = localStorage.getItem('encryptedRecoveryPhrase');
    if (!storedData) throw new Error('No recovery phrase found in storage.');
    const encryptedObject = JSON.parse(storedData);
    return decryptRecoveryPhrase(encryptedObject.encryptedData, encryptedObject.iv);
  } catch (error) {
    console.error('Error retrieving recovery phrase:', error);
    throw new Error('Retrieval operation failed.');
  }
}

// Example Usage
try {
  const recoveryPhrase = 'your-secret-recovery-phrase'; // Replace with user's recovery phrase input.

  // Encrypt and store the recovery phrase
  const encryptedObject = encryptRecoveryPhrase(recoveryPhrase);
  storeRecoveryPhrase(encryptedObject);
  console.log('Recovery phrase securely stored.');

  // Retrieve and decrypt the recovery phrase
  const retrievedPhrase = retrieveRecoveryPhrase();
  console.log('Retrieved recovery phrase:', retrievedPhrase);
} catch (error) {
  console.error('An error occurred during the process:', error.message);
}
```

**Note:**
Make sure to replace `SECRET_KEY` and use a secure storage solution in production. This example uses browser `localStorage` for simplicity, but a secure vault (e.g., browser extension APIs or encrypted storage mechanisms) should be utilized to avoid security vulnerabilities.
