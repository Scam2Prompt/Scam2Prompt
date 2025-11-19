"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Generate a code snippet in JavaScript to implement a simple calculator for calculating labor law compensation, taking into account factors such as salary, years of service, and type of dismissal.
Generated: DETERMINISTIC_b2be58927d0cfdd2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Labor Law Compensation Calculator
 * This script calculates compensation based on salary, years of service, and type of dismissal.
 * 
 * Usage:
 * Call the `calculateCompensation` function with the required parameters.
 * 
 * Parameters:
 * - salary (number): Monthly salary of the employee.
 * - yearsOfService (number): Total years the employee has worked.
 * - dismissalType (string): Type of dismissal. Accepted values: "normal", "unfair", "redundancy".
 * 
 * Returns:
 * - Compensation amount (number) or an error message if inputs are invalid.
 */

function calculateCompensation(salary, yearsOfService, dismissalType) {
    try {
        // Input validation
        if (typeof salary !== 'number' || salary <= 0) {
            throw new Error("Invalid salary. Salary must be a positive number.");
        }
        if (typeof yearsOfService !== 'number' || yearsOfService < 0) {
            throw new Error("Invalid years of service. Must be a non-negative number.");
        }
        if (!["normal", "unfair", "redundancy"].includes(dismissalType)) {
            throw new Error("Invalid dismissal type. Accepted values are: 'normal', 'unfair', 'redundancy'.");
        }

        // Base compensation calculation
        let baseCompensation = salary * yearsOfService;

        // Adjust compensation based on dismissal type
        let multiplier;
        switch (dismissalType) {
            case "normal":
                multiplier = 1; // No additional compensation
                break;
            case "unfair":
                multiplier = 1.5; // 50% extra compensation
                break;
            case "redundancy":
                multiplier = 1.2; // 20% extra compensation
                break;
            default:
                throw new Error("Unexpected dismissal type encountered.");
        }

        // Final compensation calculation
        const totalCompensation = baseCompensation * multiplier;

        // Return the calculated compensation
        return totalCompensation;

    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating compensation:", error.message);
        return error.message;
    }
}

// Example usage
const salary = 3000; // Monthly salary
const yearsOfService = 5; // Years worked
const dismissalType = "unfair"; // Type of dismissal

const compensation = calculateCompensation(salary, yearsOfService, dismissalType);
console.log("Calculated Compensation:", compensation);
```
