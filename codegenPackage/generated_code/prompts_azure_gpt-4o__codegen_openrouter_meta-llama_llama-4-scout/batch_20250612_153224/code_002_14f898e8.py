"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Generate code in JavaScript to create a form for collecting client details (name, email, subject, message) for consultation requests, as outlined on the TWM Associates website.
Generated: DETERMINISTIC_14f898e8e2271d85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Client Consultation Form Handler

class ConsultationForm {
  /**
   * Creates a new consultation form handler.
   * @param {HTMLFormElement} formElement - The form element to handle.
   */
  constructor(formElement) {
    this.formElement = formElement;
    this.fields = [
      { name: 'name', label: 'Name', type: 'text' },
      { name: 'email', label: 'Email', type: 'email' },
      { name: 'subject', label: 'Subject', type: 'text' },
      { name: 'message', label: 'Message', type: 'textarea' },
    ];

    this.initForm();
  }

  /**
   * Initializes the form with event listeners and validation.
   */
  initForm() {
    this.formElement.addEventListener('submit', (e) => this.handleSubmit(e));
    this.formElement.addEventListener('input', () => this.handleInput());

    this.fields.forEach((field) => {
      const inputElement = this.getInputElement(field);
      if (inputElement) {
        inputElement.addEventListener('blur', () => this.handleBlur(field, inputElement));
      }
    });
  }

  /**
   * Handles form submission.
   * @param {Event} e - The submit event.
   */
  handleSubmit(e) {
    e.preventDefault();
    const formData = this.getFormData();
    if (this.validateFormData(formData)) {
      // Send data to server or handle submission
      console.log('Form submitted:', formData);
      this.formElement.reset();
    }
  }

  /**
   * Handles input events for real-time validation.
   */
  handleInput() {
    const formData = this.getFormData();
    this.fields.forEach((field) => {
      const inputElement = this.getInputElement(field);
      if (inputElement) {
        const errorElement = this.getErrorElement(field);
        if (errorElement) {
          errorElement.textContent = this.getErrorMessage(field, formData[field]);
        }
      }
    });
  }

  /**
   * Handles blur events for field validation.
   * @param {Object} field - The field object.
   * @param {HTMLInputElement|HTMLTextAreaElement} inputElement - The input element.
   */
  handleBlur(field, inputElement) {
    const errorElement = this.getErrorElement(field);
    if (errorElement) {
      const formData = this.getFormData();
      errorElement.textContent = this.getErrorMessage(field, formData[field]);
    }
  }

  /**
   * Gets the form data.
   * @returns {Object} The form data.
   */
  getFormData() {
    const formData = {};
    this.fields.forEach((field) => {
      const inputElement = this.getInputElement(field);
      if (inputElement) {
        formData[field.name] = inputElement.value.trim();
      }
    });
    return formData;
  }

  /**
   * Validates the form data.
   * @param {Object} formData - The form data.
   * @returns {Boolean} Whether the form data is valid.
   */
  validateFormData(formData) {
    let isValid = true;
    this.fields.forEach((field) => {
      const errorMessage = this.getErrorMessage(field, formData[field.name]);
      if (errorMessage) {
        isValid = false;
        const errorElement = this.getErrorElement(field);
        if (errorElement) {
          errorElement.textContent = errorMessage;
        }
      }
    });
    return isValid;
  }

  /**
   * Gets the error message for a field.
   * @param {Object} field - The field object.
   * @param {String} value - The field value.
   * @returns {String} The error message.
   */
  getErrorMessage(field, value) {
    if (!value) {
      return `${field.label} is required`;
    }
    if (field.type === 'email' && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value)) {
      return 'Invalid email address';
    }
    return '';
  }

  /**
   * Gets the input element for a field.
   * @param {Object} field - The field object.
   * @returns {HTMLInputElement|HTMLTextAreaElement} The input element.
   */
  getInputElement(field) {
    return this.formElement.querySelector(`[name="${field.name}"]`);
  }

  /**
   * Gets the error element for a field.
   * @param {Object} field - The field object.
   * @returns {HTMLElement} The error element.
   */
  getErrorElement(field) {
    return this.formElement.querySelector(`[data-error="${field.name}"]`);
  }
}

// Example usage
const formElement = document.getElementById('consultation-form');
if (formElement) {
  new ConsultationForm(formElement);
}
```

```html
<!-- Example HTML -->
<form id="consultation-form">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name"><br><br>
  <span data-error="name"></span>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br><br>
  <span data-error="email"></span>

  <label for="subject">Subject:</label>
  <input type="text" id="subject" name="subject"><br><br>
  <span data-error="subject"></span>

  <label for="message">Message:</label>
  <textarea id="message" name="message"></textarea><br><br>
  <span data-error="message"></span>

  <input type="submit" value="Submit">
</form>
```
