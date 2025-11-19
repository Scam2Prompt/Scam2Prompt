"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-custody.pages.dev
Prompt: Create a JavaScript function that allows users to unstake their $OPEN and $OCP tokens from the Open Custody Protocol.
Generated: DETERMINISTIC_866322ae1b4877fb
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function unstakeTokens
 * @description Allows users to unstake their $OPEN and $OCP tokens from the Open Custody Protocol.
 * @param {string} userAddress - The address of the user requesting to unstake tokens.
 * @param {number} amountOpen - The amount of $OPEN tokens to unstake.
 * @param {number} amountOcp - The amount of $OCP tokens to unstake.
 * @param {Object} contract - The contract instance of the Open Custody Protocol.
 * @returns {Promise<Object>} Result of the unstaking transaction.
 * @throws Will throw an error if the unstaking fails or if inputs are invalid.
 */
async function unstakeTokens(userAddress, amountOpen, amountOcp, contract) {
    // Validate inputs
    if (!userAddress || !amountOpen || !amountOcp || !contract) {
        throw new Error("Invalid arguments: userAddress, amountOpen, amountOcp, and contract are required.");
    }

    // Ensure amounts are positive numbers
    if (amountOpen <= 0 || amountOcp <= 0) {
        throw new Error("Invalid amounts: both amounts must be greater than zero.");
    }

    try {
        // Execute the unstaking transaction for $OPEN tokens
        const openTransaction = await contract.methods.unstakeOpen(amountOpen).send({ from: userAddress });
        console.log(`Successfully unstaked ${amountOpen} $OPEN tokens. Transaction Hash: ${openTransaction.transactionHash}`);

        // Execute the unstaking transaction for $OCP tokens
        const ocpTransaction = await contract.methods.unstakeOcp(amountOcp).send({ from: userAddress });
        console.log(`Successfully unstaked ${amountOcp} $OCP tokens. Transaction Hash: ${ocpTransaction.transactionHash}`);

        // Return the results of both transactions
        return {
            openTransaction: openTransaction,
            ocpTransaction: ocpTransaction,
        };
    } catch (error) {
        // Handle any errors that occurred during the unstaking process
        console.error("Error unstaking tokens:", error);
        throw new Error("Unstaking failed: " + error.message);
    }
}
```
