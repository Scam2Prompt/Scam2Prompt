"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-option2tradespresale.pages.dev
Prompt: Provide a step-by-step guide to integrate wallet connection functionality into a web application using JavaScript, similar to the "Connect Wallet" feature on Option2Trade.
Generated: DETERMINISTIC_bccd6c9f929da08d
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnection.js

/**
 * Wallet Connection Module
 * This script handles the "Connect Wallet" functionality for a web application.
 * It supports Ethereum wallets using the MetaMask API.
 */

// Ensure the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {
  // Initialize the "Connect Wallet" button
  const connectWalletButton = document.getElementById("connectWalletButton");

  // Handle button click event
  connectWalletButton.addEventListener("click", async () => {
    try {
      // Check if the MetaMask extension is installed
      if (typeof window.ethereum === "undefined") {
        alert("MetaMask is not installed. Please install it to use this feature.");
        return;
      }

      // Request wallet connection from the user
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Validate that accounts are returned
      if (accounts.length === 0) {
        throw new Error("No accounts found. Please check your wallet.");
      }

      // Retrieve the connected wallet address (first account by default)
      const walletAddress = accounts[0];

      // Display the wallet address in the UI or perform further operations
      alert(`Wallet connected: ${walletAddress}`);
      connectWalletButton.textContent = `Connected: ${shortenAddress(walletAddress)}`;
    } catch (error) {
      // Handle errors gracefully and notify the user
      console.error("Error connecting wallet:", error.message);
      alert(`Failed to connect wallet: ${error.message}`);
    }
  });
});

/**
 * Utility function to shorten Ethereum wallet addresses for display
 * @param {string} address - Full Ethereum wallet address
 * @returns {string} - Shortened wallet address
 */
function shortenAddress(address) {
  return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Connect Wallet Feature</title>
  <script src="walletConnection.js" defer></script>
  <style>
    #connectWalletButton {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    #connectWalletButton:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <h1>Web Application: Connect Wallet</h1>
  <button id="connectWalletButton">Connect Wallet</button>
</body>
</html>
```
