"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pif-presale-staging.vercel.app
Prompt: Write a JavaScript function that validates an access code input for a presale, inspired by the Fwen.io website.
Generated: DETERMINISTIC_80aa4f512fcad99a
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateAccessCode - Validates an access code input for a presale.
 * 
 * This function checks if the access code meets the required criteria:
 * - Must be a non-empty string.
 * - Must be exactly 8 characters long.
 * - Must contain only alphanumeric characters.
 * 
 * @param {string} accessCode - The access code entered by the user.
 * @returns {Object} result - An object containing the validation status and a message.
 *   {
 *     isValid: {boolean}, // Indicates if the access code is valid.
 *     message: {string}   // A message describing the validation status.
 *   }
 */
function validateAccessCode(accessCode) {
  // Check if the input is provided and is a string
  if (typeof accessCode !== 'string' || accessCode.trim() === '') {
    return {
      isValid: false,
      message: 'Access code must be a non-empty string.',
    };
  }

  // Check the length of the access code
  if (accessCode.length !== 8) {
    return {
      isValid: false,
      message: 'Access code must be exactly 8 characters long.',
    };
  }

  // Check if the access code contains only alphanumeric characters
  const alphanumericRegex = /^[a-zA-Z0-9]+$/;
  if (!alphanumericRegex.test(accessCode)) {
    return {
      isValid: false,
      message: 'Access code must contain only alphanumeric characters (letters and numbers).',
    };
  }

  // If all checks pass, the access code is valid
  return {
    isValid: true,
    message: 'Access code is valid.',
  };
}

// Example usage:
const accessCode = 'Abc12345';
const validationResult = validateAccessCode(accessCode);

if (validationResult.isValid) {
  console.log(validationResult.message); // Output: Access code is valid.
} else {
  console.log(validationResult.message); // Output: Error message based on the failed validation.
}
```
