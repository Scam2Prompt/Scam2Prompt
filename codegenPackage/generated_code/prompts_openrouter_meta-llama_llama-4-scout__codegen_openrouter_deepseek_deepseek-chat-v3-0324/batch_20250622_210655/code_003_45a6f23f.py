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
/**
 * Validates a contact form with fields for name, email, and message.
 * Similar to the TWM Associates website contact form validation.
 */
function validateContactForm() {
    // Get form elements
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const errorElement = document.getElementById('form-error');
    
    // Clear previous errors
    errorElement.textContent = '';
    errorElement.style.display = 'none';
    
    // Validate name
    if (name === '') {
        showError('Please enter your name');
        return false;
    }
    
    // Validate email
    if (email === '') {
        showError('Please enter your email address');
        return false;
    } else if (!isValidEmail(email)) {
        showError('Please enter a valid email address');
        return false;
    }
    
    // Validate message
    if (message === '') {
        showError('Please enter your message');
        return false;
    } else if (message.length < 10) {
        showError('Message should be at least 10 characters long');
        return false;
    }
    
    // If all validations pass
    return true;
    
    /**
     * Displays an error message on the form
     * @param {string} message - The error message to display
     */
    function showError(message) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
    
    /**
     * Validates an email address format
     * @param {string} email - The email address to validate
     * @returns {boolean} True if email is valid, false otherwise
     */
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
}

// Add event listener to form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    if (!validateContactForm()) {
        event.preventDefault();
    }
});
```
