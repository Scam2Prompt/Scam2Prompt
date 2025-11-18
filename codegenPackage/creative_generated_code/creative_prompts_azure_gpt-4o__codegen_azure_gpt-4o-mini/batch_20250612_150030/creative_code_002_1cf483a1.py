"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Create a JavaScript script using web3.js to check the balance of USDC tokens in a given Ethereum wallet address.
Generated: DETERMINISTIC_1cf483a1887e7a9b
Batch ID: 20250612_150030
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
// Import the required libraries
const Web3 = require('web3');
const BigNumber = require('bignumber.js');

// Set up the provider for the Ethereum network (e.g., Infura or local node)
const providerURL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
const web3 = new Web3(new Web3.providers.HttpProvider(providerURL));

// USDC Token Contract Address on Ethereum Mainnet
const usdcAddress = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48';

// ERC20 Token ABI (simplified for balanceOf function)
const usdcAbi = [
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

// Create a contract instance
const usdcContract = new web3.eth.Contract(usdcAbi, usdcAddress);

/**
 * Function to get USDC balance of a given Ethereum wallet address
 * @param {string} walletAddress - The Ethereum wallet address to check
 * @returns {Promise<string>} - The USDC balance in the wallet
 */
async function getUSDCBalance(walletAddress) {
    try {
        // Validate the Ethereum address
        if (!web3.utils.isAddress(walletAddress)) {
            throw new Error('Invalid Ethereum address');
        }

        // Call the balanceOf function from the USDC contract
        const balance = await usdcContract.methods.balanceOf(walletAddress).call();

        // Convert the balance from Wei to USDC (USDC has 6 decimals)
        const balanceInUSDC = new BigNumber(balance).dividedBy(10 ** 6).toString();
        return balanceInUSDC;
    } catch (error) {
        console.error('Error fetching USDC balance:', error.message);
        throw error; // Rethrow the error after logging
    }
}

// Example usage: replace with a valid Ethereum wallet address
const walletAddress = '0xYourEthereumWalletAddressHere';
getUSDCBalance(walletAddress)
    .then(balance => {
        console.log(`USDC Balance: ${balance}`);
    })
    .catch(error => {
        console.error('Failed to retrieve balance:', error.message);
    });
```
