"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://home-io-metamask-cdn.bravesites.com
Prompt: Write JavaScript code to integrate MetaMask login functionality into a dApp, ensuring secure wallet connection and user authentication as described on the webpage.
Generated: DETERMINISTIC_5295aec26b0e832c
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');

// Initialize Web3 provider
let web3;

// Function to initialize MetaMask connection
async function initMetaMask() {
    if (window.ethereum) {
        // Create a new instance of Web3
        web3 = new Web3(window.ethereum);
        try {
            // Request account access from MetaMask
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected');
        } catch (error) {
            // Handle user rejection of account access
            console.error('User denied account access:', error);
            alert('Please allow access to your MetaMask account.');
        }
    } else {
        // Handle case where MetaMask is not installed
        console.error('MetaMask not detected. Please install it to use this dApp.');
        alert('MetaMask is required to use this dApp. Please install it.');
    }
}

// Function to get the connected account
async function getConnectedAccount() {
    try {
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please connect your wallet.');
        }
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error('Error getting connected account:', error);
        alert('Error retrieving connected account. Please try again.');
    }
}

// Function to display account information to the user
async function displayAccountInfo() {
    const account = await getConnectedAccount();
    if (account) {
        console.log(`Connected account: ${account}`);
        document.getElementById('accountInfo').textContent = `Connected account: ${account}`;
    }
}

// Event listener for connecting MetaMask
document.getElementById('connectButton').addEventListener('click', async () => {
    await initMetaMask(); // Initialize MetaMask
    await displayAccountInfo(); // Display connected account info
});

// Function to handle account change
window.ethereum.on('accountsChanged', async () => {
    console.log('Account changed');
    await displayAccountInfo(); // Update account info on change
});

// Function to handle network change
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    // Optionally: You can reload the page or handle the change appropriately
});

// Initial setup when the window loads
window.onload = async () => {
    await initMetaMask(); // Attempt to connect on page load
    await displayAccountInfo(); // Display account info if connected
};
```

Make sure to include appropriate HTML elements in your webpage, such as:

```html
<button id="connectButton">Connect MetaMask</button>
<div id="accountInfo"></div>
```

Ensure that this code is included in a secure environment and that you handle sensitive data appropriately.
