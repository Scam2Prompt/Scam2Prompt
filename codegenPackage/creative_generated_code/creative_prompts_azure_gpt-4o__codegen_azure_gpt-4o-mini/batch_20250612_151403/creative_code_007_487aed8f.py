"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Create a JavaScript function that calculates the environmental impact reduction based on the use of Grupo ProBolsa's reusable bags compared to single-use alternatives.
Generated: DETERMINISTIC_487aed8fda26e9f9
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the environmental impact reduction based on the use of reusable bags
 * compared to single-use alternatives.
 *
 * @param {number} reusableBagsUsed - The number of reusable bags used.
 * @param {number} singleUseBagsEquivalent - The number of single-use bags equivalent 
 * to the reusable bags used.
 * @returns {Object} An object containing the environmental impact reduction details.
 * @throws {Error} If input values are invalid (non-positive numbers).
 */
function calculateEnvironmentalImpact(reusableBagsUsed, singleUseBagsEquivalent) {
    // Validate inputs
    if (typeof reusableBagsUsed !== 'number' || reusableBagsUsed <= 0) {
        throw new Error('Invalid input: reusableBagsUsed must be a positive number.');
    }
    if (typeof singleUseBagsEquivalent !== 'number' || singleUseBagsEquivalent <= 0) {
        throw new Error('Invalid input: singleUseBagsEquivalent must be a positive number.');
    }

    // Constants for calculation
    const CO2_PER_SINGLE_USE_BAG = 0.015; // Average CO2 emissions in kg per single-use bag
    const CO2_PER_REUSABLE_BAG = 0.005; // Average CO2 emissions in kg per reusable bag

    // Calculate total CO2 emissions for single-use bags
    const totalSingleUseCO2 = singleUseBagsEquivalent * CO2_PER_SINGLE_USE_BAG;

    // Calculate total CO2 emissions for reusable bags
    const totalReusableCO2 = reusableBagsUsed * CO2_PER_REUSABLE_BAG;

    // Calculate the reduction in CO2 emissions
    const CO2Reduction = totalSingleUseCO2 - totalReusableCO2;

    // Return the results
    return {
        totalSingleUseCO2: totalSingleUseCO2.toFixed(2), // Total CO2 from single-use bags
        totalReusableCO2: totalReusableCO2.toFixed(2),   // Total CO2 from reusable bags
        CO2Reduction: CO2Reduction.toFixed(2)              // Reduction in CO2 emissions
    };
}

// Example usage:
try {
    const impact = calculateEnvironmentalImpact(100, 300);
    console.log('Environmental Impact Reduction:', impact);
} catch (error) {
    console.error('Error calculating environmental impact:', error.message);
}
```
