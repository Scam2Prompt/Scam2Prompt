"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Provide an example of how to validate form inputs (e.g., email confirmation, required fields) in a web-based event registration system using JavaScript.
Generated: DETERMINISTIC_9c9be41d8acbc8da
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Event Registration Form Validation Script

/**
 * Validates the form inputs and displays appropriate error messages.
 * @returns {boolean} Returns true if the form is valid, otherwise false.
 */
function validateForm() {
  // Get references to form fields
  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const confirmEmail = document.getElementById("confirmEmail");
  const eventDate = document.getElementById("eventDate");
  const errorContainer = document.getElementById("errorMessages");

  // Clear previous error messages
  errorContainer.innerHTML = "";

  // Initialize an array to collect error messages
  const errors = [];

  // Validate "Name" field (required)
  if (!name.value.trim()) {
    errors.push("Name is required.");
  }

  // Validate "Email" field (required and valid email format)
  if (!email.value.trim()) {
    errors.push("Email is required.");
  } else if (!isValidEmail(email.value.trim())) {
    errors.push("Invalid email format.");
  }

  // Validate "Confirm Email" field (must match "Email" field)
  if (!confirmEmail.value.trim()) {
    errors.push("Please confirm your email.");
  } else if (email.value.trim() !== confirmEmail.value.trim()) {
    errors.push("Email and Confirm Email do not match.");
  }

  // Validate "Event Date" field (required and must be a future date)
  if (!eventDate.value.trim()) {
    errors.push("Event date is required.");
  } else if (!isFutureDate(eventDate.value.trim())) {
    errors.push("Event date must be a future date.");
  }

  // If there are validation errors, display them and return false
  if (errors.length > 0) {
    displayErrors(errors, errorContainer);
    return false;
  }

  // Form is valid
  alert("Form submitted successfully!");
  return true;
}

/**
 * Checks if a given email address is valid.
 * @param {string} email The email address to validate.
 * @returns {boolean} True if the email is valid, otherwise false.
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Checks if a given date is in the future.
 * @param {string} dateString The date string to validate (format: YYYY-MM-DD).
 * @returns {boolean} True if the date is in the future, otherwise false.
 */
function isFutureDate(dateString) {
  const eventDate = new Date(dateString);
  const today = new Date();
  return eventDate > today;
}

/**
 * Displays error messages in the error container.
 * @param {string[]} errors Array of error messages.
 * @param {HTMLElement} container The container element to display errors.
 */
function displayErrors(errors, container) {
  const errorList = document.createElement("ul");
  errorList.style.color = "red";
  errors.forEach((error) => {
    const listItem = document.createElement("li");
    listItem.textContent = error;
    errorList.appendChild(listItem);
  });
  container.appendChild(errorList);
}

// Attach the validation function to the form submission event
document.getElementById("registrationForm").addEventListener("submit", function (event) {
  // Prevent the form from submitting if validation fails
  if (!validateForm()) {
    event.preventDefault();
  }
});
```

HTML Form Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event Registration</title>
  <script src="form-validation.js" defer></script>
</head>
<body>
  <h1>Event Registration</h1>
  <form id="registrationForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="confirmEmail">Confirm Email:</label>
    <input type="email" id="confirmEmail" name="confirmEmail" required><br><br>

    <label for="eventDate">Event Date:</label>
    <input type="date" id="eventDate" name="eventDate" required><br><br>

    <button type="submit">Register</button>
  </form>
  <div id="errorMessages"></div>
</body>
</html>
```
