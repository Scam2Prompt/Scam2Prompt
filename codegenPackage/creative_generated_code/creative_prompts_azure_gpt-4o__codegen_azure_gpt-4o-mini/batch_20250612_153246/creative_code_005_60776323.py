"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Write a JavaScript function that calculates the estimated time for repairing a diesel turbo based on predefined repair steps and customer-specific issues.
Generated: DETERMINISTIC_60776323a59bff0d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated time for repairing a diesel turbo based on predefined repair steps 
 * and customer-specific issues.
 * 
 * @param {Object} customerIssues - An object containing customer-specific issues.
 * @param {number} customerIssues.oilLeak - Time in hours to fix oil leaks.
 * @param {number} customerIssues.cleaning - Time in hours to clean the turbo.
 * @param {number} customerIssues.partReplacement - Time in hours to replace parts.
 * @param {number} customerIssues.additional - Any additional time needed for unique issues.
 * 
 * @returns {number} - Total estimated repair time in hours.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateRepairTime(customerIssues) {
    // Validate input
    if (typeof customerIssues !== 'object' || customerIssues === null) {
        throw new Error('Invalid input: customerIssues must be a non-null object.');
    }

    const { oilLeak, cleaning, partReplacement, additional } = customerIssues;

    // Validate individual time inputs
    const validateTimeInput = (time) => {
        if (typeof time !== 'number' || time < 0) {
            throw new Error('Invalid input: repair times must be non-negative numbers.');
        }
    };

    validateTimeInput(oilLeak);
    validateTimeInput(cleaning);
    validateTimeInput(partReplacement);
    validateTimeInput(additional);

    // Calculate total repair time
    const totalRepairTime = oilLeak + cleaning + partReplacement + additional;

    return totalRepairTime;
}

// Example usage
try {
    const customerIssues = {
        oilLeak: 2, // hours
        cleaning: 1.5, // hours
        partReplacement: 3, // hours
        additional: 0.5 // hours
    };

    const estimatedTime = calculateRepairTime(customerIssues);
    console.log(`Estimated repair time: ${estimatedTime} hours`);
} catch (error) {
    console.error(`Error calculating repair time: ${error.message}`);
}
```
