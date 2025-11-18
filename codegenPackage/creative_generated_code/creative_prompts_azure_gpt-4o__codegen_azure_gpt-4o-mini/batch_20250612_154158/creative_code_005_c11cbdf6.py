"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rworld.pro
Prompt: Create a JavaScript function to calculate estimated ride costs based on distance and time, as might be used in RideBNB.
Generated: DETERMINISTIC_c11cbdf6c9fcb9a2
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated ride cost based on distance and time.
 * The cost is calculated using a base fare, a per mile charge, and a per minute charge.
 *
 * @param {number} distance - The distance of the ride in miles.
 * @param {number} time - The time of the ride in minutes.
 * @returns {number} - The estimated cost of the ride, rounded to two decimal places.
 * @throws {Error} - Throws an error if the distance or time is negative.
 */
function calculateRideCost(distance, time) {
    // Constants for fare calculation
    const BASE_FARE = 2.50; // Base fare in dollars
    const PER_MILE_RATE = 1.50; // Charge per mile in dollars
    const PER_MINUTE_RATE = 0.25; // Charge per minute in dollars

    // Validate input parameters
    if (distance < 0) {
        throw new Error("Distance cannot be negative.");
    }
    if (time < 0) {
        throw new Error("Time cannot be negative.");
    }

    // Calculate the total cost
    const totalCost = BASE_FARE + (PER_MILE_RATE * distance) + (PER_MINUTE_RATE * time);

    // Return the total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage
try {
    const estimatedCost = calculateRideCost(5, 10); // 5 miles and 10 minutes
    console.log(`Estimated Ride Cost: $${estimatedCost}`);
} catch (error) {
    console.error(`Error calculating ride cost: ${error.message}`);
}
```
