"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerfairdrop.vercel.app
Prompt: Write a JavaScript function to calculate the percentage of tokens burned at launch for the $Slerf token, using the total supply and the amount burned mentioned on the Slerf Fair Drop page.
Generated: DETERMINISTIC_441521dd4f5e2a40
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the percentage of tokens burned at launch for the $Slerf token.
 * 
 * @param {number} totalSupply - The total supply of $Slerf tokens.
 * @param {number} amountBurned - The amount of $Slerf tokens burned at launch.
 * @returns {number} - The percentage of tokens burned at launch.
 * @throws {Error} - Throws an error if totalSupply is zero or if any parameter is not a number.
 */
function calculateBurnPercentage(totalSupply, amountBurned) {
    // Validate input types
    if (typeof totalSupply !== 'number' || typeof amountBurned !== 'number') {
        throw new Error('Both totalSupply and amountBurned must be numbers.');
    }

    // Check for zero total supply to avoid division by zero
    if (totalSupply <= 0) {
        throw new Error('Total supply must be greater than zero.');
    }

    // Calculate the percentage of tokens burned
    const burnPercentage = (amountBurned / totalSupply) * 100;

    // Return the calculated burn percentage
    return burnPercentage;
}

// Example usage:
try {
    const totalSupply = 1000000; // Example total supply
    const amountBurned = 250000;  // Example amount burned
    const percentageBurned = calculateBurnPercentage(totalSupply, amountBurned);
    console.log(`Percentage of $Slerf tokens burned at launch: ${percentageBurned.toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating burn percentage: ${error.message}`);
}
```
