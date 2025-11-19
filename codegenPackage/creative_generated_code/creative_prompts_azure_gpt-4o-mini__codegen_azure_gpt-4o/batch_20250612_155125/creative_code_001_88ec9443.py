"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Write a JavaScript function to calculate the weight distribution for different classes of tractors in Australian Tractor Pulling as described on Jobbo.com.au.
Generated: DETERMINISTIC_88ec944397548c4a
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate weight distribution for different classes of tractors
 * in Australian Tractor Pulling based on specifications from Jobbo.com.au.
 *
 * @param {string} tractorClass - The class of the tractor (e.g., "Lightweight", "Middleweight", "Heavyweight").
 * @param {number} totalWeight - The total weight of the tractor (in kilograms).
 * @returns {object} - An object containing the weight distribution for front and rear axles.
 * @throws Will throw an error if tractorClass is invalid or totalWeight is non-positive.
 */
function calculateWeightDistribution(tractorClass, totalWeight) {
  // Validate inputs
  if (totalWeight <= 0) {
    throw new Error("Total weight must be a positive number.");
  }
  if (!tractorClass || typeof tractorClass !== "string") {
    throw new Error("Invalid tractor class. Must be a non-empty string.");
  }

  // Define weight distribution percentages based on tractor class
  const weightDistribution = {
    Lightweight: { front: 0.4, rear: 0.6 }, // 40% front, 60% rear
    Middleweight: { front: 0.45, rear: 0.55 }, // 45% front, 55% rear
    Heavyweight: { front: 0.5, rear: 0.5 }, // 50% front, 50% rear
  };

  // Check if the tractor class is valid
  const distribution = weightDistribution[tractorClass];
  if (!distribution) {
    throw new Error(
      `Invalid tractor class '${tractorClass}'. Valid classes are: ${Object.keys(weightDistribution).join(", ")}.`
    );
  }

  // Calculate front and rear axle weights
  const frontAxleWeight = totalWeight * distribution.front;
  const rearAxleWeight = totalWeight * distribution.rear;

  // Return the weight distribution as an object
  return {
    frontAxleWeight: parseFloat(frontAxleWeight.toFixed(2)), // Rounded to 2 decimal places
    rearAxleWeight: parseFloat(rearAxleWeight.toFixed(2)), // Rounded to 2 decimal places
  };
}

// Example usage:
try {
  const result = calculateWeightDistribution("Middleweight", 3000);
  console.log("Weight Distribution:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
