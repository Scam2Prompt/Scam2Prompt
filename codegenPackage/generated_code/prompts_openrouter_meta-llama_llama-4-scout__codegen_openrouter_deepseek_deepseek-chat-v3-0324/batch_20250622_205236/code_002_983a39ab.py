"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Generate JavaScript code for validating a sweepstakes entry form with fields for first name, last name, address, city, state, zip, and email, similar to the form on thedaybrightener.com.
Generated: DETERMINISTIC_983a39abb9d7caac
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a sweepstakes entry form with fields for first name, last name, address, city, state, zip, and email.
 * @param {Object} formData - The form data object containing all field values
 * @returns {Object} An object containing validation results (isValid: boolean, errors: Object)
 */
function validateSweepstakesForm(formData) {
    const errors = {};
    const result = { isValid: true, errors };

    // Validate first name (required, letters only, 2-50 chars)
    if (!formData.firstName || !formData.firstName.trim()) {
        errors.firstName = 'First name is required';
        result.isValid = false;
    } else if (!/^[a-zA-Z\-'\s]{2,50}$/.test(formData.firstName)) {
        errors.firstName = 'First name must be 2-50 letters';
        result.isValid = false;
    }

    // Validate last name (required, letters only, 2-50 chars)
    if (!formData.lastName || !formData.lastName.trim()) {
        errors.lastName = 'Last name is required';
        result.isValid = false;
    } else if (!/^[a-zA-Z\-'\s]{2,50}$/.test(formData.lastName)) {
        errors.lastName = 'Last name must be 2-50 letters';
        result.isValid = false;
    }

    // Validate address (required, alphanumeric with common address chars)
    if (!formData.address || !formData.address.trim()) {
        errors.address = 'Address is required';
        result.isValid = false;
    } else if (!/^[a-zA-Z0-9\s\-#,.'\/]{5,100}$/.test(formData.address)) {
        errors.address = 'Please enter a valid address';
        result.isValid = false;
    }

    // Validate city (required, letters only, 2-50 chars)
    if (!formData.city || !formData.city.trim()) {
        errors.city = 'City is required';
        result.isValid = false;
    } else if (!/^[a-zA-Z\s\-']{2,50}$/.test(formData.city)) {
        errors.city = 'Please enter a valid city name';
        result.isValid = false;
    }

    // Validate state (required, must be valid US state abbreviation)
    const validStates = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'];
    if (!formData.state || !formData.state.trim()) {
        errors.state = 'State is required';
        result.isValid = false;
    } else if (!validStates.includes(formData.state.toUpperCase())) {
        errors.state = 'Please select a valid state';
        result.isValid = false;
    }

    // Validate zip code (required, valid US zip format)
    if (!formData.zip || !formData.zip.trim()) {
        errors.zip = 'Zip code is required';
        result.isValid = false;
    } else if (!/^\d{5}(-\d{4})?$/.test(formData.zip)) {
        errors.zip = 'Please enter a valid zip code';
        result.isValid = false;
    }

    // Validate email (required, valid format)
    if (!formData.email || !formData.email.trim()) {
        errors.email = 'Email is required';
        result.isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
        result.isValid = false;
    }

    return result;
}

/**
 * Handles form submission and validation
 * @param {Event} event - The form submission event
 */
function handleFormSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const form = event.target;
    const formData = {
        firstName: form.firstName.value,
        lastName: form.lastName.value,
        address: form.address.value,
        city: form.city.value,
        state: form.state.value,
        zip: form.zip.value,
        email: form.email.value
    };

    // Validate form
    const validation = validateSweepstakesForm(formData);

    // Display errors or submit form
    if (validation.isValid) {
        // Form is valid - proceed with submission
        console.log('Form is valid, submitting:', formData);
        // Here you would typically make an AJAX call or form submission
        form.submit();
    } else {
        // Form is invalid - display errors
        console.log('Form validation errors:', validation.errors);
        displayFormErrors(validation.errors);
    }
}

/**
 * Displays validation errors on the form
 * @param {Object} errors - The errors object from validation
 */
function displayFormErrors(errors) {
    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(el => el.remove());

    // Display new errors
    for (const field in errors) {
        const inputElement = document.querySelector(`[name="${field}"]`);
        if (inputElement) {
            const errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            errorElement.textContent = errors[field];
            errorElement.style.color = 'red';
            errorElement.style.fontSize = '0.8em';
            inputElement.insertAdjacentElement('afterend', errorElement);
        }
    }
}

// Add event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sweepstakes-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});
```
