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
 * @param {number} cgpa - The candidate's CGPA (out of 4.0)
 * @param {number} percentage - The candidate's percentage score
 * @returns {Object} An object containing:
 *   - eligible {boolean}: Whether candidate meets eligibility criteria
 *   - message {string}: Detailed status message
 * @throws {Error} If inputs are invalid
 */
function validateMbaEligibility(cgpa, percentage) {
    // Validate input types and ranges
    if (typeof cgpa !== 'number' || typeof percentage !== 'number') {
        throw new Error('Both CGPA and percentage must be numbers');
    }

    if (cgpa < 0 || cgpa > 4.0) {
        throw new Error('CGPA must be between 0 and 4.0');
    }

    if (percentage < 0 || percentage > 100) {
        throw new Error('Percentage must be between 0 and 100');
    }

    // Eligibility criteria
    const MIN_CGPA = 3.0;
    const MIN_PERCENTAGE = 60;

    // Check eligibility
    const meetsCgpa = cgpa >= MIN_CGPA;
    const meetsPercentage = percentage >= MIN_PERCENTAGE;
    const isEligible = meetsCgpa && meetsPercentage;

    // Generate appropriate message
    let message;
    if (isEligible) {
        message = 'Congratulations! You meet the eligibility criteria for SOMTU MBA.';
    } else {
        const reasons = [];
        if (!meetsCgpa) reasons.push(`CGPA below ${MIN_CGPA}`);
        if (!meetsPercentage) reasons.push(`percentage below ${MIN_PERCENTAGE}%`);
        message = `Not eligible: ${reasons.join(' and ')}.`;
    }

    return {
        eligible: isEligible,
        message: message
    };
}

// Example usage:
// try {
//     const result = validateMbaEligibility(3.2, 65);
//     console.log(result);
// } catch (error) {
//     console.error('Validation error:', error.message);
// }
```
