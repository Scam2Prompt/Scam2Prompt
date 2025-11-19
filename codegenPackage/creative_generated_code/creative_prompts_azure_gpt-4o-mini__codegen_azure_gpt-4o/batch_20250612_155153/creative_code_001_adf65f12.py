"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Write a JavaScript function that validates user input for a school registration form, inspired by the Colegio Panamericano's enrollment process.
Generated: DETERMINISTIC_adf65f12f7ac3117
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateRegistrationForm - Validates user input for a school registration form.
 * @param {Object} formData - The input data from the registration form.
 * @returns {Object} - An object containing validation results and error messages (if any).
 */
function validateRegistrationForm(formData) {
  const errors = {};
  const validationResult = {
    isValid: true,
    errors: errors,
  };

  // Validate first name
  if (!formData.firstName || formData.firstName.trim() === "") {
    errors.firstName = "First name is required.";
    validationResult.isValid = false;
  } else if (formData.firstName.length > 50) {
    errors.firstName = "First name cannot exceed 50 characters.";
    validationResult.isValid = false;
  }

  // Validate last name
  if (!formData.lastName || formData.lastName.trim() === "") {
    errors.lastName = "Last name is required.";
    validationResult.isValid = false;
  } else if (formData.lastName.length > 50) {
    errors.lastName = "Last name cannot exceed 50 characters.";
    validationResult.isValid = false;
  }

  // Validate date of birth
  if (!formData.dateOfBirth) {
    errors.dateOfBirth = "Date of birth is required.";
    validationResult.isValid = false;
  } else {
    const dob = new Date(formData.dateOfBirth);
    const today = new Date();
    if (isNaN(dob.getTime())) {
      errors.dateOfBirth = "Invalid date format.";
      validationResult.isValid = false;
    } else if (dob >= today) {
      errors.dateOfBirth = "Date of birth must be in the past.";
      validationResult.isValid = false;
    }
  }

  // Validate email
  if (!formData.email || formData.email.trim() === "") {
    errors.email = "Email is required.";
    validationResult.isValid = false;
  } else {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      errors.email = "Invalid email format.";
      validationResult.isValid = false;
    }
  }

  // Validate phone number
  if (formData.phoneNumber && formData.phoneNumber.trim() !== "") {
    const phoneRegex = /^\+?[0-9]{10,15}$/;
    if (!phoneRegex.test(formData.phoneNumber)) {
      errors.phoneNumber = "Phone number must be between 10 and 15 digits and may include a '+' prefix.";
      validationResult.isValid = false;
    }
  }

  // Validate grade level
  if (!formData.gradeLevel || isNaN(formData.gradeLevel)) {
    errors.gradeLevel = "Grade level is required and must be a valid number.";
    validationResult.isValid = false;
  } else if (formData.gradeLevel < 1 || formData.gradeLevel > 12) {
    errors.gradeLevel = "Grade level must be between 1 and 12.";
    validationResult.isValid = false;
  }

  // Validate additional comments (optional, max length of 500 characters)
  if (formData.additionalComments && formData.additionalComments.length > 500) {
    errors.additionalComments = "Additional comments cannot exceed 500 characters.";
    validationResult.isValid = false;
  }

  return validationResult;
}

// Example Usage
const formInput = {
  firstName: "John",
  lastName: "Doe",
  dateOfBirth: "2010-05-15",
  email: "john.doe@example.com",
  phoneNumber: "+1234567890",
  gradeLevel: 5,
  additionalComments: "Excited to enroll!",
};

const result = validateRegistrationForm(formInput);
console.log(result);
```
