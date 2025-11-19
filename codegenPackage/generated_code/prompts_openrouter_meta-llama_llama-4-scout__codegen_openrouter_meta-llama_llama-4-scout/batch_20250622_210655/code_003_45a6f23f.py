"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Create a code snippet for a simple contact form validation using JavaScript, similar to the one on the TWM Associates website."
Generated: DETERMINISTIC_45a6f23ffbef2138
Batch ID: 20250622_210655
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
 * Validates a contact form.
 * 
 * @param {object} form - The contact form element.
 * @param {object} fields - The form fields to validate.
 * @returns {boolean} True if the form is valid, false otherwise.
 */
function validateContactForm(form, fields) {
    let isValid = true;

    // Iterate over each field
    Object.keys(fields).forEach((fieldName) => {
        const field = form.elements[fieldName];
        const fieldValue = field.value.trim();
        const fieldRules = fields[fieldName];

        // Check if the field is required
        if (fieldRules.required && !fieldValue) {
            field.classList.add('invalid');
            isValid = false;
        } else {
            field.classList.remove('invalid');
        }

        // Check if the field has a minimum length
        if (fieldRules.minLength && fieldValue.length < fieldRules.minLength) {
            field.classList.add('invalid');
            isValid = false;
        }

        // Check if the field matches an email pattern
        if (fieldRules.email && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(fieldValue)) {
            field.classList.add('invalid');
            isValid = false;
        }
    });

    return isValid;
}

// Example usage
const contactForm = document.getElementById('contact-form');
const formFields = {
    name: { required: true, minLength: 2 },
    email: { required: true, email: true },
    message: { required: true, minLength: 10 },
};

contactForm.addEventListener('submit', (event) => {
    if (!validateContactForm(contactForm, formFields)) {
        event.preventDefault();
        console.error('Form is invalid');
    } else {
        console.log('Form is valid');
        // Submit the form
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
    <title>Contact Form</title>
    <style>
        .invalid {
            border-color: red;
        }
    </style>
</head>
<body>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <script src="contactFormValidator.js"></script>
</body>
</html>
```
