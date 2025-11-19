"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Generate a code snippet for integrating the CRUDO token payment system at gas stations using the Binance Smart Chain (BEP20) network.
Generated: DETERMINISTIC_2a850a094655064d
Batch ID: 20250612_161317
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
const Tx = require('ethereumjs-tx').Transaction;
require('dotenv').config();

// Setting up Web3 provider for Binance Smart Chain (BSC)
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.BSC_NODE_URL));

// BEP20 Token contract address
const tokenAddress = process.env.BEP20_TOKEN_ADDRESS; // Replace with actual token address
const tokenABI = [
    // Minimal ABI required to transfer tokens
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

// Initialize token contract
const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

// Function to transfer CRUDO tokens
async function transferTokens(fromAddress, privateKey, toAddress, amount) {
    try {
        // Convert amount to Wei (1e18 for BEP20)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Get the nonce for the transaction
        const nonce = await web3.eth.getTransactionCount(fromAddress);

        // Create a transaction object
        const txObject = {
            nonce: web3.utils.toHex(nonce),
            gasLimit: web3.utils.toHex(200000), // Set gas limit
            gasPrice: web3.utils.toHex(web3.utils.toWei('5', 'gwei')), // Set gas price
            to: tokenAddress,
            data: tokenContract.methods.transfer(toAddress, amountInWei).encodeABI()
        };

        // Sign the transaction
        const tx = new Tx(txObject, { chain: 'bsc' });
        const privateKeyBuffer = Buffer.from(privateKey, 'hex');
        tx.sign(privateKeyBuffer);

        // Serialize the transaction
        const serializedTx = tx.serialize();
        const raw = '0x' + serializedTx.toString('hex');

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(raw);
        console.log('Transaction successful with hash:', receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transfer failed');
    }
}

// Example usage of the transferTokens function
(async () => {
    const fromAddress = process.env.SENDER_ADDRESS; // Wallet address sending tokens
    const privateKey = process.env.SENDER_PRIVATE_KEY; // Private key of the sender
    const toAddress = process.env.RECEIVER_ADDRESS; // Wallet address receiving tokens
    const amount = 1; // Amount of tokens to send

    try {
        const receipt = await transferTokens(fromAddress, privateKey, toAddress, amount);
        console.log('Transfer receipt:', receipt);
    } catch (error) {
        console.error('Error during token transfer:', error.message);
    }
})();
```

**Note:** Make sure to replace the placeholder environment variables with actual values in your `.env` file:
```
BSC_NODE_URL=<Your_BSC_Node_URL>
BEP20_TOKEN_ADDRESS=<Your_BEP20_Token_Address>
SENDER_ADDRESS=<Your_Sender_Wallet_Address>
SENDER_PRIVATE_KEY=<Your_Sender_Private_Key>
RECEIVER_ADDRESS=<Your_Receiver_Wallet_Address>
```
