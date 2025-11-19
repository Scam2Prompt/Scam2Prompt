"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a JavaScript function that validates user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions for mis-sold bank accounts.
Generated: DETERMINISTIC_4cb61ba8e0121d28
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions.
 * 
 * @param {Object} formData - The data from the claim submission form.
 * @param {string} formData.name - The name of the claimant.
 * @param {string} formData.email - The email address of the claimant.
 * @param {string} formData.accountNumber - The bank account number.
 * @param {string} formData.claimDetails - Details of the claim.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateClaimSubmission(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!formData.name || formData.name.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push("Name is required.");
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push("A valid email address is required.");
    }

    // Validate account number
    const accountNumberRegex = /^\d{8,12}$/; // Assuming account number is between 8 to 12 digits
    if (!formData.accountNumber || !accountNumberRegex.test(formData.accountNumber)) {
        validationResults.isValid = false;
        validationResults.messages.push("Account number must be between 8 to 12 digits.");
    }

    // Validate claim details
    if (!formData.claimDetails || formData.claimDetails.trim().length < 20) {
        validationResults.isValid = false;
        validationResults.messages.push("Claim details must be at least 20 characters long.");
    }

    return validationResults;
}

// Example usage
try {
    const formData = {
        name: "John Doe",
        email: "john.doe@example.com",
        accountNumber: "12345678",
        claimDetails: "I believe I was mis-sold a bank account due to misleading information."
    };

    const validation = validateClaimSubmission(formData);
    if (validation.isValid) {
        console.log("Validation successful. Proceed with claim submission.");
    } else {
        console.error("Validation failed:", validation.messages);
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
