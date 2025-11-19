"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Create a JavaScript snippet for integrating a "Get a Commercial Offer" form into a website, similar to the forms used on Metamark's site.
Generated: DETERMINISTIC_25ab6c3bdbf9bce0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GetCommercialOfferForm.js

/**
 * Represents a "Get a Commercial Offer" form.
 */
class GetCommercialOfferForm {
  /**
   * Creates a new instance of the form.
   * @param {string} formId - The ID of the form element.
   * @param {string} apiEndpoint - The API endpoint to send form data to.
   */
  constructor(formId, apiEndpoint) {
    this.formId = formId;
    this.apiEndpoint = apiEndpoint;
    this.form = document.getElementById(formId);
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
  }

  /**
   * Handles form submission.
   * @param {Event} event - The form submission event.
   */
  handleSubmit(event) {
    event.preventDefault();
    const formData = this.getFormData();
    this.sendFormData(formData);
  }

  /**
   * Retrieves form data.
   * @returns {Object} - The form data.
   */
  getFormData() {
    const formData = {};
    const formElements = this.form.elements;

    for (let i = 0; i < formElements.length; i++) {
      const element = formElements[i];
      if (element.name) {
        formData[element.name] = element.value.trim();
      }
    }

    return formData;
  }

  /**
   * Sends form data to the API endpoint.
   * @param {Object} formData - The form data to send.
   */
  sendFormData(formData) {
    fetch(this.apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Form data sent successfully:', data);
      this.form.reset();
      this.displaySuccessMessage();
    })
    .catch(error => {
      console.error('Error sending form data:', error);
      this.displayErrorMessage();
    });
  }

  /**
   * Displays a success message.
   */
  displaySuccessMessage() {
    const successMessage = document.createElement('div');
    successMessage.textContent = 'Form submitted successfully!';
    successMessage.classList.add('success-message');
    this.form.parentNode.appendChild(successMessage);
    setTimeout(() => {
      successMessage.remove();
    }, 5000);
  }

  /**
   * Displays an error message.
   */
  displayErrorMessage() {
    const errorMessage = document.createElement('div');
    errorMessage.textContent = 'Error submitting form. Please try again.';
    errorMessage.classList.add('error-message');
    this.form.parentNode.appendChild(errorMessage);
    setTimeout(() => {
      errorMessage.remove();
    }, 5000);
  }
}

// Initialize the form
const form = new GetCommercialOfferForm('get-commercial-offer-form', '/api/commercial-offer');
```

```html
<!-- index.html -->

<!-- Get a Commercial Offer form -->
<form id="get-commercial-offer-form">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="phone">Phone:</label>
  <input type="tel" id="phone" name="phone" required>

  <label for="message">Message:</label>
  <textarea id="message" name="message"></textarea>

  <button type="submit">Get a Commercial Offer</button>
</form>

<!-- Styles for success and error messages -->
<style>
  .success-message {
    color: #008000;
    background-color: #C6F4D6;
    padding: 10px;
    border: 1px solid #3e8e41;
  }

  .error-message {
    color: #FF0000;
    background-color: #F2Dede;
    padding: 10px;
    border: 1px solid #FF3737;
  }
</style>
```
