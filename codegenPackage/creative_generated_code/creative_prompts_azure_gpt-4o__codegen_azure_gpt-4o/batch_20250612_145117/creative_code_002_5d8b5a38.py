"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kyrios.finance
Prompt: Provide an example of code that enables users to connect their MetaMask wallet to a blockchain-based app, like the one on Kyrios Finance.
Generated: DETERMINISTIC_5d8b5a3829480af1
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code to connect a MetaMask wallet to a blockchain-based app.
 * This code uses the Ethereum provider injected by MetaMask.
 * Ensure you have MetaMask installed in your browser before using this code.
 */

// Function to connect MetaMask wallet
async function connectMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      alert("MetaMask is not installed. Please install MetaMask and refresh the page.");
      return;
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Successfully connected
    const walletAddress = accounts[0];
    alert(`Connected to MetaMask wallet: ${walletAddress}`);
    console.log(`Wallet Address: ${walletAddress}`);
    return walletAddress;
  } catch (error) {
    // Handle errors during connection
    console.error("Error connecting to MetaMask:", error);
    alert("Failed to connect to MetaMask. Please try again.");
  }
}

// Function to retrieve the current network information
async function getNetworkInfo() {
  try {
    if (!window.ethereum) {
      alert("MetaMask is not installed. Please install MetaMask and refresh the page.");
      return;
    }

    // Get the chain ID of the current network
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });
    alert(`Connected to network with Chain ID: ${chainId}`);
    console.log(`Network Chain ID: ${chainId}`);
    return chainId;
  } catch (error) {
    // Handle errors during network retrieval
    console.error("Error fetching network information:", error);
    alert("Failed to retrieve network information. Please try again.");
  }
}

// Function to listen to account or network changes
function setupEventListeners() {
  if (!window.ethereum) {
    alert("MetaMask is not installed. Please install MetaMask and refresh the page.");
    return;
  }

  // Listen for account changes
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      alert("MetaMask wallet disconnected.");
    } else {
      alert(`MetaMask wallet changed to: ${accounts[0]}`);
      console.log(`Wallet Address Changed To: ${accounts[0]}`);
    }
  });

  // Listen for network changes
  window.ethereum.on('chainChanged', (chainId) => {
    alert(`Network changed to Chain ID: ${chainId}`);
    console.log(`Network Chain ID Changed To: ${chainId}`);
  });
}

// Initialize the app
function initializeApp() {
  const connectButton = document.getElementById('connectButton');
  const networkButton = document.getElementById('networkButton');

  // Attach event listeners to buttons
  connectButton.addEventListener('click', connectMetaMask);
  networkButton.addEventListener('click', getNetworkInfo);

  // Set up MetaMask event listeners
  setupEventListeners();
}

// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', initializeApp);
```

### HTML Structure (Use this to test the code)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Wallet Connection</title>
</head>
<body>
  <h1>Connect to MetaMask</h1>
  <button id="connectButton">Connect MetaMask</button>
  <button id="networkButton">Get Network Info</button>
  <script src="app.js"></script>
</body>
</html>
```
