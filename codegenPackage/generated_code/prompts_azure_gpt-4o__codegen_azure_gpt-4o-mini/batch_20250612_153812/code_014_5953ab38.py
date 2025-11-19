"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Write a script to integrate MetaMask Institutional features for managing crypto portfolios, as described in Consensys' Q1 2023 review.
Generated: DETERMINISTIC_5953ab38673ee4d9
Batch ID: 20250612_153812
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
import { ethers } from 'ethers';

// Define constants for MetaMask and Ethereum network
const METAMASK_PROVIDER = window.ethereum;
const NETWORK = 'mainnet'; // Change to desired network (e.g., 'rinkeby' for testnet)

// Initialize Web3 instance
const web3 = new Web3(METAMASK_PROVIDER);

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await METAMASK_PROVIDER.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        throw new Error('Connection to MetaMask failed');
    }
}

// Function to get the balance of a specific token
async function getTokenBalance(tokenAddress, account) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const balance = await tokenContract.methods.balanceOf(account).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert from Wei to Ether
    } catch (error) {
        console.error('Error fetching token balance:', error);
        throw new Error('Failed to fetch token balance');
    }
}

// Function to send tokens
async function sendTokens(tokenAddress, toAddress, amount, account) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
        
        const transaction = await tokenContract.methods.transfer(toAddress, amountInWei).send({ from: account });
        console.log('Transaction successful:', transaction);
        return transaction;
    } catch (error) {
        console.error('Error sending tokens:', error);
        throw new Error('Token transfer failed');
    }
}

// Function to fetch portfolio details
async function fetchPortfolioDetails(account) {
    try {
        // Example token addresses (replace with actual token addresses)
        const tokenAddresses = [
            '0xTokenAddress1',
            '0xTokenAddress2',
            // Add more token addresses as needed
        ];

        const balances = await Promise.all(tokenAddresses.map(address => getTokenBalance(address, account)));
        const portfolio = tokenAddresses.reduce((acc, address, index) => {
            acc[address] = balances[index];
            return acc;
        }, {});

        console.log('Portfolio details:', portfolio);
        return portfolio;
    } catch (error) {
        console.error('Error fetching portfolio details:', error);
        throw new Error('Failed to fetch portfolio details');
    }
}

// Main function to execute the script
(async () => {
    try {
        const account = await connectMetaMask();
        const portfolio = await fetchPortfolioDetails(account);
        console.log('User Portfolio:', portfolio);
        
        // Example of sending tokens (uncomment to use)
        // await sendTokens('0xTokenAddress1', '0xRecipientAddress', 1, account);
    } catch (error) {
        console.error('An error occurred in the main execution:', error);
    }
})();

// ERC20 Token ABI (simplified for balanceOf and transfer methods)
const ERC20_ABI = [
    {
        "constant": true,
        "inputs": [{ "name": "_owner", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "balance", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            { "name": "_to", "type": "address" },
            { "name": "_value", "type": "uint256" }
        ],
        "name": "transfer",
        "outputs": [{ "name": "", "type": "bool" }],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];
```
