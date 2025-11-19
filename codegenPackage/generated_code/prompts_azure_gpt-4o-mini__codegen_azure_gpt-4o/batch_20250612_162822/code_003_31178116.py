"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: Develop a JavaScript function that validates user input for a construction service request form, ensuring all required fields are filled out, based on the structure used by ExpertStroy.
Generated: DETERMINISTIC_31178116c5152bdf
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a construction service request form.
 * Ensures all required fields are filled out.
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validateConstructionServiceForm(formData) {
  // Define required fields for the form
  const requiredFields = ['name', 'email', 'phone', 'serviceType', 'address'];

  // Initialize an object to store validation results
  const validationResult = {
    isValid: true,
    errors: {}
  };

  try {
    // Iterate through required fields to check for missing values
    requiredFields.forEach((field) => {
      if (!formData[field] || formData[field].trim() === '') {
        validationResult.isValid = false;
        validationResult.errors[field] = `${field} is required.`;
      }
    });

    // Additional validation for specific fields
    if (formData.email && !isValidEmail(formData.email)) {
      validationResult.isValid = false;
      validationResult.errors.email = 'Invalid email format.';
    }

    if (formData.phone && !isValidPhoneNumber(formData.phone)) {
      validationResult.isValid = false;
      validationResult.errors.phone = 'Invalid phone number format.';
    }
  } catch (error) {
    // Handle unexpected errors
    console.error('Error during form validation:', error);
    validationResult.isValid = false;
    validationResult.errors.general = 'An unexpected error occurred during validation.';
  }

  return validationResult;
}

/**
 * Validates email format using a regular expression.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email format is valid, false otherwise.
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Validates phone number format using a regular expression.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number format is valid, false otherwise.
 */
function isValidPhoneNumber(phone) {
  const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
  return phoneRegex.test(phone);
}

// Example usage:
// const formData = {
//   name: 'John Doe',
//   email: 'john.doe@example.com',
//   phone: '+1234567890',
//   serviceType: 'Roofing',
//   address: '123 Main St'
// };
// const result = validateConstructionServiceForm(formData);
// console.log(result);
```
