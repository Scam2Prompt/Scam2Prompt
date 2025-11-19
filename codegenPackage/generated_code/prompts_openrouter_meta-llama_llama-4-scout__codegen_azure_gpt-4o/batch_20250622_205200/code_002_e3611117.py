"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Generate a code snippet in JavaScript to create a simple form validation for a power washing service company's contact page, similar to the one on Klean-Pro Utah's website.
Generated: DETERMINISTIC_e3611117724dbcda
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Form validation script for a power washing service company's contact page

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  // Select the form element
  const contactForm = document.getElementById("contactForm");

  // Attach a submit event listener to the form
  contactForm.addEventListener("submit", (event) => {
    // Prevent the form from submitting by default
    event.preventDefault();

    // Collect form input values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const message = document.getElementById("message").value.trim();

    // Initialize an empty array to store error messages
    const errors = [];

    // Validate name (required, minimum 2 characters)
    if (name.length < 2) {
      errors.push("Name must be at least 2 characters long.");
    }

    // Validate email (required, must be a valid email format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      errors.push("Please enter a valid email address.");
    }

    // Validate phone (optional, must be a valid phone number format if provided)
    const phoneRegex = /^\+?[0-9\s\-()]{7,15}$/;
    if (phone && !phoneRegex.test(phone)) {
      errors.push("Please enter a valid phone number.");
    }

    // Validate message (required, minimum 10 characters)
    if (message.length < 10) {
      errors.push("Message must be at least 10 characters long.");
    }

    // Check if there are any validation errors
    if (errors.length > 0) {
      // Display errors to the user
      const errorContainer = document.getElementById("errorContainer");
      errorContainer.innerHTML = errors.map((error) => `<p>${error}</p>`).join("");
      errorContainer.style.display = "block";
    } else {
      // If no errors, submit the form (or handle the submission logic)
      alert("Form submitted successfully!");
      contactForm.reset(); // Clear the form fields
    }
  });
});
```

```html
<!-- Example HTML structure for the contact form -->
<form id="contactForm">
  <div id="errorContainer" style="display: none; color: red;"></div>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />
  <br />
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />
  <br />
  <label for="phone">Phone (optional):</label>
  <input type="text" id="phone" name="phone" />
  <br />
  <label for="message">Message:</label>
  <textarea id="message" name="message" required></textarea>
  <br />
  <button type="submit">Submit</button>
</form>
```
