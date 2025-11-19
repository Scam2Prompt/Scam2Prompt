"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-metis.net
Prompt: Write a tutorial on how to set up security alerts and wallet guard in a MetaMask integration.
Generated: DETERMINISTIC_2118f1f8838c186a
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Integration: Setting up Security Alerts and Wallet Guard
 * This script demonstrates how to integrate MetaMask with security alerts and wallet guard functionality.
 */

// Import necessary libraries
import { ethers } from 'ethers';

/**
 * Initialize MetaMask provider
 */
async function initializeMetaMask() {
  if (typeof window.ethereum === 'undefined') {
    throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
  }

  const provider = new ethers.providers.Web3Provider(window.ethereum);

  // Request user to connect MetaMask
  try {
    const accounts = await provider.send("eth_requestAccounts", []);
    console.log("Connected account:", accounts[0]);
    return { provider, accounts };
  } catch (error) {
    console.error("Error connecting MetaMask:", error.message);
    throw error;
  }
}

/**
 * Set up security alerts for user transactions
 * @param {ethers.providers.Web3Provider} provider - Initialized MetaMask provider
 */
function setupSecurityAlerts(provider) {
  provider.on("accountsChanged", (accounts) => {
    if (accounts.length === 0) {
      alert("MetaMask is disconnected. Please reconnect.");
    } else {
      console.log("Accounts changed:", accounts);
    }
  });

  provider.on("chainChanged", (chainId) => {
    console.log("Chain changed:", chainId);
    alert(`You are now connected to chain ID: ${chainId}`);
  });

  provider.on("disconnect", (error) => {
    console.error("MetaMask disconnected:", error);
    alert("MetaMask has been disconnected.");
  });
}

/**
 * Wallet Guard: Ensure the user wallet is compatible and secure
 * @param {string} walletAddress - The user's wallet address
 */
async function walletGuard(walletAddress) {
  try {
    // Basic validation of wallet address format
    if (!ethers.utils.isAddress(walletAddress)) {
      throw new Error("Invalid wallet address format.");
    }

    console.log("Wallet address validated:", walletAddress);

    // Example check: Ensure the wallet is on the correct chain (assuming chain ID 1 for Ethereum mainnet)
    const chainId = await window.ethereum.request({ method: "eth_chainId" });
    if (parseInt(chainId, 16) !== 1) {
      throw new Error("Wallet is connected to an unsupported chain. Please switch to Ethereum mainnet.");
    }

    console.log("Wallet guard checks passed successfully.");
  } catch (error) {
    console.error("Wallet guard error:", error.message);
    alert("Wallet guard failed: " + error.message);
    throw error;
  }
}

/**
 * Main function: Integrate MetaMask with security alerts and wallet guard
 */
async function main() {
  try {
    const { provider, accounts } = await initializeMetaMask();

    // Set up security alerts
    setupSecurityAlerts(provider);

    // Perform wallet guard checks
    await walletGuard(accounts[0]);

    alert("MetaMask integration with security alerts and wallet guard is successfully set up!");
  } catch (error) {
    console.error("Error in MetaMask integration:", error.message);
    alert("Failed to set up MetaMask integration: " + error.message);
  }
}

// Execute the main function
main();
```
