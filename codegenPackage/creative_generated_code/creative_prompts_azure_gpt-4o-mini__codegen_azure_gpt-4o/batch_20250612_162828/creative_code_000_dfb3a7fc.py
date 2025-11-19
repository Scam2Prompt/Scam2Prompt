"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-pendle.finance
Prompt: How can I integrate the MetaMask SDK into my dapp for seamless wallet connectivity?
Generated: DETERMINISTIC_dfb3a7fc47401c77
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required MetaMask SDK libraries
import { MetaMaskProvider } from '@metamask/providers';

// Define constants for the Ethereum object accessible via the browser
const ethereum = window.ethereum;

// Ensure ethereum object is available (MetaMask installed)
if (!ethereum) {
  console.error('MetaMask is not installed. Please install MetaMask to use this dapp.');
  throw new Error('MetaMask not installed.');
}

// Function to connect MetaMask wallet
// This will prompt the user to connect their wallet to the dapp
async function connectWallet() {
  try {
    // Request wallet connection
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });

    // If accounts array is empty, connection failed
    if (!accounts || accounts.length === 0) {
      console.error('No accounts found after connection attempt.');
      throw new Error('Wallet connection failed.');
    }

    // Successfully connected
    console.log('Wallet connected:', accounts[0]);
    return accounts[0]; // Return the connected account
  } catch (error) {
    // Handle errors (e.g., user rejected connection)
    console.error('Failed to connect wallet:', error.message || error);
    throw error;
  }
}

// Function to get the current connected account
// Useful when you need to verify wallet connectivity
async function getConnectedAccount() {
  try {
    // Request the list of connected accounts
    const accounts = await ethereum.request({ method: 'eth_accounts' });

    // If no accounts are connected
    if (!accounts || accounts.length === 0) {
      console.log('No wallet connected.');
      return null; // Return null if no wallet is connected
    }

    // Return the first connected account
    console.log('Connected wallet:', accounts[0]);
    return accounts[0];
  } catch (error) {
    // Handle errors
    console.error('Failed to get connected account:', error.message || error);
    throw error;
  }
}

// Function to listen for account and network changes
function setupEventListeners() {
  // Listen for account changes
  ethereum.on('accountsChanged', (accounts) => {
    if (accounts && accounts.length > 0) {
      console.log('Account changed:', accounts[0]);
    } else {
      console.log('Wallet disconnected.');
    }
  });

  // Listen for network changes
  ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed. New chain ID:', chainId);
    // Reload the page to refresh the dapp state (optional)
    window.location.reload();
  });
}

// Example usage
(async function initializeDapp() {
  try {
    console.log('Initializing dapp...');

    // Check if MetaMask is installed
    if (!ethereum) {
      throw new Error('MetaMask is required but not installed.');
    }

    // Connect wallet (optional: can trigger on user action instead)
    const account = await connectWallet();
    console.log('Connected account:', account);

    // Setup listeners for account and network changes
    setupEventListeners();

    // Retrieve connected account (if any)
    const connectedAccount = await getConnectedAccount();
    console.log('Currently connected account:', connectedAccount);

    console.log('Dapp initialized successfully.');
  } catch (error) {
    console.error('Error during dapp initialization:', error.message || error);
  }
})();
```

- Make sure to replace this template code with logic specific to your dapp's use case, like handling transactions, interacting with smart contracts, or displaying UI updates.
- You should add additional security measures, such as verifying the correct network for your dapp.
