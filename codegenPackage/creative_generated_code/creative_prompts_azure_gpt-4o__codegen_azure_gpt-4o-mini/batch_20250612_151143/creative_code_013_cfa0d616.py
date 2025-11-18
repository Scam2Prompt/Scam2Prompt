"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-p.pages.dev
Prompt: Generate code to fix presale-related issues, including buying and claiming presale tokens, as described on the DApp Synchronizer Panel website.
Generated: DETERMINISTIC_cfa0d61642c22bb3
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');

// Configure Web3 provider (e.g., Infura, Alchemy, or local Ethereum node)
const web3 = new Web3(new Web3.providers.HttpProvider('YOUR_INFURA_OR_PROVIDER_URL'));

// Presale contract ABI and address
const presaleContractABI = [ /* ABI goes here */ ];
const presaleContractAddress = 'YOUR_PRESALE_CONTRACT_ADDRESS';

// Create contract instance
const presaleContract = new web3.eth.Contract(presaleContractABI, presaleContractAddress);

/**
 * Function to buy presale tokens
 * @param {string} userAddress - The Ethereum address of the user buying tokens
 * @param {number} amount - The amount of tokens to buy
 * @param {string} privateKey - The private key of the user
 */
async function buyPresaleTokens(userAddress, amount, privateKey) {
    try {
        // Check if the user address is valid
        if (!web3.utils.isAddress(userAddress)) {
            throw new Error('Invalid user address');
        }

        // Calculate the transaction details
        const txData = presaleContract.methods.buyTokens(amount).encodeABI();
        const gasPrice = await web3.eth.getGasPrice();
        const gasLimit = await presaleContract.methods.buyTokens(amount).estimateGas({ from: userAddress });

        const tx = {
            from: userAddress,
            to: presaleContractAddress,
            gas: gasLimit,
            gasPrice: gasPrice,
            data: txData,
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Tokens purchased successfully:', receipt);
    } catch (error) {
        console.error('Error buying presale tokens:', error.message);
    }
}

/**
 * Function to claim presale tokens
 * @param {string} userAddress - The Ethereum address of the user claiming tokens
 * @param {string} privateKey - The private key of the user
 */
async function claimPresaleTokens(userAddress, privateKey) {
    try {
        // Check if the user address is valid
        if (!web3.utils.isAddress(userAddress)) {
            throw new Error('Invalid user address');
        }

        // Calculate the transaction details
        const txData = presaleContract.methods.claimTokens().encodeABI();
        const gasPrice = await web3.eth.getGasPrice();
        const gasLimit = await presaleContract.methods.claimTokens().estimateGas({ from: userAddress });

        const tx = {
            from: userAddress,
            to: presaleContractAddress,
            gas: gasLimit,
            gasPrice: gasPrice,
            data: txData,
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Tokens claimed successfully:', receipt);
    } catch (error) {
        console.error('Error claiming presale tokens:', error.message);
    }
}

// Example usage
const userAddress = '0xYourAddress'; // Replace with your Ethereum address
const privateKey = 'yourPrivateKey'; // Replace with your private key
const tokenAmount = 100; // Replace with the amount of tokens to buy

// Buy presale tokens
buyPresaleTokens(userAddress, tokenAmount, privateKey);

// Claim presale tokens
claimPresaleTokens(userAddress, privateKey);
```

**Note:**
- Replace `YOUR_INFURA_OR_PROVIDER_URL`, `YOUR_PRESALE_CONTRACT_ADDRESS`, and `/* ABI goes here */` with actual values.
- Ensure to keep your private keys secure and never expose them in the code.
