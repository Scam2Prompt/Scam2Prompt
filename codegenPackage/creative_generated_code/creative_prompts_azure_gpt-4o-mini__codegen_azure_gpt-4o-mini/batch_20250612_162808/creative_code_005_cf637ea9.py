"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: How can I set up security alerts and wallet guard features in my MetaMask integration?
Generated: DETERMINISTIC_cf637ea97b2f9c07
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Security Alerts and Wallet Guard Integration
 * This script sets up a basic integration with MetaMask
 * providing security alerts and wallet guard features.
 */

// Importing necessary libraries
const { ethers } = require("ethers");

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert("Please install MetaMask to use this feature.");
}

/**
 * Initialize MetaMask and connect to the user's wallet
 */
async function connectWallet() {
    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Connected account:", accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error("User denied account access or error occurred:", error);
        alert("Could not connect to wallet. Please check your MetaMask settings.");
        throw error; // Re-throw the error for handling upstream
    }
}

/**
 * Monitor account changes and alert the user
 */
function monitorAccountChanges() {
    window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
            alert("MetaMask is locked or the user has not allowed access.");
        } else {
            alert("Account changed to: " + accounts[0]);
            console.log("New account:", accounts[0]);
        }
    });
}

/**
 * Monitor network changes and alert the user
 */
function monitorNetworkChanges() {
    window.ethereum.on('chainChanged', (chainId) => {
        alert("Network changed to: " + chainId);
        console.log("New chain ID:", chainId);
        // Reload the page to avoid issues with the new network
        window.location.reload();
    });
}

/**
 * Wallet Guard feature to check for suspicious transactions
 */
async function checkSuspiciousTransactions() {
    // Placeholder for a function that checks transaction details
    // Ideally, you would implement logic to fetch recent transactions and analyze them
    const suspiciousTransactionThreshold = 0.5; // Example threshold in ETH

    // Assume we have a function fetchRecentTransactions() that gets transactions
    const recentTransactions = await fetchRecentTransactions();
    
    for (const tx of recentTransactions) {
        if (tx.value > suspiciousTransactionThreshold) {
            alert(`Suspicious transaction detected: ${tx.value} ETH to ${tx.to}`);
            console.log("Suspicious transaction details:", tx);
            // Optionally, you could implement further actions such as blocking the transaction
        }
    }
}

/**
 * Mock function to simulate fetching recent transactions
 * This should be replaced with actual API calls or logic
 */
async function fetchRecentTransactions() {
    // Simulated response
    return [
        { value: 0.6, to: '0xAddress1' },
        { value: 0.1, to: '0xAddress2' },
    ];
}

// Main function to set up the integration
async function initMetaMaskIntegration() {
    const account = await connectWallet();
    monitorAccountChanges();
    monitorNetworkChanges();
    await checkSuspiciousTransactions();
}

// Initialize the integration on page load
window.onload = () => {
    initMetaMaskIntegration().catch(error => {
        console.error("Initialization error:", error);
    });
};
```

This code provides a basic infrastructure for integrating MetaMask with security alerts and wallet guard features, ensuring it is clean, well-documented, and includes necessary error handling.
