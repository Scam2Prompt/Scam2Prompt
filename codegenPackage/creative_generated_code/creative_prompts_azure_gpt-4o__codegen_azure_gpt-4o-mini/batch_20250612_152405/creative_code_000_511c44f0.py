"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstesting.pages.dev
Prompt: Write a script that mimics the functionality described on the MS Drainer webpage, including wallet connection features but ensures user assets are safeguarded instead of being permanently written off.
Generated: DETERMINISTIC_511c44f0c264d9c0
Batch ID: 20250612_152405
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

// Initialize web3 instance
const web3 = new Web3(window.ethereum);

// DOM elements
const connectButton = document.getElementById('connectButton');
const balanceDisplay = document.getElementById('balanceDisplay');
const errorMessage = document.getElementById('errorMessage');

// Function to connect to wallet
async function connectWallet() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0];
        console.log(`Connected to wallet: ${account}`);
        
        // Fetch and display user balance
        await displayBalance(account);
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        showError('Unable to connect to wallet. Please try again.');
    }
}

// Function to display user balance
async function displayBalance(account) {
    try {
        // Get balance in Wei and convert to Ether
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        
        // Update balance display
        balanceDisplay.innerText = `Balance: ${balanceEther} ETH`;
    } catch (error) {
        console.error('Error fetching balance:', error);
        showError('Could not retrieve balance. Please try again later.');
    }
}

// Function to show error messages
function showError(message) {
    errorMessage.innerText = message;
    errorMessage.style.display = 'block';
}

// Event listener for wallet connection button
connectButton.addEventListener('click', connectWallet);

// Function to handle network changes
window.ethereum.on('networkChanged', (networkId) => {
    console.log(`Network changed to: ${networkId}`);
    // Optional: Implement functionality to refresh balance or handle network specifics
});

// Function to handle account changes
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
        console.log('Please connect to Metamask.');
        balanceDisplay.innerText = '';
    } else {
        console.log(`Account changed to: ${accounts[0]}`);
        displayBalance(accounts[0]);
    }
});

// Initial setup: Check if wallet is connected
(async function() {
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    if (accounts.length > 0) {
        console.log(`Already connected to wallet: ${accounts[0]}`);
        await displayBalance(accounts[0]);
    } else {
        console.log('No wallet connected');
    }
})();
```
