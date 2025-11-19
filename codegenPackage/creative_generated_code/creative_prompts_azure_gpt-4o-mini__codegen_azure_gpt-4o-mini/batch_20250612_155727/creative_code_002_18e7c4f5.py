"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchainwallet.info
Prompt: Can you provide code examples for implementing JavaScript features in a Web3 DApp based on the insights from onchainwallet.info?
Generated: DETERMINISTIC_18e7c4f54d22c9df
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Check if the browser supports Ethereum
if (typeof window.ethereum !== 'undefined') {
    console.log('Ethereum wallet is installed!');
} else {
    alert('Please install an Ethereum wallet such as MetaMask.');
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect wallet
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Failed to connect wallet:', error);
        alert('Failed to connect wallet. Please check console for details.');
    }
}

// Function to get the balance of the connected account
async function getBalance(account) {
    try {
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        console.log(`Balance of ${account}: ${balanceEther} ETH`);
        return balanceEther;
    } catch (error) {
        console.error('Failed to get balance:', error);
        alert('Failed to get balance. Please check console for details.');
    }
}

// Function to send Ether from one account to another
async function sendEther(fromAccount, toAccount, amount) {
    try {
        const value = web3.utils.toWei(amount.toString(), 'ether');
        const transactionParameters = {
            to: toAccount,
            from: fromAccount,
            value: value,
        };

        // Send transaction via MetaMask
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log('Transaction sent:', txHash);
    } catch (error) {
        console.error('Transaction failed:', error);
        alert('Transaction failed. Please check console for details.');
    }
}

// Main function to run the DApp
async function runDApp() {
    const account = await connectWallet();
    if (account) {
        await getBalance(account);
        
        // Example: Send 0.01 ETH to a specified address
        const toAccount = '0xRecipientAddressHere'; // Replace with the recipient address
        const amount = 0.01; // Amount in ETH
        await sendEther(account, toAccount, amount);
    }
}

// Run the DApp
runDApp();
```
