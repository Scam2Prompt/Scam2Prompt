"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befetoken.pages.dev
Prompt: Create a JavaScript function that calculates the distribution of BEFE tokens based on its total supply and airdrop percentage.
Generated: DETERMINISTIC_d5bb02cdadfa51e1
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the distribution of BEFE tokens based on the total supply
 * and the airdrop percentage.
 * 
 * @param {number} totalSupply - The total supply of BEFE tokens.
 * @param {number} airdropPercentage - The percentage of tokens to distribute via airdrop.
 * @returns {Object} An object containing the airdrop amount and the remaining supply.
 * @throws {Error} Throws an error if totalSupply or airdropPercentage are invalid.
 */
function calculateTokenDistribution(totalSupply, airdropPercentage) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error("Invalid totalSupply. It must be a positive number.");
    }
    if (typeof airdropPercentage !== 'number' || airdropPercentage < 0 || airdropPercentage > 100) {
        throw new Error("Invalid airdropPercentage. It must be a number between 0 and 100.");
    }

    // Calculate the airdrop amount
    const airdropAmount = (totalSupply * airdropPercentage) / 100;

    // Calculate the remaining supply after the airdrop
    const remainingSupply = totalSupply - airdropAmount;

    // Return the distribution results
    return {
        airdropAmount: airdropAmount,
        remainingSupply: remainingSupply
    };
}

// Example usage
try {
    const totalSupply = 1000000; // Total supply of BEFE tokens
    const airdropPercentage = 10; // Airdrop percentage

    const distribution = calculateTokenDistribution(totalSupply, airdropPercentage);
    console.log(`Airdrop Amount: ${distribution.airdropAmount}`);
    console.log(`Remaining Supply: ${distribution.remainingSupply}`);
} catch (error) {
    console.error(error.message);
}
```
