"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promocrypt.com
Prompt: Create a JavaScript function that validates a domain purchase offer form, ensuring it meets the requirements seen on promocrypt.com.
Generated: DETERMINISTIC_f432c74d7abccc48
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a domain purchase offer form.
 * 
 * @param {Object} formData - The data object representing the form fields.
 * @param {string} formData.domain - The domain name being purchased.
 * @param {number} formData.offerPrice - The offer price for the domain.
 * @param {string} formData.email - The email address of the buyer.
 * @returns {Object} - An object containing validation results and error messages, if any.
 */
function validateDomainOffer(formData) {
    const errors = {};
    const { domain, offerPrice, email } = formData;

    // Validate domain
    if (!domain) {
        errors.domain = "Domain name is required.";
    } else if (!/^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$/.test(domain)) {
        errors.domain = "Invalid domain format.";
    }

    // Validate offer price
    if (offerPrice === undefined || offerPrice === null) {
        errors.offerPrice = "Offer price is required.";
    } else if (isNaN(offerPrice) || offerPrice <= 0) {
        errors.offerPrice = "Offer price must be a positive number.";
    }

    // Validate email
    if (!email) {
        errors.email = "Email address is required.";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        errors.email = "Email address is invalid.";
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage
const form = {
    domain: "example.com",
    offerPrice: 500,
    email: "buyer@example.com"
};

const validationResult = validateDomainOffer(form);
if (!validationResult.isValid) {
    console.error("Validation Errors:", validationResult.errors);
} else {
    console.log("Validation successful! Proceed with the domain purchase.");
}
```
