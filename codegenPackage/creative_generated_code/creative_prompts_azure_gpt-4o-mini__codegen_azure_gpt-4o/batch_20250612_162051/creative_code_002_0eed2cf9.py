"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Create a code snippet in JavaScript that validates user input for the Certificazione di alfabetizzazione digitale (CIAD) registration form mentioned on Geta Consulenze's site.
Generated: DETERMINISTIC_0eed2cf9f68a82b7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validate user input for the CIAD registration form
 * This code checks for valid input, ensuring required fields are filled
 * and meet predefined criteria such as length, format, etc.
 */

// Function to validate the registration form
function validateCIADForm(formData) {
  const errors = [];

  // Validate name field (must not be empty and must contain only letters)
  if (!formData.name || !/^[a-zA-Z\s]+$/.test(formData.name)) {
    errors.push("Invalid name. Name must contain only letters and cannot be empty.");
  }

  // Validate email field (must be in valid email format)
  if (
    !formData.email ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)
  ) {
    errors.push("Invalid email address.");
  }

  // Validate phone number (must be numeric and 10-15 characters long)
  if (
    !formData.phone ||
    !/^\d{10,15}$/.test(formData.phone)
  ) {
    errors.push("Invalid phone number. Must be numeric and 10-15 digits long.");
  }

  // Validate date of birth (must be in YYYY-MM-DD format and a valid date)
  if (!formData.dateOfBirth || !isValidDate(formData.dateOfBirth)) {
    errors.push(
      "Invalid date of birth. Must be in YYYY-MM-DD format and a valid date."
    );
  }

  // Validate CIAD certification type (must be one of the predefined options)
  const validCertificationTypes = ["basic", "advanced", "professional"];
  if (
    !formData.certificationType ||
    !validCertificationTypes.includes(formData.certificationType.toLowerCase())
  ) {
    errors.push(
      "Invalid certification type. Must be one of: basic, advanced, professional."
    );
  }

  // Return errors if any, or null if validation passes
  if (errors.length > 0) {
    return { success: false, errors };
  }

  return { success: true, errors: [] };
}

/**
 * Helper function to check if a date is valid
 * @param {string} dateStr - The date string in YYYY-MM-DD format
 * @returns {boolean} - True if the date is valid, false otherwise
 */
function isValidDate(dateStr) {
  const date = new Date(dateStr);
  return (
    date instanceof Date &&
    !isNaN(date) &&
    dateStr === date.toISOString().split("T")[0]
  );
}

// Example usage
const formData = {
  name: "Mario Rossi",
  email: "mario.rossi@example.com",
  phone: "1234567890",
  dateOfBirth: "1990-01-01",
  certificationType: "advanced",
};

const validationResult = validateCIADForm(formData);

if (!validationResult.success) {
  console.error("Validation errors:", validationResult.errors);
} else {
  console.log("Validation successful!");
}
```
