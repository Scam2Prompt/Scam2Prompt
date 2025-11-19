"""
Generated Code Metadata:
========================
Original URL: https://metlifemedicos.com.br
Prompt: Create a JavaScript code that validates user input for a life insurance quote form, ensuring compliance with privacy policies like those of MetLife.
Generated: DETERMINISTIC_9a303cf4984d7dd1
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a life insurance quote form with privacy compliance.
 * @class
 */
class InsuranceQuoteValidator {
  /**
   * Initializes the validator with default privacy policy settings.
   * @constructor
   * @param {Object} privacyPolicy - Privacy policy configuration
   */
  constructor(privacyPolicy = {}) {
    this.privacyPolicy = {
      minAge: 18,
      maxAge: 70,
      allowedCountries: ['US', 'CA'],
      dataRetentionDays: 30,
      ...privacyPolicy
    };
  }

  /**
   * Validates the entire form data
   * @param {Object} formData - User input data
   * @returns {Object} Validation result { isValid: boolean, errors: Object }
   */
  validateForm(formData) {
    const errors = {};

    // Validate personal information
    if (!this._validateName(formData.firstName)) {
      errors.firstName = 'First name must be 2-50 characters and contain only letters';
    }
    if (!this._validateName(formData.lastName)) {
      errors.lastName = 'Last name must be 2-50 characters and contain only letters';
    }
    if (!this._validateEmail(formData.email)) {
      errors.email = 'Please enter a valid email address';
    }
    if (!this._validatePhone(formData.phone)) {
      errors.phone = 'Please enter a valid phone number (10-15 digits)';
    }
    if (!this._validateDateOfBirth(formData.dateOfBirth)) {
      errors.dateOfBirth = `Age must be between ${this.privacyPolicy.minAge} and ${this.privacyPolicy.maxAge} years`;
    }
    if (!this._validateAddress(formData.address)) {
      errors.address = 'Please enter a valid address';
    }
    if (!this._validateCountry(formData.country)) {
      errors.country = `We currently only serve ${this.privacyPolicy.allowedCountries.join(', ')}`;
    }

    // Validate insurance details
    if (!this._validateCoverageAmount(formData.coverageAmount)) {
      errors.coverageAmount = 'Coverage amount must be between $10,000 and $5,000,000';
    }
    if (!this._validateTermLength(formData.termLength)) {
      errors.termLength = 'Term length must be between 10 and 30 years';
    }

    // Validate privacy consent
    if (!formData.privacyConsent) {
      errors.privacyConsent = 'You must agree to the privacy policy';
    }

    return {
      isValid: Object.keys(errors).length === 0,
      errors
    };
  }

  /**
   * Validates a name field
   * @private
   * @param {string} name - Name to validate
   * @returns {boolean} Validation result
   */
  _validateName(name) {
    return typeof name === 'string' && 
           name.length >= 2 && 
           name.length <= 50 && 
           /^[a-zA-Z\s\-']+$/.test(name);
  }

  /**
   * Validates an email address
   * @private
   * @param {string} email - Email to validate
   * @returns {boolean} Validation result
   */
  _validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return typeof email === 'string' && re.test(email);
  }

  /**
   * Validates a phone number
   * @private
   * @param {string} phone - Phone number to validate
   * @returns {boolean} Validation result
   */
  _validatePhone(phone) {
    const digits = phone.replace(/\D/g, '');
    return digits.length >= 10 && digits.length <= 15;
  }

  /**
   * Validates date of birth and age range
   * @private
   * @param {string} dateOfBirth - Date in YYYY-MM-DD format
   * @returns {boolean} Validation result
   */
  _validateDateOfBirth(dateOfBirth) {
    try {
      const dob = new Date(dateOfBirth);
      if (isNaN(dob.getTime())) return false;

      const today = new Date();
      let age = today.getFullYear() - dob.getFullYear();
      const monthDiff = today.getMonth() - dob.getMonth();
      
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
        age--;
      }

      return age >= this.privacyPolicy.minAge && age <= this.privacyPolicy.maxAge;
    } catch (e) {
      return false;
    }
  }

  /**
   * Validates address (basic validation)
   * @private
   * @param {string} address - Address to validate
   * @returns {boolean} Validation result
   */
  _validateAddress(address) {
    return typeof address === 'string' && 
           address.length >= 10 && 
           address.length <= 200;
  }

  /**
   * Validates country against allowed countries
   * @private
   * @param {string} country - Country code to validate
   * @returns {boolean} Validation result
   */
  _validateCountry(country) {
    return this.privacyPolicy.allowedCountries.includes(country?.toUpperCase());
  }

  /**
   * Validates coverage amount
   * @private
   * @param {number} amount - Coverage amount to validate
   * @returns {boolean} Validation result
   */
  _validateCoverageAmount(amount) {
    const num = Number(amount);
    return !isNaN(num) && num >= 10000 && num <= 5000000;
  }

  /**
   * Validates term length
   * @private
   * @param {number} years - Term length to validate
   * @returns {boolean} Validation result
   */
  _validateTermLength(years) {
    const num = Number(years);
    return !isNaN(num) && num >= 10 && num <= 30;
  }
}

// Example usage:
/*
const validator = new InsuranceQuoteValidator();
const formData = {
  firstName: 'John',
  lastName: 'Doe',
  email: 'john.doe@example.com',
  phone: '1234567890',
  dateOfBirth: '1980-01-01',
  address: '123 Main St, Anytown, USA',
  country: 'US',
  coverageAmount: 500000,
  termLength: 20,
  privacyConsent: true
};

const validationResult = validator.validateForm(formData);
if (!validationResult.isValid) {
  console.error('Validation errors:', validationResult.errors);
} else {
  console.log('Form is valid');
}
*/
```
