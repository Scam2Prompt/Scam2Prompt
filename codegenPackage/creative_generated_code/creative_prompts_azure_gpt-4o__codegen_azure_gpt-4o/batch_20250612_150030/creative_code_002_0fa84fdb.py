"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: How can I enable JavaScript to use Web3Modal for wallet connection in a dApp?
Generated: DETERMINISTIC_0fa84fdb23047368
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
// Ensure you have installed web3modal and ethers using npm or yarn:
// npm install web3modal ethers

import Web3Modal from "web3modal";
import { ethers } from "ethers";

// Initialize Web3Modal instance
const web3Modal = new Web3Modal({
  cacheProvider: true, // Enable caching for user selection
  providerOptions: {}, // Add custom provider options if needed (e.g., WalletConnect)
});

// Function to connect wallet
async function connectWallet() {
  try {
    // Prompt user to connect their wallet
    const provider = await web3Modal.connect();

    // Create a new ethers.js provider instance from the wallet connection
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Get the signer for transaction signing purposes
    const signer = web3Provider.getSigner();

    // Get the connected wallet's address
    const userAddress = await signer.getAddress();

    console.log("Wallet connected:", userAddress);

    // Return useful information
    return {
      provider: web3Provider,
      signer,
      userAddress,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Failed to connect wallet:", error.message);
    throw new Error("Wallet connection failed. Please try again.");
  }
}

// Function to disconnect wallet
function disconnectWallet() {
  try {
    // Clear cached provider information
    web3Modal.clearCachedProvider();

    console.log("Wallet disconnected");
  } catch (error) {
    // Handle errors gracefully
    console.error("Failed to disconnect wallet:", error.message);
  }
}

// Example usage
(async () => {
  try {
    const walletDetails = await connectWallet();
    console.log("Wallet details:", walletDetails);

    // Perform dApp-specific operations here

    // Disconnect wallet when done (optional)
    disconnectWallet();
  } catch (error) {
    console.error("Error occurred:", error.message);
  }
})();
```
