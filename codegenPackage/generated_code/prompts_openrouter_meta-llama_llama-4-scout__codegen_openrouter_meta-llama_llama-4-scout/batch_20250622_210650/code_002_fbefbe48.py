"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Generate a sample code snippet in JavaScript for a basic contact form validation, similar to the one on the textcounsellingonline.com.au website, ensuring that fields such as name, email, and message are properly validated before submission.
Generated: DETERMINISTIC_fbefbe48ef075cf5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// contactFormValidator.js

/**
 * Validates a contact form with name, email, and message fields.
 */
class ContactFormValidator {
  /**
   * Creates a new ContactFormValidator instance.
   * @param {object} form - The contact form element.
   */
  constructor(form) {
    this.form = form;
    this.fields = {
      name: form.querySelector('#name'),
      email: form.querySelector('#email'),
      message: form.querySelector('#message'),
    };
    this.errors = {};
    this.initEventListeners();
  }

  /**
   * Initializes event listeners for the form.
   */
  initEventListeners() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    Object.values(this.fields).forEach((field) => {
      field.addEventListener('blur', () => this.validateField(field));
    });
  }

  /**
   * Handles form submission.
   * @param {Event} e - The submit event.
   */
  handleSubmit(e) {
    e.preventDefault();
    Object.values(this.fields).forEach((field) => this.validateField(field));
    if (Object.keys(this.errors).length === 0) {
      // Form is valid, submit it
      console.log('Form is valid, submitting...');
      // Add your form submission logic here
    } else {
      console.log('Form has errors, not submitting.');
      this.displayErrors();
    }
  }

  /**
   * Validates a single form field.
   * @param {HTMLElement} field - The field to validate.
   */
  validateField(field) {
    let isValid = true;
    let errorMessage = '';

    switch (field.id) {
      case 'name':
        if (field.value.trim() === '') {
          isValid = false;
          errorMessage = 'Please enter your name.';
        }
        break;
      case 'email':
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(field.value.trim())) {
          isValid = false;
          errorMessage = 'Please enter a valid email address.';
        }
        break;
      case 'message':
        if (field.value.trim() === '') {
          isValid = false;
          errorMessage = 'Please enter a message.';
        }
        break;
      default:
        break;
    }

    if (!isValid) {
      this.errors[field.id] = errorMessage;
    } else {
      delete this.errors[field.id];
    }

    this.updateFieldError(field, errorMessage);
  }

  /**
   * Updates the error message for a field.
   * @param {HTMLElement} field - The field to update.
   * @param {string} errorMessage - The error message to display.
   */
  updateFieldError(field, errorMessage) {
    const errorElement = field.closest('.form-group').querySelector('.error-message');
    if (errorMessage) {
      errorElement.textContent = errorMessage;
      errorElement.style.display = 'block';
    } else {
      errorElement.textContent = '';
      errorElement.style.display = 'none';
    }
  }

  /**
   * Displays all form errors.
   */
  displayErrors() {
    Object.keys(this.errors).forEach((fieldId) => {
      const field = this.fields[fieldId];
      this.updateFieldError(field, this.errors[fieldId]);
    });
  }
}

// Example usage:
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  new ContactFormValidator(contactForm);
}
```

```html
<!-- index.html -->

<form id="contact-form">
  <div class="form-group">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" />
    <span class="error-message"></span>
  </div>
  <div class="form-group">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" />
    <span class="error-message"></span>
  </div>
  <div class="form-group">
    <label for="message">Message:</label>
    <textarea id="message" name="message"></textarea>
    <span class="error-message"></span>
  </div>
  <button type="submit">Submit</button>
</form>
```

```css
/* styles.css */

.form-group {
  margin-bottom: 20px;
}

.error-message {
  color: red;
  font-size: 12px;
  display: none;
}
```
