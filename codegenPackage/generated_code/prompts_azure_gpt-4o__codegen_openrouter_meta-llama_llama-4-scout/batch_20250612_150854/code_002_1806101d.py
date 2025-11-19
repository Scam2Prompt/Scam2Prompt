"""
Generated Code Metadata:
========================
Original URL: https://immediategpt.nl
Prompt: Generate code in JavaScript to validate form inputs (e.g., minimum length for name fields, valid email format) as described on the Immediate GPT registration page.
Generated: DETERMINISTIC_1806101d631b3063
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates form inputs based on predefined rules.
 */
class FormValidator {
  /**
   * Constructor for FormValidator.
   * @param {object} form - The form object to be validated.
   * @param {object} rules - The validation rules.
   */
  constructor(form, rules) {
    this.form = form;
    this.rules = rules;
  }

  /**
   * Validates the form inputs.
   * @returns {object} An object containing validation results.
   */
  validate() {
    const results = {};
    for (const field in this.rules) {
      if (this.form[field]) {
        results[field] = this.validateField(this.form[field], this.rules[field]);
      } else {
        results[field] = { valid: false, message: 'Field is required' };
      }
    }
    return results;
  }

  /**
   * Validates a single field based on the provided rule.
   * @param {string} value - The field value.
   * @param {object} rule - The validation rule.
   * @returns {object} An object containing validation result and message.
   */
  validateField(value, rule) {
    switch (rule.type) {
      case 'email':
        return this.validateEmail(value);
      case 'minLength':
        return this.validateMinLength(value, rule.minLength);
      case 'name':
        return this.validateName(value);
      default:
        return { valid: false, message: 'Unsupported validation rule' };
    }
  }

  /**
   * Validates an email address.
   * @param {string} email - The email address to be validated.
   * @returns {object} An object containing validation result and message.
   */
  validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (emailRegex.test(email)) {
      return { valid: true, message: '' };
    } else {
      return { valid: false, message: 'Invalid email format' };
    }
  }

  /**
   * Validates the minimum length of a field.
   * @param {string} value - The field value.
   * @param {number} minLength - The minimum length.
   * @returns {object} An object containing validation result and message.
   */
  validateMinLength(value, minLength) {
    if (value.length >= minLength) {
      return { valid: true, message: '' };
    } else {
      return { valid: false, message: `Minimum length of ${minLength} characters required` };
    }
  }

  /**
   * Validates a name field.
   * @param {string} name - The name to be validated.
   * @returns {object} An object containing validation result and message.
   */
  validateName(name) {
    const nameRegex = /^[a-zA-Z\s]+$/;
    if (nameRegex.test(name)) {
      return { valid: true, message: '' };
    } else {
      return { valid: false, message: 'Name can only contain letters and spaces' };
    }
  }
}

// Example usage:
const form = {
  name: 'John Doe',
  email: 'johndoe@example.com',
  password: 'password123',
};

const rules = {
  name: { type: 'name', minLength: 2 },
  email: { type: 'email' },
  password: { type: 'minLength', minLength: 8 },
};

const validator = new FormValidator(form, rules);
const results = validator.validate();

console.log(results);
```
