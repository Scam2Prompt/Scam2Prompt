"""
Generated Code Metadata:
========================
Original URL: https://linkmp.org
Prompt: Develop a JavaScript function to handle email subscription form submissions, similar to the functionality implied on Linkmp.org, including validation and a thank you message.
Generated: DETERMINISTIC_b5358b3d6bc7f260
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// email-subscription.js

/**
 * Handles email subscription form submissions.
 * 
 * @param {object} form - The email subscription form element.
 * @param {string} form.action - The URL to send the subscription request to.
 * @param {string} form.email - The email input field.
 * @param {string} thankYouMessageElementId - The ID of the element to display the thank you message in.
 */

function handleEmailSubscription(form, thankYouMessageElementId) {
    // Get the email input field value
    const emailInput = form.querySelector('input[type="email"]');
    const email = emailInput.value.trim();

    // Validate the email address
    if (!validateEmail(email)) {
        displayError(form, 'Please enter a valid email address.');
        return;
    }

    // Send the subscription request
    fetch(form.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Display the thank you message
            displayThankYouMessage(thankYouMessageElementId);
            // Clear the email input field
            emailInput.value = '';
        } else {
            displayError(form, data.message || 'Failed to subscribe. Please try again.');
        }
    })
    .catch(error => {
        console.error(error);
        displayError(form, 'An error occurred. Please try again.');
    });
}

/**
 * Validates an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} True if the email address is valid, false otherwise.
 */
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Displays an error message next to the form.
 * 
 * @param {object} form - The email subscription form element.
 * @param {string} message - The error message to display.
 */
function displayError(form, message) {
    const errorElement = form.querySelector('.error-message');
    if (!errorElement) {
        const errorElement = document.createElement('div');
        errorElement.classList.add('error-message');
        form.appendChild(errorElement);
    }
    errorElement.textContent = message;
}

/**
 * Displays a thank you message.
 * 
 * @param {string} elementId - The ID of the element to display the thank you message in.
 */
function displayThankYouMessage(elementId) {
    const thankYouMessageElement = document.getElementById(elementId);
    thankYouMessageElement.textContent = 'Thank you for subscribing!';
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('email-subscription-form');
    const thankYouMessageElementId = 'thank-you-message';

    form.addEventListener('submit', event => {
        event.preventDefault();
        handleEmailSubscription(form, thankYouMessageElementId);
    });
});
```
