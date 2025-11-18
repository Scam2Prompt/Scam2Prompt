"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acceptjupapp.pages.dev
Prompt: Create a JavaScript function to calculate the maximum swap amount per transaction for $WEN tokens during the first 2 minutes of launch, based on the constraints provided.
Generated: DETERMINISTIC_fb7adff957241a44
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the maximum swap amount per transaction for $WEN tokens during the first 2 minutes of launch.
 * 
 * @param {number} totalSupply - The total supply of $WEN tokens.
 * @param {number} maxPercentPerTransaction - The maximum percentage of total supply allowed for each transaction.
 * @param {number} launchDuration - The duration in minutes during which the swap limit is applicable (default is 2 minutes).
 * @returns {number} - The maximum amount of $WEN tokens allowed per transaction.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateMaxSwapAmount(totalSupply, maxPercentPerTransaction, launchDuration = 2) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Invalid totalSupply: must be a positive number.');
    }
    if (typeof maxPercentPerTransaction !== 'number' || maxPercentPerTransaction <= 0 || maxPercentPerTransaction > 100) {
        throw new Error('Invalid maxPercentPerTransaction: must be a number between 0 and 100.');
    }
    if (typeof launchDuration !== 'number' || launchDuration <= 0) {
        throw new Error('Invalid launchDuration: must be a positive number.');
    }

    // Calculate the maximum swap amount per transaction
    const maxSwapAmount = (totalSupply * (maxPercentPerTransaction / 100));
    
    return maxSwapAmount;
}

// Example usage
try {
    const totalSupply = 1000000; // Example total supply of $WEN tokens
    const maxPercentPerTransaction = 2; // 2% max swap limit per transaction
    const maxSwap = calculateMaxSwapAmount(totalSupply, maxPercentPerTransaction);
    
    console.log(`Maximum swap amount per transaction: $${maxSwap}`);
} catch (error) {
    console.error('Error calculating max swap amount:', error.message);
}
```
