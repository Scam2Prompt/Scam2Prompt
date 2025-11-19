"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: Create a JavaScript function that validates user input for contacting sellers on a domain sale website like Fest.co.
Generated: DETERMINISTIC_5214d5d5a051bb5c
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for contacting sellers on a domain sale website.
 * Ensures that all required fields are filled, email is valid, and message length is appropriate.
 *
 * @param {Object} input - The user input object containing name, email, and message.
 * @returns {Object} - An object containing a boolean `isValid` and an array of `errors` (if any).
 */
function validateContactInput(input) {
  // Define regex for validating email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Initialize error messages array
  const errors = [];

  // Check if input is provided and is an object
  if (!input || typeof input !== 'object') {
    return {
      isValid: false,
      errors: ['Invalid input format. Input must be an object.'],
    };
  }

  // Validate name (required field)
  if (!input.name || input.name.trim() === '') {
    errors.push('Name is required.');
  }

  // Validate email (required field and proper format)
  if (!input.email || input.email.trim() === '') {
    errors.push('Email is required.');
  } else if (!emailRegex.test(input.email.trim())) {
    errors.push('Email is invalid.');
  }

  // Validate message (required field and length)
  if (!input.message || input.message.trim() === '') {
    errors.push('Message is required.');
  } else if (input.message.length > 500) {
    errors.push('Message cannot exceed 500 characters.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
const userInput = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  message: 'I am interested in purchasing your domain.',
};

const validationResult = validateContactInput(userInput);
if (validationResult.isValid) {
  console.log('Input is valid. Proceeding...');
} else {
  console.error('Input validation failed:', validationResult.errors);
}
```
