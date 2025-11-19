"""
Generated Code Metadata:
========================
Original URL: https://www.punpuntoy.com
Prompt: Generate a JavaScript function that simulates the safety standards for playground equipment as described by PunPun Toy.
Generated: DETERMINISTIC_e82e8a32e3122c09
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the safety standards for playground equipment as described by PunPun Toy.
 * 
 * @param {Object} equipment - The playground equipment to be evaluated.
 * @param {string} equipment.type - The type of equipment (e.g., 'swing', 'slide', 'climbing frame').
 * @param {number} equipment.height - The height of the equipment in meters.
 * @param {number} equipment.ageGroup - The recommended age group for the equipment (in years).
 * @returns {Object} - An object containing the safety evaluation results.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function evaluatePlaygroundEquipment(equipment) {
    // Validate input
    if (!equipment || typeof equipment !== 'object') {
        throw new Error('Invalid input: equipment must be an object.');
    }
    if (!equipment.type || typeof equipment.type !== 'string') {
        throw new Error('Invalid input: equipment type must be a non-empty string.');
    }
    if (typeof equipment.height !== 'number' || equipment.height <= 0) {
        throw new Error('Invalid input: equipment height must be a positive number.');
    }
    if (typeof equipment.ageGroup !== 'number' || equipment.ageGroup <= 0) {
        throw new Error('Invalid input: equipment age group must be a positive number.');
    }

    // Define safety standards
    const safetyStandards = {
        swing: { maxHeight: 3, minAge: 3, maxAge: 12 },
        slide: { maxHeight: 2.5, minAge: 2, maxAge: 10 },
        climbingFrame: { maxHeight: 3.5, minAge: 5, maxAge: 15 }
    };

    // Get the safety standard for the given equipment type
    const standard = safetyStandards[equipment.type.toLowerCase()];

    // Check if the equipment type is recognized
    if (!standard) {
        throw new Error(`Unknown equipment type: ${equipment.type}`);
    }

    // Evaluate safety based on height and age group
    const isHeightSafe = equipment.height <= standard.maxHeight;
    const isAgeGroupSafe = equipment.ageGroup >= standard.minAge && equipment.ageGroup <= standard.maxAge;

    // Prepare the evaluation result
    const result = {
        type: equipment.type,
        height: equipment.height,
        ageGroup: equipment.ageGroup,
        isHeightSafe: isHeightSafe,
        isAgeGroupSafe: isAgeGroupSafe,
        isSafe: isHeightSafe && isAgeGroupSafe
    };

    return result;
}

// Example usage
try {
    const equipment = {
        type: 'swing',
        height: 2.5,
        ageGroup: 5
    };
    const evaluation = evaluatePlaygroundEquipment(equipment);
    console.log(evaluation);
} catch (error) {
    console.error('Error evaluating playground equipment:', error.message);
}
```
