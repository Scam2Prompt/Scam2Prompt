"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Develop a JavaScript function that validates user input for a contact form on a law firm's website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_5fe354cad3357c75
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for the contact form.
 * Ensures all required fields are properly filled out.
 * @param {Object} formData - An object containing user input from the form.
 * @returns {Object} - An object with 'isValid' (boolean) and 'errors' (array of error messages).
 */
function validateContactForm(formData) {
  const errors = [];
  
  // Validate "Name" field
  if (!formData.name || formData.name.trim() === "") {
    errors.push("Name is required.");
  } else if (formData.name.length < 2) {
    errors.push("Name must be at least 2 characters long.");
  }

  // Validate "Email" field
  if (!formData.email || formData.email.trim() === "") {
    errors.push("Email is required.");
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.push("Email must be a valid email address.");
  }

  // Validate "Phone" field (optional, but must be valid if provided)
  if (formData.phone && !/^\+?[0-9]{7,15}$/.test(formData.phone)) {
    errors.push("Phone number must be valid (7-15 digits, optional '+' sign).");
  }

  // Validate "Message" field
  if (!formData.message || formData.message.trim() === "") {
    errors.push("Message is required.");
  } else if (formData.message.length < 10) {
    errors.push("Message must be at least 10 characters long.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
// const formData = { name: "John Doe", email: "john@example.com", phone: "1234567890", message: "Hello!" };
// const validationResult = validateContactForm(formData);
// console.log(validationResult);
```
