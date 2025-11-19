"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-presale-dogcoin.pages.dev
Prompt: Create a JavaScript function that calculates the amount of DOG tokens received based on the ETH amount sent in the presale.
Generated: DETERMINISTIC_a489f5ef0a126cf7
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of DOG tokens received based on the ETH amount sent in the presale.
 *
 * @param {number} ethAmount - The amount of ETH sent in the presale.
 * @param {number} conversionRate - The conversion rate of ETH to DOG tokens.
 * @returns {number} The amount of DOG tokens received.
 * @throws {Error} Throws an error if ethAmount or conversionRate is not a positive number.
 */
function calculateDogTokens(ethAmount, conversionRate) {
    // Validate input parameters
    if (typeof ethAmount !== 'number' || ethAmount <= 0) {
        throw new Error('Invalid ETH amount. It must be a positive number.');
    }
    if (typeof conversionRate !== 'number' || conversionRate <= 0) {
        throw new Error('Invalid conversion rate. It must be a positive number.');
    }

    // Calculate the DOG tokens received
    const dogTokensReceived = ethAmount * conversionRate;

    return dogTokensReceived;
}

// Example usage
try {
    const ethAmount = 1.5; // Example ETH amount sent
    const conversionRate = 1000; // Example conversion rate (1 ETH = 1000 DOG)
    
    const tokens = calculateDogTokens(ethAmount, conversionRate);
    console.log(`You will receive ${tokens} DOG tokens for sending ${ethAmount} ETH.`);
} catch (error) {
    console.error(error.message);
}
```
