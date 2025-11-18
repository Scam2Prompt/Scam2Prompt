"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collab.host
Prompt: Write a JavaScript function to validate form fields (e.g., name and email) for webinar registration, as seen on the collab.host website.
Generated: DETERMINISTIC_fce0691d0a8ebd31
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateForm - Validates form fields for webinar registration.
 *
 * @param {Object} formData - An object containing form field values (e.g., { name: 'John', email: 'john@example.com' }).
 * @returns {Object} - Returns an object with `isValid` (boolean) and `errors` (array of error messages).
 */
function validateForm(formData) {
  const errors = [];
  const nameRegex = /^[a-zA-Z\s]+$/; // Regex to validate name (letters and spaces only)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regex to validate email format

  // Validate name field
  if (!formData.name || formData.name.trim() === '') {
    errors.push('Name is required.');
  } else if (!nameRegex.test(formData.name)) {
    errors.push('Name must contain only letters and spaces.');
  }

  // Validate email field
  if (!formData.email || formData.email.trim() === '') {
    errors.push('Email is required.');
  } else if (!emailRegex.test(formData.email)) {
    errors.push('Email must be a valid email address.');
  }

  // Return validation results
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com'
};

const validationResult = validateForm(formData);
if (validationResult.isValid) {
  console.log('Form is valid. Ready to submit.');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
