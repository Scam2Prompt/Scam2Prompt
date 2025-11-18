"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Create a script that automates signing a signature request on the Ten Testnet using MetaMask.
Generated: DETERMINISTIC_0e284dfb56ac2e24
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Script to automate signing a signature request on the Ten Testnet using MetaMask

// Import ethers.js for interacting with Ethereum blockchain
const { ethers } = require("ethers");

// Function to automate signing a signature request
async function signWithMetaMask(requestData) {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask and retry.");
    }

    // Create a provider for connecting to MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Request account access from MetaMask
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Get the signer (MetaMask account to sign with)
    const signer = provider.getSigner();

    // Display the user's address for confirmation
    const address = await signer.getAddress();
    console.log(`Connected MetaMask address: ${address}`);

    // Prepare the data to sign (e.g., a message or transaction)
    const messageToSign = requestData;
    console.log(`Message to sign: ${messageToSign}`);

    // Sign the message using MetaMask
    const signature = await signer.signMessage(messageToSign);
    console.log(`Signature: ${signature}`);

    // Return the signature
    return signature;
  } catch (error) {
    // Log and rethrow errors for debugging
    console.error("Error during signing:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Replace this message with the actual data you want to sign
    const requestMessage = "Sign this request to interact with the Ten Testnet.";

    // Call the signWithMetaMask function and sign the request
    const result = await signWithMetaMask(requestMessage);

    console.log("Signed request successfully:", result);
  } catch (error) {
    // Handle errors gracefully in production
    console.error("Failed to sign request:", error.message);
  }
})();
```

**Note**: Ensure `ethers.js` is installed using `npm install ethers`, and this script is executed in an environment where MetaMask is available and configured to interact with the Ten Testnet.
