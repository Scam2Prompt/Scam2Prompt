"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simonscat-claims.pages.dev
Prompt: Create a JavaScript function that calculates the allocation of Simon's Cat Token based on the provided tokenomics percentages.
Generated: DETERMINISTIC_17e77e3fcc360ca7
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the allocation of Simon's Cat Token based on tokenomics percentages.
 * 
 * @param {number} totalSupply - The total supply of Simon's Cat Token.
 * @param {object} tokenomics - An object containing percentage allocations for various categories.
 * @returns {object} - An object with calculated allocations for each category in tokenomics.
 * @throws {Error} - Throws an error if tokenomics percentages do not add up to 100% or if inputs are invalid.
 */
function calculateTokenAllocation(totalSupply, tokenomics) {
    // Input validation
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error("Invalid total supply. Must be a positive number.");
    }
    if (typeof tokenomics !== 'object' || tokenomics === null) {
        throw new Error("Invalid tokenomics. Must be a non-null object.");
    }

    const totalPercentage = Object.values(tokenomics).reduce((sum, percentage) => {
        if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
            throw new Error("Invalid percentage in tokenomics. Must be a number between 0 and 100.");
        }
        return sum + percentage;
    }, 0);

    // Ensure percentages add up to 100
    if (totalPercentage !== 100) {
        throw new Error("Tokenomics percentages must add up to 100.");
    }

    // Calculate allocations
    const allocations = {};
    for (const [category, percentage] of Object.entries(tokenomics)) {
        allocations[category] = (totalSupply * percentage) / 100;
    }

    return allocations;
}

// Example usage:
try {
    const totalSupply = 1000000; // 1 million tokens
    const tokenomics = {
        marketing: 20,      // 20%
        development: 30,    // 30%
        rewards: 25,        // 25%
        liquidity: 15,      // 15%
        team: 10            // 10%
    };

    const allocations = calculateTokenAllocation(totalSupply, tokenomics);
    console.log("Token Allocations:", allocations);
} catch (error) {
    console.error("Error:", error.message);
}
```
