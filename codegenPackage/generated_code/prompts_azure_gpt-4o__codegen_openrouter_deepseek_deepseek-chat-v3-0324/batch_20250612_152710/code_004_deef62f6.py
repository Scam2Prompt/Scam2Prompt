"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Write JavaScript code to implement a form validation system for a dental clinic's appointment request form, ensuring fields like name, email, phone number, and service type are correctly filled.
Generated: DETERMINISTIC_deef62f61e16a230
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dental Clinic Appointment Form Validation
 * Validates form fields including name, email, phone, and service type
 */

class FormValidator {
  constructor(formId) {
    this.form = document.getElementById(formId);
    this.fields = {
      name: {
        element: document.getElementById('name'),
        regex: /^[a-zA-Z\s]{2,50}$/,
        error: 'Please enter a valid name (2-50 letters)'
      },
      email: {
        element: document.getElementById('email'),
        regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        error: 'Please enter a valid email address'
      },
      phone: {
        element: document.getElementById('phone'),
        regex: /^[\d\s\-+]{10,15}$/,
        error: 'Please enter a valid phone number (10-15 digits)'
      },
      service: {
        element: document.getElementById('service'),
        error: 'Please select a service type'
      }
    };
    this.init();
  }

  init() {
    if (!this.form) {
      console.error('Form not found');
      return;
    }

    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (this.validateForm()) {
        this.form.submit();
      }
    });

    // Add real-time validation for fields
    Object.keys(this.fields).forEach(field => {
      if (this.fields[field].element) {
        this.fields[field].element.addEventListener('blur', () => {
          this.validateField(field);
        });
      }
    });
  }

  validateForm() {
    let isValid = true;
    
    Object.keys(this.fields).forEach(field => {
      if (!this.validateField(field)) {
        isValid = false;
      }
    });

    return isValid;
  }

  validateField(fieldName) {
    const field = this.fields[fieldName];
    const value = field.element.value.trim();
    let isValid = true;

    // Clear previous error
    this.clearError(field.element);

    // Validate required fields
    if (!value) {
      this.showError(field.element, field.error);
      return false;
    }

    // Regex validation for applicable fields
    if (field.regex && !field.regex.test(value)) {
      this.showError(field.element, field.error);
      isValid = false;
    }

    // Special validation for service dropdown
    if (fieldName === 'service' && value === 'default') {
      this.showError(field.element, field.error);
      isValid = false;
    }

    return isValid;
  }

  showError(element, message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    errorElement.style.color = 'red';
    errorElement.style.fontSize = '0.8rem';
    errorElement.style.marginTop = '5px';
    
    element.parentNode.appendChild(errorElement);
    element.classList.add('error');
  }

  clearError(element) {
    const errorElement = element.parentNode.querySelector('.error-message');
    if (errorElement) {
      element.parentNode.removeChild(errorElement);
    }
    element.classList.remove('error');
  }
}

// Initialize form validator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new FormValidator('appointmentForm');
});
```
