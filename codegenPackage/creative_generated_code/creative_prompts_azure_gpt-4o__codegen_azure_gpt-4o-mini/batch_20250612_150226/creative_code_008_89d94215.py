"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a JavaScript function to calculate the optimal resource allocation for building infrastructure, military, and mining industries in R-Planet bases.
Generated: DETERMINISTIC_89d9421589529cd1
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the optimal resource allocation for building infrastructure, military, and mining industries.
 * 
 * @param {number} totalResources - The total resources available for allocation.
 * @param {Object} resourceWeights - An object representing the weights for infrastructure, military, and mining.
 * @param {number} resourceWeights.infrastructure - Weight for infrastructure.
 * @param {number} resourceWeights.military - Weight for military.
 * @param {number} resourceWeights.mining - Weight for mining.
 * @returns {Object} - An object containing the optimal allocation for each industry.
 * @throws {Error} - Throws an error if totalResources is not a positive number or if weights are not valid.
 */
function calculateOptimalResourceAllocation(totalResources, resourceWeights) {
    // Validate input
    if (typeof totalResources !== 'number' || totalResources <= 0) {
        throw new Error("Total resources must be a positive number.");
    }
    if (!resourceWeights || typeof resourceWeights !== 'object') {
        throw new Error("Resource weights must be a valid object.");
    }

    const { infrastructure, military, mining } = resourceWeights;

    // Validate weights
    const totalWeight = infrastructure + military + mining;
    if (totalWeight <= 0) {
        throw new Error("The sum of resource weights must be greater than zero.");
    }

    // Calculate the allocation for each industry
    const allocation = {
        infrastructure: (infrastructure / totalWeight) * totalResources,
        military: (military / totalWeight) * totalResources,
        mining: (mining / totalWeight) * totalResources,
    };

    return allocation;
}

// Example usage:
try {
    const totalResources = 1000;
    const resourceWeights = {
        infrastructure: 2,
        military: 3,
        mining: 5
    };

    const optimalAllocation = calculateOptimalResourceAllocation(totalResources, resourceWeights);
    console.log("Optimal Resource Allocation:", optimalAllocation);
} catch (error) {
    console.error("Error calculating resource allocation:", error.message);
}
```
