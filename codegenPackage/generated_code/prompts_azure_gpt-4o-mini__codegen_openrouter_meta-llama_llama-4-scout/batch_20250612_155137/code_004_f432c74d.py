"""
Generated Code Metadata:
========================
Original URL: https://promocrypt.com
Prompt: Create a JavaScript function that validates a domain purchase offer form, ensuring it meets the requirements seen on promocrypt.com.
Generated: DETERMINISTIC_f432c74d7abccc48
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a domain purchase offer form.
 *
 * @param {Object} formData - The form data to be validated.
 * @param {string} formData.domain - The domain name.
 * @param {string} formData.price - The offered price.
 * @param {string} formData.contactEmail - The contact email.
 * @param {string} formData.contactPhone - The contact phone number.
 *
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */

function validateDomainPurchaseOfferForm(formData) {
    const errors = {};
    let isValid = true;

    // Domain validation
    if (!formData.domain || typeof formData.domain !== 'string' || formData.domain.trim().length === 0) {
        errors.domain = 'Domain is required';
        isValid = false;
    } else if (!/^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(formData.domain)) {
        errors.domain = 'Invalid domain format';
        isValid = false;
    }

    // Price validation
    if (!formData.price || typeof formData.price !== 'string' || formData.price.trim().length === 0) {
        errors.price = 'Price is required';
        isValid = false;
    } else {
        const price = parseFloat(formData.price);
        if (isNaN(price) || price <= 0) {
            errors.price = 'Invalid price';
            isValid = false;
        }
    }

    // Contact email validation
    if (!formData.contactEmail || typeof formData.contactEmail !== 'string' || formData.contactEmail.trim().length === 0) {
        errors.contactEmail = 'Contact email is required';
        isValid = false;
    } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(formData.contactEmail)) {
        errors.contactEmail = 'Invalid email format';
        isValid = false;
    }

    // Contact phone validation
    if (!formData.contactPhone || typeof formData.contactPhone !== 'string' || formData.contactPhone.trim().length === 0) {
        errors.contactPhone = 'Contact phone is required';
        isValid = false;
    } else if (!/^\d{3,15}$/.test(formData.contactPhone.replace(/[^0-9]/g, ''))) {
        errors.contactPhone = 'Invalid phone number format';
        isValid = false;
    }

    return { isValid, errors };
}

// Example usage:
const formData = {
    domain: 'example.com',
    price: '1000',
    contactEmail: 'user@example.com',
    contactPhone: '+1 123 456 7890',
};

const { isValid, errors } = validateDomainPurchaseOfferForm(formData);

console.log(`Is form valid: ${isValid}`);
console.log('Errors:', errors);
```
