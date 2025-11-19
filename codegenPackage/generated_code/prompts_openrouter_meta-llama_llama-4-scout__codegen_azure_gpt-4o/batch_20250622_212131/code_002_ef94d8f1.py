"""
Generated Code Metadata:
========================
Original URL: https://rayatrecruitment.com
Prompt: Generate a JavaScript code snippet to validate user input data for the online application form on the Rayat Shikshan Sanstha website, ensuring that the data is accurate and complete before submission.
Generated: DETERMINISTIC_ef94d8f1f21e20fe
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to validate user input data for an online application form.
 * Ensures data is accurate and complete before submission.
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateFormData(formData) {
  const errors = {};

  // Validate full name (required, must be at least 3 characters)
  if (!formData.fullName || formData.fullName.trim().length < 3) {
    errors.fullName = "Full name is required and must be at least 3 characters long.";
  }

  // Validate email (required, must be a valid email format)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email || !emailRegex.test(formData.email)) {
    errors.email = "A valid email address is required.";
  }

  // Validate phone number (required, must be 10 digits)
  const phoneRegex = /^\d{10}$/;
  if (!formData.phone || !phoneRegex.test(formData.phone)) {
    errors.phone = "Phone number is required and must be exactly 10 digits.";
  }

  // Validate age (optional, must be a number between 18 and 100 if provided)
  if (formData.age && (isNaN(formData.age) || formData.age < 18 || formData.age > 100)) {
    errors.age = "Age must be a number between 18 and 100.";
  }

  // Validate address (required, must not be empty)
  if (!formData.address || formData.address.trim().length === 0) {
    errors.address = "Address is required.";
  }

  // Validate course selection (required, must not be empty)
  if (!formData.course || formData.course.trim().length === 0) {
    errors.course = "Course selection is required.";
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0,
    errors: errors,
  };
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "1234567890",
  age: 25,
  address: "123 Main Street",
  course: "Computer Science",
};

const validationResult = validateFormData(formData);

if (validationResult.isValid) {
  console.log("Form data is valid. Ready for submission.");
} else {
  console.error("Form data validation failed:", validationResult.errors);
}
```
