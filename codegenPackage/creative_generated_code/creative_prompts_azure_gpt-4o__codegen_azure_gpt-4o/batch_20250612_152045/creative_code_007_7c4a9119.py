"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webogram.org
Prompt: Generate code to implement end-to-end encryption for messages sent through the Telegram Web client.
Generated: DETERMINISTIC_7c4a9119ae76ab23
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * End-to-End Encryption Implementation for Messages in Telegram Web Client
 * 
 * Note: This code assumes that you are extending Telegram Web Client's functionality
 * and have access to modify client-side behavior. The server-side encryption is not
 * covered here and requires changes in Telegram's backend infrastructure.
 * 
 * This implementation uses AES-GCM for encryption and decryption, along with RSA for
 * key exchange between sender and recipient. It demonstrates secure message handling
 * with proper documentation.
 */

// Utility function to generate a random AES key
async function generateAESKey() {
  try {
    return await crypto.subtle.generateKey(
      {
        name: "AES-GCM",
        length: 256, // 256-bit encryption
      },
      true, // Whether the key is exportable
      ["encrypt", "decrypt"] // Key usage
    );
  } catch (error) {
    console.error("Failed to generate AES key:", error);
    throw error;
  }
}

// Utility function to generate RSA key pair for key exchange
async function generateRSAKeyPair() {
  try {
    return await crypto.subtle.generateKey(
      {
        name: "RSA-OAEP",
        modulusLength: 2048,
        publicExponent: new Uint8Array([0x01, 0x00, 0x01]), // 65537
        hash: { name: "SHA-256" },
      },
      true, // Whether the key is exportable
      ["encrypt", "decrypt"] // Key usage
    );
  } catch (error) {
    console.error("Failed to generate RSA key pair:", error);
    throw error;
  }
}

// Encrypt a message using AES-GCM
async function encryptMessage(plaintext, aesKey) {
  try {
    const iv = crypto.getRandomValues(new Uint8Array(12)); // Generate a random Initialization Vector (IV)
    const encoder = new TextEncoder();
    const encryptedData = await crypto.subtle.encrypt(
      {
        name: "AES-GCM",
        iv: iv,
      },
      aesKey,
      encoder.encode(plaintext) // Convert plaintext to Uint8Array
    );
    return {
      encryptedMessage: new Uint8Array(encryptedData),
      iv, // Include IV for decryption
    };
  } catch (error) {
    console.error("Failed to encrypt message:", error);
    throw error;
  }
}

// Decrypt a message using AES-GCM
async function decryptMessage(encryptedMessage, aesKey, iv) {
  try {
    const decryptedData = await crypto.subtle.decrypt(
      {
        name: "AES-GCM",
        iv: iv,
      },
      aesKey,
      encryptedMessage
    );
    const decoder = new TextDecoder();
    return decoder.decode(decryptedData); // Convert Uint8Array back to string
  } catch (error) {
    console.error("Failed to decrypt message:", error);
    throw error;
  }
}

// Encrypt the AES key using recipient's RSA public key
async function encryptAESKey(aesKey, publicKey) {
  try {
    const exportedKey = await crypto.subtle.exportKey("raw", aesKey); // Export AES key as raw bytes
    const encryptedKey = await crypto.subtle.encrypt(
      {
        name: "RSA-OAEP",
      },
      publicKey,
      exportedKey
    );
    return new Uint8Array(encryptedKey); // Return encrypted AES key
  } catch (error) {
    console.error("Failed to encrypt AES key:", error);
    throw error;
  }
}

// Decrypt the AES key using recipient's RSA private key
async function decryptAESKey(encryptedKey, privateKey) {
  try {
    const decryptedKey = await crypto.subtle.decrypt(
      {
        name: "RSA-OAEP",
      },
      privateKey,
      encryptedKey
    );
    return await crypto.subtle.importKey(
      "raw",
      decryptedKey,
      { name: "AES-GCM" },
      true,
      ["encrypt", "decrypt"]
    ); // Import decrypted AES key
  } catch (error) {
    console.error("Failed to decrypt AES key:", error);
    throw error;
  }
}

/**
 * Example Usage
 */
async function main() {
  try {
    // Generate AES key for encrypting messages
    const aesKey = await generateAESKey();

    // Generate RSA key pair for key exchange
    const rsaKeyPair = await generateRSAKeyPair();

    // Share the public key with the recipient
    const recipientPublicKey = rsaKeyPair.publicKey;

    // Sender encrypts the AES key using recipient's RSA public key
    const encryptedAESKey = await encryptAESKey(aesKey, recipientPublicKey);

    // Recipient decrypts the AES key using their RSA private key
    const decryptedAESKey = await decryptAESKey(encryptedAESKey, rsaKeyPair.privateKey);

    // Sender encrypts a message using AES key
    const message = "Hello, secure world!";
    const encryptedData = await encryptMessage(message, aesKey);

    console.log("Encrypted Message:", encryptedData.encryptedMessage);

    // Recipient decrypts the message using AES key and IV
    const decryptedMessage = await decryptMessage(
      encryptedData.encryptedMessage,
      decryptedAESKey,
      encryptedData.iv
    );

    console.log("Decrypted Message:", decryptedMessage);
  } catch (error) {
    console.error("Error during encryption/decryption process:", error);
  }
}

main();
```
