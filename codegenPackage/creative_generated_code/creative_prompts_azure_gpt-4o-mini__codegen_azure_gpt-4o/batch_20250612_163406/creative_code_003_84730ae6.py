"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Develop a JavaScript function that validates user input for a business loan application form, ensuring it meets the criteria outlined by SGFC Finance.
Generated: DETERMINISTIC_84730ae68170b3bd
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a business loan application form.
 * @param {Object} input - The user input object to validate.
 * @param {string} input.name - Applicant's full name (required, must be at least 2 characters).
 * @param {number} input.age - Applicant's age (required, must be between 18 and 65).
 * @param {string} input.email - Applicant's email (required, must be a valid email format).
 * @param {number} input.loanAmount - Requested loan amount (required, must be between $5,000 and $500,000).
 * @param {string} input.businessName - Business name (required, must be at least 2 characters).
 * @param {number} input.experience - Years of business experience (required, must be >= 1 year).
 * @returns {Object} - Returns an object with `isValid` (boolean) and `errors` (array of strings).
 */
function validateLoanApplication(input) {
  const errors = [];

  // Validate name
  if (!input.name || input.name.trim().length < 2) {
    errors.push("Full name is required and must be at least 2 characters long.");
  }

  // Validate age
  if (!input.age || typeof input.age !== "number" || input.age < 18 || input.age > 65) {
    errors.push("Age is required and must be between 18 and 65.");
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format validation
  if (!input.email || !emailRegex.test(input.email)) {
    errors.push("A valid email is required.");
  }

  // Validate loan amount
  if (
    !input.loanAmount ||
    typeof input.loanAmount !== "number" ||
    input.loanAmount < 5000 ||
    input.loanAmount > 500000
  ) {
    errors.push("Loan amount is required and must be between $5,000 and $500,000.");
  }

  // Validate business name
  if (!input.businessName || input.businessName.trim().length < 2) {
    errors.push("Business name is required and must be at least 2 characters long.");
  }

  // Validate business experience
  if (
    input.experience === undefined ||
    typeof input.experience !== "number" ||
    input.experience < 1
  ) {
    errors.push("Business experience is required and must be at least 1 year.");
  }

  return {
    isValid: errors.length === 0,
    errors
  };
}

// Example usage:
const userInput = {
  name: "John Doe",
  age: 30,
  email: "john.doe@example.com",
  loanAmount: 20000,
  businessName: "Doe Enterprises",
  experience: 3
};

const validationResult = validateLoanApplication(userInput);
if (!validationResult.isValid) {
  console.log("Validation failed:", validationResult.errors);
} else {
  console.log("Validation succeeded!");
}
```
