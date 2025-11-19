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
 * Calculates the total number of SHROOM tokens received based on the ETH amount sent.
 * @param {number} ethAmount - The amount of ETH sent during the presale.
 * @param {number} rate - The conversion rate of ETH to SHROOM tokens (tokens per ETH).
 * @returns {number} - The total number of SHROOM tokens received.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateShroomTokens(ethAmount, rate) {
    // Validate input types and values
    if (typeof ethAmount !== 'number' || ethAmount < 0) {
        throw new Error("Invalid ethAmount: Must be a non-negative number.");
    }
    if (typeof rate !== 'number' || rate <= 0) {
        throw new Error("Invalid rate: Must be a positive number.");
    }

    // Calculate the total number of SHROOM tokens
    const shroomTokens = ethAmount * rate;

    // Return the calculated SHROOM tokens
    return shroomTokens;
}

// Example usage
try {
    const ethSent = 2.5; // ETH amount sent
    const conversionRate = 1000; // Conversion rate: 1000 SHROOM tokens per ETH

    const totalTokens = calculateShroomTokens(ethSent, conversionRate);
    console.log(`Total SHROOM tokens received: ${totalTokens}`);
} catch (error) {
    console.error(`Error calculating SHROOM tokens: ${error.message}`);
}
```
