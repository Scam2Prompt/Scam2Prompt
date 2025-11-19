"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Write a code snippet that demonstrates how to implement MetaMask's wallet connection in a web3 application.
Generated: DETERMINISTIC_4de8744e26012871
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
import { ethers } from "ethers";

// Function to connect to MetaMask wallet
async function connectToMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask to continue.");
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    // Ensure accounts are returned
    if (accounts.length === 0) {
      throw new Error("No accounts found. Please ensure your wallet is unlocked and has accounts.");
    }

    // Use ethers.js to create a provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (account holder) from the provider
    const signer = provider.getSigner();

    // Retrieve the selected account address and display it in the console
    const accountAddress = await signer.getAddress();
    console.log("Connected account:", accountAddress);

    // Return the provider, signer, and connected account address for further use
    return { provider, signer, accountAddress };
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while connecting to MetaMask:", error.message);
    return null;
  }
}

// Example usage of connectToMetaMask function
(async () => {
  const walletDetails = await connectToMetaMask();
  if (walletDetails) {
    console.log("MetaMask wallet connected successfully:", walletDetails);
  } else {
    console.log("Failed to connect to MetaMask wallet.");
  }
})();
```

This code snippet is ready for production use, fully documented, and implements robust error handling to ensure clean integration with MetaMask.
