"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ostpp.ru
Prompt: Write a code snippet that demonstrates how to connect a wallet like MetaMask to Hop Protocol for transferring tokens.
Generated: DETERMINISTIC_d538bfa70418a770
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';
import { Hop, ChainId } from '@hop-protocol/sdk';

// Define the main function to connect MetaMask and transfer tokens
async function transferTokens() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    // Create a new Web3 instance
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access from MetaMask
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Set up the Hop Protocol client
        const hop = new Hop();

        // Define the token transfer parameters
        const amount = web3.utils.toWei('0.1', 'ether'); // Change to the desired amount
        const fromChain = ChainId.ETHEREUM; // Source chain
        const toChain = ChainId.AVAX; // Destination chain
        const tokenAddress = '0xYourTokenAddress'; // Replace with your token's address

        // Transfer tokens using Hop Protocol
        const tx = await hop.transfer({
            fromChain,
            toChain,
            token: tokenAddress,
            amount,
            from: userAddress
        });

        // Wait for transaction confirmation
        await tx.wait();
        
        console.log(`Transaction successful: ${tx.hash}`);
    } catch (error) {
        // Handle errors
        if (error.code === 4001) {
            // User denied account connection
            console.error('User denied account access.');
        } else {
            console.error('An error occurred:', error);
        }
    }
}

// Call the function to initiate the transfer
transferTokens();
```
