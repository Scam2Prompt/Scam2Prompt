"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-puffer.com
Prompt: Generate code to implement security alerts and frontrun protection in a dapp using MetaMask's Wallet Guard feature.
Generated: DETERMINISTIC_cb90da0298c21cc5
Batch ID: 20250612_150658
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
import { ethers } from 'ethers';

// Initialize Web3 and set up the provider
const provider = new ethers.providers.Web3Provider(window.ethereum);
const web3 = new Web3(window.ethereum);

// Constants for security alerts and frontrun protection
const SECURITY_ALERT_THRESHOLD = 0.1; // Threshold for significant transaction size
const FRONTRUN_PROTECTION_TIME = 3000; // Time window to protect against frontrunning in milliseconds

// Variable to track transaction count
let lastTransactionTimestamp = Date.now();

// Function to send a transaction with frontrun protection
async function sendTransaction(to, value) {
    try {
        const signer = provider.getSigner();
        const transaction = {
            to: to,
            value: ethers.utils.parseEther(value.toString()),
            gasLimit: 21000, // Standard gas limit for ETH transfers
            gasPrice: await provider.getGasPrice(),
        };
        
        // Check for potential frontrunning
        if (Date.now() - lastTransactionTimestamp < FRONTRUN_PROTECTION_TIME) {
            alert('Warning: Potential frontrunning detected. Please wait before sending the next transaction.');
            return;
        }

        // Send transaction
        const txResponse = await signer.sendTransaction(transaction);
        console.log('Transaction sent:', txResponse);
        
        // Update last transaction timestamp
        lastTransactionTimestamp = Date.now();

        // Wait for transaction confirmation
        await txResponse.wait();
        console.log('Transaction confirmed:', txResponse.hash);
    } catch (error) {
        handleError(error);
    }
}

// Function to handle errors
function handleError(error) {
    // Log error to console for debugging
    console.error('An error occurred:', error);

    // Display user-friendly error message
    if (error.code === 'USER_REJECTED') {
        alert('Transaction was rejected by the user.');
    } else {
        alert('An error occurred while processing your transaction. Please try again later.');
    }
}

// Function to monitor transactions for security alerts
async function monitorTransactions() {
    provider.on('pending', async (txHash) => {
        try {
            const transaction = await provider.getTransaction(txHash);
            if (transaction && transaction.value && ethers.utils.formatEther(transaction.value) > SECURITY_ALERT_THRESHOLD) {
                alert('Security Alert: A large transaction has been detected.');
            }
        } catch (error) {
            handleError(error);
        }
    });
}

// Function to request account access and initialize monitoring
async function init() {
    if (window.ethereum) {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Account access granted');
            monitorTransactions();
        } catch (error) {
            handleError(error);
        }
    } else {
        alert('Please install MetaMask to use this feature.');
    }
}

// Start the application
init();
```
