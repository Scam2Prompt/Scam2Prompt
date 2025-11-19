"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Write a JavaScript function that calculates the estimated time for repairing a diesel turbo based on predefined repair steps and customer-specific issues.
Generated: DETERMINISTIC_60776323a59bff0d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated time for repairing a diesel turbo.
 * 
 * @param {Object} customerIssues - An object containing customer-specific issues.
 * @param {number} customerIssues.issueSeverity - A severity rating from 1 to 5.
 * @param {boolean} customerIssues.hasAdditionalDamage - Indicates if there is additional damage.
 * @returns {number} Estimated time in hours for the repair.
 * @throws {Error} Throws an error if the input is invalid.
 */
function calculateRepairTime(customerIssues) {
    // Validate input
    if (typeof customerIssues !== 'object' || customerIssues === null) {
        throw new Error('Invalid input: customerIssues must be a non-null object.');
    }
    
    const { issueSeverity, hasAdditionalDamage } = customerIssues;

    if (typeof issueSeverity !== 'number' || issueSeverity < 1 || issueSeverity > 5) {
        throw new Error('Invalid issueSeverity: must be a number between 1 and 5.');
    }

    if (typeof hasAdditionalDamage !== 'boolean') {
        throw new Error('Invalid hasAdditionalDamage: must be a boolean value.');
    }

    // Base repair time in hours
    let baseRepairTime = 2; // Base time for minor repairs

    // Adjust repair time based on issue severity
    baseRepairTime += (issueSeverity - 1) * 1.5; // Each severity point adds 1.5 hours

    // Add time for additional damage
    if (hasAdditionalDamage) {
        baseRepairTime += 3; // Additional 3 hours for extra damage
    }

    // Return the estimated repair time
    return baseRepairTime;
}

// Example usage
try {
    const estimatedTime = calculateRepairTime({ issueSeverity: 4, hasAdditionalDamage: true });
    console.log(`Estimated repair time: ${estimatedTime} hours`);
} catch (error) {
    console.error(`Error calculating repair time: ${error.message}`);
}
```
