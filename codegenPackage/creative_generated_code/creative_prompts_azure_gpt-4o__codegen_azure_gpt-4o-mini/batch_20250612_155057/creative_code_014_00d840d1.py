"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a JavaScript function to implement the "Cloudra Horizon" mechanic in Stellar Crop, where players manage floating islands with dynamic wind patterns and resource distribution.
Generated: DETERMINISTIC_00d840d1b656ffec
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function manageFloatingIslands
 * @description This function simulates the "Cloudra Horizon" mechanic in the Stellar Crop game, 
 * where players manage floating islands with dynamic wind patterns and resource distribution.
 * 
 * @param {Array} islands - An array of island objects, where each island has a name and resources.
 * @param {Object} wind - An object representing the current wind pattern and speed.
 * @returns {Array} Updated array of islands with redistributed resources based on wind direction.
 */
function manageFloatingIslands(islands, wind) {
    // Validate input
    if (!Array.isArray(islands)) {
        throw new Error("Invalid input: 'islands' should be an array");
    }
    if (typeof wind !== 'object' || wind === null || !('direction' in wind) || !('speed' in wind)) {
        throw new Error("Invalid input: 'wind' should be an object with 'direction' and 'speed'");
    }

    // Set wind impact factor based on speed
    const windImpactFactor = Math.max(0, Math.min(wind.speed, 100)) / 100;

    // Redistribute resources among islands based on wind direction
    const redistributedIslands = islands.map(island => {
        // Ensure island has the required properties
        if (!island.name || !island.resources || typeof island.resources !== 'object') {
            throw new Error(`Invalid island data: ${JSON.stringify(island)}`);
        }

        // Calculate resource redistribution based on wind direction
        const resourceKeys = Object.keys(island.resources);
        const resourceChange = {};

        resourceKeys.forEach(key => {
            // Simulate redistribution based on wind direction
            resourceChange[key] = (island.resources[key] * windImpactFactor * (wind.direction === 'east' ? 1 : -1));
        });

        // Apply the redistribution and ensure resources remain non-negative
        const newResources = resourceKeys.reduce((acc, key) => {
            const newValue = Math.max(0, island.resources[key] + resourceChange[key]);
            acc[key] = newValue;
            return acc;
        }, {});

        return {
            ...island,
            resources: newResources
        };
    });

    return redistributedIslands;
}

// Example usage:
try {
    const islands = [
        { name: 'Aether Isle', resources: { wood: 100, stone: 50 } },
        { name: 'Nimbus Isle', resources: { wood: 80, stone: 70 } }
    ];

    const wind = { direction: 'east', speed: 30 };

    const updatedIslands = manageFloatingIslands(islands, wind);
    console.log(updatedIslands);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
