"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metasmm-help.gitbook.io
Prompt: Suggest best practices for integrating the MetaMask Chrome extension into a decentralized application (dApp) built on Ethereum.
Generated: DETERMINISTIC_141fb8d652f7c7a4
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure you have included the MetaMask provider (window.ethereum)
// MetaMask must be installed in the user's browser.

// Production-ready script to integrate MetaMask into an Ethereum dApp
// Using modern JavaScript and best practices

const connectToMetaMask = async () => {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install it to use this dApp.');
    }

    // Request account access from the user
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Successfully connected
    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the connected account
  } catch (error) {
    // Handle errors (user denied access, MetaMask not installed, etc.)
    console.error('Error connecting to MetaMask:', error.message);
    throw error; // Re-throw the error for further handling
  }
};

const getCurrentAccount = async () => {
  try {
    // Check if MetaMask is available
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed.');
    }

    // Get the currently connected account
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    if (accounts.length === 0) {
      console.log('No accounts connected.');
      return null; // No account is currently connected
    }

    console.log('Current connected account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Error fetching current account:', error.message);
    throw error;
  }
};

const listenForAccountChanges = (callback) => {
  // Listen for account changes in MetaMask
  if (typeof window.ethereum === 'undefined') {
    console.warn('MetaMask is not installed. Account change listener will not work.');
    return;
  }

  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      console.log('Disconnected from MetaMask.');
      callback(null); // Notify that the user has disconnected
    } else {
      console.log('Account changed to:', accounts[0]);
      callback(accounts[0]); // Notify of the new account
    }
  });
};

const listenForChainChanges = (callback) => {
  // Listen for network/chain changes
  if (typeof window.ethereum === 'undefined') {
    console.warn('MetaMask is not installed. Chain change listener will not work.');
    return;
  }

  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network/Chain changed to:', chainId);
    callback(chainId); // Notify of the new chain ID
  });
};

// Usage example (in an async function or event listener)
(async () => {
  try {
    // Connect to MetaMask
    const account = await connectToMetaMask();

    // Fetch the currently connected account
    const currentAccount = await getCurrentAccount();

    // Listen for account changes
    listenForAccountChanges((newAccount) => {
      console.log('Account change detected:', newAccount);
      // Update your app state or UI accordingly
    });

    // Listen for chain/network changes
    listenForChainChanges((newChainId) => {
      console.log('Chain change detected:', newChainId);
      // Update your app state or UI accordingly
    });

    console.log(`Successfully connected to MetaMask with account: ${account}`);
  } catch (error) {
    console.error('Failed to initialize MetaMask integration:', error.message);
  }
})();
```
