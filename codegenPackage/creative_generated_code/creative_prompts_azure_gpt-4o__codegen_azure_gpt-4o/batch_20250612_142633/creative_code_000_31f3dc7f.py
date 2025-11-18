"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-06.vip
Prompt: Write JavaScript code to interact with Ethereum-based DeFi protocols using Web3.js, ensuring compatibility with platforms that require JavaScript-enabled environments.
Generated: DETERMINISTIC_31f3dc7f6c8da7a2
Batch ID: 20250612_142633
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
const Web3 = require('web3');

// Connect to an Ethereum node (e.g., Infura or Alchemy RPC URL)
const web3 = new Web3("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID");

// Contract ABI (simplified example for an ERC20 token)
const erc20Abi = [
    {
        "constant": true,
        "inputs": [{ "name": "_owner", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "balance", "type": "uint256" }],
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            { "name": "_to", "type": "address" },
            { "name": "_value", "type": "uint256" }
        ],
        "name": "transfer",
        "outputs": [{ "name": "success", "type": "bool" }],
        "type": "function"
    }
];

// Example ERC20 token contract address (e.g., DAI Token)
const tokenAddress = "0x6B175474E89094C44Da98b954EedeAC495271d0F";

// User's wallet address (replace with your address)
const userAddress = "0xYourWalletAddress";

// Private key for signing transactions (ensure this is kept secure in production)
const privateKey = "0xYourPrivateKey";

// Initialize the contract instance
const tokenContract = new web3.eth.Contract(erc20Abi, tokenAddress);

/**
 * Get the balance of a given address
 */
async function getTokenBalance(address) {
    try {
        const balance = await tokenContract.methods.balanceOf(address).call();
        console.log(`Balance of address ${address}:`, web3.utils.fromWei(balance, 'ether'), 'Tokens');
        return balance;
    } catch (error) {
        console.error("Error fetching token balance:", error.message);
        throw error;
    }
}

/**
 * Transfer tokens to another address
 */
async function transferTokens(toAddress, amountInEther) {
    try {
        const amount = web3.utils.toWei(amountInEther, 'ether');

        // Construct the transaction data
        const txData = tokenContract.methods.transfer(toAddress, amount).encodeABI();

        // Get the current gas price
        const gasPrice = await web3.eth.getGasPrice();

        // Get the transaction count (nonce) for the sender
        const nonce = await web3.eth.getTransactionCount(userAddress);

        // Create the raw transaction object
        const rawTx = {
            to: tokenAddress,
            data: txData,
            gasPrice,
            gas: 200000, // Estimate appropriate gas limit for the transaction
            nonce,
            value: '0x0', // No Ether is being sent, only tokens
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(rawTx, privateKey);

        // Send the signed transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log("Transaction successful with hash:", receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error("Error transferring tokens:", error.message);
        throw error;
    }
}

/**
 * Main function: Example usage
 */
async function main() {
    try {
        // Fetch the balance of the user
        await getTokenBalance(userAddress);

        // Example token transfer (1 DAI to another address)
        const recipientAddress = "0xRecipientWalletAddress";
        const amountToSend = "1"; // 1 DAI
        await transferTokens(recipientAddress, amountToSend);

        // Fetch the updated balance
        await getTokenBalance(userAddress);
    } catch (error) {
        console.error("An error occurred during the process:", error.message);
    }
}

// Execute the script
main();
```
