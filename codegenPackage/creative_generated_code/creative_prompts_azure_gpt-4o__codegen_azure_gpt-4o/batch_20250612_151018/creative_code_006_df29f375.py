"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a JavaScript function to validate user input for a web form that collects refuse and recycling pickup requests for the City of York.
Generated: DETERMINISTIC_df29f375b467a2a9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a refuse and recycling pickup request form.
 * 
 * @param {Object} formData - The user input data to validate.
 * @param {string} formData.name - The name of the user (required, at least 2 characters).
 * @param {string} formData.email - The email address of the user (required, valid email format).
 * @param {string} formData.address - The address for pickup (required, non-empty).
 * @param {string} formData.pickupDate - The requested pickup date (required, valid date in the future).
 * @param {string} formData.pickupType - The type of pickup (either "refuse" or "recycling").
 * @returns {Object} - An object containing `isValid: boolean` and `errors: string[]`.
 */
function validatePickupRequest(formData) {
    const errors = [];

    // Validate name (required, at least 2 characters)
    if (!formData.name || formData.name.trim().length < 2) {
        errors.push("Name must be at least 2 characters long.");
    }

    // Validate email (required, valid email format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.push("A valid email address is required.");
    }

    // Validate address (required, non-empty)
    if (!formData.address || formData.address.trim() === "") {
        errors.push("Address is required.");
    }

    // Validate pickup date (required, must be a valid future date)
    const today = new Date();
    const pickupDate = new Date(formData.pickupDate);
    if (!formData.pickupDate || isNaN(pickupDate.getTime()) || pickupDate <= today) {
        errors.push("Pickup date must be a valid date in the future.");
    }

    // Validate pickup type (required, must be "refuse" or "recycling")
    const validPickupTypes = ["refuse", "recycling"];
    if (!formData.pickupType || !validPickupTypes.includes(formData.pickupType.toLowerCase())) {
        errors.push("Pickup type must be either 'refuse' or 'recycling'.");
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    address: "123 Elm Street",
    pickupDate: "2023-12-15",
    pickupType: "recycling"
};

const validationResult = validatePickupRequest(formData);

if (validationResult.isValid) {
    console.log("Form is valid. Proceed with submission.");
} else {
    console.error("Form validation failed with the following errors:");
    console.error(validationResult.errors);
}
```
