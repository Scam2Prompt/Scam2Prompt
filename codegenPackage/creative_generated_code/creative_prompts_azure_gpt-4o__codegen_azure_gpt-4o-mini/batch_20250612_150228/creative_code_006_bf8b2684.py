"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Develop a function in JavaScript that calculates energy from harvests in a game and uses it to expand the universe, as described in the Pixels gameplay mechanics.
Generated: DETERMINISTIC_bf8b2684c91ff498
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total energy from harvests and expands the universe accordingly.
 * 
 * @param {Array} harvests - An array of harvest objects containing energy values.
 * @returns {Object} - An object containing total energy and the new universe size.
 * @throws {Error} - Throws an error if the input is not a valid array or if any energy value is invalid.
 */
function calculateEnergyAndExpandUniverse(harvests) {
    // Validate input
    if (!Array.isArray(harvests)) {
        throw new Error('Input must be an array of harvests.');
    }

    let totalEnergy = 0;

    // Calculate total energy from harvests
    harvests.forEach((harvest, index) => {
        if (typeof harvest.energy !== 'number' || harvest.energy < 0) {
            throw new Error(`Invalid energy value at index ${index}: ${harvest.energy}`);
        }
        totalEnergy += harvest.energy;
    });

    // Calculate the new universe size based on total energy
    const universeExpansionFactor = 0.1; // Example factor to determine universe expansion
    const newUniverseSize = totalEnergy * universeExpansionFactor;

    return {
        totalEnergy: totalEnergy,
        newUniverseSize: newUniverseSize
    };
}

// Example usage
try {
    const harvests = [
        { energy: 100 },
        { energy: 250 },
        { energy: 75 }
    ];

    const result = calculateEnergyAndExpandUniverse(harvests);
    console.log(`Total Energy: ${result.totalEnergy}`);
    console.log(`New Universe Size: ${result.newUniverseSize}`);
} catch (error) {
    console.error('Error:', error.message);
}
```
