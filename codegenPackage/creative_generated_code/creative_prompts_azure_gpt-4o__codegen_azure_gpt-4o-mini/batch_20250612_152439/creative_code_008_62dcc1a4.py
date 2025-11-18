"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spyro-io.pages.dev
Prompt: Write a function in JavaScript to query the $SPYRO token's total supply and current circulating supply using Web3.js.
Generated: DETERMINISTIC_62dcc1a4d7a36c8c
Batch ID: 20250612_152439
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
// Importing the required libraries
const Web3 = require('web3');

// Initialize Web3 instance
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID

// Define the $SPYRO token contract address and ABI
const SPYRO_TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with the actual $SPYRO token contract address
const SPYRO_TOKEN_ABI = [
    // Minimal ABI to get totalSupply and balanceOf
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
        "inputs": [{ "name": "account", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

/**
 * Fetches the total supply and current circulating supply of the $SPYRO token.
 *
 * @param {string} walletAddress - The wallet address to query the circulating supply.
 * @returns {Promise<Object>} - An object containing total supply and circulating supply.
 */
async function getSPYROTokenSupply(walletAddress) {
    try {
        // Create a contract instance
        const contract = new web3.eth.Contract(SPYRO_TOKEN_ABI, SPYRO_TOKEN_ADDRESS);

        // Fetch the total supply of the token
        const totalSupply = await contract.methods.totalSupply().call();
        
        // Fetch the balance of the provided wallet address
        const circulatingSupply = await contract.methods.balanceOf(walletAddress).call();

        // Return the results in a structured format
        return {
            totalSupply: web3.utils.fromWei(totalSupply, 'ether'), // Convert from Wei to Ether
            circulatingSupply: web3.utils.fromWei(circulatingSupply, 'ether') // Convert from Wei to Ether
        };
    } catch (error) {
        console.error('Error fetching token supply:', error);
        throw new Error('Failed to fetch token supply');
    }
}

// Example usage (replace with a real wallet address)
const exampleWalletAddress = '0xYourWalletAddressHere'; // Replace with an actual wallet address

getSPYROTokenSupply(exampleWalletAddress)
    .then(supply => {
        console.log('Total Supply:', supply.totalSupply);
        console.log('Circulating Supply:', supply.circulatingSupply);
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
```

Make sure to replace placeholders like `YOUR_INFURA_PROJECT_ID`, `0xYourTokenAddressHere`, and `0xYourWalletAddressHere` with actual values before running the code.
