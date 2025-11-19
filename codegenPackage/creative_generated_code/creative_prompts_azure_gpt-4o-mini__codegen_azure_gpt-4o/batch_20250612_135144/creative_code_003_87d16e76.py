"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.hq-innovacion.mx
Prompt: What are the best practices for using MetaMask's API to manage user accounts and permissions in a web app?
Generated: DETERMINISTIC_87d16e76af4cdb16
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This code demonstrates best practices for using MetaMask's API to manage user accounts
 * and permissions in a web application. It follows clean coding principles and includes proper
 * error handling.
 */

// Ensure the code runs only in browsers with MetaMask installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('MetaMask is not installed. Please install MetaMask to use this feature.');
}

/**
 * Function to request the user's MetaMask account
 * and connect it to your web application.
 */
async function connectToMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Successfully connected, log the user's account
        console.log('Connected account:', accounts[0]);
        return accounts[0]; // Return the first account (primary account)
    } catch (error) {
        handleMetaMaskError(error);
    }
}

/**
 * Function to detect account changes and update the UI or application state accordingly.
 */
function detectAccountChanges() {
    window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
            console.log('Account changed to:', accounts[0]);
        } else {
            console.warn('No accounts connected. Please reconnect to MetaMask.');
        }
    });
}

/**
 * Function to detect network changes and handle them appropriately.
 */
function detectNetworkChanges() {
    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Network changed to:', chainId);
        // You can add custom logic here, such as reloading the page or updating the UI
        // window.location.reload();
    });
}

/**
 * Function to handle errors from MetaMask API calls gracefully.
 *
 * @param {Error} error - The error object received from the MetaMask API.
 */
function handleMetaMaskError(error) {
    if (error.code === 4001) {
        console.error('User rejected the request.');
    } else {
        console.error('An unexpected error occurred:', error);
    }
}

/**
 * Example implementation of managing user accounts and permissions
 * when the web app loads.
 */
async function initializeApp() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed.');
        }

        // Connect to MetaMask and get user's account
        const account = await connectToMetaMask();
        console.log('App initialized with account:', account);

        // Set up listeners for account and network changes
        detectAccountChanges();
        detectNetworkChanges();
    } catch (error) {
        console.error('Initialization failed:', error);
    }
}

// Initialize the application when the page loads
window.addEventListener('load', () => {
    initializeApp();
});
```
