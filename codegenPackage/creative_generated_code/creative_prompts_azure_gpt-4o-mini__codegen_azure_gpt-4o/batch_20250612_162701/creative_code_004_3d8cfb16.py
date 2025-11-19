"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://home-io-metamask-cdn.bravesites.com
Prompt: Explain how to enhance security when using MetaMask for logging into blockchain games and NFT marketplaces.
Generated: DETERMINISTIC_3d8cfb16ff59d7f6
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Enhance security when using MetaMask for logging into blockchain games and NFT marketplaces.
 *
 * This script provides functions to securely interact with MetaMask, including:
 * - Checking if MetaMask is installed.
 * - Connecting to MetaMask securely.
 * - Signing a message for authentication.
 * - Verifying the signed message.
 */

// Import ethers.js for handling Ethereum-related operations
const ethers = require('ethers');

/**
 * Check if MetaMask is installed in the browser.
 * @returns {boolean} True if MetaMask is installed, false otherwise.
 */
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

/**
 * Connect to MetaMask securely.
 * Requests account access and returns the connected account address.
 * @returns {Promise<string>} The user's Ethereum account address.
 */
async function connectToMetaMask() {
  try {
    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    // Return the first account (primary account assumed)
    return accounts[0];
  } catch (error) {
    // Handle connection errors gracefully
    console.error('Error connecting to MetaMask:', error.message);
    throw new Error('Failed to connect to MetaMask.');
  }
}

/**
 * Sign a message securely using MetaMask.
 * The signed message can be used for authentication or authorization purposes.
 * @param {string} message - The message to be signed.
 * @returns {Promise<string>} The signed message.
 */
async function signMessage(message) {
  try {
    const account = await connectToMetaMask(); // Ensure MetaMask is connected
    const provider = new ethers.providers.Web3Provider(window.ethereum); // Initialize ethers.js provider
    const signer = provider.getSigner(account); // Get the signer object for the connected account

    // Sign the provided message
    const signature = await signer.signMessage(message);
    return signature;
  } catch (error) {
    // Handle signing errors gracefully
    console.error('Error signing the message:', error.message);
    throw new Error('Failed to sign the message.');
  }
}

/**
 * Verify a signed message.
 * Compares the message and signature to ensure it was signed by the expected account.
 * @param {string} message - The original message that was signed.
 * @param {string} signature - The signed message signature.
 * @returns {string} The recovered Ethereum address that signed the message.
 */
function verifyMessage(message, signature) {
  try {
    // Recover the address from the signed message and signature
    const recoveredAddress = ethers.utils.verifyMessage(message, signature);
    return recoveredAddress;
  } catch (error) {
    // Handle verification errors gracefully
    console.error('Error verifying the message:', error.message);
    throw new Error('Failed to verify the message.');
  }
}

/**
 * Example workflow: Authenticate user using MetaMask.
 */
async function authenticateUser() {
  try {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
      console.log('MetaMask is not installed. Please install MetaMask and try again.');
      return;
    }

    // Define a secure, unique message for authentication
    const authMessage = 'Please sign this message to authenticate yourself. [Timestamp: ' + Date.now() + ']';

    // Sign the authentication message
    const signature = await signMessage(authMessage);

    // Verify the signed message
    const recoveredAddress = verifyMessage(authMessage, signature);

    console.log('Authentication successful!');
    console.log('Signed by Ethereum address:', recoveredAddress);
  } catch (error) {
    console.error('Authentication failed:', error.message);
  }
}

// Run the example workflow
authenticateUser();
```

Note: Ensure you have `ethers.js` installed via `npm install ethers` before running the script.
