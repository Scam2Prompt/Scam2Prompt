"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Develop a JavaScript function that validates user input for a contact form, ensuring all fields are filled out correctly, inspired by the contact information layout on the Perrigo Claims site.
Generated: DETERMINISTIC_ab86a240225bbcfa
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a contact form input.
 * Ensures all fields are filled out correctly.
 * Inspired by the contact information layout on the Perrigo Claims site.
 *
 * @param {Object} formData - Object containing user input from the form.
 * @returns {Object} Validation result with a boolean status and error messages if validation fails.
 */
function validateContactForm(formData) {
  // Error messages array
  const errors = [];
  
  // Check if "Name" field is present and valid
  if (!formData.name || formData.name.trim() === "") {
    errors.push("Name is required.");
  }
  
  // Check if "Email" field is present and valid
  if (!formData.email || formData.email.trim() === "") {
    errors.push("Email is required.");
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.push("Email format is invalid.");
  }
  
  // Check if "Phone Number" field is present and valid
  if (!formData.phone || formData.phone.trim() === "") {
    errors.push("Phone Number is required.");
  } else if (!/^\d{10}$/.test(formData.phone)) {
    errors.push("Phone Number must be a 10-digit number.");
  }
  
  // Check if "Message" field is present and valid
  if (!formData.message || formData.message.trim() === "") {
    errors.push("Message is required.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example Usage:
// Assuming this is the user input object from the form
const formData = {
  name: "John Doe",
  email: "johndoe@example.com",
  phone: "1234567890",
  message: "Hello, I want to inquire about your services."
};

const validationResult = validateContactForm(formData);

if (validationResult.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Form validation failed:", validationResult.errors);
}
```
