"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiethereum.com
Prompt: Provide an example of how to use Web3.js to interact with an Ethereum smart contract for a DeFi project.
Generated: DETERMINISTIC_2f3dd4c081be577b
Batch ID: 20250612_135940
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

// Connect to an Ethereum provider (e.g., Infura, Alchemy, or local node)
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// The contract's ABI (replace with the actual ABI of the smart contract)
const contractABI = [
    // Example ABI snippet for an ERC20 token contract
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [{ "name": "", "type": "string" }],
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [{ "name": "", "type": "string" }],
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [{ "name": "", "type": "uint8" }],
        "type": "function"
    },
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
        "outputs": [{ "name": "", "type": "bool" }],
        "type": "function"
    }
];

// The smart contract's address (replace with the actual address of the DeFi smart contract)
const contractAddress = '0xYourContractAddressHere';

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Function to get token details (name, symbol, decimals)
 * Useful for interacting with ERC20 tokens in DeFi projects
 */
async function getTokenDetails() {
    try {
        const name = await contract.methods.name().call();
        const symbol = await contract.methods.symbol().call();
        const decimals = await contract.methods.decimals().call();
        console.log(`Token Name: ${name}`);
        console.log(`Token Symbol: ${symbol}`);
        console.log(`Token Decimals: ${decimals}`);
    } catch (error) {
        console.error('Error fetching token details:', error);
    }
}

/**
 * Function to get the token balance of a specific address
 * @param {string} userAddress - Ethereum address of the user
 */
async function getTokenBalance(userAddress) {
    try {
        const balance = await contract.methods.balanceOf(userAddress).call();
        const decimals = await contract.methods.decimals().call();
        const formattedBalance = balance / (10 ** decimals); // Adjust for token decimals
        console.log(`Balance of ${userAddress}: ${formattedBalance}`);
    } catch (error) {
        console.error('Error fetching token balance:', error);
    }
}

/**
 * Function to transfer tokens from the connected wallet to a recipient
 * @param {string} senderAddress - Ethereum address of the sender
 * @param {string} privateKey - Private key of the sender's wallet
 * @param {string} recipientAddress - Ethereum address of the recipient
 * @param {number} amount - Amount of tokens to transfer (adjusted for decimals)
 */
async function transferTokens(senderAddress, privateKey, recipientAddress, amount) {
    try {
        const decimals = await contract.methods.decimals().call();
        const rawAmount = amount * (10 ** decimals); // Adjust for token decimals

        // Create the transaction
        const txData = contract.methods.transfer(recipientAddress, rawAmount).encodeABI();
        const tx = {
            to: contractAddress,
            data: txData,
            gas: 2000000, // Gas limit (adjust based on contract complexity)
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Transaction successful:', receipt.transactionHash);
    } catch (error) {
        console.error('Error transferring tokens:', error);
    }
}

// Example usage:
// Replace with appropriate addresses, private key, and token amounts
const userAddress = '0xYourEthereumAddressHere';
const privateKey = 'YourPrivateKeyHere'; // WARNING: Do not expose private keys in production
const recipientAddress = '0xRecipientAddressHere';
const transferAmount = 10; // Transfer 10 tokens

// Get token details
getTokenDetails();

// Get token balance of the user
getTokenBalance(userAddress);

// Transfer tokens to the recipient
transferTokens(userAddress, privateKey, recipientAddress, transferAmount);
```
