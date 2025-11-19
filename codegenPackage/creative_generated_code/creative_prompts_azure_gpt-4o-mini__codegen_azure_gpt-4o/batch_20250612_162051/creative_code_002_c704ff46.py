"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Create a JavaScript function that validates user input for a roofing service request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_c704ff46a9125644
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
 * Validates a roofing service request form.
 * Ensures all required fields are properly filled out.
 * 
 * @param {Object} formData - An object containing user input fields.
 * @returns {Object} - Validation result with a boolean 'isValid' and an array of 'errors'.
 */
function validateRoofingServiceForm(formData) {
  // List of required fields
  const requiredFields = ['name', 'email', 'phone', 'address', 'roofType', 'requestDetails'];
  
  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: []
  };

  // Helper function to validate email format
  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  // Helper function to validate phone number format
  const isValidPhone = (phone) => {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format or basic international number
    return phoneRegex.test(phone);
  };

  // Iterate through required fields to check for missing or invalid data
  requiredFields.forEach((field) => {
    const value = formData[field];

    // Check if the field is missing or empty
    if (!value || value.trim() === '') {
      validationResult.isValid = false;
      validationResult.errors.push(`${field} is required.`);
    }

    // Additional validation for specific fields
    if (field === 'email' && value && !isValidEmail(value)) {
      validationResult.isValid = false;
      validationResult.errors.push('Invalid email format.');
    }

    if (field === 'phone' && value && !isValidPhone(value)) {
      validationResult.isValid = false;
      validationResult.errors.push('Invalid phone format.');
    }
  });

  return validationResult;
}

// Example usage:
const formInput = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  address: '123 Main St, Springfield, USA',
  roofType: 'Metal',
  requestDetails: 'Need an estimate for roof replacement.'
};

const result = validateRoofingServiceForm(formInput);
if (result.isValid) {
  console.log('Form is valid.');
} else {
  console.error('Form validation failed:', result.errors);
}
```
