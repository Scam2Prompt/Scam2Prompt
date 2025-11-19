"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiavwskgiww3elpabxoxlcv3n46mhlr4fohrwq3gyojtkwmivmo2bu.ipfs.dweb.link
Prompt: Generate a code snippet for integrating a self-custody wallet with a presale smart contract for the $BCKR token.
Generated: DETERMINISTIC_720ca63332a1f521
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
const Web3 = require('web3');

// Initialize web3 with the provider (e.g., Metamask)
const web3 = new Web3(window.ethereum);

// Presale contract ABI and address (replace with actual values)
const PRESALE_CONTRACT_ABI = [ /* ABI array here */ ];
const PRESALE_CONTRACT_ADDRESS = '0xYourPresaleContractAddress';

// Contract instance
const presaleContract = new web3.eth.Contract(PRESALE_CONTRACT_ABI, PRESALE_CONTRACT_ADDRESS);

/**
 * Function to buy $BCKR tokens during the presale
 * @param {string} walletAddress - The address of the user's wallet
 * @param {number} amount - The amount of tokens to buy
 */
async function buyTokens(walletAddress, amount) {
    try {
        // Check if the user is connected to Metamask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        if (!accounts.length) {
            throw new Error('User is not connected to Metamask');
        }

        // Convert amount to Wei before transaction
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Create transaction parameters
        const txParams = {
            from: accounts[0],  // User's wallet address
            to: PRESALE_CONTRACT_ADDRESS,
            value: amountInWei,  // The amount of Ether to send
            gas: 2000000          // Adjust gas limit as needed
        };

        // Sending transaction to buy tokens
        const transactionHash = await presaleContract.methods.buyTokens(amount).send(txParams);
        console.log('Transaction successful with hash:', transactionHash);

    } catch (error) {
        console.error('Error buying tokens:', error.message); // Log error message for debugging
    }
}

// Event listener for a button click to initiate the token purchase
document.getElementById('buyButton').addEventListener('click', () => {
    const walletAddress = web3.eth.defaultAccount; // Use default account from Metamask
    const amount = document.getElementById('amountInput').value; // Get amount from input field
    buyTokens(walletAddress, amount);
});
```

Make sure to replace placeholders like the ABI array and contract address with actual values before deploying this code to production.
