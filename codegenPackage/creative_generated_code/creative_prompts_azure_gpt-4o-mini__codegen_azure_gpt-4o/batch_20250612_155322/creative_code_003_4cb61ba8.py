"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a JavaScript function that validates user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions for mis-sold bank accounts.
Generated: DETERMINISTIC_4cb61ba8e0121d28
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a claim submission form.
 * Requirements:
 * - Full name: Must not be empty and at least 2 characters long.
 * - Email: Must be a valid email format.
 * - Phone: Must be a valid phone number (digits only, 10-15 characters).
 * - Claim details: Must not be empty and at least 20 characters long.
 * @param {Object} input - User input object containing fullName, email, phone, and claimDetails.
 * @returns {Object} - Validation result object with isValid (boolean) and errors (array of strings).
 */
function validateClaimSubmission(input) {
  const errors = [];
  
  // Validate full name
  if (!input.fullName || input.fullName.trim().length < 2) {
    errors.push("Full name must be at least 2 characters long.");
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!input.email || !emailRegex.test(input.email)) {
    errors.push("Email must be a valid email format.");
  }

  // Validate phone
  const phoneRegex = /^\d{10,15}$/;
  if (!input.phone || !phoneRegex.test(input.phone)) {
    errors.push("Phone number must contain 10-15 digits.");
  }

  // Validate claim details
  if (!input.claimDetails || input.claimDetails.trim().length < 20) {
    errors.push("Claim details must be at least 20 characters long.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
const userInput = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "1234567890",
  claimDetails: "My bank account was mis-sold because of misleading terms.",
};

const validationResult = validateClaimSubmission(userInput);
if (validationResult.isValid) {
  console.log("Validation passed!");
} else {
  console.error("Validation failed:", validationResult.errors);
}
```
