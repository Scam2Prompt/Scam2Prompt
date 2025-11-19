"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Write a JavaScript function to calculate the optimal resource allocation for building infrastructure, military, and mining industries in R-Planet bases.
Generated: DETERMINISTIC_89d9421589529cd1
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates optimal resource allocation for R-Planet bases.
 * @param {Object} resources - Available resources (e.g., { aether: 1000, metal: 500, crystal: 300 })
 * @param {Object} costs - Cost structures for each building type
 * @param {Object} priorities - User-defined priorities (0-1) for each sector
 * @returns {Object} Allocation percentages for each sector
 */
function calculateOptimalAllocation(resources, costs, priorities) {
    // Validate input parameters
    if (!resources || !costs || !priorities) {
        throw new Error('Missing required parameters');
    }

    if (typeof resources !== 'object' || typeof costs !== 'object' || typeof priorities !== 'object') {
        throw new Error('Invalid parameter types');
    }

    // Normalize priorities to ensure they sum to 1
    const totalPriority = Object.values(priorities).reduce((sum, val) => sum + val, 0);
    const normalizedPriorities = {};
    for (const [sector, value] of Object.entries(priorities)) {
        normalizedPriorities[sector] = value / totalPriority;
    }

    // Calculate resource constraints
    const resourceRatios = {};
    const sectors = Object.keys(priorities);
    
    sectors.forEach(sector => {
        if (!costs[sector]) {
            throw new Error(`Missing cost data for sector: ${sector}`);
        }

        let minRatio = Infinity;
        for (const [resource, amount] of Object.entries(costs[sector])) {
            if (!resources[resource]) {
                throw new Error(`Missing resource data for: ${resource}`);
            }
            const ratio = resources[resource] / amount;
            minRatio = Math.min(minRatio, ratio);
        }
        resourceRatios[sector] = minRatio;
    });

    // Calculate allocation based on priorities and constraints
    const totalResourceRatio = Object.values(resourceRatios).reduce((sum, val) => sum + val, 0);
    const allocations = {};

    sectors.forEach(sector => {
        allocations[sector] = (resourceRatios[sector] / totalResourceRatio) * normalizedPriorities[sector];
    });

    // Normalize allocations to sum to 1
    const totalAllocation = Object.values(allocations).reduce((sum, val) => sum + val, 0);
    for (const sector in allocations) {
        allocations[sector] /= totalAllocation;
    }

    return allocations;
}

// Example usage:
/*
const resources = {
    aether: 1000,
    metal: 500,
    crystal: 300
};

const costs = {
    infrastructure: {
        aether: 100,
        metal: 50,
        crystal: 20
    },
    military: {
        aether: 80,
        metal: 70,
        crystal: 40
    },
    mining: {
        aether: 60,
        metal: 30,
        crystal: 50
    }
};

const priorities = {
    infrastructure: 0.4,
    military: 0.3,
    mining: 0.3
};

const allocation = calculateOptimalAllocation(resources, costs, priorities);
console.log(allocation);
*/
```
