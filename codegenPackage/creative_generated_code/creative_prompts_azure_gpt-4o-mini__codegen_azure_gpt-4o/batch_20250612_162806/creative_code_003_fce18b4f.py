"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloginjpg.gitbook.io
Prompt: How can I use MetaMask to manage user accounts in a decentralized application?
Generated: DETERMINISTIC_fce18b4f7edac766
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates how to use MetaMask to manage user accounts
 * in a decentralized application (dApp). It includes connecting to MetaMask,
 * retrieving the user's accounts, and handling errors gracefully.
 */

// Check if the browser supports the Ethereum object provided by MetaMask
if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is installed');
} else {
  console.error('MetaMask is not installed. Please install it to use this dApp.');
}

// Function to connect to MetaMask and retrieve the user's account information
async function connectToMetaMask() {
  try {
    // Request permission to access the user's accounts
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Successfully retrieved accounts
    console.log('Connected account:', accounts[0]);

    // Perform actions with the user's account (e.g., display account, interact with smart contracts)
    return accounts[0];
  } catch (error) {
    // Handle errors gracefully
    if (error.code === 4001) {
      console.error('User denied account access.');
    } else {
      console.error('An error occurred while connecting to MetaMask:', error.message);
    }
  }
}

// Event listener to detect account changes (e.g., user switches accounts in MetaMask)
window.ethereum.on('accountsChanged', (accounts) => {
  if (accounts.length > 0) {
    console.log('Account changed:', accounts[0]);
    // Update application state based on the new account
  } else {
    console.warn('No accounts connected. User may have disconnected MetaMask.');
  }
});

// Event listener to detect network changes (e.g., user switches networks in MetaMask)
window.ethereum.on('chainChanged', (chainId) => {
  console.log('Network changed. New chain ID:', chainId);
  // Refresh the application or update state based on the new network
});

// Function to check the current account without connecting
async function getCurrentAccount() {
  try {
    // Retrieve accounts (if already connected)
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });

    if (accounts.length > 0) {
      console.log('Current account:', accounts[0]);
      return accounts[0];
    } else {
      console.warn('No accounts connected.');
      return null;
    }
  } catch (error) {
    console.error('An error occurred while retrieving current account:', error.message);
  }
}

// Example usage: Connect to MetaMask
(async () => {
  const userAccount = await connectToMetaMask();
  if (userAccount) {
    console.log('Successfully connected to MetaMask:', userAccount);
  } else {
    console.warn('Failed to connect to MetaMask.');
  }
})();
```

This code adheres to your requirements and demonstrates best practices for interacting with MetaMask in a decentralized application.
