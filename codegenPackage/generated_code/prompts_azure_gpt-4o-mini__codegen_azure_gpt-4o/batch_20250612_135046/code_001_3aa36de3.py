"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.com
Prompt: Write a code snippet that demonstrates how to implement WalletKit features for enhancing wallet user experience in a web3 application.
Generated: DETERMINISTIC_3aa36de39cf4b6a1
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3Modal from "web3modal";

// Initialize Web3Modal for wallet connection
const initializeWalletConnection = async () => {
  try {
    // Configure Web3Modal with WalletConnect provider
    const providerOptions = {
      walletconnect: {
        package: WalletConnectProvider, // Required
        options: {
          infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
        },
      },
    };

    const web3Modal = new Web3Modal({
      cacheProvider: true, // Enable caching for faster reconnections
      providerOptions, // Pass provider options
    });

    // Open Web3Modal to connect wallet
    const provider = await web3Modal.connect();

    // Create an ethers.js instance with the connected provider
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Get the connected wallet's signer
    const signer = web3Provider.getSigner();

    // Retrieve wallet address
    const walletAddress = await signer.getAddress();
    console.log("Connected Wallet Address:", walletAddress);

    // Example: Fetch wallet balance
    const balance = await web3Provider.getBalance(walletAddress);
    console.log("Wallet Balance:", ethers.utils.formatEther(balance));

    // Return wallet details
    return {
      provider: web3Provider,
      signer,
      walletAddress,
      balance: ethers.utils.formatEther(balance),
    };
  } catch (error) {
    console.error("Error connecting wallet:", error.message);
    throw new Error("Failed to connect wallet. Please try again.");
  }
};

// Example usage of the wallet connection function
(async () => {
  try {
    const walletDetails = await initializeWalletConnection();
    console.log("Wallet connected successfully:", walletDetails);
  } catch (error) {
    console.error("Wallet connection failed:", error.message);
  }
})();
```
