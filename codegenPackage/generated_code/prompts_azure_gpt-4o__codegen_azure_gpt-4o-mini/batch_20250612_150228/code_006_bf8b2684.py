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
 * Calculates the total energy from harvests and uses it to expand the universe.
 * 
 * @param {Array<Object>} harvests - An array of harvest objects, each containing 
 *                                    the amount of energy produced.
 * @param {number} expansionCost - The amount of energy required to expand the universe.
 * @returns {Object} - An object containing the total energy, the number of expansions 
 *                     possible, and the remaining energy after expansions.
 * @throws {Error} - Throws an error if the harvests array is empty or if the 
 *                   expansion cost is not a positive number.
 */
function calculateEnergyAndExpand(harvests, expansionCost) {
    // Validate input parameters
    if (!Array.isArray(harvests) || harvests.length === 0) {
        throw new Error("Harvests must be a non-empty array.");
    }
    if (typeof expansionCost !== 'number' || expansionCost <= 0) {
        throw new Error("Expansion cost must be a positive number.");
    }

    // Calculate total energy from harvests
    const totalEnergy = harvests.reduce((accumulator, harvest) => {
        if (typeof harvest.energy !== 'number' || harvest.energy < 0) {
            throw new Error("Each harvest must have a non-negative energy value.");
        }
        return accumulator + harvest.energy;
    }, 0);

    // Calculate the number of expansions possible
    const expansionsPossible = Math.floor(totalEnergy / expansionCost);

    // Calculate remaining energy after expansions
    const remainingEnergy = totalEnergy % expansionCost;

    // Return the results
    return {
        totalEnergy,
        expansionsPossible,
        remainingEnergy
    };
}

// Example usage
try {
    const harvests = [
        { energy: 50 },
        { energy: 30 },
        { energy: 20 }
    ];
    const expansionCost = 40;

    const result = calculateEnergyAndExpand(harvests, expansionCost);
    console.log(result);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
