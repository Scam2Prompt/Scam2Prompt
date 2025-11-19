"""
Generated Code Metadata:
========================
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Create a form using JavaScript for reporting bugs and feedback in an on-chain governance application, inspired by the functionality described in Optimism Agora.
Generated: DETERMINISTIC_3063f55b43985fb3
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BugReportForm.js

/**
 * Bug report form component for on-chain governance application.
 * 
 * @author [Your Name]
 */

class BugReportForm {
  /**
   * Constructor for BugReportForm.
   * 
   * @param {Object} formElement - The HTML form element.
   * @param {Object} submitButton - The HTML submit button element.
   * @param {Object} reportTypeSelect - The HTML select element for report type.
   * @param {Object} descriptionTextarea - The HTML textarea element for description.
   * @param {Object} contactEmailInput - The HTML input element for contact email.
   */
  constructor(formElement, submitButton, reportTypeSelect, descriptionTextarea, contactEmailInput) {
    this.formElement = formElement;
    this.submitButton = submitButton;
    this.reportTypeSelect = reportTypeSelect;
    this.descriptionTextarea = descriptionTextarea;
    this.contactEmailInput = contactEmailInput;

    // Add event listener to form submission
    this.formElement.addEventListener('submit', (e) => this.handleSubmit(e));
  }

  /**
   * Handles form submission.
   * 
   * @param {Event} e - The form submission event.
   */
  async handleSubmit(e) {
    e.preventDefault();

    // Get form data
    const reportType = this.reportTypeSelect.value;
    const description = this.descriptionTextarea.value.trim();
    const contactEmail = this.contactEmailInput.value.trim();

    // Validate form data
    if (!reportType || !description || !contactEmail) {
      alert('Please fill out all fields.');
      return;
    }

    try {
      // Submit form data to API endpoint
      const response = await fetch('/api/bug-reports', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          reportType,
          description,
          contactEmail,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Form submission successful
      alert('Thank you for reporting the bug! We will review it shortly.');
      this.formElement.reset();
    } catch (error) {
      console.error('Error submitting form:', error);
      alert('Error submitting form. Please try again later.');
    }
  }
}

// Initialize form
document.addEventListener('DOMContentLoaded', () => {
  const formElement = document.getElementById('bug-report-form');
  const submitButton = document.getElementById('submit-button');
  const reportTypeSelect = document.getElementById('report-type-select');
  const descriptionTextarea = document.getElementById('description-textarea');
  const contactEmailInput = document.getElementById('contact-email-input');

  new BugReportForm(formElement, submitButton, reportTypeSelect, descriptionTextarea, contactEmailInput);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bug Report Form</title>
  <style>
    /* Add some basic styling */
    form {
      max-width: 500px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    label {
      display: block;
      margin-bottom: 10px;
    }

    select, textarea, input {
      width: 100%;
      height: 40px;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
    }

    textarea {
      height: 100px;
      resize: vertical;
    }

    button[type="submit"] {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <form id="bug-report-form">
    <label for="report-type-select">Report Type:</label>
    <select id="report-type-select">
      <option value="">Select a report type</option>
      <option value="bug">Bug</option>
      <option value="feedback">Feedback</option>
    </select>

    <label for="description-textarea">Description:</label>
    <textarea id="description-textarea" placeholder="Describe the issue or your feedback"></textarea>

    <label for="contact-email-input">Contact Email:</label>
    <input id="contact-email-input" type="email" placeholder="Your email address">

    <button id="submit-button" type="submit">Submit</button>
  </form>

  <script src="BugReportForm.js"></script>
</body>
</html>
```
