"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io.merge.marabuspa.com
Prompt: Explain how to handle user authentication with MetaMask in a blockchain project.
Generated: DETERMINISTIC_4c201c4967f484ca
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies:
// Install ethers.js: `npm install ethers`
// Ensure you have MetaMask installed in your browser

// Import ethers.js library
const { ethers } = require('ethers');

// Function to handle user authentication with MetaMask
async function authenticateWithMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // Request user's Ethereum account (will prompt MetaMask popup)
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    // Validate if an account is returned
    if (!accounts || accounts.length === 0) {
      throw new Error("No account was returned by MetaMask.");
    }

    // Retrieve the first account (default account)
    const userAddress = accounts[0];
    console.log("User Address:", userAddress);

    // Create a signer using ethers.js
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Generate a message for the user to sign (could be a nonce or unique string)
    const message = "Authenticate with the application"; // Replace with your own message or nonce

    // User signs the message using their private key
    const signature = await signer.signMessage(message);
    console.log("Signature:", signature);

    // At this point:
    // - `userAddress` contains the Ethereum address of the user
    // - `signature` contains the signed message
    // You can send these to your backend for verification

    // Return the user's address and signature
    return {
      userAddress,
      signature,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Error during authentication:", error.message);
    throw error; // Rethrow the error for caller to handle
  }
}

// Example usage of the `authenticateWithMetaMask` function
authenticateWithMetaMask()
  .then((authData) => {
    console.log("Authentication successful:", authData);
  })
  .catch((err) => {
    console.error("Authentication failed:", err.message);
  });
```
