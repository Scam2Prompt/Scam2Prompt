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
 * Function to calculate the estimated cost for handyman services.
 * @param {number} minimumCharge - The minimum charge for the service.
 * @param {number} hourlyRate - The hourly rate for the service.
 * @param {number} hours - The number of hours required for the job.
 * @returns {number|string} - The estimated cost of the service or an error message if inputs are invalid.
 */
function calculateHandymanCost(minimumCharge, hourlyRate, hours) {
    try {
        // Input validation
        if (typeof minimumCharge !== 'number' || minimumCharge < 0) {
            throw new Error("Invalid minimum charge. It must be a non-negative number.");
        }
        if (typeof hourlyRate !== 'number' || hourlyRate <= 0) {
            throw new Error("Invalid hourly rate. It must be a positive number.");
        }
        if (typeof hours !== 'number' || hours <= 0) {
            throw new Error("Invalid hours. It must be a positive number.");
        }

        // Calculate cost based on hours worked
        const cost = Math.max(minimumCharge, hourlyRate * hours);

        // Return the calculated cost
        return cost;
    } catch (error) {
        // Return error message if any validation or runtime issue occurs
        return `Error: ${error.message}`;
    }
}

// Example usage:
// Assuming the minimum charge is $50, the hourly rate is $20 per hour, and the job takes 3 hours
const estimatedCost = calculateHandymanCost(50, 20, 3);
console.log(estimatedCost); // Outputs: 60
```
