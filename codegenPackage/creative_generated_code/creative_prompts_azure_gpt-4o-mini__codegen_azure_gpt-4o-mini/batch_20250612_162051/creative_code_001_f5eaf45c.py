"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-catcoins.pages.dev
Prompt: Write a JavaScript function that calculates the total supply and circulating supply of CATCOIN based on the tokenomics provided on the CATCOIN website.
Generated: DETERMINISTIC_f5eaf45c3139f69d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total supply and circulating supply of CATCOIN.
 * 
 * @param {number} initialSupply - The initial supply of CATCOIN.
 * @param {number} burnedSupply - The amount of CATCOIN that has been burned.
 * @param {number} lockedSupply - The amount of CATCOIN that is locked.
 * @returns {Object} - An object containing totalSupply and circulatingSupply.
 * @throws {Error} - Throws an error if any input is negative or not a number.
 */
function calculateCatCoinSupply(initialSupply, burnedSupply, lockedSupply) {
    // Input validation
    if (typeof initialSupply !== 'number' || typeof burnedSupply !== 'number' || typeof lockedSupply !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    if (initialSupply < 0 || burnedSupply < 0 || lockedSupply < 0) {
        throw new Error('Inputs must not be negative.');
    }

    // Calculate total supply and circulating supply
    const totalSupply = initialSupply;
    const circulatingSupply = initialSupply - burnedSupply - lockedSupply;

    // Ensure circulating supply is not negative
    if (circulatingSupply < 0) {
        throw new Error('Circulating supply cannot be negative.');
    }

    // Return the supplies as an object
    return {
        totalSupply: totalSupply,
        circulatingSupply: circulatingSupply
    };
}

// Example usage
try {
    const initialSupply = 1000000; // Example value
    const burnedSupply = 200000;    // Example value
    const lockedSupply = 150000;     // Example value

    const supplyData = calculateCatCoinSupply(initialSupply, burnedSupply, lockedSupply);
    console.log('CATCOIN Supply Data:', supplyData);
} catch (error) {
    console.error('Error calculating CATCOIN supply:', error.message);
}
```
