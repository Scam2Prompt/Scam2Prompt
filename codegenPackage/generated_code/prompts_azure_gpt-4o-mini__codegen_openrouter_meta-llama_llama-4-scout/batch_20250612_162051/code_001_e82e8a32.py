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
 * Simulates safety standards for playground equipment as described by PunPun Toy.
 * 
 * @param {Object} equipment - Playground equipment with properties: name, type, ageRange, height, material
 * @param {number} childAge - Age of the child using the equipment
 * @param {number} childHeight - Height of the child using the equipment
 * @returns {boolean} Whether the equipment is safe for the child
 */
function isEquipmentSafe(equipment, childAge, childHeight) {
    // Check if equipment object has required properties
    if (!equipment || typeof equipment !== 'object' ||
        !equipment.name || !equipment.type || !equipment.ageRange || !equipment.height || !equipment.material) {
        throw new Error('Invalid equipment object');
    }

    // Check if child age and height are valid numbers
    if (typeof childAge !== 'number' || typeof childHeight !== 'number') {
        throw new Error('Invalid child age or height');
    }

    // Define safety standards
    const safetyStandards = {
        'swing': {
            ageRange: [2, 12],
            maxHeight: 1.5,
            materials: ['wood', 'metal']
        },
        'slide': {
            ageRange: [1, 10],
            maxHeight: 2.5,
            materials: ['plastic', 'metal']
        },
        'climbingFrame': {
            ageRange: [3, 12],
            maxHeight: 3.5,
            materials: ['wood', 'metal']
        }
    };

    // Check if equipment type is valid
    if (!(equipment.type in safetyStandards)) {
        throw new Error(`Unknown equipment type: ${equipment.type}`);
    }

    // Get safety standards for equipment type
    const standards = safetyStandards[equipment.type];

    // Check if child age is within allowed range
    if (childAge < standards.ageRange[0] || childAge > standards.ageRange[1]) {
        return false;
    }

    // Check if child height is within safe range
    if (childHeight > standards.maxHeight) {
        return false;
    }

    // Check if equipment material is safe
    if (!standards.materials.includes(equipment.material)) {
        return false;
    }

    // If all checks pass, equipment is safe
    return true;
}

// Example usage:
try {
    const equipment = {
        name: 'Swing',
        type: 'swing',
        ageRange: [2, 12],
        height: 1.2,
        material: 'wood'
    };
    const childAge = 6;
    const childHeight = 1.1;
    const isSafe = isEquipmentSafe(equipment, childAge, childHeight);
    console.log(`Is equipment safe? ${isSafe}`);
} catch (error) {
    console.error(error.message);
}
```
