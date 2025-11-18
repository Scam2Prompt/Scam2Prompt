"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-realio.network
Prompt: Show how to use MetaMask's Wallet Guard feature to implement frontrun protection and security alerts in a blockchain application.
Generated: DETERMINISTIC_30c1a1d97239fafd
Batch ID: 20250612_150816
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
import WalletGuard from '@metamask/wallet-guard'; // Hypothetical import for illustration purposes
import { ethers } from 'ethers';

// Initialize Web3 with MetaMask
const web3 = new Web3(window.ethereum);

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this application.');
}

/**
 * Function to initialize Wallet Guard for frontrun protection and security alerts
 */
async function initializeWalletGuard() {
    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Initialize Wallet Guard with desired options for frontrun protection
        const guardOptions = {
            onFrontrunDetected: (transaction) => {
                alert(`Frontrun detected for transaction: ${transaction.hash}`);
                console.log(transaction); // Log the transaction details for further analysis
            },
            onSuspiciousActivityDetected: (activity) => {
                alert(`Suspicious activity detected: ${activity.type}`);
                console.log(activity); // Log the activity details
            }
        };

        // Activate Wallet Guard
        WalletGuard.init(guardOptions);
        console.log('Wallet Guard initialized successfully.');
        
    } catch (error) {
        // Handle errors that might occur during wallet initialization or access requests
        console.error('Error initializing Wallet Guard:', error.message);
    }
}

/**
 * Function to send a transaction
 * @param {string} to - Recipient address
 * @param {number} value - Amount to send in Ether
 */
async function sendTransaction(to, value) {
    try {
        const accounts = await web3.eth.getAccounts();
        const transactionParameters = {
            to: to,
            from: accounts[0],
            value: web3.utils.toHex(web3.utils.toWei(value.toString(), 'ether')),
            gas: '2000000',
        };

        // Send the transaction using MetaMask
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log('Transaction sent successfully:', txHash);
    } catch (error) {
        // Handle transaction errors
        console.error('Transaction error:', error.message);
    }
}

// Initialize Wallet Guard when the document is ready
document.addEventListener('DOMContentLoaded', async () => {
    await initializeWalletGuard();
});

// Example usage: Send a transaction (replace with valid params)
sendTransaction('0xRecipientAddressHere', 0.01);
```

### Note:
- The `@metamask/wallet-guard` import is hypothetical and serves as an example. Adjust the import based on the actual package provided by MetaMask when implementing the Wallet Guard feature.
- Ensure that you have the necessary libraries installed, and adjust configurations as needed for your specific environment and application requirements.
