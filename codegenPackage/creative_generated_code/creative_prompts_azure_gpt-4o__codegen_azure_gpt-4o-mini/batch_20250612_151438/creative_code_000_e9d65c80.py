"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapptoolkit.com
Prompt: Write code using the Web3Modal SDK to connect a user's wallet to a decentralized application, ensuring compatibility with multiple chains like Ethereum, Binance, and Polygon.
Generated: DETERMINISTIC_e9d65c80777e9437
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3Modal from "web3modal";
import { ethers } from "ethers";

// Define supported chains
const supportedChains = [
  {
    chainId: '0x1', // Ethereum Mainnet
    name: 'Ethereum'
  },
  {
    chainId: '0x38', // Binance Smart Chain
    name: 'Binance Smart Chain'
  },
  {
    chainId: '0x89', // Polygon Mainnet
    name: 'Polygon'
  }
];

// Initialize Web3Modal instance
const web3Modal = new Web3Modal({
  cacheProvider: true, // Set to true to cache provider connection
  providerOptions: {} // Add wallet provider options if needed
});

/**
 * Connect to the user's wallet
 * @returns {Promise<void>}
 */
async function connectWallet() {
  try {
    // Open the modal to connect to the wallet
    const provider = await web3Modal.connect();

    // Create an ethers provider from the connected wallet
    const ethersProvider = new ethers.providers.Web3Provider(provider);

    // Get the signer for the connected wallet
    const signer = ethersProvider.getSigner();

    // Fetch and log the user's address
    const userAddress = await signer.getAddress();
    console.log(`Connected wallet address: ${userAddress}`);

    // Optionally, you can set the network or handle chain switching here
    // const network = await ethersProvider.getNetwork();
    // console.log(`Connected to network: ${network.name}`);

    // Handle additional logic such as fetching balances, etc.
  } catch (error) {
    // Handle any errors that occurred during connection
    console.error("Failed to connect wallet:", error);
  }
}

// Example usage: calling connectWallet when the user clicks a button
document.getElementById("connectButton").addEventListener("click", connectWallet);

// Ensure proper cleanup on disconnect if needed
window.addEventListener("beforeunload", () => {
  // Clear the cached provider to ensure fresh connection on reload
  web3Modal.clearCachedProvider();
});
```
