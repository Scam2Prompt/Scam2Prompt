"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Develop a JavaScript function to validate the eligibility criteria for SOMTU MBA admission based on the provided requirements, such as CGPA and percentage.
Generated: DETERMINISTIC_ffebfaa74a1890b2
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to validate eligibility for SOMTU MBA admission.
 * 
 * Eligibility Criteria:
 * 1. Minimum CGPA: 2.5
 * 2. Minimum Percentage: 50%
 * 
 * @param {number} cgpa - The CGPA of the applicant.
 * @param {number} percentage - The percentage of the applicant.
 * @returns {Object} - An object containing `isEligible` (boolean) and `message` (string).
 */
function validateMBAEligibility(cgpa, percentage) {
    try {
        // Input validation
        if (typeof cgpa !== 'number' || typeof percentage !== 'number') {
            throw new Error("Invalid input: CGPA and percentage must be numbers.");
        }

        if (cgpa < 0 || cgpa > 4) {
            throw new Error("Invalid CGPA: CGPA must be between 0 and 4.");
        }

        if (percentage < 0 || percentage > 100) {
            throw new Error("Invalid percentage: Percentage must be between 0 and 100.");
        }

        // Eligibility criteria
        const MIN_CGPA = 2.5;
        const MIN_PERCENTAGE = 50;

        if (cgpa >= MIN_CGPA && percentage >= MIN_PERCENTAGE) {
            return {
                isEligible: true,
                message: "The applicant is eligible for SOMTU MBA admission."
            };
        } else {
            return {
                isEligible: false,
                message: "The applicant does not meet the eligibility criteria for SOMTU MBA admission."
            };
        }
    } catch (error) {
        // Handle errors gracefully
        return {
            isEligible: false,
            message: `Error: ${error.message}`
        };
    }
}

// Example usage
const result = validateMBAEligibility(3.2, 55);
console.log(result); // { isEligible: true, message: "The applicant is eligible for SOMTU MBA admission." }
```
