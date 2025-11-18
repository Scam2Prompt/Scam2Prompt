"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Generate code using JavaScript to validate email input and ensure all required fields are completed before submitting the contact form on The Prepper Codex website.
Generated: DETERMINISTIC_14a96c4f6282d128
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to validate email input and ensure required fields are completed before submitting the contact form

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Select the form element
  const contactForm = document.getElementById("contactForm");
  
  // Error message container
  const errorContainer = document.getElementById("formErrors");

  // Utility function to validate an email address
  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  // Form submission handler
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent the form from submitting initially

    // Clear previous error messages
    errorContainer.innerHTML = "";

    // Get all input elements in the form
    const formInputs = contactForm.querySelectorAll("input, textarea");
    const errors = [];

    // Validate each input field
    formInputs.forEach((input) => {
      const isRequired = input.hasAttribute("required");
      const value = input.value.trim();

      // Check if required fields are completed
      if (isRequired && !value) {
        errors.push(`${input.name} is required.`);
      }

      // Special validation for email field
      if (input.type === "email" && value && !isValidEmail(value)) {
        errors.push("Please enter a valid email address.");
      }
    });

    // Display errors or submit the form if validation passes
    if (errors.length > 0) {
      // Display error messages
      errorContainer.innerHTML = errors.map((error) => `<p>${error}</p>`).join("");
      errorContainer.style.color = "red";
    } else {
      // Submit the form (replace with actual submission logic, e.g., AJAX call)
      console.log("Form submitted successfully!");
      contactForm.reset(); // Clear the form after successful submission
    }
  });
});
```

```html
<!-- Example HTML for the contact form -->
<form id="contactForm">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />

  <label for="message">Message:</label>
  <textarea id="message" name="message" required></textarea>

  <button type="submit">Submit</button>
</form>

<!-- Container for error messages -->
<div id="formErrors"></div>
```
