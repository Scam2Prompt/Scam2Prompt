"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Create a JavaScript function that validates user input for the admission query form at SMA Rizvi Textile Institute, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_313c15c5657f3c26
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate the admission query form at SMA Rizvi Textile Institute.
 * Ensures all required fields are filled correctly and provides feedback if validation fails.
 * @param {Object} formData - An object representing the input fields from the form.
 * @returns {Object} - Result object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validateAdmissionForm(formData) {
  // Result object to track validation status and errors
  const result = {
    isValid: true,
    errors: [],
  };

  // Required fields for the form
  const requiredFields = [
    { field: "fullName", message: "Full name is required." },
    { field: "email", message: "Email is required." },
    { field: "phone", message: "Phone number is required." },
    { field: "address", message: "Address is required." },
    { field: "query", message: "Query is required." },
  ];

  // Validate required fields
  requiredFields.forEach(({ field, message }) => {
    if (!formData[field] || formData[field].trim() === "") {
      result.isValid = false;
      result.errors.push(message);
    }
  });

  // Validate email format using regular expression
  if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    result.isValid = false;
    result.errors.push("Invalid email format.");
  }

  // Validate phone number format (basic check for numeric values and length)
  if (formData.phone && !/^\d{10}$/.test(formData.phone)) {
    result.isValid = false;
    result.errors.push("Phone number must be 10 digits.");
  }

  // Return the validation result
  return result;
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "1234567890",
  address: "123 Elm Street",
  query: "What are the course offerings?",
};

const validationResult = validateAdmissionForm(formData);
if (validationResult.isValid) {
  console.log("Form is valid.");
} else {
  console.log("Form is invalid. Errors:", validationResult.errors);
}
```
