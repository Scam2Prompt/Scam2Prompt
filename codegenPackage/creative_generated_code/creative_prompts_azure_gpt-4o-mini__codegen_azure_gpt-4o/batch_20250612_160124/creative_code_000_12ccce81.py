"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: How can I implement a Web3Modal example in my JavaScript application?
Generated: DETERMINISTIC_12ccce819538d48c
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3Modal from "web3modal"; // Web3Modal for wallet connection
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import { ethers } from "ethers"; // Ethers.js for interacting with Ethereum blockchain

// Configure the Web3Modal instance
async function initWeb3Modal() {
  try {
    // Options for Web3Modal
    const providerOptions = {
      walletconnect: {
        package: WalletConnectProvider, // Use WalletConnect as provider
        options: {
          infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
        },
      },
    };

    // Initialize Web3Modal
    const web3Modal = new Web3Modal({
      cacheProvider: true, // Enable caching of the provider
      providerOptions, // Add provider options
      theme: "dark", // Choose the theme: 'dark', 'light' or 'default'
    });

    return web3Modal;
  } catch (error) {
    console.error("Error initializing Web3Modal:", error);
    throw error;
  }
}

// Function to connect wallet using Web3Modal
async function connectWallet() {
  try {
    const web3Modal = await initWeb3Modal();

    // Prompt user to connect their wallet
    const instance = await web3Modal.connect();

    // Initialize provider using Ethers.js
    const provider = new ethers.providers.Web3Provider(instance);

    // Fetch signer (connected account)
    const signer = provider.getSigner();

    // Get connected account's address
    const address = await signer.getAddress();
    console.log("Connected address:", address);

    // Return provider and signer for further use
    return { provider, signer, address };
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw error;
  }
}

// Function to disconnect wallet
async function disconnectWallet(web3Modal) {
  try {
    if (web3Modal && web3Modal.clearCachedProvider) {
      // Clear cached provider
      web3Modal.clearCachedProvider();
      console.log("Wallet disconnected.");
    }
  } catch (error) {
    console.error("Error disconnecting wallet:", error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const { provider, signer, address } = await connectWallet();

    // Perform additional operations (e.g., smart contract interaction)
    console.log("Signer object:", signer);

    // Disconnect wallet
    const web3Modal = await initWeb3Modal();
    await disconnectWallet(web3Modal);
  } catch (error) {
    console.error("An error occurred:", error);
  }
})();
```

Note:
1. Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
2. Ensure you install required dependencies: `npm install web3modal @walletconnect/web3-provider ethers`.
