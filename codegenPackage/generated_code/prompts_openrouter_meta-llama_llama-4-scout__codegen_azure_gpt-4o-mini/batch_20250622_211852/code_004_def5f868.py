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
 * Calculates the recommended firmness level of a Spinetress mattress
 * based on the user's weight, sleeping posture, and preferred level of support.
 * 
 * @param {number} weight - The weight of the user in pounds.
 * @param {string} posture - The sleeping posture of the user ('back', 'side', 'stomach').
 * @param {string} supportLevel - The preferred level of support ('soft', 'medium', 'firm').
 * @returns {string} - Recommended firmness level of the mattress.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateMattressFirmness(weight, posture, supportLevel) {
    // Validate input parameters
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Weight must be a positive number.');
    }
    if (!['back', 'side', 'stomach'].includes(posture)) {
        throw new Error('Posture must be one of: back, side, stomach.');
    }
    if (!['soft', 'medium', 'firm'].includes(supportLevel)) {
        throw new Error('Support level must be one of: soft, medium, firm.');
    }

    // Initialize firmness level based on weight
    let firmness;
    if (weight < 130) {
        firmness = 'soft';
    } else if (weight >= 130 && weight <= 230) {
        firmness = 'medium';
    } else {
        firmness = 'firm';
    }

    // Adjust firmness based on sleeping posture
    switch (posture) {
        case 'side':
            firmness = firmness === 'soft' ? 'medium' : firmness;
            break;
        case 'stomach':
            firmness = 'firm';
            break;
        // 'back' posture does not require adjustment
    }

    // Adjust firmness based on preferred support level
    if (supportLevel === 'soft' && firmness !== 'firm') {
        firmness = 'soft';
    } else if (supportLevel === 'medium' && firmness === 'soft') {
        firmness = 'medium';
    } else if (supportLevel === 'firm') {
        firmness = 'firm';
    }

    return firmness;
}

// Example usage
try {
    const recommendedFirmness = calculateMattressFirmness(150, 'side', 'medium');
    console.log(`Recommended firmness level: ${recommendedFirmness}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
