"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnice.xyz
Prompt: Write a JavaScript script to interact with Ethereum smart contracts using Web3.js, specifically for DeFi applications.
Generated: DETERMINISTIC_cc8e201c2fda7dfa
Batch ID: 20250612_153527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
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
// Import required packages
const Web3 = require('web3');

// Configuration settings
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura Project ID
const PRIVATE_KEY = 'your-private-key'; // Replace with your Ethereum wallet private key
const CONTRACT_ADDRESS = 'your-contract-address'; // Replace with the deployed smart contract address
const CONTRACT_ABI = [ /* Replace with your contract's ABI */ ]; // ABI of the smart contract

// Initialize Web3 instance with Infura provider
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);

// Initialize the contract instance
const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

// Wallet account address from private key
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.eth.defaultAccount = account.address;

// Function to read data from the smart contract (example: get balance of a token)
async function getTokenBalance(address) {
    try {
        const balance = await contract.methods.balanceOf(address).call();
        console.log(`Balance of ${address}: ${balance}`);
        return balance;
    } catch (error) {
        console.error('Error fetching token balance:', error);
        throw error;
    }
}

// Function to interact with the smart contract (example: transfer tokens)
async function transferTokens(toAddress, amount) {
    try {
        // Construct the transaction
        const tx = contract.methods.transfer(toAddress, amount);
        const gas = await tx.estimateGas({ from: account.address });
        const gasPrice = await web3.eth.getGasPrice();

        const data = tx.encodeABI();
        const nonce = await web3.eth.getTransactionCount(account.address);

        const signedTx = await web3.eth.accounts.signTransaction({
            to: CONTRACT_ADDRESS,
            data,
            gas,
            gasPrice,
            nonce,
            chainId: 1 // Ensure you use the correct chain ID (1 is Ethereum Mainnet)
        }, PRIVATE_KEY);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Transaction successful:', receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error('Error transferring tokens:', error);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        const userAddress = 'user-ethereum-address'; // Replace with the Ethereum address to check balance or transfer to
        await getTokenBalance(userAddress);

        const transferTo = 'recipient-ethereum-address'; // Replace with the recipient's Ethereum address
        const amountToTransfer = '1000000000000000000'; // Example: Transfer 1 token (assuming 18 decimals)
        await transferTokens(transferTo, amountToTransfer);
    } catch (error) {
        console.error('An error occurred during execution:', error);
    }
})();
```

**Note:** Replace placeholder values such as `your-infura-project-id`, `your-private-key`, `your-contract-address`, `your-contract-ABI`, and Ethereum addresses with actual values before running the script. Ensure sensitive information like private keys is securely managed in production environments.
