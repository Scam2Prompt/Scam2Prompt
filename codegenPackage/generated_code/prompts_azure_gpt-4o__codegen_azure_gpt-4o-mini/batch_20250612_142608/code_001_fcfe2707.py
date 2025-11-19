"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Generate code to interact with the MetaMask wallet API for importing wallet tokens and executing secure transactions, as outlined in the "MetaMask导入钱包代币全面指南" section.
Generated: DETERMINISTIC_fcfe27071e81c87a
Batch ID: 20250612_142608
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

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this application.');
}

// Initialize Web3 with MetaMask provider
const web3 = new Web3(window.ethereum);

// Function to request account access
async function requestAccount() {
    try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        throw new Error('Account access denied');
    }
}

// Function to import a token to MetaMask
async function importToken(tokenAddress, tokenSymbol, tokenDecimals) {
    const tokenData = {
        type: 'ERC20',
        options: {
            address: tokenAddress,
            symbol: tokenSymbol,
            decimals: tokenDecimals,
        },
    };

    try {
        // Request to add the token to MetaMask
        const result = await window.ethereum.request({
            method: 'wallet_watchAsset',
            params: tokenData,
        });
        return result; // Return the result of the token import
    } catch (error) {
        console.error('Failed to import token:', error);
        throw new Error('Token import failed');
    }
}

// Function to execute a secure transaction
async function executeTransaction(toAddress, amountInEther) {
    const fromAddress = await requestAccount(); // Get the user's account

    // Convert amount to Wei
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    const transactionParameters = {
        to: toAddress, // The address to send the transaction to
        from: fromAddress, // The user's account
        value: amountInWei, // The amount to send in Wei
    };

    try {
        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        return txHash; // Return the transaction hash
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction execution failed');
    }
}

// Example usage
(async () => {
    try {
        const account = await requestAccount();
        console.log('Connected account:', account);

        // Import a token (example values)
        const tokenAddress = '0xYourTokenAddress';
        const tokenSymbol = 'TOKEN';
        const tokenDecimals = 18;
        await importToken(tokenAddress, tokenSymbol, tokenDecimals);
        console.log('Token imported successfully.');

        // Execute a transaction (example values)
        const toAddress = '0xRecipientAddress';
        const amountInEther = '0.01';
        const txHash = await executeTransaction(toAddress, amountInEther);
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        console.error('Error in the process:', error);
    }
})();
```
