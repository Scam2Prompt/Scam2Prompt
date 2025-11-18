"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-chrome.github.io
Prompt: Provide a code example for integrating the MetaMask Chrome Extension into a dApp to request wallet permissions.
Generated: DETERMINISTIC_645e8c0213d57c64
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code for integrating the MetaMask Chrome Extension into a dApp 
 * to request wallet permissions.
 * 
 * This code is production-ready, well-documented, and follows best practices.
 */

// Ensure the code is executed after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', async () => {
  // Check if MetaMask is installed
  if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install MetaMask to use this dApp.');
    alert('MetaMask is not installed. Please install MetaMask to continue.');
    return;
  }

  // DOM elements for interaction
  const connectButton = document.getElementById('connectWalletButton');
  const walletAddressDisplay = document.getElementById('walletAddress');

  /**
   * Function to request wallet permissions (connect to MetaMask).
   */
  async function connectWallet() {
    try {
      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Display the connected wallet address
      const walletAddress = accounts[0]; // Take the first account
      walletAddressDisplay.textContent = `Connected Wallet Address: ${walletAddress}`;
      console.log(`Wallet connected: ${walletAddress}`);
    } catch (error) {
      // Handle errors appropriately
      console.error('Error connecting to MetaMask:', error);
      alert(`Failed to connect to MetaMask: ${error.message}`);
    }
  }

  // Attach event listener to the "Connect Wallet" button
  connectButton.addEventListener('click', connectWallet);

  /**
   * Optional: Detect account changes via MetaMask and update the UI accordingly.
   * MetaMask triggers this event when the user switches accounts or disconnects.
   */
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      // User has disconnected their wallet
      walletAddressDisplay.textContent = 'No wallet connected';
      alert('Wallet disconnected.');
    } else {
      // Update to the new wallet address
      const walletAddress = accounts[0];
      walletAddressDisplay.textContent = `Connected Wallet Address: ${walletAddress}`;
      console.log(`Wallet changed: ${walletAddress}`);
    }
  });

  /**
   * Optional: Detect network changes via MetaMask and log them.
   * MetaMask triggers this event when the user changes the blockchain network.
   */
  window.ethereum.on('chainChanged', (chainId) => {
    console.log(`Network changed to chain ID: ${chainId}`);
    alert(`Network changed to chain ID: ${chainId}`);
    // Reload the page to ensure the dApp interacts with the correct network
    window.location.reload();
  });
});
```

```html
<!-- Example HTML to use with the JavaScript code -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Integration Example</title>
</head>
<body>
  <h1>MetaMask Integration Example</h1>
  <button id="connectWalletButton">Connect Wallet</button>
  <p id="walletAddress">No wallet connected</p>
  <script src="app.js"></script>
</body>
</html>
```
