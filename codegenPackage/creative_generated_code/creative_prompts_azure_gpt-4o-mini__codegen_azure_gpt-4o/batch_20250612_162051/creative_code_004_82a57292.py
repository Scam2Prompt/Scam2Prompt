"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.albertozofrea.it
Prompt: Construct a JavaScript function that validates user input for a contact form based on the details provided on the Alberto Zofrea site.
Generated: DETERMINISTIC_82a57292a4e49156
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
 * Validates user input for a contact form.
 * Fields validated:
 * - Name: Must be non-empty and only contain alphabetic characters and spaces.
 * - Email: Must be a valid email format.
 * - Message: Must be non-empty and not exceed 500 characters.
 * 
 * @param {Object} input - The user's form input.
 * @param {string} input.name - The user's name.
 * @param {string} input.email - The user's email address.
 * @param {string} input.message - The user's message.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateContactForm(input) {
  // Initialize an array to store error messages
  const errors = [];

  // Validate name: must be non-empty and only contain alphabetic characters and spaces
  if (!input.name || !/^[a-zA-Z\s]+$/.test(input.name)) {
    errors.push("Name must be non-empty and contain only alphabetic characters and spaces.");
  }

  // Validate email: must follow a standard email format
  const emailRegex =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regular expression for validating email format
  if (!input.email || !emailRegex.test(input.email)) {
    errors.push("Please enter a valid email address.");
  }

  // Validate message: must be non-empty and not exceed 500 characters
  if (!input.message || input.message.length > 500) {
    errors.push("Message must be non-empty and not exceed 500 characters.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors, // Array containing error messages if validation fails
  };
}

// Example usage
const formInput = {
  name: "John Doe",
  email: "john.doe@example.com",
  message: "Hello, Alberto Zofrea!",
};

const validationResult = validateContactForm(formInput);

// Log the result of validation
if (validationResult.isValid) {
  console.log("Validation successful!");
} else {
  console.error("Validation failed with errors:", validationResult.errors);
}
```
