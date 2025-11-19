"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: "Generate a consultation form validation script using JavaScript, ensuring that user input for name, email, country, and phone number is properly formatted and validated."
Generated: DETERMINISTIC_02db33c8b1e22774
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// consultationFormValidator.js

/**
 * Validates a consultation form's user input.
 */
class ConsultationFormValidator {
  /**
   * @param {object} formData - The consultation form data.
   * @param {string} formData.name - The user's name.
   * @param {string} formData.email - The user's email.
   * @param {string} formData.country - The user's country.
   * @param {string} formData.phoneNumber - The user's phone number.
   */
  constructor(formData) {
    this.formData = formData;
  }

  /**
   * Validates the user's name.
   * @returns {boolean} True if the name is valid, false otherwise.
   */
  validateName() {
    const nameRegex = /^[a-zA-Z\s]+$/; // Allow letters and spaces
    return nameRegex.test(this.formData.name) && this.formData.name.trim() !== '';
  }

  /**
   * Validates the user's email.
   * @returns {boolean} True if the email is valid, false otherwise.
   */
  validateEmail() {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(this.formData.email);
  }

  /**
   * Validates the user's country.
   * @returns {boolean} True if the country is valid, false otherwise.
   */
  validateCountry() {
    return this.formData.country.trim() !== '';
  }

  /**
   * Validates the user's phone number.
   * @returns {boolean} True if the phone number is valid, false otherwise.
   */
  validatePhoneNumber() {
    const phoneNumberRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return phoneNumberRegex.test(this.formData.phoneNumber);
  }

  /**
   * Validates the entire form.
   * @returns {object} An object containing validation results and error messages.
   */
  validateForm() {
    const validationResults = {
      isValid: true,
      errors: {},
    };

    if (!this.validateName()) {
      validationResults.isValid = false;
      validationResults.errors.name = 'Please enter a valid name.';
    }

    if (!this.validateEmail()) {
      validationResults.isValid = false;
      validationResults.errors.email = 'Please enter a valid email address.';
    }

    if (!this.validateCountry()) {
      validationResults.isValid = false;
      validationResults.errors.country = 'Please select a country.';
    }

    if (!this.validatePhoneNumber()) {
      validationResults.isValid = false;
      validationResults.errors.phoneNumber = 'Please enter a valid phone number.';
    }

    return validationResults;
  }
}

// Example usage:
function main() {
  try {
    const formData = {
      name: 'John Doe',
      email: 'johndoe@example.com',
      country: 'USA',
      phoneNumber: '(123) 456-7890',
    };

    const validator = new ConsultationFormValidator(formData);
    const validationResults = validator.validateForm();

    if (validationResults.isValid) {
      console.log('The form is valid.');
    } else {
      console.log('The form has errors:');
      Object.keys(validationResults.errors).forEach((field) => {
        console.log(`${field}: ${validationResults.errors[field]}`);
      });
    }
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

main();
```
