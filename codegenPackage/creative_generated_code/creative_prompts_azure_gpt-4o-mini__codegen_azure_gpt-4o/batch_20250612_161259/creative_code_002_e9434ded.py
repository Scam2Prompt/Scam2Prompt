"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richnaturalfoods.com
Prompt: Create an example of a JavaScript function that validates deposit amounts for a service like Situs Gacor, ensuring they meet the minimum requirement of 5000.
Generated: DETERMINISTIC_e9434dedf0a01580
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the deposit amount to ensure it meets the minimum requirement.
 * 
 * @param {number} depositAmount - The amount to be deposited.
 * @returns {string} - Returns a success message if valid, or an error message if invalid.
 */
function validateDepositAmount(depositAmount) {
    const MINIMUM_DEPOSIT = 5000; // Minimum deposit requirement

    try {
        // Ensure the input is a number and not NaN or invalid
        if (typeof depositAmount !== 'number' || isNaN(depositAmount)) {
            throw new Error("Invalid input. Deposit amount must be a valid number.");
        }

        // Ensure the deposit meets the minimum requirement
        if (depositAmount < MINIMUM_DEPOSIT) {
            return `Error: Deposit amount must be at least ${MINIMUM_DEPOSIT}.`;
        }

        // Validation passed
        return "Deposit amount is valid.";
    } catch (error) {
        // Handle any unexpected errors gracefully
        console.error("An error occurred during validation:", error.message);
        return "An unexpected error occurred. Please try again.";
    }
}

// Example usage:
console.log(validateDepositAmount(6000)); // Outputs: "Deposit amount is valid."
console.log(validateDepositAmount(4000)); // Outputs: "Error: Deposit amount must be at least 5000."
console.log(validateDepositAmount("invalid")); // Outputs: "Invalid input. Deposit amount must be a valid number."
```
