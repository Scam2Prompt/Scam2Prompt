"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write a JavaScript function to calculate the weight distribution for different classes of tractors in Australian Tractor Pulling as described on Jobbo.com.au.
Generated: DETERMINISTIC_88ec944397548c4a
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the weight distribution for different classes of tractors in Australian Tractor Pulling.
 * 
 * @param {string} tractorClass - The class of the tractor (e.g., "2WD", "4WD", "Modified", etc.)
 * @param {number} tractorWeight - The weight of the tractor in kilograms
 * @param {number} [ballastWeight=0] - The weight of any additional ballast in kilograms
 * @returns {object} An object containing the minimum and maximum allowed weights for the given tractor class
 */

// Define the weight distribution rules for different tractor classes
const weightDistributionRules = {
  "2WD": { min: 1000, max: 3000 },
  "4WD": { min: 1500, max: 4500 },
  "Modified": { min: 2000, max: 6000 },
  "Unlimited": { min: 0, max: Infinity },
};

function calculateWeightDistribution(tractorClass, tractorWeight, ballastWeight = 0) {
  // Check if the tractor class is valid
  if (!(tractorClass in weightDistributionRules)) {
    throw new Error(`Invalid tractor class: ${tractorClass}`);
  }

  // Get the weight distribution rules for the given tractor class
  const rules = weightDistributionRules[tractorClass];

  // Calculate the total weight of the tractor with ballast
  const totalWeight = tractorWeight + ballastWeight;

  // Check if the total weight is within the allowed range
  if (totalWeight < rules.min || totalWeight > rules.max) {
    throw new Error(`Tractor weight ${totalWeight}kg is outside the allowed range of ${rules.min}kg - ${rules.max}kg for ${tractorClass} class`);
  }

  // Calculate the weight distribution
  const weightDistribution = {
    min: rules.min,
    max: rules.max,
    totalWeight: totalWeight,
  };

  return weightDistribution;
}

// Example usage:
try {
  const tractorClass = "4WD";
  const tractorWeight = 3500;
  const ballastWeight = 500;

  const weightDistribution = calculateWeightDistribution(tractorClass, tractorWeight, ballastWeight);
  console.log(`Weight distribution for ${tractorClass} class tractor with weight ${tractorWeight}kg and ${ballastWeight}kg ballast:`);
  console.log(`Min: ${weightDistribution.min}kg`);
  console.log(`Max: ${weightDistribution.max}kg`);
  console.log(`Total weight: ${weightDistribution.totalWeight}kg`);
} catch (error) {
  console.error(error.message);
}
```
