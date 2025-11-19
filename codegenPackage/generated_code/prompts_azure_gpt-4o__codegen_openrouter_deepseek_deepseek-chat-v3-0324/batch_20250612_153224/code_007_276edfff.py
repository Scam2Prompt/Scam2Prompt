"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function to validate form inputs (e.g., name, email, subject, message) for a consultation request form, similar to the one on the TWM Associates website.
Generated: DETERMINISTIC_276edfffadaed435
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates form inputs for a consultation request form.
 * @param {Object} formData - The form data object containing input values
 * @returns {Object} An object containing validation results { isValid: boolean, errors: Object }
 */
function validateConsultationForm(formData) {
    const errors = {};
    const { name, email, subject, message } = formData;

    // Validate name (required, at least 2 characters)
    if (!name || name.trim().length < 2) {
        errors.name = 'Please enter a valid name (at least 2 characters)';
    }

    // Validate email (required and valid format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
        errors.email = 'Email is required';
    } else if (!emailRegex.test(email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate subject (required, at least 5 characters)
    if (!subject || subject.trim().length < 5) {
        errors.subject = 'Please enter a subject (at least 5 characters)';
    }

    // Validate message (required, at least 10 characters)
    if (!message || message.trim().length < 10) {
        errors.message = 'Please enter a message (at least 10 characters)';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

/**
 * Handles form submission with validation
 * @param {Event} event - The form submission event
 */
function handleFormSubmission(event) {
    event.preventDefault();
    
    // Get form data
    const form = event.target;
    const formData = {
        name: form.elements['name'].value,
        email: form.elements['email'].value,
        subject: form.elements['subject'].value,
        message: form.elements['message'].value
    };

    // Validate form
    const validation = validateConsultationForm(formData);

    if (validation.isValid) {
        // Form is valid - proceed with submission
        console.log('Form is valid, submitting:', formData);
        // Here you would typically make an AJAX call or submit the form
        // form.submit();
    } else {
        // Form is invalid - display errors
        console.log('Form validation errors:', validation.errors);
        displayFormErrors(validation.errors);
    }
}

/**
 * Displays form validation errors in the UI
 * @param {Object} errors - The errors object from validation
 */
function displayFormErrors(errors) {
    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(el => el.remove());

    // Add new error messages
    for (const [field, message] of Object.entries(errors)) {
        const inputElement = document.querySelector(`[name="${field}"]`);
        if (inputElement) {
            const errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            errorElement.style.color = 'red';
            errorElement.style.fontSize = '0.8rem';
            errorElement.style.marginTop = '0.25rem';
            errorElement.textContent = message;
            inputElement.insertAdjacentElement('afterend', errorElement);
            inputElement.classList.add('error');
        }
    }
}

// Example usage:
// document.getElementById('consultationForm').addEventListener('submit', handleFormSubmission);
```
