"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Generate a JavaScript function to validate form fields for a web agency's contact form, ensuring proper error handling as mentioned on digistrategy.in.
Generated: DETERMINISTIC_c657970ca983f0a6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the fields of a contact form.
 *
 * @param {HTMLFormElement} form - The form element to validate.
 * @returns {boolean} - Returns true if all fields are valid, false otherwise.
 */
function validateContactForm(form) {
    // Retrieve the form fields
    const name = form.querySelector('input[name="name"]');
    const email = form.querySelector('input[name="email"]');
    const message = form.querySelector('textarea[name="message"]');
    
    // Clear previous error messages
    clearErrorMessages(form);

    // Initialize validation status
    let isValid = true;

    // Validate name
    if (!name.value.trim()) {
        showError(name, "Name is required.");
        isValid = false;
    }

    // Validate email
    if (!validateEmail(email.value.trim())) {
        showError(email, "Please enter a valid email address.");
        isValid = false;
    }

    // Validate message
    if (!message.value.trim()) {
        showError(message, "Message cannot be empty.");
        isValid = false;
    }

    return isValid;
}

/**
 * Validates the email format using regex.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email is valid, false otherwise.
 */
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Displays an error message next to the input field.
 *
 * @param {HTMLElement} field - The input field to display the error message next to.
 * @param {string} message - The error message to display.
 */
function showError(field, message) {
    const error = document.createElement('span');
    error.className = 'error-message';
    error.textContent = message;
    field.classList.add('input-error');
    field.parentNode.insertBefore(error, field.nextSibling);
}

/**
 * Clears all error messages from the form.
 *
 * @param {HTMLFormElement} form - The form element to clear error messages from.
 */
function clearErrorMessages(form) {
    const errorMessages = form.querySelectorAll('.error-message');
    errorMessages.forEach(error => error.remove());
    
    const inputFields = form.querySelectorAll('input, textarea');
    inputFields.forEach(field => field.classList.remove('input-error'));
}

// Example usage: Attach the validation to the form's submit event
const contactForm = document.querySelector('#contact-form');
contactForm.addEventListener('submit', function(event) {
    // Prevent form submission if validation fails
    if (!validateContactForm(contactForm)) {
        event.preventDefault();
    }
});
```
