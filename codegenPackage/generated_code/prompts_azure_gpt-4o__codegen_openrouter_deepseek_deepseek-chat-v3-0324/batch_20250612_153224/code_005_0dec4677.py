"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Create a JavaScript function for a "Prayer Request" form that validates user input and sends the data to a backend service for processing, inspired by ChurchProWeb's website features.
Generated: DETERMINISTIC_0dec467785800781
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Prayer Request Form Handler
 * Validates user input and submits data to backend service
 */

class PrayerRequestForm {
  constructor(formId, endpointUrl) {
    this.form = document.getElementById(formId);
    this.endpointUrl = endpointUrl;
    this.init();
  }

  init() {
    if (!this.form) {
      console.error('Form element not found');
      return;
    }

    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (this.validate()) {
        this.submit();
      }
    });
  }

  validate() {
    const name = this.form.querySelector('[name="name"]').value.trim();
    const email = this.form.querySelector('[name="email"]').value.trim();
    const request = this.form.querySelector('[name="request"]').value.trim();
    const privacyChecked = this.form.querySelector('[name="privacy"]').checked;

    // Clear previous errors
    this.clearErrors();

    let isValid = true;

    if (!name) {
      this.showError('name', 'Please enter your name');
      isValid = false;
    }

    if (email && !this.validateEmail(email)) {
      this.showError('email', 'Please enter a valid email address');
      isValid = false;
    }

    if (!request) {
      this.showError('request', 'Please enter your prayer request');
      isValid = false;
    }

    if (!privacyChecked) {
      this.showError('privacy', 'You must agree to the privacy policy');
      isValid = false;
    }

    return isValid;
  }

  validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  showError(fieldName, message) {
    const field = this.form.querySelector(`[name="${fieldName}"]`);
    if (!field) return;

    let errorElement = field.nextElementSibling;
    if (!errorElement || !errorElement.classList.contains('error-message')) {
      errorElement = document.createElement('div');
      errorElement.className = 'error-message';
      field.parentNode.insertBefore(errorElement, field.nextSibling);
    }

    errorElement.textContent = message;
    field.classList.add('error');
  }

  clearErrors() {
    const errorMessages = this.form.querySelectorAll('.error-message');
    errorMessages.forEach(el => el.remove());

    const errorFields = this.form.querySelectorAll('.error');
    errorFields.forEach(el => el.classList.remove('error'));
  }

  async submit() {
    const formData = new FormData(this.form);
    const submitButton = this.form.querySelector('button[type="submit"]');
    const originalButtonText = submitButton.textContent;

    try {
      submitButton.disabled = true;
      submitButton.textContent = 'Submitting...';

      const response = await fetch(this.endpointUrl, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      this.showSuccessMessage(result.message || 'Your prayer request has been submitted successfully.');
      this.form.reset();
    } catch (error) {
      console.error('Error submitting prayer request:', error);
      this.showError('form', 'There was an error submitting your request. Please try again later.');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = originalButtonText;
    }
  }

  showSuccessMessage(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.textContent = message;

    const existingSuccess = this.form.querySelector('.success-message');
    if (existingSuccess) {
      existingSuccess.remove();
    }

    this.form.insertBefore(successDiv, this.form.firstChild);
    setTimeout(() => successDiv.remove(), 5000);
  }
}

// Initialize the form when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new PrayerRequestForm('prayer-request-form', '/api/prayer-requests');
});
```
