"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cohencues.com
Prompt: Create a JavaScript function that validates user input for a custom cue order form, ensuring all required fields are filled out as described on the Cohen Cues website.
Generated: DETERMINISTIC_b313e8fbb0bf808c
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a custom cue order form.
 * Ensures all required fields are filled out as described on the Cohen Cues website.
 * 
 * Required fields:
 * - cueType: Type of cue selected (string, must not be empty).
 * - woodType: Type of wood selected (string, must not be empty).
 * - weight: Desired cue weight (number, must be within a valid range).
 * - customerName: Name of the customer (string, must not be empty).
 * - email: Customer's email address (string, must be valid format).
 * - phone: Customer's phone number (string, must be valid format).
 * - specialRequests: Optional field for special requests (if included, must be a string).
 * 
 * @param {Object} formData - The input data from the user.
 * @returns {Object} - An object indicating whether validation passed and an array of error messages.
 */
function validateCueOrderForm(formData) {
  const errors = [];

  // Helper function to validate email format
  const isValidEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  // Helper function to validate phone format (simple regex for demonstration)
  const isValidPhone = (phone) => /^\+?[0-9\s\-()]{7,15}$/.test(phone);

  // Validate cueType
  if (!formData.cueType || typeof formData.cueType !== 'string' || formData.cueType.trim() === '') {
    errors.push('Cue type is required and must be a non-empty string.');
  }

  // Validate woodType
  if (!formData.woodType || typeof formData.woodType !== 'string' || formData.woodType.trim() === '') {
    errors.push('Wood type is required and must be a non-empty string.');
  }

  // Validate weight
  if (typeof formData.weight !== 'number' || formData.weight < 16 || formData.weight > 21) {
    errors.push('Weight is required and must be a number between 16 and 21.');
  }

  // Validate customerName
  if (!formData.customerName || typeof formData.customerName !== 'string' || formData.customerName.trim() === '') {
    errors.push('Customer name is required and must be a non-empty string.');
  }

  // Validate email
  if (!formData.email || typeof formData.email !== 'string' || !isValidEmail(formData.email)) {
    errors.push('A valid email address is required.');
  }

  // Validate phone
  if (!formData.phone || typeof formData.phone !== 'string' || !isValidPhone(formData.phone)) {
    errors.push('A valid phone number is required.');
  }

  // Validate specialRequests (optional field)
  if (formData.specialRequests && typeof formData.specialRequests !== 'string') {
    errors.push('Special requests, if provided, must be a string.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors,
  };
}

// Example usage:
const formData = {
  cueType: 'Pool Cue',
  woodType: 'Maple',
  weight: 19,
  customerName: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  specialRequests: 'Please add custom engraving.',
};

const validationResult = validateCueOrderForm(formData);

if (validationResult.isValid) {
  console.log('Form is valid!');
} else {
  console.log('Form validation failed:', validationResult.errors);
}
```
