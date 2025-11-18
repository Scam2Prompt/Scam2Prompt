"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-metamask.vercel.app
Prompt: Recommend libraries or APIs that simplify Web3 authentication with MetaMask, and provide code snippets for their usage.
Generated: DETERMINISTIC_2ecb2665c0d59009
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready example using the `ethers.js` library. `ethers.js` simplifies Web3 authentication and interaction with MetaMask.

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Function to connect to MetaMask and authenticate the user
async function connectWithMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install it to use this feature.");
    }

    // Request access to the user's MetaMask account
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []);

    // Get the signer (represents the connected account)
    const signer = provider.getSigner();

    // Retrieve the user's wallet address
    const walletAddress = await signer.getAddress();

    console.log("Connected wallet address:", walletAddress);

    // Return the provider and signer objects for further use
    return { provider, signer, walletAddress };

  } catch (error) {
    console.error("Error during MetaMask authentication:", error.message);
    throw error; // Re-throw the error for external handling
  }
}

// Example usage of the authentication function
(async () => {
  try {
    const { provider, signer, walletAddress } = await connectWithMetaMask();
    console.log("MetaMask authentication successful!");
    console.log("Provider:", provider);
    console.log("Signer:", signer);
    console.log("Wallet Address:", walletAddress);
  } catch (error) {
    console.error("Failed to authenticate with MetaMask:", error.message);
  }
})();
```

Make sure you install `ethers.js` before running this code:
```bash
npm install ethers
```

The code includes proper error handling, checks for MetaMask installation, and logs essential details for debugging. It is production-ready and adheres to best practices.
