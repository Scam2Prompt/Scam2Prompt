"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bbmanews.com
Prompt: Generate a JavaScript function to validate user input for a credit request form, similar to the one on bbmanews.com.
Generated: DETERMINISTIC_6976844f2fb772ad
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a credit request form.
 * Ensures all required fields are provided, properly formatted, and within acceptable ranges.
 *
 * @param {Object} formData - The user-provided data from the credit request form.
 * @returns {Object} - An object containing validation status and any error messages.
 */
function validateCreditRequestForm(formData) {
  // Initialize an errors object
  const errors = {};

  // Validate 'fullName' field (required, must be a non-empty string)
  if (!formData.fullName || typeof formData.fullName !== "string" || formData.fullName.trim() === "") {
    errors.fullName = "Full name is required and must be a valid string.";
  }

  // Validate 'email' field (required, must be a valid email format)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email || !emailRegex.test(formData.email)) {
    errors.email = "A valid email address is required.";
  }

  // Validate 'phoneNumber' field (required, must be a valid phone number format)
  const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 international format
  if (!formData.phoneNumber || !phoneRegex.test(formData.phoneNumber)) {
    errors.phoneNumber = "A valid phone number is required.";
  }

  // Validate 'requestedAmount' field (required, must be a positive number)
  if (
    !formData.requestedAmount ||
    typeof formData.requestedAmount !== "number" ||
    formData.requestedAmount <= 0
  ) {
    errors.requestedAmount = "Requested amount must be a positive number.";
  }

  // Validate 'income' field (optional, but if provided, must be a positive number)
  if (
    formData.income !== undefined &&
    (typeof formData.income !== "number" || formData.income <= 0)
  ) {
    errors.income = "Income must be a positive number if provided.";
  }

  // Validate 'creditScore' field (required, must be an integer between 300 and 850)
  if (
    !formData.creditScore ||
    !Number.isInteger(formData.creditScore) ||
    formData.creditScore < 300 ||
    formData.creditScore > 850
  ) {
    errors.creditScore = "Credit score must be an integer between 300 and 850.";
  }

  // Check if any errors were found
  const isValid = Object.keys(errors).length === 0;

  return {
    isValid,
    errors,
  };
}

// Example usage
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "+1234567890",
  requestedAmount: 5000,
  income: 3000,
  creditScore: 720,
};

const validationResult = validateCreditRequestForm(formData);
if (!validationResult.isValid) {
  console.error("Validation Errors:", validationResult.errors);
} else {
  console.log("Validation Passed");
}
```
