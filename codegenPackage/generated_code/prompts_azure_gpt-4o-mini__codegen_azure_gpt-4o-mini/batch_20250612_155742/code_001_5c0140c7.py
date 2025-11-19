"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Write a JavaScript function that calculates the nutritional benefits of Colágeno Hidrolizado CH+H based on user input about their age and activity level.
Generated: DETERMINISTIC_5c0140c7c0489d50
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the nutritional benefits of Colágeno Hidrolizado CH+H based on user input.
 * 
 * @param {number} age - The age of the user in years.
 * @param {string} activityLevel - The activity level of the user ('low', 'moderate', 'high').
 * @returns {object} - An object containing the recommended daily intake and benefits.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateCollagenBenefits(age, activityLevel) {
    // Validate input types
    if (typeof age !== 'number' || age <= 0) {
        throw new Error('Invalid age. Age must be a positive number.');
    }
    if (typeof activityLevel !== 'string' || !['low', 'moderate', 'high'].includes(activityLevel)) {
        throw new Error('Invalid activity level. Must be one of: low, moderate, high.');
    }

    // Base collagen intake recommendation
    let dailyIntake = 0;

    // Determine daily intake based on age and activity level
    if (age < 30) {
        dailyIntake = 5; // 5g for users under 30
    } else if (age < 50) {
        dailyIntake = 10; // 10g for users between 30 and 49
    } else {
        dailyIntake = 15; // 15g for users 50 and older
    }

    // Adjust intake based on activity level
    switch (activityLevel) {
        case 'low':
            dailyIntake *= 1; // No change for low activity
            break;
        case 'moderate':
            dailyIntake *= 1.2; // Increase by 20% for moderate activity
            break;
        case 'high':
            dailyIntake *= 1.5; // Increase by 50% for high activity
            break;
    }

    // Nutritional benefits
    const benefits = [
        'Supports skin elasticity and hydration',
        'Promotes joint health and mobility',
        'Aids in muscle recovery and growth',
        'Contributes to healthy hair and nails'
    ];

    // Return the results
    return {
        recommendedDailyIntake: dailyIntake.toFixed(2) + 'g',
        benefits: benefits
    };
}

// Example usage
try {
    const userAge = 35; // Example user age
    const userActivityLevel = 'moderate'; // Example user activity level
    const result = calculateCollagenBenefits(userAge, userActivityLevel);
    console.log(result);
} catch (error) {
    console.error('Error calculating collagen benefits:', error.message);
}
```
