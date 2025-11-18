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
// MetaMask Login Integration for dApp

// Check if MetaMask is installed
async function isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Connect to MetaMask wallet
async function connectWallet() {
    try {
        if (!await isMetaMaskInstalled()) {
            alert('MetaMask is not installed. Please install it to proceed.');
            return null;
        }
        
        // Request accounts from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure your MetaMask wallet is unlocked and connected.');
        }
        
        const userWalletAddress = accounts[0];
        console.log('Wallet connected: ', userWalletAddress);
        
        return userWalletAddress;
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        alert(`Failed to connect wallet: ${error.message}`);
        return null;
    }
}

// Authenticate the user (example authentication action)
async function authenticateUser(walletAddress) {
    try {
        // Example of sending the wallet address for server-side authentication
        const response = await fetch('/authenticate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ walletAddress })
        });

        if (!response.ok) {
            throw new Error('Authentication failed. Please try again.');
        }

        const data = await response.json();
        console.log('Authentication successful:', data);
        alert(`Welcome, user authenticated with wallet address: ${walletAddress}`);
    } catch (error) {
        console.error('Error during authentication:', error);
        alert(`Authentication failed: ${error.message}`);
    }
}

// Event handler for MetaMask login
async function handleMetaMaskLogin() {
    const walletAddress = await connectWallet();
    if (walletAddress) {
        await authenticateUser(walletAddress);
    }
}

// Attach event listener to login button
document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.getElementById('loginButton');
    if (loginButton) {
        loginButton.addEventListener('click', handleMetaMaskLogin);
    } else {
        console.error('Login button not found on page.');
    }
});

/* Example HTML:
<button id="loginButton">Login with MetaMask</button>
*/
```
