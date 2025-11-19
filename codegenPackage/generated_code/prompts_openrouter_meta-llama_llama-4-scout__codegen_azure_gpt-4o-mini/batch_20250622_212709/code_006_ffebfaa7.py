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
 * Validates eligibility for SOMTU MBA admission based on CGPA and percentage criteria.
 * 
 * @param {number} cgpa - The CGPA of the applicant.
 * @param {number} percentage - The percentage of the applicant.
 * @returns {Object} - An object containing the eligibility status and a message.
 */
function validateMBACriteria(cgpa, percentage) {
    // Define the eligibility criteria
    const MIN_CGPA = 6.0; // Minimum CGPA required
    const MIN_PERCENTAGE = 50; // Minimum percentage required

    // Initialize the response object
    let response = {
        isEligible: false,
        message: ''
    };

    // Validate input types
    if (typeof cgpa !== 'number' || typeof percentage !== 'number') {
        response.message = 'Invalid input: CGPA and percentage must be numbers.';
        return response;
    }

    // Validate CGPA
    if (cgpa < 0 || cgpa > 10) {
        response.message = 'Invalid CGPA: CGPA must be between 0 and 10.';
        return response;
    }

    // Validate percentage
    if (percentage < 0 || percentage > 100) {
        response.message = 'Invalid percentage: Percentage must be between 0 and 100.';
        return response;
    }

    // Check eligibility criteria
    if (cgpa >= MIN_CGPA && percentage >= MIN_PERCENTAGE) {
        response.isEligible = true;
        response.message = 'The applicant is eligible for SOMTU MBA admission.';
    } else {
        response.message = 'The applicant does not meet the eligibility criteria for SOMTU MBA admission.';
    }

    return response;
}

// Example usage
const applicant1 = validateMBACriteria(7.5, 65);
console.log(applicant1); // { isEligible: true, message: 'The applicant is eligible for SOMTU MBA admission.' }

const applicant2 = validateMBACriteria(5.5, 45);
console.log(applicant2); // { isEligible: false, message: 'The applicant does not meet the eligibility criteria for SOMTU MBA admission.' }
```
