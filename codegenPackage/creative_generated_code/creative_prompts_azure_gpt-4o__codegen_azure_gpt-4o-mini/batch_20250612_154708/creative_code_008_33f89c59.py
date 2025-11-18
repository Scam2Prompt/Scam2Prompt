"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alienbasse.org
Prompt: Develop a function to programmatically set slippage tolerance for swaps on Alien Base, ensuring accurate trade execution.
Generated: DETERMINISTIC_33f89c594b7437bc
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to set slippage tolerance for swaps on Alien Base
 * @param {number} slippage - The desired slippage percentage (0 to 100)
 * @param {string} userAddress - The wallet address of the user
 * @param {object} contractInstance - Instance of the smart contract for swaps
 * @returns {Promise<boolean>} - Returns true if slippage is set successfully, otherwise false
 * @throws {Error} - Throws an error if the input parameters are invalid or if the transaction fails
 */
async function setSlippageTolerance(slippage, userAddress, contractInstance) {
    // Validate input parameters
    if (typeof slippage !== 'number' || slippage < 0 || slippage > 100) {
        throw new Error('Invalid slippage percentage. It must be a number between 0 and 100.');
    }
    if (typeof userAddress !== 'string' || !/^0x[a-fA-F0-9]{40}$/.test(userAddress)) {
        throw new Error('Invalid user address. It must be a valid Ethereum address.');
    }
    if (!contractInstance || typeof contractInstance.methods !== 'object') {
        throw new Error('Invalid contract instance provided.');
    }

    try {
        // Call the smart contract method to set slippage tolerance
        const transaction = await contractInstance.methods.setSlippageTolerance(slippage)
            .send({ from: userAddress });

        // Check if the transaction was successful
        if (transaction.status) {
            console.log(`Slippage tolerance set to ${slippage}% for address: ${userAddress}`);
            return true;
        } else {
            console.error('Transaction failed. Unable to set slippage tolerance.');
            return false;
        }
    } catch (error) {
        // Log error and rethrow for further handling if necessary
        console.error('Error while setting slippage tolerance:', error);
        throw new Error('Failed to set slippage tolerance: ' + error.message);
    }
}

// Example usage (ensure to replace with actual values)
// const userAddress = '0xYourWalletAddressHere';
// const slippage = 1; // 1%
// const contractInstance = new web3.eth.Contract(ABI, contractAddress);
// setSlippageTolerance(slippage, userAddress, contractInstance)
//     .then(success => console.log('Slippage set:', success))
//     .catch(error => console.error('Error:', error.message));
```
