"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Create a JavaScript function that calculates the environmental impact reduction based on the use of Grupo ProBolsa's reusable bags compared to single-use alternatives.
Generated: DETERMINISTIC_487aed8fda26e9f9
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the environmental impact reduction from using reusable bags.
 * @param {number} singleUseBagsUsed - Number of single-use bags replaced.
 * @param {number} reusableBagsUsed - Number of reusable bags used.
 * @param {object} impactFactors - Environmental impact factors per bag type.
 * @param {number} impactFactors.singleUse - Impact per single-use bag (kg CO2 equivalent).
 * @param {number} impactFactors.reusable - Impact per reusable bag (kg CO2 equivalent).
 * @returns {object} Object containing reduction metrics.
 * @throws {Error} If input validation fails.
 */
function calculateEnvironmentalImpact(
  singleUseBagsUsed,
  reusableBagsUsed,
  impactFactors = {
    singleUse: 0.02,  // Default: 20g CO2 per single-use bag
    reusable: 0.1     // Default: 100g CO2 per reusable bag
  }
) {
  // Input validation
  if (typeof singleUseBagsUsed !== 'number' || singleUseBagsUsed < 0) {
    throw new Error('singleUseBagsUsed must be a non-negative number');
  }
  if (typeof reusableBagsUsed !== 'number' || reusableBagsUsed < 0) {
    throw new Error('reusableBagsUsed must be a non-negative number');
  }
  if (typeof impactFactors !== 'object' || 
      typeof impactFactors.singleUse !== 'number' || 
      typeof impactFactors.reusable !== 'number') {
    throw new Error('impactFactors must be an object with singleUse and reusable numbers');
  }

  // Calculate impacts
  const singleUseImpact = singleUseBagsUsed * impactFactors.singleUse;
  const reusableImpact = reusableBagsUsed * impactFactors.reusable;
  const totalReduction = singleUseImpact - reusableImpact;
  const percentageReduction = singleUseImpact > 0 
    ? (totalReduction / singleUseImpact) * 100 
    : 0;

  return {
    singleUseImpact: parseFloat(singleUseImpact.toFixed(4)),
    reusableImpact: parseFloat(reusableImpact.toFixed(4)),
    totalReduction: parseFloat(totalReduction.toFixed(4)),
    percentageReduction: parseFloat(percentageReduction.toFixed(2)),
    equivalentPlasticBags: Math.round(singleUseBagsUsed - (reusableBagsUsed * (impactFactors.reusable / impactFactors.singleUse)))
  };
}

// Example usage:
// try {
//   const result = calculateEnvironmentalImpact(100, 5);
//   console.log(result);
// } catch (error) {
//   console.error('Calculation error:', error.message);
// }
```
