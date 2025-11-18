"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feg-chain.pages.dev
Prompt: Provide code examples for integrating the FEG Aggregator/Router functionality into a decentralized application (dApp) to source the most affordable token trading rates across multiple DEXs.
Generated: DETERMINISTIC_10bde711643e9f67
Batch ID: 20250612_152249
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
const axios = require('axios');

// Initialize Web3 and set up the provider (Infura, Alchemy, etc.)
const web3 = new Web3(new Web3.providers.HttpProvider('YOUR_INFURA_OR_ALCHEMY_URL'));

// Define the FEG Aggregator/Router smart contract ABI and address
const FEG_ROUTER_ABI = [
    // Add the necessary ABI parts required for the functions you are using
];

const FEG_ROUTER_ADDRESS = 'YOUR_FEG_ROUTER_CONTRACT_ADDRESS';

// Create a contract instance
const fegRouterContract = new web3.eth.Contract(FEG_ROUTER_ABI, FEG_ROUTER_ADDRESS);

/**
 * Fetch the best trading rate for a token pair across multiple DEXs
 * @param {string} fromToken - The address of the token to sell
 * @param {string} toToken - The address of the token to buy
 * @param {number} amountIn - The amount of the fromToken to trade
 * @returns {Object} - The best rate and DEX details
 */
async function getBestTradingRate(fromToken, toToken, amountIn) {
    try {
        // Call the FEG router to get the best price
        const rate = await fegRouterContract.methods.getBestRate(fromToken, toToken, amountIn).call();
        return {
            rate: rate[0], // Assuming the first element is the best rate
            dex: rate[1], // Assuming the second element is the DEX identifier
        };
    } catch (error) {
        console.error("Error fetching the best trading rate:", error);
        throw new Error("Failed to fetch trading rate.");
    }
}

/**
 * Execute a trade on the FEG router
 * @param {string} fromToken - The address of the token to sell
 * @param {string} toToken - The address of the token to buy
 * @param {number} amountIn - The amount of the fromToken to trade
 * @param {string} to - The recipient address
 * @param {string} privateKey - The private key of the sender
 * @returns {string} - The transaction hash
 */
async function executeTrade(fromToken, toToken, amountIn, to, privateKey) {
    try {
        const account = web3.eth.accounts.privateKeyToAccount(privateKey);
        web3.eth.accounts.wallet.add(account);
        const nonce = await web3.eth.getTransactionCount(account.address);

        // Create the transaction
        const tx = {
            from: account.address,
            to: FEG_ROUTER_ADDRESS,
            value: '0', // Set to '0' if not sending ETH
            gas: 2000000,
            nonce: nonce,
            data: fegRouterContract.methods.swapTokens(fromToken, toToken, amountIn, to).encodeABI(),
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        return receipt.transactionHash;
    } catch (error) {
        console.error("Error executing trade:", error);
        throw new Error("Trade execution failed.");
    }
}

// Example usage
(async () => {
    const fromToken = 'TOKEN_ADDRESS_1'; // Replace with actual token address
    const toToken = 'TOKEN_ADDRESS_2'; // Replace with actual token address
    const amountIn = web3.utils.toWei('1', 'ether'); // Amount to trade (1 Ether in this case)
    const recipientAddress = 'RECIPIENT_ADDRESS'; // Replace with recipient address
    const privateKey = 'YOUR_PRIVATE_KEY'; // Replace with actual private key

    try {
        const bestRate = await getBestTradingRate(fromToken, toToken, amountIn);
        console.log("Best Rate:", bestRate);

        const txHash = await executeTrade(fromToken, toToken, amountIn, recipientAddress, privateKey);
        console.log("Trade executed, transaction hash:", txHash);
    } catch (error) {
        console.error("Error in trading process:", error);
    }
})();
```

**Note:** Make sure to replace placeholders like `YOUR_INFURA_OR_ALCHEMY_URL`, `YOUR_FEG_ROUTER_CONTRACT_ADDRESS`, `TOKEN_ADDRESS_1`, `TOKEN_ADDRESS_2`, `RECIPIENT_ADDRESS`, and `YOUR_PRIVATE_KEY` with actual values. Also, ensure that the ABI for `FEG_ROUTER_ABI` includes the necessary methods you will invoke.
