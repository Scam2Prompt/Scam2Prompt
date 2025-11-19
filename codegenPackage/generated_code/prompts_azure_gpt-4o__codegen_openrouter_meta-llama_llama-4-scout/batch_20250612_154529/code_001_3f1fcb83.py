"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a validation script in JavaScript for a ticket booking form that ensures the "Email Address" is properly formatted, the "Phone Number" contains only digits, and at least one "Preferred Method of Communication" is selected.
Generated: DETERMINISTIC_3f1fcb838e673f27
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a ticket booking form.
 */
class TicketBookingFormValidator {
  /**
   * Creates a new instance of the validator.
   * @param {object} formData - The data from the ticket booking form.
   */
  constructor(formData) {
    this.formData = formData;
  }

  /**
   * Validates the email address.
   * @returns {boolean} True if the email address is valid, false otherwise.
   */
  validateEmail() {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(this.formData.email);
  }

  /**
   * Validates the phone number.
   * @returns {boolean} True if the phone number is valid, false otherwise.
   */
  validatePhoneNumber() {
    const phoneNumberRegex = /^\d+$/;
    return phoneNumberRegex.test(this.formData.phoneNumber);
  }

  /**
   * Validates the preferred method of communication.
   * @returns {boolean} True if at least one method is selected, false otherwise.
   */
  validatePreferredMethod() {
    return this.formData.preferredMethods.length > 0;
  }

  /**
   * Validates the entire form.
   * @returns {object} An object containing the validation results.
   */
  validateForm() {
    const results = {
      email: this.validateEmail(),
      phoneNumber: this.validatePhoneNumber(),
      preferredMethod: this.validatePreferredMethod(),
    };

    return results;
  }

  /**
   * Gets the error messages for the form.
   * @param {object} results - The validation results.
   * @returns {object} An object containing the error messages.
   */
  getErrorMessages(results) {
    const errorMessages = {};

    if (!results.email) {
      errorMessages.email = 'Please enter a valid email address.';
    }

    if (!results.phoneNumber) {
      errorMessages.phoneNumber = 'Please enter a valid phone number containing only digits.';
    }

    if (!results.preferredMethod) {
      errorMessages.preferredMethod = 'Please select at least one preferred method of communication.';
    }

    return errorMessages;
  }
}

// Example usage:
function main() {
  try {
    const formData = {
      email: 'example@example.com',
      phoneNumber: '1234567890',
      preferredMethods: ['email', 'phone'],
    };

    const validator = new TicketBookingFormValidator(formData);
    const results = validator.validateForm();
    const errorMessages = validator.getErrorMessages(results);

    if (Object.keys(errorMessages).length > 0) {
      console.log('Validation errors:');
      console.log(errorMessages);
    } else {
      console.log('Form is valid.');
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

main();
```
