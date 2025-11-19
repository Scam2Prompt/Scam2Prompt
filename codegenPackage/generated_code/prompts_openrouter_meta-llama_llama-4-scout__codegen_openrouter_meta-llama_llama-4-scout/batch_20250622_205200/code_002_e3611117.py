"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Generate a code snippet in JavaScript to create a simple form validation for a power washing service company's contact page, similar to the one on Klean-Pro Utah's website.
Generated: DETERMINISTIC_e3611117724dbcda
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// FormValidation.js

class FormValidator {
  /**
   * Constructor for FormValidator
   * @param {object} form - The HTML form element to validate
   * @param {object} fields - An object containing field names and their validation rules
   */
  constructor(form, fields) {
    this.form = form;
    this.fields = fields;
    this.errors = {};

    // Bind event listener to form submission
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
  }

  /**
   * Validate a single field
   * @param {string} fieldName - The name of the field to validate
   * @param {string} fieldValue - The value of the field to validate
   * @returns {boolean} - True if valid, false otherwise
   */
  validateField(fieldName, fieldValue) {
    const rules = this.fields[fieldName];
    if (!rules) return true; // No rules defined for this field

    let isValid = true;
    if (rules.required && !fieldValue.trim()) {
      this.errors[fieldName] = 'This field is required';
      isValid = false;
    }

    if (rules.email && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(fieldValue)) {
      this.errors[fieldName] = 'Invalid email address';
      isValid = false;
    }

    if (rules.minLength && fieldValue.length < rules.minLength) {
      this.errors[fieldName] = `Minimum length of ${rules.minLength} characters required`;
      isValid = false;
    }

    return isValid;
  }

  /**
   * Handle form submission event
   * @param {Event} event - The form submission event
   */
  handleSubmit(event) {
    event.preventDefault();

    // Reset errors object
    this.errors = {};

    // Validate all fields
    let isValid = true;
    Array.from(this.form.elements).forEach((element) => {
      if (element.name) {
        const isFieldValid = this.validateField(element.name, element.value);
        if (!isFieldValid) {
          isValid = false;
        }
      }
    });

    // Display errors or submit form
    if (isValid) {
      // Form is valid, submit it
      console.log('Form is valid, submitting...');
      // Add your form submission logic here
    } else {
      // Display errors
      this.displayErrors();
    }
  }

  /**
   * Display form validation errors
   */
  displayErrors() {
    const errorElement = this.form.querySelector('.form-errors');
    if (!errorElement) return;

    // Clear existing errors
    errorElement.innerHTML = '';

    Object.keys(this.errors).forEach((fieldName) => {
      const fieldError = document.createElement('div');
      fieldError.classList.add('form-error');
      fieldError.textContent = this.errors[fieldName];
      errorElement.appendChild(fieldError);
    });
  }
}

// Example usage
const contactForm = document.getElementById('contact-form');
const validator = new FormValidator(contactForm, {
  name: { required: true, minLength: 2 },
  email: { required: true, email: true },
  message: { required: true, minLength: 10 },
});

// Add event listener to clear errors on input change
Array.from(contactForm.elements).forEach((element) => {
  if (element.name) {
    element.addEventListener('input', () => {
      const errorElement = contactForm.querySelector(`.form-error[data-field="${element.name}"]`);
      if (errorElement) {
        errorElement.remove();
      }
    });
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Power Washing Service Contact Form</title>
  <style>
    .form-error {
      color: red;
      font-size: 0.8em;
    }
  </style>
</head>
<body>
  <form id="contact-form">
    <div>
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" />
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" />
    </div>
    <div>
      <label for="message">Message:</label>
      <textarea id="message" name="message"></textarea>
    </div>
    <div class="form-errors"></div>
    <button type="submit">Submit</button>
  </form>

  <script src="FormValidation.js"></script>
</body>
</html>
```
