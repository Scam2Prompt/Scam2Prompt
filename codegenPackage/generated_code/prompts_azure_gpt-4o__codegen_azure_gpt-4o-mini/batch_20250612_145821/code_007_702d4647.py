"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.eu
Prompt: Provide an example of integrating an Arbitrum-compatible wallet into a web application using JavaScript.
Generated: DETERMINISTIC_702d4647a2dd7eb1
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define a function to initialize the wallet connection
async function initWallet() {
    // Check if the browser has a wallet provider (like MetaMask)
    if (window.ethereum) {
        // Create a new Web3 instance with the provider
        const web3 = new Web3(window.ethereum);
        
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected successfully');

            // Get the user's accounts
            const accounts = await web3.eth.getAccounts();
            console.log('Connected account:', accounts[0]);

            // Set the provider for future use
            web3.eth.defaultAccount = accounts[0];

            // Return the web3 instance and the connected account
            return { web3, account: accounts[0] };
        } catch (error) {
            // Handle errors related to account access
            console.error('User denied account access or error occurred:', error);
            alert('Please allow access to your wallet to continue.');
        }
    } else {
        // Handle the case where the wallet provider is not available
        console.error('No wallet provider found. Please install MetaMask or another wallet.');
        alert('Please install a wallet like MetaMask to use this application.');
    }
}

// Example usage of the initWallet function
document.getElementById('connectButton').addEventListener('click', async () => {
    const walletInfo = await initWallet();
    if (walletInfo) {
        // Proceed with further actions using walletInfo.web3 and walletInfo.account
        console.log('Wallet info:', walletInfo);
    }
});

// Optional: Handle network changes
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    // Reload the page or update the application state as needed
    window.location.reload();
});

// Optional: Handle account changes
window.ethereum.on('accountsChanged', (accounts) => {
    console.log('Account changed to:', accounts[0]);
    // Update the application state with the new account
});
```
