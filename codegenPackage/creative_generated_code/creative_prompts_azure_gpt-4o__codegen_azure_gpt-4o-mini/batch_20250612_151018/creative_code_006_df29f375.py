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
 * Validates user input for refuse and recycling pickup requests.
 * @param {Object} formData - The data from the web form.
 * @param {string} formData.name - The name of the requester.
 * @param {string} formData.address - The address for pickup.
 * @param {string} formData.pickupType - The type of pickup (e.g., "refuse" or "recycling").
 * @returns {Object} - An object containing the validation result and error messages, if any.
 */
function validatePickupRequest(formData) {
    const errors = [];
    const validPickupTypes = ["refuse", "recycling"];
    
    // Validate name
    if (!formData.name || typeof formData.name !== "string" || formData.name.trim() === "") {
        errors.push("Name is required and must be a non-empty string.");
    }

    // Validate address
    if (!formData.address || typeof formData.address !== "string" || formData.address.trim() === "") {
        errors.push("Address is required and must be a non-empty string.");
    }

    // Validate pickup type
    if (!formData.pickupType || !validPickupTypes.includes(formData.pickupType)) {
        errors.push(`Pickup type is required and must be one of the following: ${validPickupTypes.join(", ")}.`);
    }

    // Return validation results
    if (errors.length > 0) {
        return {
            isValid: false,
            errors: errors,
        };
    } else {
        return {
            isValid: true,
            errors: [],
        };
    }
}

// Example usage
const requestData = {
    name: "John Doe",
    address: "123 Main St, York, PA",
    pickupType: "refuse",
};

const validationResult = validatePickupRequest(requestData);

if (!validationResult.isValid) {
    console.error("Validation errors:", validationResult.errors);
} else {
    console.log("Validation successful! Ready to process the pickup request.");
}
```
