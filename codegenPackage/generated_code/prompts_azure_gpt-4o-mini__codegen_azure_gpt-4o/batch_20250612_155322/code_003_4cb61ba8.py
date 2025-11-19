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
 * Validates user input for a claim submission form.
 * Requirements:
 * - Full Name: Required, must be at least 2 characters.
 * - Email: Required, must be a valid email format.
 * - Phone Number: Optional, but if provided, must be a valid UK phone number.
 * - Claim Amount: Required, must be a positive number.
 * - Claim Reason: Required, must be at least 10 characters.
 * 
 * @param {Object} formData - The user input data.
 * @param {string} formData.fullName - Full name of the user.
 * @param {string} formData.email - Email address of the user.
 * @param {string} [formData.phoneNumber] - Optional phone number of the user.
 * @param {number} formData.claimAmount - Claim amount submitted by the user.
 * @param {string} formData.claimReason - Reason for the claim.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateClaimSubmission(formData) {
  const errors = {};

  // Validate Full Name
  if (!formData.fullName || formData.fullName.trim().length < 2) {
    errors.fullName = "Full Name is required and must be at least 2 characters.";
  }

  // Validate Email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email || !emailRegex.test(formData.email)) {
    errors.email = "A valid email address is required.";
  }

  // Validate Phone Number (Optional)
  const ukPhoneRegex = /^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$/;
  if (formData.phoneNumber && !ukPhoneRegex.test(formData.phoneNumber)) {
    errors.phoneNumber = "If provided, phone number must be a valid UK number.";
  }

  // Validate Claim Amount
  if (formData.claimAmount === undefined || formData.claimAmount <= 0) {
    errors.claimAmount = "Claim Amount is required and must be a positive number.";
  }

  // Validate Claim Reason
  if (!formData.claimReason || formData.claimReason.trim().length < 10) {
    errors.claimReason = "Claim Reason is required and must be at least 10 characters.";
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "+447123456789",
  claimAmount: 1000,
  claimReason: "The bank account was mis-sold due to incorrect advice.",
};

const validationResult = validateClaimSubmission(formData);
if (validationResult.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Form validation failed:", validationResult.errors);
}
```
