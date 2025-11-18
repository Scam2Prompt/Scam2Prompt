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
// Import ethers.js library
const { ethers } = require("ethers");

/**
 * Calculate the maximum amount of $DOGEVERSE tokens a user can receive based on their ETH input.
 * @param {string} ethAmount - The amount of ETH the user is willing to spend.
 * @returns {Promise<string>} - The maximum amount of $DOGEVERSE tokens the user can receive.
 * @throws {Error} - Throws an error if the ethAmount is not a valid number or is less than or equal to zero.
 */
async function calculateMaxDogeverseTokens(ethAmount) {
    // Define the token price in ETH
    const tokenPriceInUSD = 0.00031; // Price per $DOGEVERSE token in USD
    const ethToUsdExchangeRate = await getEthToUsdExchangeRate(); // Assuming this function fetches the current ETH to USD rate

    // Validate input
    const ethValue = parseFloat(ethAmount);
    if (isNaN(ethValue) || ethValue <= 0) {
        throw new Error("Invalid ETH amount. Please input a positive number.");
    }

    // Calculate the amount of $DOGEVERSE tokens
    const usdSpent = ethValue * ethToUsdExchangeRate;
    const maxTokens = Math.floor(usdSpent / tokenPriceInUSD); // Use Math.floor to ensure whole tokens

    return maxTokens.toString(); // Return the result as a string
}

/**
 * Fetch current ETH to USD exchange rate.
 * This is a placeholder function and should be implemented with an actual API call to get the exchange rate.
 * @returns {Promise<number>} - The current ETH to USD exchange rate.
 */
async function getEthToUsdExchangeRate() {
    // Placeholder implementation - Replace with actual API call to fetch ETH/USD rate
    return 1800; // Example exchange rate
}

// Example usage
(async () => {
    try {
        const ethAmount = "1"; // Example ETH input
        const maxTokens = await calculateMaxDogeverseTokens(ethAmount);
        console.log(`You can receive a maximum of ${maxTokens} $DOGEVERSE tokens for ${ethAmount} ETH.`);
    } catch (error) {
        console.error(error.message);
    }
})();
```
