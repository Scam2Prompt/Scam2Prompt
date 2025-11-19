"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Develop a JavaScript function that validates user input for an insurance quote request form, ensuring all necessary fields are filled out correctly.
Generated: DETERMINISTIC_c4dd2c66057520ea
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateInsuranceForm
 * Validates user input for an insurance quote request form.
 * Ensures all necessary fields are filled out correctly.
 *
 * @param {Object} formData - User input data from the form.
 * @returns {Object} Validation result with a boolean `isValid` and an array `errors`.
 */
function validateInsuranceForm(formData) {
  const errors = [];

  // Required fields
  const requiredFields = [
    { field: 'fullName', message: 'Full Name is required.' },
    { field: 'email', message: 'Email is required.' },
    { field: 'phoneNumber', message: 'Phone Number is required.' },
    { field: 'age', message: 'Age is required.' },
    { field: 'insuranceType', message: 'Insurance Type is required.' },
  ];

  // Field validation
  requiredFields.forEach(({ field, message }) => {
    if (!formData[field] || formData[field].trim() === '') {
      errors.push(message);
    }
  });

  // Validate email format
  if (formData.email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      errors.push('Invalid email format.');
    }
  }

  // Validate phone number format
  if (formData.phoneNumber) {
    const phoneRegex = /^[0-9]{10}$/; // Example: 10-digit phone number
    if (!phoneRegex.test(formData.phoneNumber)) {
      errors.push('Invalid phone number format. Must be 10 digits.');
    }
  }

  // Validate age (must be a positive integer)
  if (formData.age) {
    const age = parseInt(formData.age, 10);
    if (isNaN(age) || age <= 0) {
      errors.push('Age must be a positive number.');
    }
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors,
  };
}

// Example usage:
const formData = {
  fullName: 'John Doe',
  email: 'john.doe@example.com',
  phoneNumber: '1234567890',
  age: '30',
  insuranceType: 'Life',
};

const validationResult = validateInsuranceForm(formData);
if (validationResult.isValid) {
  console.log('Form is valid.');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
