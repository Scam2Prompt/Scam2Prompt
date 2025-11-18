"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Create a script using Web3.js to query and manage collateralized vaults within the QiDao protocol, ensuring the collateral value exceeds the debt amount.
Generated: DETERMINISTIC_6fa8a1eba8a82ffd
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
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
// Load required modules
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up constants
const RPC_URL = 'https://polygon-rpc.com'; // Polygon network RPC endpoint
const VAULT_MANAGER_ADDRESS = '0x1234567890abcdef1234567890abcdef12345678'; // Replace with QiDao Vault Manager address
const VAULT_MANAGER_ABI = [
    // Replace with actual ABI of QiDao Vault Manager contract
    {
        "constant": true,
        "inputs": [{ "name": "_vaultId", "type": "uint256" }],
        "name": "getVaultCollateral",
        "outputs": [{ "name": "", "type": "uint256" }],
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{ "name": "_vaultId", "type": "uint256" }],
        "name": "getVaultDebt",
        "outputs": [{ "name": "", "type": "uint256" }],
        "type": "function"
    }
];

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(RPC_URL));

// Initialize Vault Manager contract
const vaultManager = new web3.eth.Contract(VAULT_MANAGER_ABI, VAULT_MANAGER_ADDRESS);

/**
 * Fetch collateral and debt values for a QiDao vault and check if collateral value exceeds debt amount.
 * @param {number} vaultId - The ID of the vault to query.
 * @returns {Promise<object>} - Returns an object with collateral and debt values, and status.
 */
async function checkVaultStatus(vaultId) {
    try {
        // Fetch collateral value
        const collateral = await vaultManager.methods.getVaultCollateral(vaultId).call();
        // Fetch debt amount
        const debt = await vaultManager.methods.getVaultDebt(vaultId).call();

        // Convert values from Wei to Ether (assuming collateral and debt are in Wei)
        const collateralEth = ethers.utils.formatEther(collateral);
        const debtEth = ethers.utils.formatEther(debt);

        // Check if collateral value exceeds debt amount
        const isSafe = parseFloat(collateralEth) > parseFloat(debtEth);

        // Return an object with details
        return {
            vaultId,
            collateral: collateralEth,
            debt: debtEth,
            isSafe
        };
    } catch (error) {
        // Handle errors gracefully
        console.error(`Error fetching vault data for ID ${vaultId}:`, error.message);
        throw new Error('Failed to fetch vault data');
    }
}

/**
 * Main function to query vaults and log their statuses.
 */
async function main() {
    try {
        const vaultId = 1; // Replace with the vault ID you want to query
        const vaultStatus = await checkVaultStatus(vaultId);

        console.log(`Vault ID: ${vaultStatus.vaultId}`);
        console.log(`Collateral: ${vaultStatus.collateral} ETH`);
        console.log(`Debt: ${vaultStatus.debt} ETH`);
        console.log(`Status: ${vaultStatus.isSafe ? 'Safe' : 'Unsafe'}`);
    } catch (error) {
        console.error('Error in main function:', error.message);
    }
}

// Execute the script
main();
```
