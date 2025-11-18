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
 * Function to calculate the environmental impact reduction of using Grupo ProBolsa's reusable bags
 * compared to single-use alternatives.
 * 
 * @param {number} reusableBagsUsed - Number of reusable bags used.
 * @param {number} singleUseBagImpact - Environmental impact of a single-use bag (e.g., in grams of CO2 or waste).
 * @param {number} reuseCount - Average number of times a reusable bag can be used.
 * @returns {object} - An object containing the environmental impact reduction in total and per reusable bag.
 */
function calculateImpactReduction(reusableBagsUsed, singleUseBagImpact, reuseCount) {
  try {
    // Input validation
    if (
      typeof reusableBagsUsed !== 'number' || reusableBagsUsed < 0 ||
      typeof singleUseBagImpact !== 'number' || singleUseBagImpact <= 0 ||
      typeof reuseCount !== 'number' || reuseCount <= 0
    ) {
      throw new Error('Invalid input: All parameters must be positive numbers.');
    }

    // Calculate total environmental impact for single-use bags
    const singleUseTotalImpact = reusableBagsUsed * singleUseBagImpact;

    // Calculate total environmental impact for reusable bags
    const reusableBagTotalImpact = reusableBagsUsed * (singleUseBagImpact / reuseCount);

    // Calculate reduction in environmental impact
    const totalReduction = singleUseTotalImpact - reusableBagTotalImpact;
    const reductionPerBag = totalReduction / reusableBagsUsed;

    // Return results as an object
    return {
      totalReduction: parseFloat(totalReduction.toFixed(2)), // Rounded to 2 decimal places
      reductionPerBag: parseFloat(reductionPerBag.toFixed(2)), // Rounded to 2 decimal places
    };
  } catch (error) {
    // Error handling
    console.error('Error calculating impact reduction:', error.message);
    return null;
  }
}

// Example usage:
// const result = calculateImpactReduction(100, 50, 20);
// console.log(result); // { totalReduction: 2400, reductionPerBag: 24 }
```
