"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-faq.io
Prompt: Develop a sample code that connects a Web3 application to Rabby Wallet, emphasizing its non-custodial nature and user-friendly interface.
Generated: DETERMINISTIC_817779622f575554
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Rabby Wallet Integration Example for a Web3 Application
 * This script demonstrates how to connect a Web3 application to Rabby Wallet.
 * Rabby Wallet is a non-custodial wallet with a user-friendly interface.
 */

// Import required packages
import Web3 from 'web3';

// Entry point for connecting Rabby Wallet
async function connectRabbyWallet() {
  try {
    // Check if Rabby Wallet is available in the browser
    if (window.ethereum && window.ethereum.isRabby) {
      console.log("Rabby Wallet detected!");

      // Initialize Web3 instance using Rabby Wallet's provider
      const web3 = new Web3(window.ethereum);

      // Request wallet connection from the user
      const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts',
      });

      // Check if accounts are returned
      if (accounts.length === 0) {
        throw new Error("No accounts returned. Please unlock Rabby Wallet.");
      }

      console.log("Connected account:", accounts[0]);

      // Fetch the connected network ID
      const networkId = await web3.eth.net.getId();
      console.log("Connected network ID:", networkId);

      // Display a confirmation message
      console.log("Successfully connected to Rabby Wallet!");
      
      // Return the Web3 instance and connected account for further use
      return { web3, account: accounts[0], networkId };
    } else {
      throw new Error("Rabby Wallet not detected. Please install Rabby Wallet.");
    }
  } catch (error) {
    // Handle connection errors
    console.error("Error connecting to Rabby Wallet:", error.message);
    alert(`Failed to connect to Rabby Wallet: ${error.message}`);
  }
}

// Example usage
(async () => {
  const result = await connectRabbyWallet();

  if (result) {
    console.log("Web3 instance:", result.web3);
    console.log("Connected account:", result.account);
    console.log("Network ID:", result.networkId);
  }
})();

/*
 * Notes:
 * 1. Ensure Rabby Wallet is installed in the browser before using this script.
 * 2. This script assumes a modern browser that provides the `window.ethereum` object.
 * 3. Follow additional security best practices in production environments.
 */
```
