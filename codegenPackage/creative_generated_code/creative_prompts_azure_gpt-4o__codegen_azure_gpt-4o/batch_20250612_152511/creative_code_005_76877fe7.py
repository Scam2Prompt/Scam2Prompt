"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ten-testnet.pages.dev
Prompt: Suggest tools or APIs that can replicate the "three-click setup" for encrypted communication between MetaMask and a blockchain network, as seen on the Ten Gateway Testnet site.
Generated: DETERMINISTIC_76877fe7caa61e73
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a JavaScript code snippet using the Web3.js library to replicate the "three-click setup" for encrypted communication between MetaMask and a blockchain network:

```javascript
// Import required dependencies
const Web3 = require('web3');

// Function to initialize connection to blockchain via MetaMask
async function setupEncryptedCommunication() {
  try {
    // Check if MetaMask is available in the user's browser
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
    }

    // Request user to connect MetaMask to the application
    console.log('Requesting MetaMask connection...');
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Instantiate Web3 with MetaMask's provider
    const web3 = new Web3(window.ethereum);

    // Retrieve the user's connected account
    const accounts = await web3.eth.getAccounts();
    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. Please ensure MetaMask is connected to an account.');
    }

    const userAccount = accounts[0];
    console.log('Connected account:', userAccount);

    // Example: Fetch the chain ID to confirm network connection
    const chainId = await web3.eth.getChainId();
    console.log('Connected to chain ID:', chainId);

    // Encrypt a message for demonstration purposes
    const message = 'Hello, blockchain world!';
    console.log('Original message:', message);

    // Encrypt the message using MetaMask's eth_getEncryptionPublicKey (EIP-1024)
    const encryptionPublicKey = await window.ethereum.request({
      method: 'eth_getEncryptionPublicKey',
      params: [userAccount],
    });

    const encryptedMessage = await encryptMessage(message, encryptionPublicKey);
    console.log('Encrypted message:', encryptedMessage);

    // Decrypt the message for verification
    const decryptedMessage = await decryptMessage(encryptedMessage, userAccount);
    console.log('Decrypted message:', decryptedMessage);

    console.log('Encrypted communication setup successfully!');
  } catch (error) {
    console.error('Error during encrypted communication setup:', error.message);
  }
}

// Helper function to encrypt a message
async function encryptMessage(message, publicKey) {
  try {
    const encryptedMessage = await window.ethereum.request({
      method: 'eth_encrypt',
      params: [message, publicKey],
    });
    return encryptedMessage;
  } catch (error) {
    throw new Error('Failed to encrypt the message: ' + error.message);
  }
}

// Helper function to decrypt a message
async function decryptMessage(encryptedMessage, userAccount) {
  try {
    const decryptedMessage = await window.ethereum.request({
      method: 'eth_decrypt',
      params: [encryptedMessage, userAccount],
    });
    return decryptedMessage;
  } catch (error) {
    throw new Error('Failed to decrypt the message: ' + error.message);
  }
}

// Execute the setup function
setupEncryptedCommunication();
```

### Notes:
- Ensure MetaMask is installed in the browser for this code to work.
- The code uses experimental APIs like `eth_getEncryptionPublicKey`, `eth_encrypt`, and `eth_decrypt`. Make sure your blockchain or MetaMask version supports EIP-1024 (encryption/decryption APIs).
- Install Web3.js via npm: `npm install web3`.
