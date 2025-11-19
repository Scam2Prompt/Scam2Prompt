"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Write a tutorial on setting up security alerts and Wallet Guard in MetaMask for better protection.
Generated: DETERMINISTIC_6fbd41bf81e513cb
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Security Alerts and Wallet Guard Setup

// This script provides a simple walkthrough for setting up security alerts and Wallet Guard in MetaMask.

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to proceed.');
}

// Function to set up security alerts by listening to events
async function setupSecurityAlerts() {
    const provider = window.ethereum;

    // Check if the user has granted access to their accounts
    try {
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        console.log('Connected accounts:', accounts);
        alert('Security alerts are now active for your account: ' + accounts[0]);
        
        // Listen for network changes
        provider.on('networkChanged', (networkId) => {
            console.log(`Network changed to: ${networkId}`);
            alert('Network changed, please check your connection.');
        });

        // Listen for account changes
        provider.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            alert('Account changed, please verify your new account.');
        });

    } catch (error) {
        console.error('Error requesting accounts:', error);
        alert('Failed to connect to wallet. Please try again.');
    }
}

// Function to enable Wallet Guard
async function enableWalletGuard() {
    const provider = window.ethereum;

    try {
        // Assume Wallet Guard is a feature that we can enable in the settings
        // This is a hypothetical function call to enable the feature
        const result = await provider.request({ method: 'wallet_enableGuard' });
        
        if (result) {
            console.log('Wallet Guard enabled:', result);
            alert('Wallet Guard is successfully enabled.');
        } else {
            console.warn('Failed to enable Wallet Guard.');
            alert('Failed to enable Wallet Guard. Check your MetaMask settings.');
        }

    } catch (error) {
        console.error('Error enabling Wallet Guard:', error);
        alert('There was an issue enabling Wallet Guard. Please try again.');
    }
}

// Main function to initialize the setup
async function init() {
    await setupSecurityAlerts();
    await enableWalletGuard();
}

// Start the setup process 
init().catch((error) => {
    console.error('Error during initialization:', error);
    alert('An error occurred during setup. Please refresh the page and try again.');
});
```
