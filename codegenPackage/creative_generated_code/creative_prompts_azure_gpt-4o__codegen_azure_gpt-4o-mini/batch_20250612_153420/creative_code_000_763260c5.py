"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfa-ai.pages.dev
Prompt: Write a script to interact with the $NFAI V2 contract at address `0x17c5...20d9` to perform a 1:1 token swap for $NFAI V1 tokens using Web3.js.
Generated: DETERMINISTIC_763260c596c14494
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const { abi: NFAIV2_ABI } = require('./NFAI_V2_ABI.json'); // Replace with actual ABI file path
const { abi: NFAIV1_ABI } = require('./NFAI_V1_ABI.json'); // Replace with actual ABI file path

// Define constants
const NFAI_V2_ADDRESS = '0x17c5...20d9'; // Replace with the actual NFAI V2 contract address
const NFAI_V1_ADDRESS = 'YOUR_NFAI_V1_CONTRACT_ADDRESS'; // Replace with actual NFAI V1 contract address
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with the private key of the wallet
const INFURA_URL = 'YOUR_INFURA_URL'; // Replace with your Infura or Alchemy URL

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Create a function to perform the token swap
async function swapTokens(amount) {
    try {
        // Validate input amount
        if (amount <= 0) {
            throw new Error('Amount must be greater than zero');
        }

        // Create account from private key
        const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
        web3.eth.accounts.wallet.add(account);
        web3.eth.defaultAccount = account.address;

        // Create contract instances
        const nfaiv2 = new web3.eth.Contract(NFAIV2_ABI, NFAI_V2_ADDRESS);
        const nfaiv1 = new web3.eth.Contract(NFAIV1_ABI, NFAI_V1_ADDRESS);

        // Check allowance (if necessary, depending on token implementation)
        const allowance = await nfaiv1.methods.allowance(account.address, NFAI_V2_ADDRESS).call();
        if (allowance < amount) {
            // If not enough allowance, approve the transfer
            await nfaiv1.methods.approve(NFAI_V2_ADDRESS, amount).send({ from: account.address });
        }

        // Execute the token swap
        const swapTx = await nfaiv2.methods.swap(amount).send({ from: account.address });
        console.log('Swap transaction successful:', swapTx.transactionHash);
        
    } catch (error) {
        console.error('Error during token swap:', error.message);
    }
}

// Example usage of the swapTokens function
const amountToSwap = web3.utils.toWei('1', 'ether'); // Amount to swap, in this case, 1 token
swapTokens(amountToSwap);
```

Make sure to replace placeholder values (such as private key, Infura URL, and contract ABI paths) with actual data before running the script. Additionally, ensure that the `swap` method in the NFAI V2 contract is correctly defined in the ABI and matches your swapping logic.
