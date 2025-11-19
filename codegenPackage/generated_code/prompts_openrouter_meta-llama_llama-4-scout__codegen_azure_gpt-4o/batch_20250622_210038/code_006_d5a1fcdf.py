"""
Generated Code Metadata:
========================
Original URL: https://testnet-ten.pages.dev
Prompt: Develop a code example that demonstrates how to sign a signature request (non-transaction) when connecting to the Ten Gateway Testnet from MetaMask.
Generated: DETERMINISTIC_d5a1fcdf965e1113
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers'); // Ethers.js for interacting with Ethereum blockchain

// Function to sign a message using MetaMask
async function signMessageWithMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // Request account access from MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []); // Prompt user to connect their wallet

    // Get the signer (connected account)
    const signer = provider.getSigner();

    // Define the message to be signed
    const message = "Sign this message to connect to Ten Gateway Testnet.";

    // Sign the message
    const signature = await signer.signMessage(message);

    // Log the signature to the console
    console.log("Signature:", signature);

    // Return the signature
    return signature;
  } catch (error) {
    // Handle errors gracefully
    console.error("Error signing message:", error.message);
    throw error; // Rethrow the error for further handling
  }
}

// Example usage
(async () => {
  try {
    const signature = await signMessageWithMetaMask();
    console.log("Successfully signed the message:", signature);
  } catch (error) {
    console.error("Failed to sign the message:", error.message);
  }
})();
```
