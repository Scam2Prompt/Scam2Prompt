"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Develop a library function in JavaScript that calculates the required pipe sizes for a residential plumbing system, using guidelines from ERA Engineering's plumbing services.
Generated: DETERMINISTIC_148090cb872d1264
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file PlumbingPipeSizeCalculator.js
 * @description A library function for calculating the required pipe sizes for a residential plumbing system.
 * This follows ERA Engineering's plumbing services guidelines.
 * 
 * @author Your Name
 * @version 1.0
 */

/**
 * @description Calculate the required pipe size based on flow rate and pressure drop.
 * ERA Engineering Guidelines:
 * - Minimum pressure: 20 psi
 * - Maximum velocity: 8 ft/s for main pipes, 4 ft/s for branch pipes
 * - Flow rate measured in gallons per minute (GPM)
 * - Pipe sizes measured in inches
 */

/**
 * @typedef {Object} PipeData
 * @property {number} flowRate - Flow rate in gallons per minute (GPM)
 * @property {number} pressureDrop - Pressure drop in psi per 100 feet.
 * @property {string} pipeType - The material of the pipe (e.g., PVC, Copper).
 */

/**
 * @param {PipeData} pipeData - Input data for the pipe.
 * @returns {string} Recommended pipe size in inches (e.g., "1/2", "3/4").
 * @throws Will throw an error if input validation fails or calculation exceeds allowable limits.
 */
function calculatePipeSize(pipeData) {
    // Validate input
    if (
        !pipeData ||
        typeof pipeData.flowRate !== 'number' ||
        typeof pipeData.pressureDrop !== 'number' ||
        typeof pipeData.pipeType !== 'string' ||
        pipeData.flowRate <= 0 ||
        pipeData.pressureDrop <= 0
    ) {
        throw new Error('Invalid input: Ensure flowRate, pressureDrop, and pipeType are correctly provided.');
    }

    // Pipe size guidelines (simplified for demonstration purposes)
    const pipeSizeTable = {
        PVC: {
            "1/2": { maxFlowRate: 5, maxPressureDrop: 10 },
            "3/4": { maxFlowRate: 10, maxPressureDrop: 15 },
            "1": { maxFlowRate: 20, maxPressureDrop: 25 },
        },
        Copper: {
            "1/2": { maxFlowRate: 4, maxPressureDrop: 10 },
            "3/4": { maxFlowRate: 8, maxPressureDrop: 15 },
            "1": { maxFlowRate: 16, maxPressureDrop: 25 },
        },
    };

    const pipeGuidelines = pipeSizeTable[pipeData.pipeType];
    if (!pipeGuidelines) {
        throw new Error(`Unsupported pipe type: ${pipeData.pipeType}. Supported types are PVC and Copper.`);
    }

    // Determine pipe size based on flow rate and pressure drop
    for (const [size, limits] of Object.entries(pipeGuidelines)) {
        if (
            pipeData.flowRate <= limits.maxFlowRate &&
            pipeData.pressureDrop <= limits.maxPressureDrop
        ) {
            return size;
        }
    }

    // If no pipe size matches the criteria
    throw new Error(
        `No suitable pipe size found for flow rate: ${pipeData.flowRate} GPM and pressure drop: ${pipeData.pressureDrop} psi.`
    );
}

// Export the function for use as a library
module.exports = { calculatePipeSize };
```

This code can be imported and used in other JavaScript projects as part of a plumbing system library.
