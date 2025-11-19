"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: How can I integrate the MetaMask SDK into my dapp for enhanced Web3 functionality?
Generated: DETERMINISTIC_66616ca7a74819ec
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is clean, production-ready JavaScript code to integrate MetaMask SDK into a dApp. The code uses MetaMask's `window.ethereum` provider and adheres to industry best practices.

```javascript
// Import MetaMask SDK (optional for modular functionality)
import { MetaMaskSDK } from '@metamask/sdk';

// Function to check if MetaMask is installed
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Initialize MetaMask SDK (optional step)
const options = {
  preferProvider: 'injected', // Prefer the browser's injected provider (MetaMask)
  autoConnect: false,        // Disable automatic connection
};
const metaMaskSDK = new MetaMaskSDK(options);

// Function to connect the dApp to MetaMask
async function connectToMetaMask() {
  if (!isMetaMaskInstalled()) {
    console.error('MetaMask is not installed. Please install MetaMask and try again.');
    alert('MetaMask is not installed. Please install the extension.');
    return;
  }

  try {
    // Request account permissions
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    alert(`Connected to MetaMask account: ${accounts[0]}`);
    
    // Update UI or perform post-connection operations here
    handleAccountChange(accounts[0]);
  } catch (error) {
    console.error('Error connecting to MetaMask:', error.message);
    alert('Failed to connect to MetaMask. Check the console for details.');
  }
}

// Function to listen for account changes
function handleAccountChange(account) {
  console.log('Account changed to:', account);
  // Update UI or take necessary steps when the account changes
}

// Listen for account changes (helpful for detecting user switches within MetaMask)
window.ethereum?.on('accountsChanged', (accounts) => {
  if (accounts.length > 0) {
    handleAccountChange(accounts[0]);
  } else {
    console.warn('No accounts connected.');
  }
});

// Listen for chain/network changes
window.ethereum?.on('chainChanged', (chainId) => {
  console.log('Chain changed to:', chainId);
  // Handle network/chain changes appropriately
});

// Example button click handler for connecting to MetaMask
document.getElementById('connectButton').addEventListener('click', connectToMetaMask);

// Example HTML:
// <button id="connectButton">Connect to MetaMask</button>
```

### Key Notes:
- The code assumes that the HTML contains a button with the `id="connectButton"`.
- It adds listeners for account and chain changes, allowing the dApp to react dynamically to user actions.
- Proper error handling ensures usability and helps debug issues.
