"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Develop a JavaScript function that calculates the cost estimation for glass and aluminum projects based on user inputs, similar to the offerings of CristalesGraf.
Generated: DETERMINISTIC_9cc3680962042119
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
 * Calculates the cost estimation for glass and aluminum projects.
 * 
 * @param {number} glassArea - The area of glass in square meters.
 * @param {number} aluminumLength - The length of aluminum in meters.
 * @param {number} glassCostPerSqM - The cost of glass per square meter.
 * @param {number} aluminumCostPerMeter - The cost of aluminum per meter.
 * @returns {Object} An object containing the total cost and a breakdown of costs.
 * @throws {Error} Throws an error if any input is negative or not a number.
 */
function calculateCostEstimation(glassArea, aluminumLength, glassCostPerSqM, aluminumCostPerMeter) {
    // Validate inputs
    if (
        typeof glassArea !== 'number' || glassArea < 0 ||
        typeof aluminumLength !== 'number' || aluminumLength < 0 ||
        typeof glassCostPerSqM !== 'number' || glassCostPerSqM < 0 ||
        typeof aluminumCostPerMeter !== 'number' || aluminumCostPerMeter < 0
    ) {
        throw new Error('All inputs must be non-negative numbers.');
    }

    // Calculate individual costs
    const glassCost = glassArea * glassCostPerSqM;
    const aluminumCost = aluminumLength * aluminumCostPerMeter;

    // Calculate total cost
    const totalCost = glassCost + aluminumCost;

    // Return cost breakdown
    return {
        totalCost: totalCost,
        glassCost: glassCost,
        aluminumCost: aluminumCost
    };
}

// Example usage:
try {
    const estimation = calculateCostEstimation(10, 5, 50, 20);
    console.log('Cost Estimation:', estimation);
} catch (error) {
    console.error('Error calculating cost estimation:', error.message);
}
```
