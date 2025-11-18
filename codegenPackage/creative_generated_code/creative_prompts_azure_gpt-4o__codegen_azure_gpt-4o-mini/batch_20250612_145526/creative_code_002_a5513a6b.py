"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catcoinhq.com
Prompt: Generate code in JavaScript to interact with the Catcoin token on Binance Smart Chain (BSC) using Web3.js, including retrieving the total supply and circulating supply.
Generated: DETERMINISTIC_a5513a6bb7e06d5e
Batch ID: 20250612_145526
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
// Import the Web3 library to interact with the Ethereum blockchain
const Web3 = require('web3');

// Initialize a Web3 instance connected to the Binance Smart Chain (BSC) mainnet
const web3 = new Web3('https://bsc-dataseed.binance.org/');

// The contract address of the Catcoin token on the Binance Smart Chain
const catcoinAddress = '0xYourCatcoinTokenAddress'; // Replace with the actual contract address

// The ABI (Application Binary Interface) of the Catcoin token contract
const catcoinABI = [
    // Only including the functions we need for this example
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "circulatingSupply", // Adjust according to the actual function name in the contract
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

// Create a contract instance to interact with the Catcoin token
const catcoinContract = new web3.eth.Contract(catcoinABI, catcoinAddress);

/**
 * Function to retrieve total supply and circulating supply of Catcoin token
 */
async function getCatcoinSupply() {
    try {
        // Fetch total supply from the contract
        const totalSupply = await catcoinContract.methods.totalSupply().call();

        // Fetch circulating supply from the contract
        const circulatingSupply = await catcoinContract.methods.circulatingSupply().call();

        // Log the results in a readable format
        console.log(`Total Supply: ${web3.utils.fromWei(totalSupply, 'ether')} Catcoins`);
        console.log(`Circulating Supply: ${web3.utils.fromWei(circulatingSupply, 'ether')} Catcoins`);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching Catcoin supply:', error);
    }
}

// Execute the function to retrieve and display the supplies
getCatcoinSupply();
```

Make sure to replace `'0xYourCatcoinTokenAddress'` and the ABI method for circulating supply with the actual values based on the Catcoin token contract.
