"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Write a JavaScript snippet that calculates the ideal thickness for a Spinetress mattress based on user weight and sleeping position, incorporating the unique features of the Spinetress product line.
Generated: DETERMINISTIC_5439b4853eb043b8
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the ideal thickness for a Spinetress mattress
 * based on user weight and sleeping position.
 * 
 * Spinetress mattresses are designed with unique features to provide
 * optimal support and comfort. This function uses predefined rules
 * to determine the ideal thickness.
 * 
 * @param {number} weight - The user's weight in kilograms.
 * @param {string} position - The user's sleeping position ('back', 'side', 'stomach').
 * @returns {number} - The ideal mattress thickness in centimeters.
 * @throws {Error} - Throws an error if input is invalid.
 */
function calculateIdealThickness(weight, position) {
    // Validate input
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error("Invalid weight. Weight must be a positive number.");
    }
    if (typeof position !== 'string' || !['back', 'side', 'stomach'].includes(position.toLowerCase())) {
        throw new Error("Invalid sleeping position. Must be 'back', 'side', or 'stomach'.");
    }

    // Define base thickness values for Spinetress mattresses
    const baseThickness = {
        back: 20,    // Base thickness for back sleepers
        side: 25,    // Base thickness for side sleepers
        stomach: 18  // Base thickness for stomach sleepers
    };

    // Adjust thickness based on weight
    let weightAdjustment;
    if (weight < 50) {
        weightAdjustment = -2; // Lighter individuals need less thickness
    } else if (weight <= 100) {
        weightAdjustment = 0;  // Average weight requires no adjustment
    } else {
        weightAdjustment = 3;  // Heavier individuals need more thickness
    }

    // Calculate ideal thickness
    const idealThickness = baseThickness[position.toLowerCase()] + weightAdjustment;

    // Ensure thickness is within reasonable bounds
    const minThickness = 15; // Minimum thickness for Spinetress mattresses
    const maxThickness = 30; // Maximum thickness for Spinetress mattresses
    return Math.min(Math.max(idealThickness, minThickness), maxThickness);
}

// Example usage:
try {
    const userWeight = 75; // User's weight in kilograms
    const userPosition = 'side'; // User's sleeping position
    const mattressThickness = calculateIdealThickness(userWeight, userPosition);
    console.log(`Ideal mattress thickness: ${mattressThickness} cm`);
} catch (error) {
    console.error(error.message);
}
```
