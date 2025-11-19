"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Develop a library function in JavaScript that calculates the required pipe sizes for a residential plumbing system, using guidelines from ERA Engineering's plumbing services.
Generated: DETERMINISTIC_148090cb872d1264
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @module PipeSizing
 * @description A library for calculating required pipe sizes for a residential plumbing system
 * based on guidelines from ERA Engineering's plumbing services.
 */

/**
 * Calculates the required pipe size based on the flow rate and pipe material.
 * 
 * @param {number} flowRate - The flow rate in gallons per minute (GPM).
 * @param {string} material - The material of the pipe (e.g., 'PVC', 'Copper', 'Galvanized').
 * @returns {string} - The recommended pipe size in inches.
 * @throws {Error} - Throws an error if the flow rate is not a positive number or if the material is invalid.
 */
function calculatePipeSize(flowRate, material) {
    // Validate input parameters
    if (typeof flowRate !== 'number' || flowRate <= 0) {
        throw new Error('Flow rate must be a positive number.');
    }

    const materialSizes = {
        'PVC': { 1: 20, 1.5: 40, 2: 60, 3: 100 },
        'Copper': { 1: 30, 1.5: 50, 2: 80, 3: 120 },
        'Galvanized': { 1: 25, 1.5: 45, 2: 70, 3: 110 }
    };

    // Check if the material is valid
    if (!materialSizes[material]) {
        throw new Error('Invalid material. Please choose from PVC, Copper, or Galvanized.');
    }

    // Determine the appropriate pipe size based on flow rate
    for (const [size, maxFlow] of Object.entries(materialSizes[material])) {
        if (flowRate <= maxFlow) {
            return `${size} inch`;
        }
    }

    // If no suitable size is found, return a message indicating the need for larger pipes
    return 'Consider using larger pipe sizes for the given flow rate.';
}

// Example usage
try {
    const pipeSize = calculatePipeSize(45, 'PVC');
    console.log(`Recommended pipe size: ${pipeSize}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}

export { calculatePipeSize };
```
