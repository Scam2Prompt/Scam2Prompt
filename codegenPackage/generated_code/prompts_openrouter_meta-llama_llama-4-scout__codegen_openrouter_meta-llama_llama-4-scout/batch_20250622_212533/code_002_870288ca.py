"""
Generated Code Metadata:
========================
Original URL: https://metamask.ro
Prompt: What are the key features of MetaMask that make it a secure gateway to blockchain apps, and how can developers utilize these features in their applications?
Generated: DETERMINISTIC_870288ca16ebd282
Batch ID: 20250622_212533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MetaMask Secure Gateway Example
 * 
 * This example demonstrates how to interact with MetaMask's secure features
 * and utilize them in a blockchain application.
 */

// Import required libraries
const Web3 = require('web3');

// Set up Web3 provider
let web3;

/**
 * Connect to MetaMask
 * 
 * @returns {Promise<Web3>} A promise resolving to the Web3 provider
 */
async function connectToMetaMask() {
    try {
        // Check if MetaMask is installed
        if (window.ethereum) {
            // Request access to MetaMask
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Create a new Web3 provider
            web3 = new Web3(window.ethereum);
            return web3;
        } else {
            throw new Error('MetaMask is not installed');
        }
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        throw error;
    }
}

/**
 * Get user's Ethereum accounts
 * 
 * @param {Web3} web3 The Web3 provider
 * @returns {Promise<string[]>} A promise resolving to the user's Ethereum accounts
 */
async function getAccounts(web3) {
    try {
        // Get the user's Ethereum accounts
        const accounts = await web3.eth.getAccounts();
        return accounts;
    } catch (error) {
        console.error('Error getting accounts:', error);
        throw error;
    }
}

/**
 * Sign a transaction
 * 
 * @param {Web3} web3 The Web3 provider
 * @param {string} from The sender's Ethereum account
 * @param {string} to The recipient's Ethereum account
 * @param {number} value The transaction value
 * @returns {Promise<string>} A promise resolving to the signed transaction hash
 */
async function signTransaction(web3, from, to, value) {
    try {
        // Create a new transaction
        const tx = {
            from,
            to,
            value: web3.utils.toWei(value.toString(), 'ether'),
        };
        // Sign the transaction
        const txHash = await web3.eth.sendTransaction(tx);
        return txHash;
    } catch (error) {
        console.error('Error signing transaction:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        // Connect to MetaMask
        const web3 = await connectToMetaMask();
        console.log('Connected to MetaMask');

        // Get user's Ethereum accounts
        const accounts = await getAccounts(web3);
        console.log('Accounts:', accounts);

        // Sign a transaction
        const from = accounts[0];
        const to = '0xRecipientAddress';
        const value = 1;
        const txHash = await signTransaction(web3, from, to, value);
        console.log('Transaction Hash:', txHash);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
```
