"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Develop a JavaScript function to calculate the total cost of a course, including the 76-week Graduate Diploma of Management (Learning) program for $18,000.
Generated: DETERMINISTIC_2be3bdb8054a8a70
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of a course.
 * Includes error handling and validation for input parameters.
 * 
 * @param {number} baseCost - The base cost of the course in dollars.
 * @param {number} durationWeeks - The duration of the course in weeks.
 * @param {number} additionalFees - Any additional fees to be added to the base cost.
 * @returns {number} - The total cost of the course.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateTotalCourseCost(baseCost, durationWeeks, additionalFees = 0) {
    // Validate input parameters
    if (typeof baseCost !== 'number' || baseCost <= 0) {
        throw new Error("Invalid base cost. It must be a positive number.");
    }
    if (typeof durationWeeks !== 'number' || durationWeeks <= 0) {
        throw new Error("Invalid duration. It must be a positive number.");
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error("Invalid additional fees. It must be a non-negative number.");
    }

    // Calculate total cost
    const totalCost = baseCost + additionalFees;

    // Return the total cost
    return totalCost;
}

// Example usage:
try {
    const baseCost = 18000; // Base cost of the Graduate Diploma of Management (Learning) program
    const durationWeeks = 76; // Duration of the program in weeks
    const additionalFees = 0; // No additional fees for this example

    const totalCost = calculateTotalCourseCost(baseCost, durationWeeks, additionalFees);
    console.log(`The total cost of the course is $${totalCost}.`);
} catch (error) {
    console.error(`Error calculating course cost: ${error.message}`);
}
```
