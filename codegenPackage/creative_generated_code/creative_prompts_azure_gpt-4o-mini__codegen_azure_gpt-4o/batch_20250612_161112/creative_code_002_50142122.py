"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Create a JavaScript function to validate user input for an online registration form for ECLAT's online training courses in nail and eyelash techniques.
Generated: DETERMINISTIC_501421220ca25047
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for ECLAT's online registration form.
 * 
 * @param {Object} userInput - Object containing form data.
 * @param {string} userInput.fullName - Full name of the user (must be non-empty and only contain letters).
 * @param {string} userInput.email - Email address of the user (must be valid format).
 * @param {string} userInput.phoneNumber - Phone number of the user (must be valid format).
 * @param {string} userInput.courseSelection - Selected course (must be non-empty).
 * @returns {Object} Validation result containing a boolean `isValid` and an array `errors` with error messages (if any).
 */
function validateRegistrationForm(userInput) {
  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: [],
  };

  // Validate full name (must be non-empty and only contain alphabetic characters)
  if (!userInput.fullName || !/^[a-zA-Z\s]+$/.test(userInput.fullName)) {
    validationResult.isValid = false;
    validationResult.errors.push("Full name must be non-empty and contain only letters.");
  }

  // Validate email address (must follow standard email format)
  if (
    !userInput.email ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userInput.email)
  ) {
    validationResult.isValid = false;
    validationResult.errors.push("Email must be a valid email address.");
  }

  // Validate phone number (must follow standard phone number format)
  if (
    !userInput.phoneNumber ||
    !/^\+?[\d\s\-()]+$/.test(userInput.phoneNumber)
  ) {
    validationResult.isValid = false;
    validationResult.errors.push("Phone number must be valid and can include country code.");
  }

  // Validate course selection (must be non-empty)
  if (!userInput.courseSelection || userInput.courseSelection.trim() === "") {
    validationResult.isValid = false;
    validationResult.errors.push("Course selection must not be empty.");
  }

  // Return validation result
  return validationResult;
}

// Example usage:
const userInput = {
  fullName: "Jane Doe",
  email: "jane.doe@example.com",
  phoneNumber: "+1234567890",
  courseSelection: "Advanced Nail Techniques",
};

const validation = validateRegistrationForm(userInput);

if (validation.isValid) {
  console.log("Validation successful! User input is valid.");
} else {
  console.error("Validation failed. Errors:", validation.errors);
}
```
