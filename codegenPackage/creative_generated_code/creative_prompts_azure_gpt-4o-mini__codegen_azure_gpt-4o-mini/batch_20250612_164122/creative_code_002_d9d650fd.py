"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://handyfix.co.nz
Prompt: Create a JavaScript function that calculates the estimated cost for handyman services based on a minimum charge and hourly rate mentioned on the Handyfix website.
Generated: DETERMINISTIC_d9d650fd93d8262f
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost for handyman services.
 * 
 * @param {number} hours Worked hours. Must be a non-negative number.
 * @param {number} hourlyRate Hourly rate for services. Must be a non-negative number.
 * @param {number} minimumCharge Minimum charge for services. Must be a non-negative number.
 * @returns {number} The estimated cost for the handyman services.
 * @throws {Error} If any of the parameters are not non-negative numbers.
 */
function calculateHandymanCost(hours, hourlyRate, minimumCharge) {
    // Validate input parameters
    if (typeof hours !== 'number' || hours < 0) {
        throw new Error('Invalid input: hours must be a non-negative number.');
    }
    if (typeof hourlyRate !== 'number' || hourlyRate < 0) {
        throw new Error('Invalid input: hourlyRate must be a non-negative number.');
    }
    if (typeof minimumCharge !== 'number' || minimumCharge < 0) {
        throw new Error('Invalid input: minimumCharge must be a non-negative number.');
    }

    // Calculate total cost based on hours and hourly rate
    const totalCost = hours * hourlyRate;

    // Return the greater of total cost or minimum charge
    return Math.max(totalCost, minimumCharge);
}

// Example usage:
try {
    const estimatedCost = calculateHandymanCost(3, 50, 100);
    console.log(`Estimated Cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
