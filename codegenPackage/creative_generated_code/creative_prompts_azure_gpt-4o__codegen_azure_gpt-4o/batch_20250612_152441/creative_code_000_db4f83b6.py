"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signetfaucet14.pages.dev
Prompt: Write a script using Web3.js to interact with the Signet Faucet on the Babylon Chain and claim a specified amount within the range of 0.00001 to 0.1.
Generated: DETERMINISTIC_db4f83b6521f0449
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to interact with the Signet Faucet on the Babylon Chain using Web3.js
 * and claim a specified amount within the range of 0.00001 to 0.1.
 * 
 * Ensure you have Web3.js installed (`npm install web3`) and the Babylon Chain faucet contract address and ABI.
 * Replace placeholders with actual values specific to your setup.
 */

const Web3 = require('web3');
require('dotenv').config(); // For managing sensitive data like private keys securely

// Environment variables (replace with actual values or set in .env file)
const RPC_URL = process.env.RPC_URL || '<YOUR_RPC_URL>'; // Babylon Chain RPC URL
const FAUCET_CONTRACT_ADDRESS = process.env.FAUCET_CONTRACT_ADDRESS || '<FAUCET_CONTRACT_ADDRESS>';
const PRIVATE_KEY = process.env.PRIVATE_KEY || '<YOUR_PRIVATE_KEY>'; // Wallet private key for signing transactions
const CLAIM_AMOUNT = parseFloat(process.env.CLAIM_AMOUNT || '0.01'); // Amount to claim (default 0.01)

// Check if claim amount is within the valid range
if (CLAIM_AMOUNT < 0.00001 || CLAIM_AMOUNT > 0.1) {
    console.error('Error: Claim amount must be between 0.00001 and 0.1.');
    process.exit(1);
}

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(RPC_URL));

// Faucet contract ABI (replace with actual ABI of the faucet contract)
const FAUCET_CONTRACT_ABI = [
    // Example ABI structure (replace with actual ABI)
    {
        "constant": true,
        "inputs": [],
        "name": "claimTokens",
        "outputs": [],
        "type": "function"
    }
];

// Initialize contract instance
const faucetContract = new web3.eth.Contract(FAUCET_CONTRACT_ABI, FAUCET_CONTRACT_ADDRESS);

async function claimTokens() {
    try {
        // Get wallet address from private key
        const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
        const walletAddress = account.address;

        console.log(`Claiming ${CLAIM_AMOUNT} tokens to wallet address: ${walletAddress}`);

        // Calculate transaction data
        const data = faucetContract.methods.claimTokens(web3.utils.toWei(CLAIM_AMOUNT.toString(), 'ether')).encodeABI();

        // Get current gas price
        const gasPrice = await web3.eth.getGasPrice();

        // Estimate gas for the transaction
        const gas = await faucetContract.methods.claimTokens(web3.utils.toWei(CLAIM_AMOUNT.toString(), 'ether')).estimateGas({ from: walletAddress });

        // Build transaction
        const tx = {
            to: FAUCET_CONTRACT_ADDRESS,
            data: data,
            gas: gas,
            gasPrice: gasPrice,
        };

        // Sign transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

        // Send transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        console.log('Transaction successful!', receipt);
    } catch (error) {
        console.error('Error claiming tokens:', error.message);
    }
}

// Execute the claimTokens function
claimTokens();
```

**Note:** Replace placeholders like `<YOUR_RPC_URL>`, `<FAUCET_CONTRACT_ADDRESS>`, and the ABI structure with actual values specific to your Babylon Chain configuration. Install Web3.js (`npm install web3`) and configure `.env` file for environment variables (`npm install dotenv`).
