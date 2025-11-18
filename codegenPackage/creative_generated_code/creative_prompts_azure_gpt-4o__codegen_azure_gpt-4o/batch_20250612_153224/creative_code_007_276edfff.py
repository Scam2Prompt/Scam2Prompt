"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function to validate form inputs (e.g., name, email, subject, message) for a consultation request form, similar to the one on the TWM Associates website.
Generated: DETERMINISTIC_276edfffadaed435
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates form inputs for a consultation request form.
 * @param {Object} formData - An object containing the form inputs.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.subject - The subject of the consultation request.
 * @param {string} formData.message - The message body of the consultation request.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validateFormInputs(formData) {
  // Initialize an object to store validation results
  const validationResults = {
    isValid: true, // Overall form validity
    errors: {}     // Specific error messages for each field
  };

  // Helper function to validate email format
  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  // Validate name (non-empty, alphabetic characters)
  if (!formData.name || formData.name.trim() === "") {
    validationResults.isValid = false;
    validationResults.errors.name = "Name is required.";
  } else if (!/^[a-zA-Z\s]+$/.test(formData.name)) {
    validationResults.isValid = false;
    validationResults.errors.name = "Name can only contain alphabetic characters.";
  }

  // Validate email (non-empty, proper format)
  if (!formData.email || formData.email.trim() === "") {
    validationResults.isValid = false;
    validationResults.errors.email = "Email is required.";
  } else if (!isValidEmail(formData.email)) {
    validationResults.isValid = false;
    validationResults.errors.email = "Invalid email format.";
  }

  // Validate subject (non-empty, reasonable length)
  if (!formData.subject || formData.subject.trim() === "") {
    validationResults.isValid = false;
    validationResults.errors.subject = "Subject is required.";
  } else if (formData.subject.length > 100) {
    validationResults.isValid = false;
    validationResults.errors.subject = "Subject cannot exceed 100 characters.";
  }

  // Validate message (non-empty, reasonable length)
  if (!formData.message || formData.message.trim() === "") {
    validationResults.isValid = false;
    validationResults.errors.message = "Message is required.";
  } else if (formData.message.length > 500) {
    validationResults.isValid = false;
    validationResults.errors.message = "Message cannot exceed 500 characters.";
  }

  // Return the validation results
  return validationResults;
}

// Example usage
const formData = {
  name: "John Doe",
  email: "john.doe@example.com",
  subject: "Consultation Request",
  message: "I would like to schedule a consultation regarding your services."
};

const result = validateFormInputs(formData);
if (result.isValid) {
  console.log("Form inputs are valid.");
} else {
  console.error("Form validation errors:", result.errors);
}
```
