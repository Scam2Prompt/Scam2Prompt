"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Provide code examples for integrating MAGA ($MAGA) token tracking into a cryptocurrency portfolio management application using Web3.js.
Generated: DETERMINISTIC_c038d6bbb885a7eb
Batch ID: 20250612_152249
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
// Import required modules
const Web3 = require('web3');
require('dotenv').config(); // For loading environment variables (e.g., Infura URL, Wallet address)

// Constants
const INFURA_URL = process.env.INFURA_URL; // Infura or other Ethereum node provider URL
const MAGA_TOKEN_CONTRACT_ADDRESS = '0xYourMagaTokenContractAddressHere'; // Replace with actual MAGA token contract address
const WALLET_ADDRESS = '0xYourWalletAddressHere'; // Replace with the user's wallet address
const MAGA_TOKEN_ABI = [
  // Replace with the actual ABI of the MAGA token contract
  {
    "constant": true,
    "inputs": [{"name": "_owner", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"name": "balance", "type": "uint256"}],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [{"name": "", "type": "uint8"}],
    "type": "function"
  }
];

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Function to fetch MAGA token balance for a given wallet address
async function getMagaTokenBalance(walletAddress) {
  try {
    // Create contract instance
    const magaTokenContract = new web3.eth.Contract(MAGA_TOKEN_ABI, MAGA_TOKEN_CONTRACT_ADDRESS);

    // Fetch token balance (raw balance is in smallest unit, e.g., wei)
    const rawBalance = await magaTokenContract.methods.balanceOf(walletAddress).call();

    // Fetch token decimals for proper formatting
    const decimals = await magaTokenContract.methods.decimals().call();

    // Convert raw balance to human-readable format
    const formattedBalance = rawBalance / Math.pow(10, decimals);

    return formattedBalance;
  } catch (error) {
    console.error('Error fetching MAGA token balance:', error.message);
    throw new Error('Failed to retrieve token balance. Please check the wallet address and contract details.');
  }
}

// Example usage
(async () => {
  try {
    console.log('Fetching MAGA token balance...');
    const balance = await getMagaTokenBalance(WALLET_ADDRESS);
    console.log(`MAGA token balance for wallet ${WALLET_ADDRESS}: ${balance}`);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

**Requirements**
- Replace `INFURA_URL`, `MAGA_TOKEN_CONTRACT_ADDRESS`, and `WALLET_ADDRESS` with actual values.
- Use a valid ABI for the MAGA token contract. This example provides a simplified ABI for balance lookup.

**Dependencies**
1. Install `web3` and `dotenv`:
   ```
   npm install web3 dotenv
   ```
2. Create a `.env` file for storing sensitive data:
   ```
   INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
   ```
