"""
Generated Code Metadata:
========================
Original URL: https://dapp-ordizkio.pages.dev
Prompt: "Create a basic example of how to connect a wallet to a dapp like OrdiZK for cross-chain transactions using Web3.js or Ethers.js."
Generated: DETERMINISTIC_e79a853a9651305f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
require('dotenv').config();

// Wallet connection handler
async function connectWallet() {
    try {
        // Check if Web3 provider is available (e.g., MetaMask)
        if (window.ethereum) {
            console.log('Web3 provider detected');
            
            // Create Ethers provider from window.ethereum
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            
            // Request account access
            console.log('Requesting account access...');
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            
            // Get signer
            const signer = provider.getSigner();
            const address = await signer.getAddress();
            
            console.log(`Connected to wallet: ${address}`);
            
            return {
                provider,
                signer,
                address
            };
        } else {
            throw new Error('No Web3 provider detected. Please install MetaMask or another Web3 wallet.');
        }
    } catch (error) {
        console.error('Error connecting wallet:', error);
        throw error;
    }
}

// Example cross-chain transaction
async function sendCrossChainTransaction(signer, toAddress, amount, chainId) {
    try {
        // Get current network
        const network = await signer.provider.getNetwork();
        
        // Check if we're on the correct chain
        if (network.chainId !== chainId) {
            throw new Error(`Please switch to chain ID ${chainId}`);
        }
        
        // Create transaction
        const tx = {
            to: toAddress,
            value: ethers.utils.parseEther(amount.toString())
        };
        
        console.log(`Sending ${amount} ETH to ${toAddress} on chain ${chainId}`);
        
        // Send transaction
        const transaction = await signer.sendTransaction(tx);
        const receipt = await transaction.wait();
        
        console.log('Transaction successful:', receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw error;
    }
}

// Main execution (example usage)
(async () => {
    try {
        // Connect wallet
        const { signer, address } = await connectWallet();
        
        // Example transaction parameters
        const toAddress = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'; // Example address
        const amount = 0.01; // ETH
        const chainId = 1; // Mainnet
        
        // Send transaction
        await sendCrossChainTransaction(signer, toAddress, amount, chainId);
    } catch (error) {
        console.error('Application error:', error);
    }
})();
```
