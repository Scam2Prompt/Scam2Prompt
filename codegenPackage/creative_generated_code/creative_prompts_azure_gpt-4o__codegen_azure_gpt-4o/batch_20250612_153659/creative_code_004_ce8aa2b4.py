"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Provide JavaScript code to handle form submission and display a confirmation message when the user submits their name, email, and message, based on the contact form at https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_ce8aa2b4a15a3f0e
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to handle form submission and display confirmation message

document.addEventListener("DOMContentLoaded", () => {
  // Select the form element and confirmation message container
  const contactForm = document.getElementById("contact-form");
  const confirmationContainer = document.getElementById("confirmation-message");

  // Add an event listener for form submission
  contactForm.addEventListener("submit", (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Collect form data
    const name = contactForm.querySelector('input[name="name"]').value.trim();
    const email = contactForm.querySelector('input[name="email"]').value.trim();
    const message = contactForm.querySelector('textarea[name="message"]').value.trim();

    // Input validation
    if (!name || !email || !message) {
      alert("Please fill out all fields before submitting.");
      return;
    }

    if (!validateEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }

    // Simulate form submission (e.g., send data to a server via AJAX)
    // This example demonstrates a successful submission with a confirmation message
    setTimeout(() => {
      displayConfirmationMessage(name);
      contactForm.reset(); // Reset the form fields
    }, 500); // Simulate network delay
  });

  /**
   * Validate email format using a regular expression.
   * @param {string} email - The email address to validate.
   * @returns {boolean} - Returns true if the email is valid, otherwise false.
   */
  function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  /**
   * Display a confirmation message after successful form submission.
   * @param {string} name - The name of the user, used in the confirmation message.
   */
  function displayConfirmationMessage(name) {
    confirmationContainer.innerHTML = `
      <p>Thank you, <strong>${name}</strong>, for your message! We'll get back to you soon.</p>
    `;
    confirmationContainer.style.display = "block";
  }
});
```

**HTML Structure for Reference** (you must ensure the form and confirmation container exists in your HTML):
```html
<form id="contact-form">
  <input type="text" name="name" placeholder="Your Name" required />
  <input type="email" name="email" placeholder="Your Email" required />
  <textarea name="message" placeholder="Your Message" required></textarea>
  <button type="submit">Send Message</button>
</form>

<div id="confirmation-message" style="display: none;"></div>
```
