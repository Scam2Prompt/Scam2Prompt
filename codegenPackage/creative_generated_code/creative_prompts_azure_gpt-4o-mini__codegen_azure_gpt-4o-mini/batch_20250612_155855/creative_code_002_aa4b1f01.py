"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Generate a JavaScript function that connects to a user's Metamask wallet and allows them to swap tokens for BULLDOGITO COIN.
Generated: DETERMINISTIC_aa4b1f01b68582e8
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3'; // Library to interact with Ethereum blockchain
import { ethers } from 'ethers'; // Library for interacting with Ethereum and other blockchains

// Define the token swap function
async function swapTokensForBulldogitoCoin() {
    // Check if the Metamask extension is installed
    if (!window.ethereum) {
        alert("Please install Metamask to use this feature.");
        return;
    }

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a Web3 instance
        const web3 = new Web3(window.ethereum);

        // Define the contract address and ABI for the Bulldogito Coin
        const bulldogitoCoinAddress = '0xYourBulldogitoCoinContractAddress'; // Replace with actual contract address
        const bulldogitoCoinABI = [ /* Replace with actual ABI */ ];

        // Create a contract instance
        const bulldogitoCoinContract = new web3.eth.Contract(bulldogitoCoinABI, bulldogitoCoinAddress);

        // Define the token you want to swap (e.g., USDT)
        const tokenAddress = '0xYourTokenAddress'; // Replace with actual token address
        const tokenABI = [ /* Replace with actual ABI */ ];
        const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

        // Get the user's account
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Define amount to swap (in tokens) and other swap parameters
        const amountToSwap = web3.utils.toWei('1', 'ether'); // Example: swapping 1 token
        const slippage = 0.05; // 5% slippage tolerance

        // Allow the contract to spend user's tokens
        await tokenContract.methods.approve(bulldogitoCoinAddress, amountToSwap).send({ from: userAddress });

        // Execute the swap (this will depend on your swap logic and smart contract)
        const tx = await bulldogitoCoinContract.methods.swapTokens(tokenAddress, amountToSwap).send({ from: userAddress });

        console.log('Token swap successful: ', tx);
        alert('Swap successful!');

    } catch (error) {
        console.error('An error occurred during the token swap:', error);
        alert('An error occurred: ' + error.message);
    }
}

// Example usage: Call the swap function when a button is clicked
document.getElementById('swapButton').addEventListener('click', swapTokensForBulldogitoCoin);
```

**Note:** Replace `0xYourBulldogitoCoinContractAddress`, `0xYourTokenAddress`, and the ABI placeholders with the actual values for the Bulldogito Coin and the token being swapped. Make sure the swap logic in the `swapTokens` method is correctly implemented in your smart contract.
