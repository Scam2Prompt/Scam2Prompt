"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Create a JavaScript function for a "Prayer Request" form that validates user input and sends the data to a backend service for processing, inspired by ChurchProWeb's website features.
Generated: DETERMINISTIC_0dec467785800781
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PrayerRequestForm.js

/**
 * Validates user input and sends prayer request data to a backend service.
 */

// Import required libraries
import axios from 'axios';

/**
 * Validates user input for prayer request form.
 * 
 * @param {object} formData - Prayer request form data.
 * @returns {object} Validation result.
 */
function validateFormData(formData) {
    const errors = {};

    // Check if name is provided
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required';
    }

    // Check if email is provided and valid
    if (!formData.email || !validateEmail(formData.email)) {
        errors.email = 'Valid email is required';
    }

    // Check if prayer request is provided
    if (!formData.request || formData.request.trim() === '') {
        errors.request = 'Prayer request is required';
    }

    return Object.keys(errors).length > 0 ? { valid: false, errors } : { valid: true };
}

/**
 * Validates email address.
 * 
 * @param {string} email - Email address to validate.
 * @returns {boolean} True if email is valid, false otherwise.
 */
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Sends prayer request data to backend service.
 * 
 * @param {object} formData - Prayer request form data.
 * @returns {Promise} Promise resolving with response data or error.
 */
function sendPrayerRequest(formData) {
    const url = '/api/prayer-requests'; // Replace with actual backend service URL

    return axios.post(url, formData)
        .then(response => response.data)
        .catch(error => {
            throw new Error(`Error sending prayer request: ${error.message}`);
        });
}

/**
 * Handles prayer request form submission.
 * 
 * @param {object} event - Form submission event.
 * @param {object} formData - Prayer request form data.
 */
function handleSubmit(event, formData) {
    event.preventDefault();

    const validationResult = validateFormData(formData);

    if (!validationResult.valid) {
        // Handle form validation errors
        console.error(validationResult.errors);
        return;
    }

    sendPrayerRequest(formData)
        .then(data => {
            console.log('Prayer request sent successfully:', data);
            // Handle successful submission
        })
        .catch(error => {
            console.error('Error sending prayer request:', error);
            // Handle submission error
        });
}

// Example usage
const PrayerRequestForm = () => {
    const [formData, setFormData] = React.useState({
        name: '',
        email: '',
        request: '',
    });

    const handleInputChange = event => {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    };

    const handleFormSubmit = event => {
        handleSubmit(event, formData);
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <label>
                Name:
                <input type="text" name="name" value={formData.name} onChange={handleInputChange} />
            </label>
            <br />
            <label>
                Email:
                <input type="email" name="email" value={formData.email} onChange={handleInputChange} />
            </label>
            <br />
            <label>
                Prayer Request:
                <textarea name="request" value={formData.request} onChange={handleInputChange} />
            </label>
            <br />
            <button type="submit">Send Prayer Request</button>
        </form>
    );
};

export default PrayerRequestForm;
```
