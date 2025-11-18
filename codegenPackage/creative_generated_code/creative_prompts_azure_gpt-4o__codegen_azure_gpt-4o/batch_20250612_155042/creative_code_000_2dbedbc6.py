"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ribbons.bond
Prompt: Write JavaScript code to integrate MetaMask functionality for connecting a user's wallet on a webpage, referencing the requirements for JavaScript-enabled environments.
Generated: DETERMINISTIC_2dbedbc6407c3ead
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Integration Script
// This script enables connecting a user's MetaMask wallet on a webpage.

// Check if MetaMask is installed and available
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Connect MetaMask wallet
async function connectWallet() {
  try {
    // Request the user's wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (accounts.length > 0) {
      // Successfully connected
      const userWalletAddress = accounts[0];
      console.log('Wallet connected:', userWalletAddress);
      document.getElementById('walletAddress').textContent = `Connected Wallet Address: ${userWalletAddress}`;
    } else {
      console.error('No accounts found.');
      alert('No accounts found. Please ensure MetaMask is configured properly.');
    }
  } catch (error) {
    // Handle errors
    console.error('Error connecting wallet:', error.message || error);
    alert('Failed to connect wallet. Please check MetaMask and try again.');
  }
}

// Detect account changes (e.g., user switches accounts in MetaMask)
function detectAccountChange() {
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length > 0) {
      console.log('Account changed. New account:', accounts[0]);
      document.getElementById('walletAddress').textContent = `Connected Wallet Address: ${accounts[0]}`;
    } else {
      console.log('All accounts disconnected.');
      document.getElementById('walletAddress').textContent = 'No wallet connected.';
    }
  });
}

// Detect network changes (e.g., user switches networks in MetaMask)
function detectNetworkChange() {
  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed. New chain ID:', chainId);
    alert(`Network changed. New chain ID: ${chainId}`);
    // Reload the page to ensure proper network configuration
    window.location.reload();
  });
}

// Initialize MetaMask functionality
function initializeMetaMask() {
  if (isMetaMaskInstalled()) {
    console.log('MetaMask is installed.');
    document.getElementById('status').textContent = 'MetaMask is installed.';
    detectAccountChange();
    detectNetworkChange();
  } else {
    console.error('MetaMask is not installed.');
    document.getElementById('status').textContent = 'MetaMask is not installed. Please install MetaMask to proceed.';
    alert('MetaMask is not installed. Please install it to use this functionality.');
  }
}

// Attach event listeners to buttons
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);

// Initialize on page load
window.addEventListener('DOMContentLoaded', initializeMetaMask);
```

```html
<!-- Sample HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Integration</title>
</head>
<body>
  <h1>MetaMask Wallet Integration</h1>
  <p id="status">Checking MetaMask status...</p>
  <button id="connectWalletButton">Connect Wallet</button>
  <p id="walletAddress">No wallet connected.</p>

  <script src="metamask.js"></script> <!-- Link to the above script -->
</body>
</html>
```
