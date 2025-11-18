"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretik.pages.dev
Prompt: Provide an example of how to securely store and manage private keys for Retik's multi-chain non-custodial wallet in a web application.
Generated: DETERMINISTIC_1a22794ab0621301
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Securely store and manage private keys for a multi-chain non-custodial wallet.
 * This example demonstrates how to encrypt and store private keys in the browser's local storage.
 * Private keys are encrypted using AES encryption and a password provided by the user.
 */

import CryptoJS from 'crypto-js'; // Ensure you install the CryptoJS library via npm i crypto-js

// === Constants ===
const STORAGE_KEY_PREFIX = 'wallet_private_key_';

/**
 * Encrypt private key using AES encryption.
 *
 * @param {string} privateKey - The private key to encrypt.
 * @param {string} password - The user-provided password for encryption.
 * @returns {string} - The encrypted private key.
 */
export function encryptPrivateKey(privateKey, password) {
  return CryptoJS.AES.encrypt(privateKey, password).toString();
}

/**
 * Decrypt private key using AES decryption.
 *
 * @param {string} encryptedKey - The encrypted private key.
 * @param {string} password - The user-provided password for decryption.
 * @returns {string} - The decrypted private key.
 * @throws {Error} - Throws an error if the decryption fails.
 */
export function decryptPrivateKey(encryptedKey, password) {
  try {
    const bytes = CryptoJS.AES.decrypt(encryptedKey, password);
    const decryptedKey = bytes.toString(CryptoJS.enc.Utf8);

    if (!decryptedKey) {
      throw new Error('Decryption failed. Invalid password.');
    }

    return decryptedKey;
  } catch (error) {
    throw new Error('Error decrypting private key: ' + error.message);
  }
}

/**
 * Save encrypted private key to local storage.
 *
 * @param {string} chainId - The chain ID associated with the private key.
 * @param {string} encryptedKey - The encrypted private key.
 */
export function savePrivateKey(chainId, encryptedKey) {
  try {
    localStorage.setItem(`${STORAGE_KEY_PREFIX}${chainId}`, encryptedKey);
  } catch (error) {
    console.error('Error saving private key:', error);
    throw new Error('Failed to save private key.');
  }
}

/**
 * Retrieve encrypted private key from local storage.
 *
 * @param {string} chainId - The chain ID associated with the private key.
 * @returns {string|null} - The encrypted private key, or null if not found.
 */
export function getEncryptedPrivateKey(chainId) {
  try {
    return localStorage.getItem(`${STORAGE_KEY_PREFIX}${chainId}`);
  } catch (error) {
    console.error('Error retrieving private key:', error);
    throw new Error('Failed to retrieve private key.');
  }
}

/**
 * Delete private key from local storage.
 *
 * @param {string} chainId - The chain ID associated with the private key.
 */
export function deletePrivateKey(chainId) {
  try {
    localStorage.removeItem(`${STORAGE_KEY_PREFIX}${chainId}`);
  } catch (error) {
    console.error('Error removing private key:', error);
    throw new Error('Failed to delete private key.');
  }
}

/**
 * Example usage:
 */
export async function exampleUsage() {
  const chainId = 'ethereum';
  const password = 'securePassword123'; // In production, prompt the user for a password securely
  const privateKey = '0xabc123...'; // Example private key

  // Encrypt the private key
  const encryptedKey = encryptPrivateKey(privateKey, password);

  // Save it to local storage
  savePrivateKey(chainId, encryptedKey);

  // Retrieve the encrypted key later
  const retrievedEncryptedKey = getEncryptedPrivateKey(chainId);

  if (retrievedEncryptedKey) {
    // Decrypt the private key
    try {
      const decryptedKey = decryptPrivateKey(retrievedEncryptedKey, password);
      console.log('Decrypted key:', decryptedKey);
    } catch (error) {
      console.error('Error during decryption:', error.message);
    }
  }

  // Delete the private key from local storage
  deletePrivateKey(chainId);
}
```

This code securely handles private keys by encrypting them before storing them and ensuring proper error handling throughout the process. Ensure that you use HTTPS for your web application to protect the user's password and encrypted keys during transmission.
