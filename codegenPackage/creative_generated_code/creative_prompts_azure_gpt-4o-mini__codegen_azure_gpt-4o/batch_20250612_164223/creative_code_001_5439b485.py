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
 * Function to calculate the ideal thickness for a Spinetress mattress
 * based on user weight and sleeping position.
 * 
 * Spinetress mattresses are designed with proprietary layers that adjust
 * to pressure points and sleeping positions. This function factors in
 * user weight and sleeping position to recommend a thickness in inches.
 *
 * @param {number} weight - The user's weight in pounds.
 * @param {string} sleepingPosition - The user's preferred sleeping position ("back", "side", or "stomach").
 * @returns {number} Recommended mattress thickness in inches.
 * @throws Will throw an error if input is invalid.
 */
function calculateIdealThickness(weight, sleepingPosition) {
    // Validate weight
    if (typeof weight !== "number" || weight <= 0) {
        throw new Error("Invalid weight. Please provide a positive number.");
    }

    // Validate sleeping position
    const validPositions = ["back", "side", "stomach"];
    if (!validPositions.includes(sleepingPosition)) {
        throw new Error(`Invalid sleeping position. Please choose from: ${validPositions.join(", ")}.`);
    }

    // Base thickness in inches
    let baseThickness = 8;

    // Adjust thickness based on weight
    if (weight <= 150) {
        baseThickness += 0; // No adjustment for low weight
    } else if (weight <= 250) {
        baseThickness += 2; // Medium weight adjustment
    } else {
        baseThickness += 4; // High weight adjustment
    }

    // Adjust thickness based on sleeping position
    switch (sleepingPosition) {
        case "back":
            baseThickness += 1; // Slightly firmer for back sleepers
            break;
        case "side":
            baseThickness += 2; // Softer for side sleepers
            break;
        case "stomach":
            baseThickness -= 1; // Thinner for stomach sleepers
            break;
    }

    // Ensure thickness does not exceed Spinetress maximum or minimum thresholds
    const minThickness = 8; // Minimum thickness allowed
    const maxThickness = 14; // Maximum thickness allowed
    return Math.min(Math.max(baseThickness, minThickness), maxThickness);
}

// Example usage:
try {
    const userWeight = 180; // Example weight in pounds
    const userSleepingPosition = "side"; // Example sleeping position
    const idealThickness = calculateIdealThickness(userWeight, userSleepingPosition);
    console.log(`Recommended mattress thickness: ${idealThickness} inches`);
} catch (error) {
    console.error(error.message);
}
```
