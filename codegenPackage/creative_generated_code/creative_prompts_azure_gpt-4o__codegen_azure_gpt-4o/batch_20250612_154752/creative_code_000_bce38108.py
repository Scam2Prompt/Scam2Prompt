"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao1.pro
Prompt: Write code to integrate a MetaMask wallet connection for a dApp, referencing the wallet connection process described on the DAO1 platform.
Generated: DETERMINISTIC_bce3810874484117
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Wallet Connection for a dApp
 * This script provides functionality to connect a MetaMask wallet to a decentralized application (dApp).
 * It includes error handling, user notifications, and follows best practices.
 */

// Ensure the script is executed after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Element references
  const connectButton = document.getElementById('connectWalletButton');
  const walletAddressDisplay = document.getElementById('walletAddress');

  // Add event listener to the connect button
  connectButton.addEventListener('click', connectToMetaMask);
});

/**
 * Connect to MetaMask wallet
 * This function triggers the MetaMask wallet connection flow and updates the UI with the connected wallet address.
 */
async function connectToMetaMask() {
  try {
    // Check if the MetaMask extension is installed
    if (!window.ethereum) {
      alert('MetaMask is not installed. Please install it to use this dApp.');
      return;
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Update the UI with the connected wallet address
    const walletAddress = accounts[0];
    displayWalletAddress(walletAddress);

    console.log('Connected wallet address:', walletAddress);
  } catch (error) {
    // Handle errors during the connection process
    console.error('Error connecting to MetaMask:', error);
    alert(`Failed to connect to MetaMask: ${error.message}`);
  }
}

/**
 * Display wallet address in the UI
 * @param {string} walletAddress - The connected wallet address
 */
function displayWalletAddress(walletAddress) {
  const walletAddressDisplay = document.getElementById('walletAddress');
  walletAddressDisplay.textContent = `Connected Wallet: ${walletAddress}`;
}

/**
 * Listen for account changes (e.g., when the user switches accounts in MetaMask)
 */
if (window.ethereum) {
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length > 0) {
      // Update the UI with the newly connected wallet address
      displayWalletAddress(accounts[0]);
      console.log('Wallet address updated:', accounts[0]);
    } else {
      // Handle case where MetaMask account is disconnected
      const walletAddressDisplay = document.getElementById('walletAddress');
      walletAddressDisplay.textContent = 'Wallet disconnected';
      console.log('MetaMask wallet disconnected.');
    }
  });
}
```

### HTML Example for Integration:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Wallet Connection</title>
</head>
<body>
  <button id="connectWalletButton">Connect MetaMask Wallet</button>
  <p id="walletAddress">Wallet not connected</p>

  <!-- Include the JavaScript file -->
  <script src="walletConnection.js"></script>
</body>
</html>
```
