"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://methamaskeslugiysss.godaddysites.com
Prompt: Generate a code snippet for integrating MetaMask login functionality into a web application.
Generated: DETERMINISTIC_fa7c652cea6e01c9
Batch ID: 20250612_155701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3
let web3;

// Function to connect to MetaMask
async function connectMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    // Create a new instance of Web3 with MetaMask's provider
    web3 = new Web3(window.ethereum);

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('MetaMask connected successfully.');

        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        console.log('Connected account:', accounts[0]);
        
        // Return the connected account
        return accounts[0];
    } catch (error) {
        // Handle errors (e.g., user denied account access)
        console.error('Failed to connect to MetaMask:', error.message);
        return null;
    }
}

// Function to check connection status
async function checkConnection() {
    if (web3) {
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
            console.log('Already connected to MetaMask:', accounts[0]);
            return accounts[0];
        } else {
            console.log('No account found. Please connect your MetaMask.');
            return null;
        }
    } else {
        console.log('Web3 is not initialized. Please connect using MetaMask.');
        return null;
    }
}

// Example usage
document.getElementById('connectButton').addEventListener('click', async () => {
    const account = await connectMetaMask();
    if (account) {
        // Proceed with the application logic (e.g., updating UI, fetching data, etc.)
        console.log('Proceeding with account:', account);
    }
});

// Optional: Handle account change
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length > 0) {
        console.log('Account changed to:', accounts[0]);
    } else {
        console.log('Please connect to MetaMask.');
    }
});

// Optional: Handle network change
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
});

// Note: Ensure to include a button with id 'connectButton' in your HTML to trigger the connection.
```

Ensure you have installed the `web3` package in your project to run this code:
```bash
npm install web3
```
