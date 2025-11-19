"""
Generated Code Metadata:
========================
Original URL: https://zk.fest.co
Prompt: Create a JavaScript function that validates user input for contacting sellers on a domain sale website like Fest.co.
Generated: DETERMINISTIC_5214d5d5a051bb5c
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for contacting sellers on a domain sale website.
 * @param {Object} userInput - The user input object containing name, email, and message.
 * @returns {Object} - An object containing isValid (boolean) and errors (array of error messages).
 */
function validateContactInput(userInput) {
  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: []
  };

  try {
    // Check if userInput is an object
    if (typeof userInput !== 'object' || userInput === null) {
      throw new Error("Invalid input format. Expected an object.");
    }

    // Validate name
    if (!userInput.name || typeof userInput.name !== 'string' || userInput.name.trim().length < 2) {
      validationResult.isValid = false;
      validationResult.errors.push("Name must be a string with at least 2 characters.");
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || typeof userInput.email !== 'string' || !emailRegex.test(userInput.email)) {
      validationResult.isValid = false;
      validationResult.errors.push("Email must be a valid email address.");
    }

    // Validate message
    if (!userInput.message || typeof userInput.message !== 'string' || userInput.message.trim().length < 10) {
      validationResult.isValid = false;
      validationResult.errors.push("Message must be a string with at least 10 characters.");
    }

  } catch (error) {
    // Handle unexpected errors
    validationResult.isValid = false;
    validationResult.errors.push(error.message);
  }

  return validationResult;
}

// Example usage:
const userInput = {
  name: "John Doe",
  email: "john.doe@example.com",
  message: "I am interested in purchasing this domain."
};

const result = validateContactInput(userInput);
if (result.isValid) {
  console.log("Validation passed!");
} else {
  console.error("Validation failed:", result.errors);
}
```
