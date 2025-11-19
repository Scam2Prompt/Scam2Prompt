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
 * Calculates the total cost of a course based on the program type and additional fees.
 * 
 * @param {string} program - The name of the program (e.g., "Graduate Diploma of Management (Learning)").
 * @param {number} baseCost - The base cost of the program.
 * @param {number} additionalFees - Any additional fees associated with the program.
 * @returns {number} - The total cost of the course.
 * @throws {Error} - Throws an error if the program name is invalid or if costs are negative.
 */
function calculateTotalCost(program, baseCost, additionalFees = 0) {
    // Validate input parameters
    if (typeof program !== 'string' || program.trim() === '') {
        throw new Error('Invalid program name. It must be a non-empty string.');
    }
    if (typeof baseCost !== 'number' || baseCost < 0) {
        throw new Error('Invalid base cost. It must be a non-negative number.');
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error('Invalid additional fees. It must be a non-negative number.');
    }

    // Calculate total cost
    const totalCost = baseCost + additionalFees;

    // Return the total cost
    return totalCost;
}

// Example usage
try {
    const programName = "Graduate Diploma of Management (Learning)";
    const baseCost = 18000; // Base cost for the program
    const additionalFees = 0; // No additional fees

    const totalCost = calculateTotalCost(programName, baseCost, additionalFees);
    console.log(`The total cost for the ${programName} is $${totalCost.toFixed(2)}.`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
