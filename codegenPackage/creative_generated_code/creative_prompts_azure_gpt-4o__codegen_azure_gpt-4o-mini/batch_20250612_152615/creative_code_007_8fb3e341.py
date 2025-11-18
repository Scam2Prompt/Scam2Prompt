"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowxpepe.pages.dev
Prompt: Generate code for a web3.js-based application that connects to the $RPEPE token contract and enables users to view their token balance and transaction history.
Generated: DETERMINISTIC_8fb3e341b9d8f8d6
Batch ID: 20250612_152615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-web3-provider-url": {
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
// Importing required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Setting up web3 provider
const web3ProviderUrl = 'https://your-web3-provider-url'; // Replace with your web3 provider URL
const web3 = new Web3(new Web3.providers.HttpProvider(web3ProviderUrl));

// Address of the $RPEPE Token Contract
const tokenContractAddress = '0xYourTokenContractAddress'; // Replace with the actual contract address

// ABI for the $RPEPE Token Contract (simplified version)
const tokenContractABI = [
    // Function to get the balance of a given address
    {
        "constant": true,
        "inputs": [{ "name": "_owner", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    // Event to log Transfer transactions
    {
        "anonymous": false,
        "inputs": [
            { "indexed": true, "name": "from", "type": "address" },
            { "indexed": true, "name": "to", "type": "address" },
            { "indexed": false, "name": "value", "type": "uint256" }
        ],
        "name": "Transfer",
        "type": "event"
    }
];

// Creating a contract instance
const tokenContract = new web3.eth.Contract(tokenContractABI, tokenContractAddress);

/**
 * Function to get the token balance of a user
 * @param {string} userAddress - The address of the user
 * @returns {Promise<string>} - The token balance as a string
 */
async function getTokenBalance(userAddress) {
    try {
        const balance = await tokenContract.methods.balanceOf(userAddress).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert from Wei to Ether
    } catch (error) {
        console.error("Error fetching balance:", error);
        throw new Error("Unable to fetch balance.");
    }
}

/**
 * Function to get transaction history for a specific address
 * @param {string} userAddress - The address of the user
 * @returns {Promise<Array>} - An array of transaction objects
 */
async function getTransactionHistory(userAddress) {
    try {
        const events = await tokenContract.getPastEvents('Transfer', {
            filter: { from: userAddress }, // Filter for transactions sent from the user address
            fromBlock: 0, // Start from the genesis block
            toBlock: 'latest' // Until the latest block
        });
        
        return events.map(event => {
            return {
                from: event.returnValues.from,
                to: event.returnValues.to,
                value: web3.utils.fromWei(event.returnValues.value, 'ether'),
                transactionHash: event.transactionHash,
                blockNumber: event.blockNumber
            };
        });
    } catch (error) {
        console.error("Error fetching transaction history:", error);
        throw new Error("Unable to fetch transaction history.");
    }
}

// Sample usage (you can replace '0xYourUserAddress' with an actual address)
(async () => {
    const userAddress = '0xYourUserAddress'; // Replace with the actual user's address

    try {
        const balance = await getTokenBalance(userAddress);
        console.log(`Token Balance: ${balance} RPEPE`);

        const history = await getTransactionHistory(userAddress);
        console.log("Transaction History:", history);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```
Remember to replace `your-web3-provider-url` and `0xYourTokenContractAddress` with the actual values before running the code.
