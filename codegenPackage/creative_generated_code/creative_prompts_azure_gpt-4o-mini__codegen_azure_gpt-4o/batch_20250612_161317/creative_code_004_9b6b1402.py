"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Explain how to use Metamask for wallet integration in a decentralized application.
Generated: DETERMINISTIC_9b6b1402641328f6
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (ensure they are installed in your project)
const Web3 = require('web3');

// Initialize the web3 instance
let web3;

// Function to check if MetaMask is installed
function checkMetaMaskInstallation() {
  if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
    return true;
  } else {
    console.error('MetaMask is not installed.');
    return false;
  }
}

// Function to connect MetaMask wallet
async function connectMetaMask() {
  try {
    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the connected account
  } catch (error) {
    console.error('Error connecting MetaMask wallet:', error.message);
    throw error; // Re-throw for higher-level handling
  }
}

// Function to initialize web3 with MetaMask's provider
function initializeWeb3() {
  try {
    if (!checkMetaMaskInstallation()) {
      throw new Error('MetaMask is not installed.');
    }

    // Initialize web3 using MetaMask's provider
    web3 = new Web3(window.ethereum);
    console.log('Web3 initialized successfully.');
  } catch (error) {
    console.error('Error initializing web3:', error.message);
    throw error;
  }
}

// Function to listen for account changes
function listenForAccountChanges() {
  if (window.ethereum) {
    // Listen for account changes
    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length > 0) {
        console.log('Account changed:', accounts[0]);
      } else {
        console.warn('No accounts connected.');
      }
    });
  } else {
    console.warn('MetaMask is not installed.');
  }
}

// Function to listen for network changes
function listenForNetworkChanges() {
  if (window.ethereum) {
    // Listen for network changes
    window.ethereum.on('chainChanged', (chainId) => {
      console.log('Network changed. New chain ID:', chainId);
      // Reinitialize web3 to reflect the new network
      initializeWeb3();
    });
  } else {
    console.warn('MetaMask is not installed.');
  }
}

// Example usage
(async () => {
  try {
    // Initialize MetaMask integration
    initializeWeb3();

    // Connect MetaMask wallet
    const account = await connectMetaMask();

    // Set up event listeners for account and network changes
    listenForAccountChanges();
    listenForNetworkChanges();

    console.log('MetaMask integration complete. Connected account:', account);
  } catch (error) {
    console.error('Error during MetaMask integration:', error.message);
  }
})();
```

### Notes:
- Ensure the `web3` library is installed by running `npm install web3`.
- This code assumes a modern browser environment where MetaMask is installed as a browser extension.
- Place this script in the appropriate context where MetaMask functionality is needed, such as the frontend of your decentralized application (DApp).
