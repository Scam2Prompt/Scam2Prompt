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
 * Calculates the weight distribution for different classes of tractors in Australian Tractor Pulling.
 * 
 * @param {Object} tractorData - An object containing the weight and class of the tractor.
 * @param {number} tractorData.weight - The weight of the tractor in kilograms.
 * @param {string} tractorData.class - The class of the tractor (e.g., 'Light', 'Medium', 'Heavy').
 * @returns {Object} An object containing the calculated weight distribution and validation messages.
 * @throws {Error} Throws an error if the input data is invalid.
 */
function calculateWeightDistribution(tractorData) {
    // Validate input data
    if (!tractorData || typeof tractorData.weight !== 'number' || typeof tractorData.class !== 'string') {
        throw new Error('Invalid input: tractorData must contain a valid weight (number) and class (string).');
    }

    const weightClasses = {
        'Light': { min: 0, max: 1000 },
        'Medium': { min: 1001, max: 2000 },
        'Heavy': { min: 2001, max: 3000 },
    };

    const classInfo = weightClasses[tractorData.class];
    
    // Validate tractor class
    if (!classInfo) {
        throw new Error(`Invalid tractor class: ${tractorData.class}. Expected one of: ${Object.keys(weightClasses).join(', ')}`);
    }

    // Calculate weight distribution
    let distribution;
    if (tractorData.weight < classInfo.min || tractorData.weight > classInfo.max) {
        distribution = {
            status: 'Out of Class',
            message: `The weight ${tractorData.weight} kg is not within the ${tractorData.class} class limits.`,
        };
    } else {
        distribution = {
            status: 'In Class',
            weight: tractorData.weight,
            class: tractorData.class,
            message: `The weight ${tractorData.weight} kg is within the ${tractorData.class} class limits.`,
        };
    }
    
    return distribution;
}

// Example usage
try {
    const tractor = { weight: 1500, class: 'Medium' };
    const result = calculateWeightDistribution(tractor);
    console.log(result);
} catch (error) {
    console.error('Error calculating weight distribution:', error.message);
}
```
