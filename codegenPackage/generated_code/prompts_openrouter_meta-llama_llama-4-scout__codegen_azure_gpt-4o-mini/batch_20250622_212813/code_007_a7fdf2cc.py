"""
Generated Code Metadata:
========================
Original URL: https://satyloud.io
Prompt: Create a JavaScript function to check if a Solana wallet is eligible for the Initial Attention Offering whitelist on Loud, using the provided eligibility criteria.
Generated: DETERMINISTIC_a7fdf2cc1bcc54d8
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if a Solana wallet is eligible for the Initial Attention Offering (IAO) whitelist on Loud.
 * 
 * @param {string} walletAddress - The Solana wallet address to check.
 * @param {Object} eligibilityCriteria - The criteria for eligibility.
 * @param {number} eligibilityCriteria.minBalance - The minimum balance required in the wallet.
 * @param {number} eligibilityCriteria.minTransactions - The minimum number of transactions required.
 * @param {Function} getWalletInfo - A function that retrieves wallet information, including balance and transaction count.
 * @returns {Promise<boolean>} - Returns true if the wallet is eligible, false otherwise.
 * @throws {Error} - Throws an error if the wallet address is invalid or if there is an issue retrieving wallet information.
 */
async function isWalletEligibleForIAO(walletAddress, eligibilityCriteria, getWalletInfo) {
    // Validate the wallet address format
    if (!/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(walletAddress)) {
        throw new Error('Invalid wallet address format.');
    }

    try {
        // Retrieve wallet information
        const walletInfo = await getWalletInfo(walletAddress);

        // Check if walletInfo is valid
        if (!walletInfo || typeof walletInfo.balance !== 'number' || typeof walletInfo.transactionCount !== 'number') {
            throw new Error('Invalid wallet information retrieved.');
        }

        // Check eligibility based on criteria
        const isEligible = walletInfo.balance >= eligibilityCriteria.minBalance &&
                           walletInfo.transactionCount >= eligibilityCriteria.minTransactions;

        return isEligible;
    } catch (error) {
        // Handle errors that may occur during the wallet info retrieval
        console.error('Error checking wallet eligibility:', error);
        throw new Error('Failed to check wallet eligibility. Please try again later.');
    }
}

// Example usage (assuming getWalletInfo is defined elsewhere):
// const eligibilityCriteria = { minBalance: 1.5, minTransactions: 10 };
// isWalletEligibleForIAO('YourWalletAddressHere', eligibilityCriteria, getWalletInfo)
//     .then(isEligible => console.log('Is eligible:', isEligible))
//     .catch(error => console.error('Eligibility check failed:', error.message));
```
