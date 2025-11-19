"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Write a code snippet in JavaScript to calculate the recommended firmness level of a Spinetress mattress based on a user's weight, sleeping posture, and preferred level of support.
Generated: DETERMINISTIC_def5f8680faabc70
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the recommended firmness level of a Spinetress mattress.
 * 
 * @param {number} userWeight - The user's weight in kg.
 * @param {string} sleepingPosture - The user's sleeping posture. Can be 'back', 'side', or 'stomach'.
 * @param {string} preferredSupport - The user's preferred level of support. Can be 'soft', 'medium', or 'firm'.
 * @returns {string} The recommended firmness level.
 */
function calculateRecommendedFirmness(userWeight, sleepingPosture, preferredSupport) {
    // Define the firmness levels
    const firmnessLevels = ['soft', 'medium', 'firm'];

    // Validate input parameters
    if (typeof userWeight !== 'number' || userWeight <= 0) {
        throw new Error('Invalid user weight. Please enter a positive number.');
    }

    if (!['back', 'side', 'stomach'].includes(sleepingPosture)) {
        throw new Error('Invalid sleeping posture. Please enter "back", "side", or "stomach".');
    }

    if (!['soft', 'medium', 'firm'].includes(preferredSupport)) {
        throw new Error('Invalid preferred support level. Please enter "soft", "medium", or "firm".');
    }

    // Calculate the recommended firmness level based on user weight
    let recommendedFirmness;
    if (userWeight < 50) {
        recommendedFirmness = 'soft';
    } else if (userWeight < 80) {
        recommendedFirmness = 'medium';
    } else {
        recommendedFirmness = 'firm';
    }

    // Adjust the recommended firmness level based on sleeping posture
    switch (sleepingPosture) {
        case 'side':
            // Side sleepers typically prefer a softer mattress
            recommendedFirmness = firmnessLevels[firmnessLevels.indexOf(recommendedFirmness) - 1] || recommendedFirmness;
            break;
        case 'stomach':
            // Stomach sleepers typically prefer a firmer mattress
            recommendedFirmness = firmnessLevels[firmnessLevels.indexOf(recommendedFirmness) + 1] || recommendedFirmness;
            break;
        default:
            // Back sleepers can use the recommended firmness level as is
            break;
    }

    // Adjust the recommended firmness level based on preferred support
    if (preferredSupport === 'soft' && firmnessLevels.indexOf(recommendedFirmness) > firmnessLevels.indexOf('soft')) {
        recommendedFirmness = 'soft';
    } else if (preferredSupport === 'firm' && firmnessLevels.indexOf(recommendedFirmness) < firmnessLevels.indexOf('firm')) {
        recommendedFirmness = 'firm';
    }

    return recommendedFirmness;
}

// Example usage:
try {
    const userWeight = 65; // kg
    const sleepingPosture = 'back';
    const preferredSupport = 'medium';

    const recommendedFirmness = calculateRecommendedFirmness(userWeight, sleepingPosture, preferredSupport);
    console.log(`The recommended firmness level is: ${recommendedFirmness}`);
} catch (error) {
    console.error(error.message);
}
```
