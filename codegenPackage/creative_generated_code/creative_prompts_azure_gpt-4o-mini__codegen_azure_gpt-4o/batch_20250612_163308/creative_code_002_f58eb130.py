"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Create a function in JavaScript that validates user input for a roofing service request form, ensuring all required fields are filled out correctly before submission.
Generated: DETERMINISTIC_f58eb130d65a40be
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a roofing service request form.
 * Ensures all required fields are filled and properly formatted.
 * @param {Object} formData - An object containing the form data.
 * @returns {Object} - An object with `isValid` (boolean) and `errors` (array of error messages).
 */
function validateRoofingRequestForm(formData) {
  const errors = [];

  // Required fields and their validation rules
  const requiredFields = {
    name: {
      required: true,
      regex: /^[a-zA-Z\s]+$/, // Name should contain only letters and spaces
      errorMessage: "Name is required and must contain only letters and spaces."
    },
    email: {
      required: true,
      regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email validation
      errorMessage: "A valid email address is required."
    },
    phone: {
      required: true,
      regex: /^\d{10}$/, // Basic phone validation: 10 digits
      errorMessage: "Phone number is required and must be exactly 10 digits."
    },
    address: {
      required: true,
      errorMessage: "Address is required."
    },
    roofType: {
      required: true,
      errorMessage: "Roof type is required."
    }
  };

  // Validate each required field
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    if (rules.required && (!value || value.trim() === "")) {
      errors.push(`${rules.errorMessage}`);
      continue;
    }

    if (rules.regex && !rules.regex.test(value)) {
      errors.push(`${rules.errorMessage}`);
    }
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
const formData = {
  name: "John Doe",
  email: "johndoe@example.com",
  phone: "1234567890",
  address: "123 Elm Street",
  roofType: "Shingles"
};

const validationResult = validateRoofingRequestForm(formData);

if (validationResult.isValid) {
  console.log("Form is valid and ready to submit!");
} else {
  console.error("Form has errors:", validationResult.errors);
}
```
