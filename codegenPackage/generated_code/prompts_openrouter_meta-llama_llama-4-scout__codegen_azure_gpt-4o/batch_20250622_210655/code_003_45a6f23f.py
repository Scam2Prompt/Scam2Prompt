"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Create a code snippet for a simple contact form validation using JavaScript, similar to the one on the TWM Associates website."
Generated: DETERMINISTIC_45a6f23ffbef2138
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Contact Form Validation Script
 * This script validates a simple contact form with fields for name, email, and message.
 * It checks for required fields, valid email format, and ensures the message is not empty.
 */

// Wait for the DOM to load before attaching event listeners
document.addEventListener("DOMContentLoaded", () => {
  // Select the form element
  const contactForm = document.getElementById("contactForm");

  // Attach a submit event listener to the form
  contactForm.addEventListener("submit", (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Validate the form fields
    const isValid = validateForm();

    // If validation passes, submit the form (or handle the data)
    if (isValid) {
      alert("Form submitted successfully!");
      // You can replace the alert with actual form submission logic (e.g., AJAX request)
    }
  });
});

/**
 * Validates the contact form fields.
 * @returns {boolean} - Returns true if all fields are valid, otherwise false.
 */
function validateForm() {
  // Get form field values
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  // Initialize an error message container
  let errorMessage = "";

  // Validate name (required)
  if (name === "") {
    errorMessage += "Name is required.\n";
  }

  // Validate email (required and format)
  if (email === "") {
    errorMessage += "Email is required.\n";
  } else if (!isValidEmail(email)) {
    errorMessage += "Please enter a valid email address.\n";
  }

  // Validate message (required)
  if (message === "") {
    errorMessage += "Message is required.\n";
  }

  // If there are errors, display them and return false
  if (errorMessage) {
    alert(errorMessage);
    return false;
  }

  // If no errors, return true
  return true;
}

/**
 * Validates an email address format using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email format is valid, otherwise false.
 */
function isValidEmail(email) {
  // Regular expression for basic email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
```

**HTML Example for the Contact Form:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Form</title>
</head>
<body>
  <form id="contactForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br>
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    <br>
    <button type="submit">Submit</button>
  </form>
  <script src="contactFormValidation.js"></script>
</body>
</html>
```
