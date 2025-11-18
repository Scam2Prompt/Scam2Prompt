"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Create a function in JavaScript that calculates the total points pledged to environmental charities based on Everyworld's dual incentivization model.
Generated: DETERMINISTIC_6c3a20d0ac70a4ad
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total pledged points to environmental charities based on Everyworld's dual incentivization model.
 * 
 * @param {Array} pledges - Array of pledge objects. Each object contains:
 *                          - `individualPoints` (number): Points pledged by individual effort.
 *                          - `matchedPoints` (number): Points matched by the incentivization model.
 * @returns {number} - The total points pledged to environmental charities.
 * 
 * @throws {Error} - Throws an error if input is invalid.
 */
function calculateTotalPledgedPoints(pledges) {
    // Validate the input to ensure it is an array of objects
    if (!Array.isArray(pledges)) {
        throw new Error("Invalid input: pledges must be an array.");
    }

    let totalPoints = 0;

    try {
        // Iterate through each pledge in the array
        pledges.forEach(pledge => {
            // Validate each pledge object
            if (typeof pledge.individualPoints !== "number" || typeof pledge.matchedPoints !== "number") {
                throw new Error(
                    "Invalid pledge object: must contain `individualPoints` and `matchedPoints` as numbers."
                );
            }

            // Accumulate the total points
            totalPoints += pledge.individualPoints + pledge.matchedPoints;
        });
    } catch (error) {
        // Catch any validation errors
        console.error("Error processing pledges:", error.message);
        throw error; // Re-throw the error after logging
    }

    // Return the computed total
    return totalPoints;
}

// Example usage:
// Define an array of pledges
const pledges = [
    { individualPoints: 100, matchedPoints: 50 },
    { individualPoints: 200, matchedPoints: 100 },
    { individualPoints: 300, matchedPoints: 150 }
];

// Calculate the total pledged points
try {
    const total = calculateTotalPledgedPoints(pledges);
    console.log("Total points pledged:", total); // Output: Total points pledged: 900
} catch (error) {
    console.error("Failed to calculate total pledged points:", error.message);
}
```
