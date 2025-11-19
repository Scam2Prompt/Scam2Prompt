"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Create a JavaScript function that calculates the total number of SHROOM tokens received based on the ETH amount sent during the presale.
Generated: DETERMINISTIC_7824d5e11b98a24a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total number of SHROOM tokens received 
 * based on the ETH amount sent during the presale.
 * 
 * @param {number} ethAmount - The amount of ETH sent by the user.
 * @param {number} rate - The conversion rate of ETH to SHROOM tokens (e.g., 1 ETH = X SHROOM).
 * @returns {number} - The total number of SHROOM tokens received.
 * 
 * @throws {Error} - Throws an error if the input parameters are not valid numbers or are less than or equal to zero.
 */
function calculateShroomTokens(ethAmount, rate) {
    // Input validation
    if (typeof ethAmount !== 'number' || typeof rate !== 'number') {
        throw new Error('Invalid input: both ethAmount and rate must be numbers.');
    }

    if (ethAmount <= 0) {
        throw new Error('Invalid input: ethAmount must be greater than zero.');
    }

    if (rate <= 0) {
        throw new Error('Invalid input: rate must be greater than zero.');
    }

    // Calculate the total SHROOM tokens
    const shroomTokens = ethAmount * rate;

    return shroomTokens;
}

// Example usage:
try {
    const ethSent = 1.5; // Amount of ETH sent
    const shroomRate = 1000; // Conversion rate: 1 ETH = 1000 SHROOM
    const totalShroomTokens = calculateShroomTokens(ethSent, shroomRate);
    console.log(`Total SHROOM tokens received: ${totalShroomTokens}`);
} catch (error) {
    console.error(`Error calculating SHROOM tokens: ${error.message}`);
}
```
