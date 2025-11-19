"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Generate a function in JavaScript that dynamically calculates the token allocation for different BASE amounts during a presale, using the pricing structure described on the webpage.
Generated: DETERMINISTIC_c2049d8a7fee7c86
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates token allocation for different BASE amounts during a presale.
 * 
 * @param {number} baseAmount - The BASE amount for which to calculate token allocation.
 * @param {object} pricingStructure - The pricing structure object containing tiers and their corresponding token allocations.
 * @returns {object} An object containing the calculated token allocation.
 */
function calculateTokenAllocation(baseAmount, pricingStructure) {
    // Check if baseAmount and pricingStructure are valid
    if (typeof baseAmount !== 'number' || baseAmount <= 0) {
        throw new Error('Invalid base amount. It must be a positive number.');
    }

    if (typeof pricingStructure !== 'object' || pricingStructure === null) {
        throw new Error('Invalid pricing structure. It must be a non-null object.');
    }

    // Sort pricing tiers in ascending order
    const sortedTiers = Object.keys(pricingStructure).sort((a, b) => a - b).map(Number);

    // Initialize token allocation
    let tokenAllocation = 0;

    // Initialize remaining base amount
    let remainingBaseAmount = baseAmount;

    // Iterate over pricing tiers
    for (let i = 0; i < sortedTiers.length; i++) {
        const tier = sortedTiers[i];
        const tokensPerTier = pricingStructure[tier];

        // If remaining base amount exceeds current tier, allocate tokens for this tier
        if (remainingBaseAmount >= tier) {
            tokenAllocation += tokensPerTier;
            remainingBaseAmount -= tier;
        } 
        // If remaining base amount is less than current tier, allocate tokens for remaining amount
        else {
            // Calculate token allocation for remaining base amount
            const tokenAllocationForRemaining = (remainingBaseAmount / tier) * tokensPerTier;
            tokenAllocation += tokenAllocationForRemaining;
            break;
        }
    }

    return {
        tokenAllocation: tokenAllocation,
        remainingBaseAmount: remainingBaseAmount
    };
}

// Example usage:
const pricingStructure = {
    100: 50,
    500: 200,
    1000: 400
};

try {
    const baseAmount = 750;
    const result = calculateTokenAllocation(baseAmount, pricingStructure);
    console.log(`Token allocation for ${baseAmount} BASE: ${result.tokenAllocation}`);
    console.log(`Remaining BASE amount: ${result.remainingBaseAmount}`);
} catch (error) {
    console.error(error.message);
}
```
