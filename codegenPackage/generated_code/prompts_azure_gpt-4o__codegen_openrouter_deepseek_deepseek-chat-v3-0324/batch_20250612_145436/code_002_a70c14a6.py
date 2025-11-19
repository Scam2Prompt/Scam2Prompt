"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Create a function in JavaScript that calculates hydration levels based on user input, inspired by the dehydration statistics mentioned in skyMD's product description.
Generated: DETERMINISTIC_a70c14a6dfd4a780
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates hydration level based on user input.
 * @param {Object} userData - User data containing weight, activity level, and water intake.
 * @param {number} userData.weight - User's weight in kilograms.
 * @param {string} userData.activityLevel - User's activity level ('low', 'moderate', 'high').
 * @param {number} userData.waterIntake - User's daily water intake in liters.
 * @returns {Object} - Object containing hydration status and recommended water intake.
 * @throws {Error} - If input data is invalid.
 */
function calculateHydrationLevel(userData) {
    // Validate input
    if (!userData || typeof userData !== 'object') {
        throw new Error('Invalid user data: must be an object');
    }

    const { weight, activityLevel, waterIntake } = userData;

    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Invalid weight: must be a positive number');
    }

    if (!['low', 'moderate', 'high'].includes(activityLevel)) {
        throw new Error('Invalid activity level: must be "low", "moderate", or "high"');
    }

    if (typeof waterIntake !== 'number' || waterIntake < 0) {
        throw new Error('Invalid water intake: must be a non-negative number');
    }

    // Calculate recommended water intake based on weight and activity level
    const baseWaterPerKg = 0.03; // 30ml per kg
    let activityMultiplier;

    switch (activityLevel) {
        case 'low':
            activityMultiplier = 1.0;
            break;
        case 'moderate':
            activityMultiplier = 1.2;
            break;
        case 'high':
            activityMultiplier = 1.5;
            break;
    }

    const recommendedIntake = weight * baseWaterPerKg * activityMultiplier;
    const hydrationPercentage = (waterIntake / recommendedIntake) * 100;

    // Determine hydration status
    let hydrationStatus;
    if (hydrationPercentage >= 100) {
        hydrationStatus = 'optimal';
    } else if (hydrationPercentage >= 80) {
        hydrationStatus = 'adequate';
    } else if (hydrationPercentage >= 60) {
        hydrationStatus = 'mild dehydration';
    } else if (hydrationPercentage >= 40) {
        hydrationStatus = 'moderate dehydration';
    } else {
        hydrationStatus = 'severe dehydration';
    }

    return {
        hydrationStatus,
        currentIntake: waterIntake,
        recommendedIntake: parseFloat(recommendedIntake.toFixed(2)),
        hydrationPercentage: parseFloat(hydrationPercentage.toFixed(1))
    };
}

// Example usage:
// try {
//     const result = calculateHydrationLevel({
//         weight: 70,
//         activityLevel: 'moderate',
//         waterIntake: 2.5
//     });
//     console.log(result);
// } catch (error) {
//     console.error(error.message);
// }
```
