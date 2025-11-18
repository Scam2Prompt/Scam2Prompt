"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy.pages.dev
Prompt: Provide an example of using Web3.js to query Beefy Finance vault details, including APY, total deposits, and rewards.
Generated: DETERMINISTIC_9f7a1ec9ef35d406
Batch ID: 20250612_150342
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
// Importing required libraries
const Web3 = require('web3');
const axios = require('axios');

// Setting up the Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://bsc-dataseed.binance.org/'));

// Beefy Finance Vault Contract ABI (simplified for demonstration)
const vaultABI = [
    // Only the relevant functions
    {
        "constant": true,
        "inputs": [],
        "name": "getDepositedAmount",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "getAPY",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "getRewardToken",
        "outputs": [{ "name": "", "type": "address" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
];

// Beefy Finance Vault Address (replace with actual vault address)
const vaultAddress = '0x...'; // Example vault address

/**
 * Fetch vault details including APY, total deposits, and rewards token
 */
async function fetchVaultDetails() {
    try {
        // Creating a contract instance
        const vaultContract = new web3.eth.Contract(vaultABI, vaultAddress);

        // Fetching vault details
        const totalDeposits = await vaultContract.methods.getDepositedAmount().call();
        const apy = await vaultContract.methods.getAPY().call();
        const rewardTokenAddress = await vaultContract.methods.getRewardToken().call();

        // Logging the details
        console.log(`Total Deposits: ${web3.utils.fromWei(totalDeposits, 'ether')} BNB`);
        console.log(`APY: ${apy / 1e18}%`); // Assuming APY is returned in wei
        console.log(`Reward Token Address: ${rewardTokenAddress}`);
        
    } catch (error) {
        console.error('Error fetching vault details:', error.message);
    }
}

// Execute the function to fetch vault details
fetchVaultDetails();
```
