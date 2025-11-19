"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Create a JavaScript function that validates user input for a contact form aimed at assisted living services, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_70085bb296eba252
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a contact form for assisted living services.
 * @param {Object} formData - The form data object containing user input.
 * @returns {Object} An object containing validation results.
 */
function validateContactForm(formData) {
    const errors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required';
    } else if (formData.name.length > 100) {
        errors.name = 'Name must be less than 100 characters';
    }

    // Validate email
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required';
    } else if (!emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone
    if (!formData.phone || formData.phone.trim() === '') {
        errors.phone = 'Phone number is required';
    } else if (!phoneRegex.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number';
    }

    // Validate message
    if (!formData.message || formData.message.trim() === '') {
        errors.message = 'Message is required';
    } else if (formData.message.length > 1000) {
        errors.message = 'Message must be less than 1000 characters';
    }

    // Validate service type
    if (!formData.serviceType || formData.serviceType.trim() === '') {
        errors.serviceType = 'Service type is required';
    }

    // Validate preferred contact method
    if (!formData.contactMethod || formData.contactMethod.trim() === '') {
        errors.contactMethod = 'Preferred contact method is required';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

/**
 * Handles form submission with validation.
 * @param {Event} event - The form submission event.
 */
function handleFormSubmit(event) {
    event.preventDefault();

    // Get form data
    const form = event.target;
    const formData = {
        name: form.name.value,
        email: form.email.value,
        phone: form.phone.value,
        message: form.message.value,
        serviceType: form.serviceType.value,
        contactMethod: form.contactMethod.value
    };

    // Validate form
    const validation = validateContactForm(formData);

    if (validation.isValid) {
        // Form is valid, proceed with submission
        console.log('Form is valid. Submitting:', formData);
        // Here you would typically send the data to a server
        // form.submit();
        alert('Thank you for your submission! We will contact you soon.');
        form.reset();
    } else {
        // Form is invalid, display errors
        console.log('Form validation errors:', validation.errors);
        displayFormErrors(validation.errors);
    }
}

/**
 * Displays form validation errors to the user.
 * @param {Object} errors - The errors object from validation.
 */
function displayFormErrors(errors) {
    // Clear previous errors
    const errorElements = document.querySelectorAll('.error-message');
    errorElements.forEach(el => el.textContent = '');

    // Display new errors
    for (const [field, message] of Object.entries(errors)) {
        const errorElement = document.querySelector(`.${field}-error`);
        if (errorElement) {
            errorElement.textContent = message;
        }
    }
}

// Add event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#contactForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});
```
