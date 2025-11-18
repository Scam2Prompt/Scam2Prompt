"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-frm-staking.ferrumnetwork.io
Prompt: Generate a JavaScript function to enable staking functionality using Ferrum Network's staking technology for Arbitrum-based assets.
Generated: DETERMINISTIC_089da81389a0fab0
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function enableStaking
 * @description Enables staking functionality for Arbitrum-based assets using Ferrum Network's staking technology.
 * @param {string} assetAddress - The address of the asset to be staked.
 * @param {number} amount - The amount of the asset to stake.
 * @param {string} userAddress - The address of the user who is staking the asset.
 * @param {object} ferrumApi - An instance of the Ferrum Network API for staking operations.
 * @returns {Promise<string>} Transaction hash if staking is successful, otherwise throws an error.
 * @throws {Error} Throws an error if the staking process fails.
 */

async function enableStaking(assetAddress, amount, userAddress, ferrumApi) {
    // Validate inputs
    if (!isValidAddress(assetAddress)) {
        throw new Error('Invalid asset address provided.');
    }
    if (amount <= 0) {
        throw new Error('Amount must be greater than zero.');
    }
    if (!isValidAddress(userAddress)) {
        throw new Error('Invalid user address provided.');
    }

    try {
        // Check if the user has enough balance to stake
        const balance = await ferrumApi.getBalance(userAddress, assetAddress);
        if (balance < amount) {
            throw new Error('Insufficient balance to stake the specified amount.');
        }

        // Initiate the staking transaction
        const transaction = await ferrumApi.stake(assetAddress, amount, userAddress);

        // Wait for the transaction to be confirmed
        const receipt = await ferrumApi.waitForTransaction(transaction.hash);

        if (receipt.status !== 'success') {
            throw new Error('Staking transaction failed.');
        }

        // Return the transaction hash
        return transaction.hash;

    } catch (error) {
        // Log the error for debugging purposes
        console.error('Error enabling staking:', error);
        throw new Error('An error occurred while enabling staking. Please try again later.');
    }
}

/**
 * @function isValidAddress
 * @description Validates if the provided string is a valid Ethereum address.
 * @param {string} address - The address to validate.
 * @returns {boolean} True if valid, otherwise false.
 */
function isValidAddress(address) {
    return /^0x[a-fA-F0-9]{40}$/.test(address);
}
```
