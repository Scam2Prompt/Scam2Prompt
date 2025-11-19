"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Develop a JavaScript function to validate and format phone numbers and email addresses for student registrations at Red & White International, ensuring proper data collection and communication.
Generated: DETERMINISTIC_8e84499a9d46f4ae
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and formats phone numbers and email addresses for student registrations.
 * @module ValidationUtils
 */

/**
 * Regular expression pattern for validating phone numbers.
 * @type {RegExp}
 */
const phoneNumberPattern = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;

/**
 * Regular expression pattern for validating email addresses.
 * @type {RegExp}
 */
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

/**
 * Validates a phone number.
 * @param {string} phoneNumber - The phone number to validate.
 * @returns {string|null} The formatted phone number, or null if invalid.
 */
function validatePhoneNumber(phoneNumber) {
  // Check if phone number matches the pattern
  const match = phoneNumber.match(phoneNumberPattern);
  if (match) {
    // Format phone number as (XXX) XXX-XXXX
    return `(${match[1]}) ${match[2]}-${match[3]}`;
  }
  return null;
}

/**
 * Validates an email address.
 * @param {string} email - The email address to validate.
 * @returns {string|null} The email address, or null if invalid.
 */
function validateEmail(email) {
  // Check if email matches the pattern
  if (emailPattern.test(email)) {
    return email.toLowerCase(); // Normalize email to lowercase
  }
  return null;
}

/**
 * Validates and formats a student's registration information.
 * @param {object} registrationInfo - The student's registration information.
 * @param {string} registrationInfo.phoneNumber - The student's phone number.
 * @param {string} registrationInfo.email - The student's email address.
 * @returns {object} The validated and formatted registration information, or null if invalid.
 */
function validateRegistrationInfo(registrationInfo) {
  try {
    const phoneNumber = validatePhoneNumber(registrationInfo.phoneNumber);
    const email = validateEmail(registrationInfo.email);

    if (!phoneNumber || !email) {
      throw new Error('Invalid phone number or email address');
    }

    return {
      phoneNumber,
      email,
    };
  } catch (error) {
    // Log the error and return null
    // For demonstration purposes, use console.error
    // In a real application, use a logging library or framework
    console.error('Error validating registration info:', error);
    return null;
  }
}

// Example usage:
const registrationInfo = {
  phoneNumber: '(123) 456-7890',
  email: 'student@example.com',
};

const validatedInfo = validateRegistrationInfo(registrationInfo);
if (validatedInfo) {
  // Use validatedInfo.phoneNumber and validatedInfo.email
  // For demonstration purposes, use console.log
  // In a real application, use a logging library or framework
  console.log('Validated phone number:', validatedInfo.phoneNumber);
  console.log('Validated email:', validatedInfo.email);
} else {
  // Handle invalid registration info
  // For demonstration purposes, use console.error
  // In a real application, use a logging library or framework
  console.error('Invalid registration info');
}
```
