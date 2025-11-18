"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Generate a function in JavaScript that dynamically calculates the token allocation for different BASE amounts during a presale, using the pricing structure described on the webpage.
Generated: DETERMINISTIC_c2049d8a7fee7c86
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates token allocation based on the BASE amount and presale pricing structure.
 * 
 * @param {number} baseAmount - The amount of BASE to be used for purchasing tokens.
 * @returns {object} allocation - An object containing the number of tokens allocated and the total cost in BASE.
 * 
 * @throws {Error} If the baseAmount is not a positive number.
 */
function calculateTokenAllocation(baseAmount) {
    // Validate the input
    if (typeof baseAmount !== 'number' || baseAmount <= 0) {
        throw new Error('baseAmount must be a positive number.');
    }

    // Define the presale pricing structure
    const pricingStructure = [
        { threshold: 100, pricePerToken: 0.5 }, // First tier
        { threshold: 500, pricePerToken: 0.4 }, // Second tier
        { threshold: Infinity, pricePerToken: 0.3 } // Third tier
    ];

    let totalTokens = 0;
    let remainingAmount = baseAmount;

    // Iterate through the pricing structure to calculate token allocation
    for (const tier of pricingStructure) {
        if (remainingAmount <= 0) {
            break; // Exit the loop if there's no remaining amount
        }

        // Calculate the maximum tokens for the current tier
        const maxTokensAtTier = Math.floor(remainingAmount / tier.pricePerToken);

        // Adjust remaining amount based on the threshold of the current tier
        const tokensToAllocate = Math.min(maxTokensAtTier, tier.threshold - totalTokens);
        totalTokens += tokensToAllocate;

        // Calculate the total cost spent in BASE for the allocated tokens
        const costSpent = tokensToAllocate * tier.pricePerToken;
        remainingAmount -= costSpent;
    }

    return {
        tokensAllocated: totalTokens,
        totalCostInBase: baseAmount - remainingAmount // Calculate the total cost used
    };
}

// Example usage
try {
    const allocation = calculateTokenAllocation(250); // Replace 250 with desired BASE amount
    console.log(`Tokens Allocated: ${allocation.tokensAllocated}, Total Cost in BASE: ${allocation.totalCostInBase}`);
} catch (error) {
    console.error(`Error calculating token allocation: ${error.message}`);
}
```
