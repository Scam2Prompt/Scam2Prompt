"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Create a code snippet in JavaScript to validate user input for a martial arts school's registration form, including fields for name, age, and contact information.
Generated: DETERMINISTIC_6d93db92a997e9a2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to validate the registration form input
function validateRegistrationForm(formData) {
  // Object to store validation errors
  const errors = {};

  // Validate name (must be non-empty and only contain letters and spaces)
  if (!formData.name || typeof formData.name !== 'string' || !/^[a-zA-Z\s]+$/.test(formData.name)) {
    errors.name = "Name must be a non-empty string containing only letters and spaces.";
  }

  // Validate age (must be a number between 5 and 100)
  if (!formData.age || typeof formData.age !== 'number' || formData.age < 5 || formData.age > 100) {
    errors.age = "Age must be a number between 5 and 100.";
  }

  // Validate contact information (must be a valid email or phone number)
  if (
    !formData.contact ||
    typeof formData.contact !== 'string' ||
    (!/^\d{10}$/.test(formData.contact) && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.contact))
  ) {
    errors.contact = "Contact must be a valid 10-digit phone number or email address.";
  }

  // Return errors object (empty if no errors)
  return errors;
}

// Example usage
const formData = {
  name: "John Doe",
  age: 25,
  contact: "john.doe@example.com",
};

const validationErrors = validateRegistrationForm(formData);

if (Object.keys(validationErrors).length === 0) {
  console.log("Form is valid. Proceed with registration.");
} else {
  console.error("Form validation failed:", validationErrors);
}
```
