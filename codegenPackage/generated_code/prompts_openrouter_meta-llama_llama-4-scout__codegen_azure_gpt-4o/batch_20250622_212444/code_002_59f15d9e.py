"""
Generated Code Metadata:
========================
Original URL: https://privnote.chat
Prompt: Generate a code example in Node.js for encrypting and decrypting notes using binary encryption (0s and 1s).
Generated: DETERMINISTIC_59f15d9ec74d5ab9
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the 'crypto' module for encryption and decryption
const crypto = require('crypto');

// Configuration for encryption
const ENCRYPTION_KEY = crypto.randomBytes(32); // 256-bit key
const IV_LENGTH = 16; // Initialization vector length (128-bit)

// Function to encrypt a note
function encryptNote(note) {
  try {
    // Generate a random initialization vector (IV)
    const iv = crypto.randomBytes(IV_LENGTH);

    // Create a cipher instance using AES-256-CBC
    const cipher = crypto.createCipheriv('aes-256-cbc', ENCRYPTION_KEY, iv);

    // Encrypt the note and convert it to binary (base64 encoding)
    let encrypted = cipher.update(note, 'utf8', 'base64');
    encrypted += cipher.final('base64');

    // Return the encrypted note along with the IV (needed for decryption)
    return {
      iv: iv.toString('base64'),
      encryptedData: encrypted,
    };
  } catch (error) {
    console.error('Error encrypting note:', error.message);
    throw new Error('Encryption failed');
  }
}

// Function to decrypt a note
function decryptNote(encryptedNote) {
  try {
    // Extract the IV and encrypted data from the input
    const iv = Buffer.from(encryptedNote.iv, 'base64');
    const encryptedData = encryptedNote.encryptedData;

    // Create a decipher instance using AES-256-CBC
    const decipher = crypto.createDecipheriv('aes-256-cbc', ENCRYPTION_KEY, iv);

    // Decrypt the data and convert it back to UTF-8
    let decrypted = decipher.update(encryptedData, 'base64', 'utf8');
    decrypted += decipher.final('utf8');

    // Return the decrypted note
    return decrypted;
  } catch (error) {
    console.error('Error decrypting note:', error.message);
    throw new Error('Decryption failed');
  }
}

// Example usage
try {
  const note = 'This is a secret note.';
  console.log('Original Note:', note);

  // Encrypt the note
  const encryptedNote = encryptNote(note);
  console.log('Encrypted Note:', encryptedNote);

  // Decrypt the note
  const decryptedNote = decryptNote(encryptedNote);
  console.log('Decrypted Note:', decryptedNote);
} catch (error) {
  console.error('An error occurred:', error.message);
}
```
