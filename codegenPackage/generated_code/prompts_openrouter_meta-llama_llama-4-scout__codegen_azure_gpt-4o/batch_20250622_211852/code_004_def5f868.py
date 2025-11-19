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
 * Function to calculate the recommended firmness level of a Spinetress mattress.
 * 
 * @param {number} weight - The user's weight in kilograms.
 * @param {string} sleepingPosture - The user's sleeping posture. Accepted values: 'back', 'side', 'stomach'.
 * @param {string} supportPreference - The user's preferred level of support. Accepted values: 'soft', 'medium', 'firm'.
 * @returns {string} - The recommended firmness level. Possible values: 'soft', 'medium', 'firm', 'extra firm'.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateMattressFirmness(weight, sleepingPosture, supportPreference) {
    // Validate weight
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error("Invalid weight. Please provide a positive number.");
    }

    // Validate sleeping posture
    const validPostures = ['back', 'side', 'stomach'];
    if (!validPostures.includes(sleepingPosture)) {
        throw new Error(`Invalid sleeping posture. Accepted values are: ${validPostures.join(', ')}`);
    }

    // Validate support preference
    const validSupportPreferences = ['soft', 'medium', 'firm'];
    if (!validSupportPreferences.includes(supportPreference)) {
        throw new Error(`Invalid support preference. Accepted values are: ${validSupportPreferences.join(', ')}`);
    }

    // Determine base firmness based on weight
    let baseFirmness;
    if (weight < 60) {
        baseFirmness = 'soft';
    } else if (weight >= 60 && weight <= 90) {
        baseFirmness = 'medium';
    } else {
        baseFirmness = 'firm';
    }

    // Adjust firmness based on sleeping posture
    if (sleepingPosture === 'side') {
        if (baseFirmness === 'firm') baseFirmness = 'medium';
    } else if (sleepingPosture === 'stomach') {
        if (baseFirmness === 'soft') baseFirmness = 'medium';
    }

    // Further adjust firmness based on support preference
    if (supportPreference === 'soft' && baseFirmness !== 'soft') {
        baseFirmness = 'soft';
    } else if (supportPreference === 'firm' && baseFirmness !== 'firm') {
        baseFirmness = baseFirmness === 'soft' ? 'medium' : 'firm';
    }

    // Handle edge cases for extra firm recommendation
    if (weight > 100 && supportPreference === 'firm') {
        return 'extra firm';
    }

    return baseFirmness;
}

// Example usage:
try {
    const firmness = calculateMattressFirmness(75, 'back', 'medium');
    console.log(`Recommended firmness level: ${firmness}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
