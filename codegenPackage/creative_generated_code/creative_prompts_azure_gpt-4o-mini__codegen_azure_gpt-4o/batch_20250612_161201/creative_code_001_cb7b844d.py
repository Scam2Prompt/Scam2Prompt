"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mintmomentco.com
Prompt: Write a JavaScript function to validate the contact form inputs for a portfolio site like Mint Moment Co.
Generated: DETERMINISTIC_cb7b844dfd52462a
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the inputs of a contact form.
 * @param {Object} formData - An object containing the contact form data.
 * @param {string} formData.name - The name input from the user.
 * @param {string} formData.email - The email input from the user.
 * @param {string} formData.message - The message input from the user.
 * @returns {Object} An object containing validation status and error messages.
 */
function validateContactForm(formData) {
  const errors = {};
  let isValid = true;

  // Validate name: must not be empty and should only contain letters and spaces
  if (!formData.name || formData.name.trim() === '') {
    errors.name = 'Name is required.';
    isValid = false;
  } else if (!/^[a-zA-Z\s]+$/.test(formData.name)) {
    errors.name = 'Name can only contain letters and spaces.';
    isValid = false;
  }

  // Validate email: must not be empty and should match standard email format
  if (!formData.email || formData.email.trim() === '') {
    errors.email = 'Email is required.';
    isValid = false;
  } else if (
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)
  ) {
    errors.email = 'Email is invalid.';
    isValid = false;
  }

  // Validate message: must not be empty and should have a minimum length
  if (!formData.message || formData.message.trim() === '') {
    errors.message = 'Message is required.';
    isValid = false;
  } else if (formData.message.length < 10) {
    errors.message = 'Message must be at least 10 characters long.';
    isValid = false;
  }

  // Return validation status and error messages
  return { isValid, errors };
}

// Example usage:
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  message: 'Hello, I am interested in your services!',
};

const result = validateContactForm(formData);
if (result.isValid) {
  console.log('Form is valid.');
} else {
  console.log('Form validation failed:', result.errors);
}
```
