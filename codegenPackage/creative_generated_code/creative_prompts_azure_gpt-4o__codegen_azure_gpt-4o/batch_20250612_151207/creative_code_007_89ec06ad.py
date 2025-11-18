"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Create a JavaScript function using ethers.js to calculate the maximum $DOGEVERSE tokens a user can receive based on their ETH input during the presale, referencing the token price of $0.00031 per $DOGEVERSE.
Generated: DETERMINISTIC_89ec06ad29509298
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateMaxTokens
 * Calculates the maximum $DOGEVERSE tokens a user can receive based on their ETH input during the presale.
 * 
 * @param {string} ethInput - The amount of ETH input by the user, in wei (string format for precision).
 * @param {string} ethPriceUSD - The current price of ETH in USD, as a string (to handle high precision).
 * @returns {string} - The maximum number of $DOGEVERSE tokens the user can receive, as a string.
 * 
 * @throws {Error} If inputs are invalid or a calculation error occurs.
 */
async function calculateMaxTokens(ethInput, ethPriceUSD) {
    try {
        // Validate ETH input and ETH price in USD
        if (!ethers.utils.isHexString(ethInput)) {
            throw new Error('Invalid ETH input. Please provide the amount in wei as a hex string.');
        }
        if (isNaN(parseFloat(ethPriceUSD)) || parseFloat(ethPriceUSD) <= 0) {
            throw new Error('Invalid ETH price in USD. Please provide a valid positive number as a string.');
        }

        // Constants
        const tokenPriceUSD = 0.00031; // Price of 1 $DOGEVERSE token in USD

        // Convert ETH input (in wei) to ETH (in decimal)
        const ethDecimal = ethers.utils.formatEther(ethInput);

        // Calculate total USD value of the ETH input
        const ethUSDValue = parseFloat(ethDecimal) * parseFloat(ethPriceUSD);

        // Calculate the maximum number of $DOGEVERSE tokens the user can receive
        const maxTokens = ethUSDValue / tokenPriceUSD;

        // Return result as a string for precision
        return maxTokens.toString();
    } catch (error) {
        // Catch and throw errors for proper error handling
        throw new Error(`Error calculating max tokens: ${error.message}`);
    }
}

// Example usage:
// (Assumes ethers.js is already imported and properly installed)
// const ethers = require('ethers');
// const ethInput = '0xde0b6b3a7640000';  // 1 ETH in wei (hex string)
// const ethPriceUSD = '1800.00';          // Example ETH price in USD
// calculateMaxTokens(ethInput, ethPriceUSD)
//     .then(maxTokens => console.log(`Maximum $DOGEVERSE tokens: ${maxTokens}`))
//     .catch(error => console.error(error.message));
```
