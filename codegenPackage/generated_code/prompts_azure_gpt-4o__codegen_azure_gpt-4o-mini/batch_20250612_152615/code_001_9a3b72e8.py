"""
Generated Code Metadata:
========================
Original URL: https://icrossingappxyz.com
Prompt: Create a code snippet in JavaScript that encrypts personal data before sending it to the "Identitas Kependudukan Digital" app, ensuring compliance with the data security practices mentioned.
Generated: DETERMINISTIC_9a3b72e8254fdf71
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Encrypts personal data before sending it to the Identitas Kependudukan Digital app.
 * This function uses the Web Crypto API for secure encryption.
 * 
 * @param {Object} personalData - The personal data to encrypt.
 * @param {string} personalData.name - The name of the individual.
 * @param {string} personalData.nik - The National Identity Number.
 * @param {string} personalData.dob - The date of birth in YYYY-MM-DD format.
 * @param {string} password - The password used for encryption.
 * @returns {Promise<string>} - A promise that resolves to the encrypted data in base64 format.
 */
async function encryptPersonalData(personalData, password) {
    try {
        // Convert the password to a Uint8Array
        const encoder = new TextEncoder();
        const keyMaterial = await window.crypto.subtle.importKey(
            'raw',
            encoder.encode(password),
            { name: 'PBKDF2' },
            false,
            ['deriveBits', 'deriveKey']
        );

        // Derive a key from the password
        const salt = window.crypto.getRandomValues(new Uint8Array(16));
        const key = await window.crypto.subtle.deriveKey(
            {
                name: 'PBKDF2',
                salt: salt,
                iterations: 100000,
                hash: 'SHA-256'
            },
            keyMaterial,
            { name: 'AES-GCM', length: 256 },
            false,
            ['encrypt']
        );

        // Convert personal data to a JSON string
        const dataString = JSON.stringify(personalData);
        const dataBuffer = encoder.encode(dataString);

        // Encrypt the data
        const iv = window.crypto.getRandomValues(new Uint8Array(12)); // Initialization vector
        const encryptedData = await window.crypto.subtle.encrypt(
            {
                name: 'AES-GCM',
                iv: iv
            },
            key,
            dataBuffer
        );

        // Combine salt, iv, and encrypted data for transmission
        const combinedData = new Uint8Array(salt.length + iv.length + encryptedData.byteLength);
        combinedData.set(salt, 0);
        combinedData.set(iv, salt.length);
        combinedData.set(new Uint8Array(encryptedData), salt.length + iv.length);

        // Convert to base64 for easy transmission
        return btoa(String.fromCharCode(...combinedData));
    } catch (error) {
        console.error('Encryption failed:', error);
        throw new Error('Failed to encrypt personal data.');
    }
}

// Example usage
const personalData = {
    name: 'John Doe',
    nik: '1234567890123456',
    dob: '1990-01-01'
};

const password = 'securePassword123';

encryptPersonalData(personalData, password)
    .then(encryptedData => {
        console.log('Encrypted Data:', encryptedData);
        // Send encryptedData to the Identitas Kependudukan Digital app
    })
    .catch(error => {
        console.error('Error encrypting data:', error);
    });
```
