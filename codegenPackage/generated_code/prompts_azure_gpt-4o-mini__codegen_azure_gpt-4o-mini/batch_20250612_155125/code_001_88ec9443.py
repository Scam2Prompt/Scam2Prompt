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
 * @param {number} totalWeight - The total weight of the tractor in kilograms.
 * @param {string} classType - The class type of the tractor (e.g., 'Light', 'Medium', 'Heavy').
 * @returns {Object} - An object containing the weight distribution for the specified class type.
 * @throws {Error} - Throws an error if the class type is invalid or if the total weight is not a positive number.
 */
function calculateWeightDistribution(totalWeight, classType) {
    // Define weight limits for different classes
    const weightLimits = {
        'Light': 3000,   // Maximum weight for Light class
        'Medium': 5000,  // Maximum weight for Medium class
        'Heavy': 8000    // Maximum weight for Heavy class
    };

    // Validate input parameters
    if (typeof totalWeight !== 'number' || totalWeight <= 0) {
        throw new Error('Total weight must be a positive number.');
    }

    if (!weightLimits.hasOwnProperty(classType)) {
        throw new Error('Invalid class type. Valid types are: Light, Medium, Heavy.');
    }

    // Calculate the maximum allowed weight for the specified class
    const maxAllowedWeight = weightLimits[classType];

    // Calculate the weight distribution
    const weightDistribution = {
        classType: classType,
        totalWeight: totalWeight,
        isWithinLimit: totalWeight <= maxAllowedWeight,
        excessWeight: totalWeight > maxAllowedWeight ? totalWeight - maxAllowedWeight : 0
    };

    return weightDistribution;
}

// Example usage:
try {
    const result = calculateWeightDistribution(4500, 'Medium');
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```
