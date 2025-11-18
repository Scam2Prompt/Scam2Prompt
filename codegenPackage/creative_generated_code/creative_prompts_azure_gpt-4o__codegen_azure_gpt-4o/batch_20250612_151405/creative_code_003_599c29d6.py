"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp.busta.gg
Prompt: Provide an example of JavaScript code to enable wallet connection (e.g., MetaMask) for a dApp like the one on Busta.gg.
Generated: DETERMINISTIC_599c29d6b0455665
Batch ID: 20250612_151405
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
 * Enable wallet connection for a dApp (e.g., MetaMask).
 * This script handles connecting to MetaMask, retrieving accounts,
 * and basic error handling.
 */

// Check if the browser has MetaMask installed
async function connectWallet() {
  try {
    // Ensure the window.ethereum object is available (MetaMask installed)
    if (typeof window.ethereum !== 'undefined') {
      console.log("MetaMask detected!");

      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // If successful, display the connected account
      console.log("Connected account:", accounts[0]);

      // Return the connected account for further use
      return accounts[0];
    } else {
      // MetaMask is not installed
      console.error("MetaMask is not installed. Please install MetaMask and try again.");
      alert("MetaMask is not installed. Please install MetaMask and try again.");
      return null;
    }
  } catch (error) {
    // Handle errors during the request process
    console.error("An error occurred during wallet connection:", error);

    // Provide feedback to the user
    alert("An error occurred during wallet connection. Please try again.");

    // Return null to indicate failure
    return null;
  }
}

// Listen for account changes (e.g., user switches wallet accounts)
function listenForAccountChanges() {
  if (typeof window.ethereum !== 'undefined') {
    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length > 0) {
        console.log("Account changed:", accounts[0]);
        alert(`Account changed: ${accounts[0]}`);
      } else {
        console.log("No accounts are connected.");
        alert("No accounts are connected. Please reconnect your wallet.");
      }
    });
  }
}

// Example usage of the connectWallet function
document.getElementById("connectWalletButton").addEventListener("click", async () => {
  const connectedAccount = await connectWallet();
  if (connectedAccount) {
    // Update UI or perform actions with the connected account
    console.log("Wallet connected successfully:", connectedAccount);
  }
});

// Initialize account change listener when the page loads
listenForAccountChanges();
```

**HTML Example:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wallet Connection Example</title>
</head>
<body>
  <h1>Connect to MetaMask</h1>
  <button id="connectWalletButton">Connect Wallet</button>
  <script src="walletConnection.js"></script>
</body>
</html>
```
