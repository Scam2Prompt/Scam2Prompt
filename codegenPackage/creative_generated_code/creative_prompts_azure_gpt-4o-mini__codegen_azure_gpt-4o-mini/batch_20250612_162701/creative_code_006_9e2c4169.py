"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Provide an example of how to use the MetaMask Institutional features for managing crypto portfolios effectively.
Generated: DETERMINISTIC_9e2c416967ed717d
Batch ID: 20250612_162701
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
import { MetaMaskInpageProvider } from '@metamask/providers';

// Initialize MetaMask provider
const provider = new MetaMaskInpageProvider();
const web3 = new Web3(provider);

// Function to request account access
async function requestAccountAccess() {
    try {
        // Request account access from MetaMask
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        console.log('Accounts:', accounts);
        return accounts[0]; // Return the first account
    } catch (error) {
        // Handle errors in account access
        console.error('Error requesting account access:', error);
        throw new Error('Account access denied');
    }
}

// Function to get balance of a specific token
async function getTokenBalance(tokenAddress, account) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const balance = await tokenContract.methods.balanceOf(account).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert balance to ether
    } catch (error) {
        console.error('Error fetching token balance:', error);
        throw new Error('Failed to fetch token balance');
    }
}

// Function to transfer tokens
async function transferTokens(tokenAddress, to, amount, account) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether'); // Convert amount to wei
        const transaction = await tokenContract.methods.transfer(to, amountInWei).send({ from: account });
        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Error transferring tokens:', error);
        throw new Error('Token transfer failed');
    }
}

// Main function to demonstrate MetaMask Institutional features
async function main() {
    try {
        // Request account access
        const account = await requestAccountAccess();
        
        // Define token address (example: DAI)
        const tokenAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // DAI Token Address
        const balance = await getTokenBalance(tokenAddress, account);
        console.log(`Token Balance for ${account}:`, balance);

        // Example transfer (use caution; this is a demo)
        const recipientAddress = '0xRecipientAddress'; // Replace with actual recipient address
        const amountToSend = 1; // Amount in DAI
        await transferTokens(tokenAddress, recipientAddress, amountToSend, account);
        
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute the main function
main();
```
