"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Develop a feature that enables end-to-end encrypted messaging on the XMTP network, as mentioned in the halo.social documentation.
Generated: DETERMINISTIC_eed2027cec74a6bc
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies from the XMTP SDK
const { Client, Message } = require('@xmtp/xmtp-js');
const crypto = require('crypto');

/**
 * Initialize XMTP client for a given wallet.
 * @param {Object} wallet - Wallet object compatible with XMTP.
 * @returns {Promise<Client>} - XMTP client instance.
 */
async function initializeXmtpClient(wallet) {
  try {
    // Create XMTP client
    const client = await Client.create(wallet, { env: 'production' });
    console.log('XMTP client initialized successfully.');
    return client;
  } catch (error) {
    console.error('Failed to initialize XMTP client:', error.message);
    throw error;
  }
}

/**
 * Generate an encryption key for end-to-end encryption.
 * @returns {string} - Encryption key in hex format.
 */
function generateEncryptionKey() {
  return crypto.randomBytes(32).toString('hex');
}

/**
 * Encrypt a message using AES-256-CBC.
 * @param {string} message - Plaintext message.
 * @param {string} encryptionKey - Hexadecimal encryption key.
 * @returns {string} - Base64-encoded ciphertext.
 */
function encryptMessage(message, encryptionKey) {
  const keyBuffer = Buffer.from(encryptionKey, 'hex');
  const iv = crypto.randomBytes(16); // Initialization vector
  const cipher = crypto.createCipheriv('aes-256-cbc', keyBuffer, iv);
  let encrypted = cipher.update(message, 'utf8', 'base64');
  encrypted += cipher.final('base64');
  return `${iv.toString('base64')}:${encrypted}`;
}

/**
 * Decrypt a message encrypted with AES-256-CBC.
 * @param {string} encryptedMessage - Base64-encoded ciphertext.
 * @param {string} encryptionKey - Hexadecimal encryption key.
 * @returns {string} - Decrypted plaintext message.
 */
function decryptMessage(encryptedMessage, encryptionKey) {
  const [ivBase64, ciphertextBase64] = encryptedMessage.split(':');
  const keyBuffer = Buffer.from(encryptionKey, 'hex');
  const iv = Buffer.from(ivBase64, 'base64');
  const decipher = crypto.createDecipheriv('aes-256-cbc', keyBuffer, iv);
  let decrypted = decipher.update(ciphertextBase64, 'base64', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

/**
 * Send an encrypted message using the XMTP client.
 * @param {Client} client - XMTP client instance.
 * @param {string} recipientAddress - Ethereum address of the recipient.
 * @param {string} message - Plaintext message to be sent.
 * @param {string} encryptionKey - Encryption key in hex format.
 */
async function sendEncryptedMessage(client, recipientAddress, message, encryptionKey) {
  try {
    const encryptedMessage = encryptMessage(message, encryptionKey);
    const conversation = await client.conversations.newConversation(recipientAddress);
    await conversation.send(encryptedMessage);
    console.log(`Encrypted message sent to ${recipientAddress}.`);
  } catch (error) {
    console.error('Failed to send encrypted message:', error.message);
    throw error;
  }
}

/**
 * Receive and decrypt messages for a given XMTP conversation.
 * @param {Client} client - XMTP client instance.
 * @param {string} encryptionKey - Encryption key in hex format.
 */
async function receiveAndDecryptMessages(client, encryptionKey) {
  try {
    const conversations = await client.conversations.list();
    for (const conversation of conversations) {
      const messages = await conversation.messages();
      for (const message of messages) {
        try {
          const decryptedMessage = decryptMessage(message.content, encryptionKey);
          console.log(`Received message from ${message.senderAddress}: ${decryptedMessage}`);
        } catch (decryptionError) {
          console.error('Failed to decrypt message:', decryptionError.message);
        }
      }
    }
  } catch (error) {
    console.error('Failed to receive and decrypt messages:', error.message);
    throw error;
  }
}

// Example usage:

(async () => {
  try {
    const wallet = /* Your wallet object here */;
    const xmtpClient = await initializeXmtpClient(wallet);

    const encryptionKey = generateEncryptionKey();
    const recipientAddress = '0xRecipientEthereumAddress';
    const messageToSend = 'Hello, this is an encrypted message!';

    // Send an encrypted message
    await sendEncryptedMessage(xmtpClient, recipientAddress, messageToSend, encryptionKey);

    // Receive and decrypt messages
    await receiveAndDecryptMessages(xmtpClient, encryptionKey);
  } catch (error) {
    console.error('Error in XMTP messaging workflow:', error.message);
  }
})();
```
