"""
Generated Code Metadata:
========================
Original URL: https://parsflooring.net
Prompt: Develop a JavaScript function to validate user input for a flooring quote request form, ensuring that the input data includes required fields such as name, email, phone number, and flooring specifications.
Generated: DETERMINISTIC_55bb5b8ecb39e3fa
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a flooring quote request form.
 * Ensures required fields are present and properly formatted.
 * @param {Object} formData - The user input data to validate.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateFlooringQuoteRequest(formData) {
  // Initialize an object to store validation results
  const validationResult = {
    isValid: true,
    errors: [],
  };

  // Helper function to validate email format
  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  // Helper function to validate phone number format
  const isValidPhoneNumber = (phoneNumber) => {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phoneRegex.test(phoneNumber);
  };

  // Validate 'name' field
  if (!formData.name || formData.name.trim() === "") {
    validationResult.isValid = false;
    validationResult.errors.push("Name is required.");
  }

  // Validate 'email' field
  if (!formData.email || formData.email.trim() === "") {
    validationResult.isValid = false;
    validationResult.errors.push("Email is required.");
  } else if (!isValidEmail(formData.email)) {
    validationResult.isValid = false;
    validationResult.errors.push("Invalid email format.");
  }

  // Validate 'phoneNumber' field
  if (!formData.phoneNumber || formData.phoneNumber.trim() === "") {
    validationResult.isValid = false;
    validationResult.errors.push("Phone number is required.");
  } else if (!isValidPhoneNumber(formData.phoneNumber)) {
    validationResult.isValid = false;
    validationResult.errors.push("Invalid phone number format.");
  }

  // Validate 'flooringSpecifications' field
  if (!formData.flooringSpecifications || formData.flooringSpecifications.trim() === "") {
    validationResult.isValid = false;
    validationResult.errors.push("Flooring specifications are required.");
  }

  // Return the validation result
  return validationResult;
}

// Example usage:
const userInput = {
  name: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "+1234567890",
  flooringSpecifications: "Laminate flooring for 500 sq ft",
};

const result = validateFlooringQuoteRequest(userInput);
if (result.isValid) {
  console.log("Validation passed!");
} else {
  console.error("Validation failed:", result.errors);
}
```
