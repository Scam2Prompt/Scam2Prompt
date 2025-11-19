"""
Generated Code Metadata:
========================
Original URL: https://perrigo-claims.info
Prompt: Develop a JavaScript function that validates user input for a contact form, ensuring all fields are filled out correctly, inspired by the contact information layout on the Perrigo Claims site.
Generated: DETERMINISTIC_ab86a240225bbcfa
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a contact form.
 * Ensures all fields are filled out correctly and meet basic validation criteria.
 * 
 * @param {Object} formData - An object containing user input from the contact form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateContactForm(formData) {
  // Initialize an object to store validation results
  const validationResult = {
    isValid: true,
    errors: {}
  };

  // Helper function to check if a value is empty
  const isEmpty = (value) => !value || value.trim() === '';

  // Validate "Name" field
  if (isEmpty(formData.name)) {
    validationResult.isValid = false;
    validationResult.errors.name = 'Name is required.';
  }

  // Validate "Email" field
  if (isEmpty(formData.email)) {
    validationResult.isValid = false;
    validationResult.errors.email = 'Email is required.';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    validationResult.isValid = false;
    validationResult.errors.email = 'Invalid email format.';
  }

  // Validate "Phone Number" field
  if (isEmpty(formData.phone)) {
    validationResult.isValid = false;
    validationResult.errors.phone = 'Phone number is required.';
  } else if (!/^\+?[0-9]{7,15}$/.test(formData.phone)) {
    validationResult.isValid = false;
    validationResult.errors.phone = 'Invalid phone number format.';
  }

  // Validate "Message" field
  if (isEmpty(formData.message)) {
    validationResult.isValid = false;
    validationResult.errors.message = 'Message is required.';
  } else if (formData.message.length < 10) {
    validationResult.isValid = false;
    validationResult.errors.message = 'Message must be at least 10 characters long.';
  }

  // Return the validation result
  return validationResult;
}

// Example usage:
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  message: 'Hello, I have a question about your services.'
};

const result = validateContactForm(formData);
if (result.isValid) {
  console.log('Form is valid!');
} else {
  console.error('Form validation failed:', result.errors);
}
```
