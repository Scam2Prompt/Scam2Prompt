"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoo.tech
Prompt: Create a step-by-step guide for integrating MetaMask wallet connection into a decentralized app (DApp) similar to Cryptoo.tech.
Generated: DETERMINISTIC_9912dd62d7db272b
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code for integrating a MetaMask wallet connection into a decentralized app (DApp). The code follows best practices for JavaScript and uses the Web3.js library.

```javascript
// Import necessary dependencies
// Ensure you install web3 using: npm install web3
const Web3 = require('web3');

// Step 1: Initialize Web3 instance
let web3;
if (window.ethereum) {
    // Modern browsers with MetaMask installed
    web3 = new Web3(window.ethereum);
} else if (window.web3) {
    // Legacy browsers or older MetaMask versions
    web3 = new Web3(window.web3.currentProvider);
} else {
    alert('MetaMask not detected. Please install MetaMask to use this DApp.');
}

// Step 2: Connect to MetaMask wallet
async function connectWallet() {
    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get user's Ethereum accounts
        const accounts = await web3.eth.getAccounts();

        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure MetaMask is unlocked.');
        }

        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to MetaMask:', error.message);
        alert(`Failed to connect to MetaMask: ${error.message}`);
    }
}

// Step 3: Detect account changes
function detectAccountChange() {
    window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
            console.log('MetaMask is locked or no accounts detected.');
            alert('MetaMask is locked or not connected.');
        } else {
            console.log('Account changed to:', accounts[0]);
        }
    });
}

// Step 4: Detect network changes
function detectNetworkChange() {
    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Network changed. Current chain ID:', chainId);
        alert(`Network changed to chain ID: ${chainId}`);
        // Reload the DApp to ensure proper network handling
        window.location.reload();
    });
}

// Step 5: Initialize DApp
async function initializeDApp() {
    try {
        const account = await connectWallet();
        console.log('DApp initialized with account:', account);

        // Set up listeners for account and network changes
        detectAccountChange();
        detectNetworkChange();
    } catch (error) {
        console.error('Error initializing DApp:', error.message);
        alert(`Failed to initialize DApp: ${error.message}`);
    }
}

// Step 6: Call initializeDApp to start the application
initializeDApp();
```

**Important Notes:**
1. Ensure you have MetaMask installed in your browser.
2. Test the code in a browser environment as MetaMask is a browser extension.
3. The code assumes that you are working with a front-end JavaScript environment.
4. Install and include Web3.js in your project using `npm install web3`.
