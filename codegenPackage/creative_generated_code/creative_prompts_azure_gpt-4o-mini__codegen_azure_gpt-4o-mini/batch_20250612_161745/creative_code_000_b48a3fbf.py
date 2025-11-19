"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Generate a code snippet to interact with the Mello Token smart contract on Binance Smart Chain using Web3.js.
Generated: DETERMINISTIC_b48a3fbff1fe8ce0
Batch ID: 20250612_161745
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
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
// Import the required libraries
const Web3 = require('web3');

// Connect to the Binance Smart Chain (BSC) mainnet
const web3 = new Web3(new Web3.providers.HttpProvider('https://bsc-dataseed.binance.org/'));

// Mello Token smart contract address (replace with the actual contract address)
const melloTokenAddress = '0xYourMelloTokenContractAddress';

// ABI for the Mello Token smart contract (replace with the actual ABI)
const melloTokenABI = [
    // Add the necessary function signatures that you want to interact with
    // Example:
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

// Create a contract instance
const melloTokenContract = new web3.eth.Contract(melloTokenABI, melloTokenAddress);

// Function to fetch total supply of Mello Tokens
async function getTotalSupply() {
    try {
        const totalSupply = await melloTokenContract.methods.totalSupply().call();
        console.log(`Total Supply of Mello Tokens: ${totalSupply}`);
    } catch (error) {
        console.error('Error fetching total supply:', error);
    }
}

// Function to fetch balance of a given address
async function getBalance(address) {
    if (!web3.utils.isAddress(address)) {
        console.error('Invalid address provided.');
        return;
    }

    try {
        const balance = await melloTokenContract.methods.balanceOf(address).call();
        console.log(`Balance of ${address}: ${balance}`);
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Example usage
(async () => {
    await getTotalSupply();
    // Replace with a valid wallet address to check balance
    await getBalance('0xYourWalletAddress');
})();
```
