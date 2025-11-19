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
 * @module PipeSizingCalculator
 * @description A library function to calculate required pipe sizes for a residential plumbing system
 *              based on guidelines from ERA Engineering's plumbing services.
 */

/**
 * Calculates the required pipe size based on the flow rate.
 * @param {number} flowRate - The flow rate in gallons per minute (GPM).
 * @returns {string} - The recommended pipe size (e.g., "1/2 inch", "3/4 inch").
 * @throws {Error} - Throws an error if the flow rate is not a positive number.
 */
function calculatePipeSize(flowRate) {
    // Validate the input
    if (typeof flowRate !== 'number' || flowRate <= 0) {
        throw new Error("Invalid input: flowRate must be a positive number.");
    }

    // Define the pipe size recommendations based on flow rate
    const pipeSizes = [
        { maxFlowRate: 10, size: "1/2 inch" },
        { maxFlowRate: 20, size: "3/4 inch" },
        { maxFlowRate: 30, size: "1 inch" },
        { maxFlowRate: 40, size: "1 1/4 inch" },
        { maxFlowRate: 50, size: "1 1/2 inch" },
        { maxFlowRate: 60, size: "2 inch" }
    ];

    // Determine the appropriate pipe size
    for (const pipe of pipeSizes) {
        if (flowRate <= pipe.maxFlowRate) {
            return pipe.size;
        }
    }

    // If flow rate exceeds the largest size recommendation, return an appropriate message
    return "Flow rate exceeds recommended values. Consider consulting a professional.";
}

// Export the calculatePipeSize function for use in other modules
module.exports = {
    calculatePipeSize
};
```
