"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Write a JavaScript snippet that calculates the ideal thickness for a Spinetress mattress based on user weight and sleeping position, incorporating the unique features of the Spinetress product line.
Generated: DETERMINISTIC_5439b4853eb043b8
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the ideal thickness for a Spinetress mattress based on user weight and sleeping position.
 * The Spinetress mattress is designed with unique features to provide optimal support and comfort.
 * 
 * @param {number} weight - The weight of the user in kilograms.
 * @param {string} position - The sleeping position of the user ('back', 'side', 'stomach').
 * @returns {number} - The recommended mattress thickness in centimeters.
 * @throws {Error} - Throws an error if weight is not a positive number or if position is invalid.
 */
function calculateMattressThickness(weight, position) {
    // Validate input parameters
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Weight must be a positive number.');
    }
    
    const validPositions = ['back', 'side', 'stomach'];
    if (!validPositions.includes(position)) {
        throw new Error(`Invalid sleeping position. Must be one of: ${validPositions.join(', ')}.`);
    }

    // Initialize base thickness
    let thickness = 15; // Base thickness in cm

    // Adjust thickness based on weight
    if (weight > 100) {
        thickness += 5; // Add 5 cm for users over 100 kg
    }

    // Adjust thickness based on sleeping position
    switch (position) {
        case 'side':
            thickness += 3; // Add 3 cm for side sleepers
            break;
        case 'stomach':
            thickness -= 2; // Reduce 2 cm for stomach sleepers
            break;
        case 'back':
            // No adjustment for back sleepers
            break;
        default:
            throw new Error('Unexpected error in sleeping position logic.');
    }

    // Ensure minimum thickness of 15 cm
    return Math.max(thickness, 15);
}

// Example usage of the function
try {
    const userWeight = 85; // User weight in kg
    const userPosition = 'side'; // User sleeping position
    const idealThickness = calculateMattressThickness(userWeight, userPosition);
    console.log(`The ideal mattress thickness for a ${userPosition} sleeper weighing ${userWeight} kg is ${idealThickness} cm.`);
} catch (error) {
    console.error(error.message);
}
```
