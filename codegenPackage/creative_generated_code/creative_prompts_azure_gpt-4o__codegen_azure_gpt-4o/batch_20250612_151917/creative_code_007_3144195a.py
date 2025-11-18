"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaixkogin.gitbook.io
Prompt: What are the best practices for securing Metamask login as outlined in the GitBook documentation on Metamask Login?
Generated: DETERMINISTIC_3144195a6bbecdfc
Batch ID: 20250612_151917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation of secure MetaMask login, adhering to best practices commonly outlined in documentation and GitBook resources:

```javascript
// Secure MetaMask Login Implementation

// Import ethers.js to interact with Ethereum wallets and blockchain
const { ethers } = require("ethers");

/**
 * Initialize MetaMask-based login process.
 */
async function secureMetaMaskLogin() {
  try {
    // 1. Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // 2. Request account access from the user
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const userAddress = accounts[0]; // Retrieve the first account (default behavior)
    console.log("User Address:", userAddress);

    // 3. Generate a nonce for authentication
    const nonce = generateNonce(); // Generate a cryptographically secure random nonce
    console.log("Generated Nonce:", nonce);

    // 4. Prompt the user to sign the nonce
    const signedMessage = await signMessage(nonce, userAddress);
    console.log("Signed Message:", signedMessage);

    // 5. Verify the signed message on the server (mock server-side call here)
    const isAuthenticated = await verifySignatureOnServer(userAddress, nonce, signedMessage);
    if (isAuthenticated) {
      console.log("Login successful! User authenticated.");
    } else {
      console.error("Authentication failed. Invalid signature.");
    }
  } catch (error) {
    console.error("An error occurred during login:", error.message);
  }
}

/**
 * Generate a cryptographically secure random nonce.
 * @returns {string} A randomly generated nonce
 */
function generateNonce() {
  return ethers.utils.hexlify(ethers.utils.randomBytes(16)); // Generate a random 16-byte nonce
}

/**
 * Prompt the user to sign a message using their MetaMask account.
 * @param {string} message - The message/nonce to be signed
 * @param {string} userAddress - The user's Ethereum address
 * @returns {Promise<string>} The signed message
 */
async function signMessage(message, userAddress) {
  try {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner(userAddress);
    return await signer.signMessage(message);
  } catch (error) {
    throw new Error("Failed to sign message: " + error.message);
  }
}

/**
 * Simulate server-side signature verification.
 * This would typically involve proper backend logic to ensure security.
 * @param {string} userAddress - The user's Ethereum address
 * @param {string} nonce - The nonce sent to the user
 * @param {string} signedMessage - The signed message from the user
 * @returns {Promise<boolean>} Whether the signature is valid
 */
async function verifySignatureOnServer(userAddress, nonce, signedMessage) {
  try {
    // Recover the address from the signed message and nonce
    const recoveredAddress = ethers.utils.verifyMessage(nonce, signedMessage);
    console.log("Recovered Address:", recoveredAddress);

    // Compare the recovered address with the user's address
    return recoveredAddress.toLowerCase() === userAddress.toLowerCase();
  } catch (error) {
    console.error("Failed to verify signature on server:", error.message);
    return false;
  }
}

// Trigger the MetaMask login process
secureMetaMaskLogin();
```

### Key Features of Code:
- **MetaMask Installation Check**: Ensures the user has MetaMask installed before proceeding.
- **Nonce Generation**: Creates a cryptographically secure nonce for authentication.
- **Message Signing**: Uses the MetaMask user's private key to sign the nonce.
- **Signature Verification**: Verifies the signed message against the user's public key (Ethereum address).
- **Error Handling**: Implements robust error handling for all steps in the authentication process.

### Notes:
- Replace the `verifySignatureOnServer` function with a secure backend implementation for production systems.
- Always use HTTPS and secure channels for communication between the frontend and backend.
