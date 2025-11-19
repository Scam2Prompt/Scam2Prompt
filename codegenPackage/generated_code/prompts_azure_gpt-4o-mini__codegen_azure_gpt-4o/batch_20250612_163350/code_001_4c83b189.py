"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Generate a JavaScript code snippet that creates a contact form for a family counseling center, similar to the one used by Dr. Raheleh Sadeghi's practice.
Generated: DETERMINISTIC_4c83b1895c5dfb37
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Contact Form for a Family Counseling Center
// This code creates a simple contact form using HTML, CSS, and JavaScript.
// It includes validation and error handling for user inputs.

// HTML structure for the contact form
const formHTML = `
  <style>
    /* Basic styling for the contact form */
    .contact-form {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    .contact-form h2 {
      text-align: center;
      margin-bottom: 20px;
    }
    .contact-form label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .contact-form input, .contact-form textarea, .contact-form button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .contact-form button {
      background-color: #007BFF;
      color: white;
      border: none;
      cursor: pointer;
    }
    .contact-form button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
    .success {
      color: green;
      font-size: 1em;
      text-align: center;
    }
  </style>
  <div class="contact-form">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <label for="name">Full Name</label>
      <input type="text" id="name" name="name" placeholder="Your full name" required />
      <span class="error" id="nameError"></span>

      <label for="email">Email Address</label>
      <input type="email" id="email" name="email" placeholder="Your email address" required />
      <span class="error" id="emailError"></span>

      <label for="message">Message</label>
      <textarea id="message" name="message" placeholder="Your message" rows="5" required></textarea>
      <span class="error" id="messageError"></span>

      <button type="submit">Submit</button>
      <div class="success" id="successMessage"></div>
    </form>
  </div>
`;

// Append the form to the body
document.body.innerHTML = formHTML;

// JavaScript for form validation and submission
document.getElementById('contactForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  // Clear previous error messages
  document.getElementById('nameError').textContent = '';
  document.getElementById('emailError').textContent = '';
  document.getElementById('messageError').textContent = '';
  document.getElementById('successMessage').textContent = '';

  // Get form values
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  let isValid = true;

  // Validate name
  if (name === '') {
    document.getElementById('nameError').textContent = 'Name is required.';
    isValid = false;
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === '') {
    document.getElementById('emailError').textContent = 'Email is required.';
    isValid = false;
  } else if (!emailRegex.test(email)) {
    document.getElementById('emailError').textContent = 'Please enter a valid email address.';
    isValid = false;
  }

  // Validate message
  if (message === '') {
    document.getElementById('messageError').textContent = 'Message is required.';
    isValid = false;
  }

  // If all inputs are valid, simulate form submission
  if (isValid) {
    // Simulate a successful submission
    document.getElementById('successMessage').textContent = 'Thank you for contacting us! We will get back to you shortly.';
    // Clear the form
    document.getElementById('contactForm').reset();
  }
});
```
