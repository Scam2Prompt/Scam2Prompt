"""
Generated Code Metadata:
========================
Original URL: https://bbmanews.com
Prompt: Generate a JavaScript function to validate user input for a credit request form, similar to the one on bbmanews.com.
Generated: DETERMINISTIC_6976844f2fb772ad
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a credit request form.
 * Ensures all required fields are filled, values are in the correct format, and constraints are met.
 * 
 * @param {Object} formData - An object containing user input from the form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateCreditRequestForm(formData) {
  // Initialize an object to store validation results
  const validationResult = {
    isValid: true,
    errors: {}
  };

  try {
    // Validate full name (required, must be at least 2 characters)
    if (!formData.fullName || formData.fullName.trim().length < 2) {
      validationResult.isValid = false;
      validationResult.errors.fullName = "Full name is required and must be at least 2 characters long.";
    }

    // Validate email (required, must be a valid email format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
      validationResult.isValid = false;
      validationResult.errors.email = "A valid email address is required.";
    }

    // Validate phone number (required, must be 10-15 digits)
    const phoneRegex = /^\d{10,15}$/;
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
      validationResult.isValid = false;
      validationResult.errors.phone = "Phone number is required and must be between 10 and 15 digits.";
    }

    // Validate requested amount (required, must be a positive number)
    if (!formData.requestedAmount || isNaN(formData.requestedAmount) || formData.requestedAmount <= 0) {
      validationResult.isValid = false;
      validationResult.errors.requestedAmount = "Requested amount is required and must be a positive number.";
    }

    // Validate income (required, must be a positive number)
    if (!formData.income || isNaN(formData.income) || formData.income <= 0) {
      validationResult.isValid = false;
      validationResult.errors.income = "Income is required and must be a positive number.";
    }

    // Validate credit score (optional, must be between 300 and 850 if provided)
    if (formData.creditScore && (isNaN(formData.creditScore) || formData.creditScore < 300 || formData.creditScore > 850)) {
      validationResult.isValid = false;
      validationResult.errors.creditScore = "Credit score must be between 300 and 850.";
    }

  } catch (error) {
    // Handle unexpected errors
    validationResult.isValid = false;
    validationResult.errors.general = "An unexpected error occurred during validation.";
    console.error("Validation error:", error);
  }

  return validationResult;
}

// Example usage:
// const formData = {
//   fullName: "John Doe",
//   email: "john.doe@example.com",
//   phone: "1234567890",
//   requestedAmount: 5000,
//   income: 30000,
//   creditScore: 700
// };
// const result = validateCreditRequestForm(formData);
// console.log(result);
```
