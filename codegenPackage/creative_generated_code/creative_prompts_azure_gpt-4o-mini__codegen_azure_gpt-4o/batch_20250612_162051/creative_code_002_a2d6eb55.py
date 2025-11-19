"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Write a JavaScript function that validates user input based on the requirements outlined in NPORS Form 5.
Generated: DETERMINISTIC_a2d6eb5558e8f206
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user input based on NPORS Form 5 requirements.
 * This validation checks for:
 * - Name: Non-empty string, no special characters, max length 50.
 * - Email: Proper email format.
 * - Phone: Numeric, 10-15 digits.
 * - Date of Birth: Valid date and age >= 18.
 * - Certificate Number: Alphanumeric, max length 20.
 * 
 * @param {Object} userInput - The user input object to validate.
 * @returns {Object} - Validation result with a boolean status and an array of error messages.
 */
function validateNPORSForm5(userInput) {
  const errors = [];

  // Validate Name: Non-empty, no special characters, max length 50
  if (!userInput.name || typeof userInput.name !== 'string' || userInput.name.length > 50 || /[^a-zA-Z\s]/.test(userInput.name)) {
    errors.push('Name must be a non-empty string, contain no special characters, and be at most 50 characters long.');
  }

  // Validate Email: Proper email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!userInput.email || !emailRegex.test(userInput.email)) {
    errors.push('Email must be in a valid format.');
  }

  // Validate Phone: Numeric, 10-15 digits
  const phoneRegex = /^\d{10,15}$/;
  if (!userInput.phone || !phoneRegex.test(userInput.phone)) {
    errors.push('Phone must be a numeric value with 10 to 15 digits.');
  }

  // Validate Date of Birth: Valid date and age >= 18
  const today = new Date();
  const birthDate = new Date(userInput.dateOfBirth);
  const age = today.getFullYear() - birthDate.getFullYear();
  const monthDifference = today.getMonth() - birthDate.getMonth();
  if (
    !userInput.dateOfBirth ||
    isNaN(birthDate.getTime()) || // Invalid date
    age < 18 || // Age less than 18
    (age === 18 && monthDifference < 0) || // Age is exactly 18, but month is earlier
    (age === 18 && monthDifference === 0 && today.getDate() < birthDate.getDate()) // Same month, check day
  ) {
    errors.push('Date of Birth must be a valid date and the user must be at least 18 years old.');
  }

  // Validate Certificate Number: Alphanumeric, max length 20
  const certificateRegex = /^[a-zA-Z0-9]{1,20}$/;
  if (!userInput.certificateNumber || !certificateRegex.test(userInput.certificateNumber)) {
    errors.push('Certificate Number must be an alphanumeric value with a maximum length of 20 characters.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example Usage:
// const userInput = {
//   name: "John Doe",
//   email: "john.doe@example.com",
//   phone: "1234567890",
//   dateOfBirth: "2000-01-01",
//   certificateNumber: "CERT12345"
// };
// console.log(validateNPORSForm5(userInput));
```
