"""
Generated Code Metadata:
========================
Original URL: https://ostpp.ru
Prompt: Write JavaScript code using web3.js to connect a MetaMask wallet to Hop Protocol and initiate a token transfer between Ethereum and Optimism networks. Include steps for handling transaction fees and relayer interactions.
Generated: DETERMINISTIC_c70e19cea28d20fd
Batch ID: 20250612_154847
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
import { Hop } from '@hop-protocol/sdk';

// Initialize Web3 and connect to MetaMask
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('MetaMask connected');
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
    }
}

// Function to initiate token transfer using Hop Protocol
async function transferTokens(amount, tokenAddress, fromChain, toChain) {
    try {
        // Ensure the user is connected to MetaMask
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please connect MetaMask.');
        }

        const senderAddress = accounts[0];

        // Initialize Hop SDK
        const hop = new Hop({ chain: fromChain });

        // Get the transfer parameters
        const transferParams = {
            from: senderAddress,
            to: senderAddress, // Sending to self for simplicity
            amount: web3.utils.toWei(amount.toString(), 'ether'), // Convert to wei
            token: tokenAddress,
            fromChain: fromChain,
            toChain: toChain,
        };

        // Estimate gas fees
        const gasEstimate = await hop.estimateGas(transferParams);
        console.log(`Estimated gas: ${gasEstimate}`);

        // Initiate the transfer
        const tx = await hop.transfer(transferParams);
        console.log('Transaction sent:', tx);

        // Wait for transaction confirmation
        const receipt = await tx.wait();
        console.log('Transaction confirmed:', receipt);
    } catch (error) {
        console.error('Error during token transfer:', error);
    }
}

// Example usage
(async () => {
    await connectMetaMask();
    const amountToTransfer = 0.1; // Amount in ETH
    const tokenAddress = '0xYourTokenAddress'; // Replace with your token address
    const fromChain = 'ethereum'; // Source chain
    const toChain = 'optimism'; // Destination chain

    await transferTokens(amountToTransfer, tokenAddress, fromChain, toChain);
})();
```

**Note:** Replace `'0xYourTokenAddress'` with the actual token address you wish to transfer. Ensure that the Hop SDK is properly installed and configured in your project.
