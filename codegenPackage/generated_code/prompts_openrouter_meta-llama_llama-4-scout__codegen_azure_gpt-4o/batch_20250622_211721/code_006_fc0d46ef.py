"""
Generated Code Metadata:
========================
Original URL: https://sergiupopa.com
Prompt: Generate a code snippet for a contact form, similar to the one on sergiupopa.com, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_fc0d46ef4c50644e
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Form</title>
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .contact-form {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .contact-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      color: #333;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
      color: #555;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    .form-group textarea {
      resize: vertical;
      min-height: 100px;
    }

    .form-group input:focus,
    .form-group textarea:focus {
      border-color: #007BFF;
      outline: none;
    }

    .form-group .error {
      color: #d9534f;
      font-size: 14px;
      margin-top: 5px;
    }

    .submit-btn {
      display: inline-block;
      background-color: #007BFF;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .submit-btn:hover {
      background-color: #0056b3;
    }

    .success-message {
      color: #28a745;
      font-size: 16px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="contact-form">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required>
        <div class="error" id="nameError"></div>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
        <div class="error" id="emailError"></div>
      </div>
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" required></textarea>
        <div class="error" id="messageError"></div>
      </div>
      <button type="submit" class="submit-btn">Send Message</button>
      <div class="success-message" id="successMessage"></div>
    </form>
  </div>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form from submitting normally

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('messageError').textContent = '';
      document.getElementById('successMessage').textContent = '';

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      let hasError = false;

      // Validate name
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        hasError = true;
      }

      // Validate email
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        hasError = true;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        hasError = true;
      }

      // Validate message
      if (message === '') {
        document.getElementById('messageError').textContent = 'Message is required.';
        hasError = true;
      }

      // If no errors, simulate form submission
      if (!hasError) {
        // Simulate successful submission
        document.getElementById('successMessage').textContent = 'Thank you for your message! We will get back to you soon.';
        // Optionally, clear the form fields
        document.getElementById('contactForm').reset();
      }
    });
  </script>
</body>
</html>
```
