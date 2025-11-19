"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rahelesadeghi.ir
Prompt: Generate a JavaScript code snippet that creates a contact form for a family counseling center, similar to the one used by Dr. Raheleh Sadeghi's practice.
Generated: DETERMINISTIC_4c83b1895c5dfb37
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to create a contact form for a family counseling center

// Wait for the DOM content to load before executing the script
document.addEventListener("DOMContentLoaded", () => {
  // Create the form element
  const form = document.createElement("form");

  // Set form attributes
  form.setAttribute("id", "contactForm");
  form.setAttribute("action", "#"); // Placeholder for server-side endpoint
  form.setAttribute("method", "POST");
  form.setAttribute("novalidate", true); // Disable HTML5 validation for custom validation

  // Add a heading to the form
  const heading = document.createElement("h2");
  heading.textContent = "Contact Us";
  form.appendChild(heading);

  // Create Name input field
  const nameField = createInputField("text", "fullName", "Full Name", true);
  form.appendChild(nameField);

  // Create Email input field
  const emailField = createInputField("email", "emailAddress", "Email Address", true);
  form.appendChild(emailField);

  // Create Phone input field
  const phoneField = createInputField("tel", "phoneNumber", "Phone Number", false);
  form.appendChild(phoneField);

  // Create Message textarea
  const messageField = document.createElement("div");
  const messageLabel = document.createElement("label");
  messageLabel.setAttribute("for", "message");
  messageLabel.textContent = "Your Message";
  messageField.appendChild(messageLabel);

  const messageInput = document.createElement("textarea");
  messageInput.setAttribute("id", "message");
  messageInput.setAttribute("name", "message");
  messageInput.setAttribute("rows", "5");
  messageInput.setAttribute("required", true);
  messageField.appendChild(messageInput);

  form.appendChild(messageField);

  // Create Submit button
  const submitButton = document.createElement("button");
  submitButton.setAttribute("type", "submit");
  submitButton.textContent = "Send";
  form.appendChild(submitButton);

  // Append the form to the document body
  document.body.appendChild(form);

  // Add form submission event handling
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent the default form submission

    // Validate the form fields
    const errors = validateForm(form);

    if (errors.length > 0) {
      alert("Please correct the following errors:\n" + errors.join("\n"));
    } else {
      alert("Form submitted successfully!");
      // Logic to send form data to the server (e.g., using fetch or XMLHttpRequest) goes here
    }
  });
});

/**
 * Helper function to create an input field with associated label
 * @param {string} type - The type of the input field (e.g., "text", "email")
 * @param {string} name - The name attribute for the input field
 * @param {string} labelText - The text for the label
 * @param {boolean} required - Whether the input field is required
 * @returns {HTMLElement} - A div element containing the label and input field
 */
function createInputField(type, name, labelText, required) {
  const field = document.createElement("div");

  const label = document.createElement("label");
  label.setAttribute("for", name);
  label.textContent = labelText;
  field.appendChild(label);

  const input = document.createElement("input");
  input.setAttribute("type", type);
  input.setAttribute("id", name);
  input.setAttribute("name", name);
  if (required) input.setAttribute("required", true);
  field.appendChild(input);

  return field;
}

/**
 * Validate the form fields
 * @param {HTMLFormElement} form - The form to validate
 * @returns {string[]} - An array of error messages
 */
function validateForm(form) {
  const errors = [];

  // Validate Name
  const name = form.querySelector("#fullName").value.trim();
  if (name === "") {
    errors.push("Full Name is required.");
  }

  // Validate Email
  const email = form.querySelector("#emailAddress").value.trim();
  if (email === "") {
    errors.push("Email Address is required.");
  } else if (!isValidEmail(email)) {
    errors.push("Invalid Email Address format.");
  }

  // Validate Phone (optional, but if provided must be valid)
  const phone = form.querySelector("#phoneNumber").value.trim();
  if (phone !== "" && !isValidPhone(phone)) {
    errors.push("Invalid Phone Number format.");
  }

  // Validate Message
  const message = form.querySelector("#message").value.trim();
  if (message === "") {
    errors.push("Message is required.");
  }

  return errors;
}

/**
 * Check if an email address is valid
 * @param {string} email - The email address to validate
 * @returns {boolean} - Whether the email address is valid
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Check if a phone number is valid
 * @param {string} phone - The phone number to validate
 * @returns {boolean} - Whether the phone number is valid
 */
function isValidPhone(phone) {
  const phoneRegex = /^[0-9+\-()\s]{10,15}$/; // Basic validation for phone numbers
  return phoneRegex.test(phone);
}
```
