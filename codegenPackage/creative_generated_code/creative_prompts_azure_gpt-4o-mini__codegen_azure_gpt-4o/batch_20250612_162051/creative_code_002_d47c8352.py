"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Create a JavaScript function that validates user input for a contact form on a roofing service website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_d47c835209daeb2a
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
 * Validates user input for a contact form.
 * This function checks if all required fields are filled out correctly.
 * It returns an object containing validation status and error messages.
 * @param {Object} formData - The data submitted from the form.
 * @returns {Object} - An object with `isValid` (boolean) and `errors` (array of error messages).
 */
function validateContactForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = [
    { name: 'fullName', message: 'Full name is required.' },
    { name: 'email', message: 'Email is required.' },
    { name: 'phoneNumber', message: 'Phone number is required.' },
    { name: 'message', message: 'Message is required.' },
  ];

  const errors = [];

  // Check if required fields are provided and valid
  requiredFields.forEach(field => {
    if (!formData[field.name] || formData[field.name].trim() === '') {
      errors.push(field.message);
    }
  });

  // Additional validation for email format
  if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())) {
    errors.push('Invalid email format.');
  }

  // Additional validation for phone number format
  if (formData.phoneNumber && !/^\d{10,15}$/.test(formData.phoneNumber.trim())) {
    errors.push('Phone number must contain only digits and be between 10–15 characters.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
// const formData = {
//   fullName: 'John Doe',
//   email: 'john.doe@example.com',
//   phoneNumber: '1234567890',
//   message: 'I need roofing services.',
// };
// const validationResult = validateContactForm(formData);
// console.log(validationResult);
```
