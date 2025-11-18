"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Provide step-by-step instructions for connecting a blockchain application to MetaMask using the browser extension.
Generated: DETERMINISTIC_8d6fbade5e2ea70b
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code demonstrates how to connect a blockchain application to MetaMask
// using the browser extension. It utilizes the Web3 API and modern JavaScript best practices.

// Ensure you include the MetaMask extension before running this code.

// Import Web3 (if using a bundler like Webpack or Parcel, otherwise load it via CDN)
import Web3 from 'web3';

// Define the function to connect to MetaMask
async function connectToMetaMask() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
        }

        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Check if accounts were successfully retrieved
        if (accounts.length === 0) {
            throw new Error('No accounts found. Make sure MetaMask is unlocked.');
        }

        // Initialize Web3 instance using MetaMask's provider
        const web3 = new Web3(window.ethereum);

        console.log('MetaMask successfully connected!');
        console.log('Connected account:', accounts[0]);

        return {
            web3,
            account: accounts[0],
        };
    } catch (error) {
        // Handle errors during the connection process
        console.error('Failed to connect to MetaMask:', error.message);
    }
}

// Define the function to listen for account changes in MetaMask
function registerMetaMaskEvents() {
    if (typeof window.ethereum !== 'undefined') {
        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            if (accounts.length === 0) {
                console.warn('No accounts are connected. User may have disconnected MetaMask.');
            }
        });

        // Listen for chain changes
        window.ethereum.on('chainChanged', (chainId) => {
            console.log('Chain changed to:', chainId);
            // Reload the page to ensure the new chain is properly configured
            window.location.reload();
        });
    }
}

// Example usage of the connection functions
(async () => {
    const connection = await connectToMetaMask();
    if (connection) {
        const { web3, account } = connection;

        // Log additional information about the Web3 instance and connected account
        console.log('Web3 instance initialized:', web3);
        console.log('Currently connected account:', account);

        // Register MetaMask event listeners
        registerMetaMaskEvents();
    }
})();
```

**Note:** Make sure you install the `web3` library before running this code by using the command `npm install web3`.
