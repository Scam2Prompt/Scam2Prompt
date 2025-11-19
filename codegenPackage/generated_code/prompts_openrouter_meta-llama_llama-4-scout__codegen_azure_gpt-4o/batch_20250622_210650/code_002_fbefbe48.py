"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Generate a sample code snippet in JavaScript for a basic contact form validation, similar to the one on the textcounsellingonline.com.au website, ensuring that fields such as name, email, and message are properly validated before submission.
Generated: DETERMINISTIC_fbefbe48ef075cf5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Contact Form Validation Script

// Function to validate the contact form
function validateContactForm() {
  // Get form field values
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  // Initialize an empty errors array
  const errors = [];

  // Validate name field
  if (name === "") {
    errors.push("Name is required.");
  } else if (name.length < 2) {
    errors.push("Name must be at least 2 characters long.");
  }

  // Validate email field
  if (email === "") {
    errors.push("Email is required.");
  } else if (!isValidEmail(email)) {
    errors.push("Please enter a valid email address.");
  }

  // Validate message field
  if (message === "") {
    errors.push("Message is required.");
  } else if (message.length < 10) {
    errors.push("Message must be at least 10 characters long.");
  }

  // Display errors or submit the form
  if (errors.length > 0) {
    displayErrors(errors);
    return false; // Prevent form submission
  }

  // If no errors, form is valid
  alert("Form submitted successfully!");
  return true; // Allow form submission
}

// Helper function to validate email format
function isValidEmail(email) {
  // Regular expression for basic email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Helper function to display errors
function displayErrors(errors) {
  const errorContainer = document.getElementById("error-messages");
  errorContainer.innerHTML = ""; // Clear previous errors

  errors.forEach((error) => {
    const errorElement = document.createElement("p");
    errorElement.textContent = error;
    errorElement.style.color = "red";
    errorContainer.appendChild(errorElement);
  });
}

// Attach validation function to form submission
document.getElementById("contact-form").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission
  validateContactForm(); // Call validation function
});
```

```html
<!-- Sample HTML for the Contact Form -->
<form id="contact-form">
  <div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" />
  </div>
  <div>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" />
  </div>
  <div>
    <label for="message">Message:</label>
    <textarea id="message" name="message"></textarea>
  </div>
  <div id="error-messages"></div>
  <button type="submit">Submit</button>
</form>
```
