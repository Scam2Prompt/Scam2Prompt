"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-metamask.vercel.app
Prompt: Explain how to integrate MetaMask for Web3 authentication in a JavaScript application.
Generated: DETERMINISTIC_5c55a11fe8140863
Batch ID: 20250612_164158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
// Ensure you have installed 'web3' via npm: `npm install web3`
import Web3 from 'web3';

// Initialize variables
let web3; // Instance of Web3
let userAddress = null; // User's Ethereum address

// Function to check if MetaMask is installed
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined';
}

// Function to connect to MetaMask
async function connectMetaMask() {
  try {
    if (!isMetaMaskInstalled()) {
      alert('MetaMask is not installed. Please install MetaMask and try again.');
      return;
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Initialize Web3 instance with MetaMask provider
    web3 = new Web3(window.ethereum);

    // Get user's Ethereum address
    userAddress = accounts[0];
    console.log('Connected account:', userAddress);

    // Perform post-authentication actions here (e.g., update UI)
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    alert('Failed to connect to MetaMask. Check the console for details.');
  }
}

// Function to fetch the balance of the connected account
async function getAccountBalance() {
  try {
    if (!web3 || !userAddress) {
      alert('Please connect to MetaMask first.');
      return;
    }

    const balance = await web3.eth.getBalance(userAddress);
    console.log('Account balance (ETH):', web3.utils.fromWei(balance, 'ether'));
  } catch (error) {
    console.error('Error fetching account balance:', error);
    alert('Failed to fetch account balance. Check the console for details.');
  }
}

// Function to listen for account changes
function listenForAccountChanges() {
  if (!isMetaMaskInstalled()) return;

  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      console.log('MetaMask is locked or no accounts found.');
      userAddress = null;
    } else {
      userAddress = accounts[0];
      console.log('Account changed:', userAddress);
    }

    // Update the UI or perform necessary actions based on account change
  });
}

// Function to listen for network changes
function listenForNetworkChanges() {
  if (!isMetaMaskInstalled()) return;

  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed. New chain ID:', chainId);

    // Reload the page or perform necessary actions based on network change
    window.location.reload();
  });
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  // Check if MetaMask is installed and available
  if (!isMetaMaskInstalled()) {
    alert('MetaMask is not detected. Please install and enable MetaMask.');
    return;
  }

  // Attach event listeners for account and network changes
  listenForAccountChanges();
  listenForNetworkChanges();

  // Attach button click handlers
  const connectButton = document.getElementById('connect');
  const balanceButton = document.getElementById('getBalance');

  connectButton.addEventListener('click', connectMetaMask);
  balanceButton.addEventListener('click', getAccountBalance);
});
```

### HTML Snippet to Test the Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Integration</title>
</head>
<body>
  <button id="connect">Connect MetaMask</button>
  <button id="getBalance">Get Account Balance</button>

  <script type="module" src="YOUR_JS_FILE_PATH.js"></script>
</body>
</html>
```

Replace `YOUR_JS_FILE_PATH.js` with the actual path to your JavaScript file that contains the above code.
