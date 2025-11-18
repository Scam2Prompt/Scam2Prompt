"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.netlify.app
Prompt: Generate JavaScript code for a form validation system that ensures users provide valid input for fields such as name, email, phone, and company website, based on Acme's example form.
Generated: DETERMINISTIC_bbcf02360b180beb
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Form Validation Module
// This module validates user input for name, email, phone, and company website fields.
// Author: [Your Name]
// Date: [Date]

const formValidation = (() => {
    // Regular expressions for validation
    const regex = {
        name: /^[A-Za-z\s]+$/,
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phone: /^\+?[1-9]\d{1,14}$/, // E.164 format
        website: /^(https?:\/\/)?([a-z0-9-]+\.)+[a-z]{2,6}(\/[^\s]*)?$/i
    };

    /**
     * Validate the input fields.
     * @param {Object} fields - An object containing the input values to validate.
     * @returns {Object} - An object containing validation status and messages.
     */
    const validateFields = (fields) => {
        const results = {
            isValid: true,
            messages: {}
        };

        // Validate each field
        for (const field in fields) {
            if (fields.hasOwnProperty(field)) {
                switch (field) {
                    case 'name':
                        if (!regex.name.test(fields[field])) {
                            results.isValid = false;
                            results.messages.name = 'Name must contain only letters and spaces.';
                        }
                        break;

                    case 'email':
                        if (!regex.email.test(fields[field])) {
                            results.isValid = false;
                            results.messages.email = 'Please enter a valid email address.';
                        }
                        break;

                    case 'phone':
                        if (!regex.phone.test(fields[field])) {
                            results.isValid = false;
                            results.messages.phone = 'Phone number must be in E.164 format.';
                        }
                        break;

                    case 'website':
                        if (!regex.website.test(fields[field])) {
                            results.isValid = false;
                            results.messages.website = 'Please enter a valid website URL.';
                        }
                        break;

                    default:
                        break;
                }
            }
        }

        return results;
    };

    /**
     * Handle form submission.
     * @param {Event} event - The form submission event.
     */
    const handleSubmit = (event) => {
        event.preventDefault(); // Prevent default form submission

        // Gather input values
        const fields = {
            name: document.getElementById('name').value.trim(),
            email: document.getElementById('email').value.trim(),
            phone: document.getElementById('phone').value.trim(),
            website: document.getElementById('website').value.trim()
        };

        // Validate fields
        const validationResults = validateFields(fields);

        // Handle validation results
        if (validationResults.isValid) {
            // Proceed with form submission (e.g., send data to server)
            console.log('Form submitted successfully:', fields);
        } else {
            // Display validation messages to the user
            displayValidationMessages(validationResults.messages);
        }
    };

    /**
     * Display validation messages to the user.
     * @param {Object} messages - An object containing validation messages.
     */
    const displayValidationMessages = (messages) => {
        const messageContainer = document.getElementById('validation-messages');
        messageContainer.innerHTML = ''; // Clear previous messages

        for (const key in messages) {
            if (messages.hasOwnProperty(key)) {
                const messageElement = document.createElement('div');
                messageElement.textContent = messages[key];
                messageElement.classList.add('error-message');
                messageContainer.appendChild(messageElement);
            }
        }
    };

    // Attach event listener for form submission
    document.getElementById('form').addEventListener('submit', handleSubmit);

    return {
        validateFields,
        handleSubmit
    };
})();

// HTML Structure (for reference)
// <form id="form">
//     <input type="text" id="name" placeholder="Name" required>
//     <input type="email" id="email" placeholder="Email" required>
//     <input type="tel" id="phone" placeholder="Phone" required>
//     <input type="url" id="website" placeholder="Company Website" required>
//     <button type="submit">Submit</button>
// </form>
// <div id="validation-messages"></div>
```
