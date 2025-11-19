"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tf-fund.com
Prompt: How do I create a JavaScript function to validate user inputs for a trust fund application?
Generated: DETERMINISTIC_a6a14446fd571e8b
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateTrustFundApplication - Validates user inputs for a trust fund application.
 * 
 * @param {Object} input - The user input object containing fields to validate.
 * @param {string} input.fullName - Full name of the applicant.
 * @param {string} input.email - Email of the applicant.
 * @param {number} input.age - Age of the applicant.
 * @param {number} input.amountRequested - Amount of money requested in the application.
 * @returns {Object} - An object containing validation result and error messages, if any.
 */
function validateTrustFundApplication(input) {
  const errors = [];
  let isValid = true;

  // Validate Full Name
  if (typeof input.fullName !== 'string' || input.fullName.trim().length === 0) {
    errors.push("Full name is required and must be a non-empty string.");
    isValid = false;
  }

  // Validate Email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (typeof input.email !== 'string' || !emailRegex.test(input.email)) {
    errors.push("A valid email address is required.");
    isValid = false;
  }

  // Validate Age
  if (typeof input.age !== 'number' || input.age < 18 || input.age > 100) {
    errors.push("Age must be a number between 18 and 100.");
    isValid = false;
  }

  // Validate Amount Requested
  if (typeof input.amountRequested !== 'number' || input.amountRequested <= 0) {
    errors.push("Amount requested must be a positive number.");
    isValid = false;
  }

  // Return validation result
  return {
    isValid,
    errors
  };
}

// Example usage:
// const userInput = { fullName: "John Doe", email: "john.doe@example.com", age: 25, amountRequested: 5000 };
// const validationResult = validateTrustFundApplication(userInput);
// console.log(validationResult);

```
