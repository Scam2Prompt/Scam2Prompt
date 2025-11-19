"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Develop a function in JavaScript that calculates energy from harvests in a game and uses it to expand the universe, as described in the Pixels gameplay mechanics.
Generated: DETERMINISTIC_bf8b2684c91ff498
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the energy from harvests and uses it to expand the universe.
 * 
 * @param {Array<number>} harvests - Array of energy values from each harvest.
 * @param {number} currentUniverseSize - Current size of the universe.
 * @param {number} expansionCost - Energy cost per unit of universe expansion.
 * @returns {Object} An object containing the new universe size and remaining energy.
 * @throws {Error} If inputs are invalid.
 */
function expandUniverse(harvests, currentUniverseSize, expansionCost) {
    // Validate inputs
    if (!Array.isArray(harvests) || harvests.some(isNaN)) {
        throw new Error('Harvests must be an array of numbers');
    }
    if (typeof currentUniverseSize !== 'number' || isNaN(currentUniverseSize) || currentUniverseSize < 0) {
        throw new Error('Current universe size must be a non-negative number');
    }
    if (typeof expansionCost !== 'number' || isNaN(expansionCost) || expansionCost <= 0) {
        throw new Error('Expansion cost must be a positive number');
    }

    // Calculate total energy from harvests
    const totalEnergy = harvests.reduce((sum, harvest) => sum + harvest, 0);

    // Calculate possible expansion
    const expansionUnits = Math.floor(totalEnergy / expansionCost);
    const remainingEnergy = totalEnergy % expansionCost;

    // Update universe size
    const newUniverseSize = currentUniverseSize + expansionUnits;

    return {
        newUniverseSize,
        remainingEnergy,
        energyUsed: expansionUnits * expansionCost
    };
}

// Example usage:
try {
    const result = expandUniverse([10, 20, 30], 100, 15);
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
}
```
