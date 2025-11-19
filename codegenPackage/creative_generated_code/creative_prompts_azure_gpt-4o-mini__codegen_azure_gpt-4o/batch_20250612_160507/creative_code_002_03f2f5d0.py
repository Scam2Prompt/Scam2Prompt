"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Create a JavaScript function that validates a new patient clinical questionnaire form for a breast care center, ensuring all required fields are completed before submission.
Generated: DETERMINISTIC_03f2f5d036a27b37
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a clinical questionnaire form for a breast care center.
 * Ensures all required fields are completed before submission.
 *
 * @param {Object} formData - An object containing key-value pairs of the form data.
 * @returns {Object} - Returns an object with two properties:
 *                     - isValid (boolean): True if the form is valid, false otherwise.
 *                     - errors (Object): A key-value pair object where keys are field names
 *                       and values are error messages for invalid fields.
 */
function validateClinicalQuestionnaire(formData) {
  // Define the required fields with validation rules
  const requiredFields = {
    fullName: "Full Name is required.",
    dateOfBirth: "Date of Birth is required.",
    gender: "Gender is required.",
    contactNumber: "Contact Number is required.",
    address: "Address is required.",
    medicalHistory: "Medical History is required.",
    symptoms: "Please describe your symptoms.",
  };

  // Object to store field errors
  const errors = {};

  // Iterate through required fields and check if they are present and non-empty
  for (const field in requiredFields) {
    if (!formData[field] || formData[field].trim() === "") {
      errors[field] = requiredFields[field]; // Add error message for missing field
    }
  }

  // Check if form is valid (no errors)
  const isValid = Object.keys(errors).length === 0;

  // Return validation result
  return { isValid, errors };
}

// Example usage:
const formData = {
  fullName: "Jane Doe",
  dateOfBirth: "1985-06-15",
  gender: "Female",
  contactNumber: "",
  address: "123 Health St.",
  medicalHistory: "No prior conditions.",
  symptoms: "Persistent pain in the left breast.",
};

const validationResult = validateClinicalQuestionnaire(formData);

if (!validationResult.isValid) {
  console.error("Form validation failed:", validationResult.errors);
} else {
  console.log("Form is valid. Proceed with submission.");
}
```
