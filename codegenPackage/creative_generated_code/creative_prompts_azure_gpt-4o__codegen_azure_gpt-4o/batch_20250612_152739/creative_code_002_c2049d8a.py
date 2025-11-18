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
 * Function to calculate token allocation during a presale based on BASE amount and pricing structure.
 * @param {number} baseAmount - The amount of BASE being contributed.
 * @returns {number} - The number of tokens allocated.
 * @throws {Error} - Throws an error if the input is invalid or if pricing structure is not defined.
 */

// Example pricing structure (replace with actual values from the webpage)
const pricingStructure = [
  { minBase: 0, maxBase: 1000, pricePerToken: 0.5 },
  { minBase: 1001, maxBase: 5000, pricePerToken: 0.4 },
  { minBase: 5001, maxBase: Infinity, pricePerToken: 0.3 }
];

function calculateTokenAllocation(baseAmount) {
  // Validate baseAmount
  if (typeof baseAmount !== 'number' || baseAmount <= 0) {
    throw new Error("Invalid base amount. It must be a positive number.");
  }

  // Determine the applicable pricing tier
  const pricingTier = pricingStructure.find(
    (tier) => baseAmount >= tier.minBase && baseAmount <= tier.maxBase
  );

  // If no pricing tier matches, throw an error
  if (!pricingTier) {
    throw new Error("No applicable pricing structure found for the given base amount.");
  }

  // Calculate token allocation
  const tokensAllocated = baseAmount / pricingTier.pricePerToken;

  return tokensAllocated;
}

// Example usage:
// Replace with actual values to test the function
try {
  const baseAmount = 1200; // Example BASE amount
  const tokens = calculateTokenAllocation(baseAmount);
  console.log(`Tokens allocated for BASE amount ${baseAmount}: ${tokens}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
