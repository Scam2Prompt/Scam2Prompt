"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Generate code to create a contact form for a personal blog using HTML, CSS, and JavaScript, ensuring it includes fields for name, email, and message.
Generated: DETERMINISTIC_86e83f9cd0285bf2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Form</title>
  <!-- External CSS -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f4;
    }

    .contact-form {
      max-width: 600px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }

    .contact-form h2 {
      margin-bottom: 20px;
      text-align: center;
      color: #333;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
      color: #333;
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
      height: 120px;
    }

    .form-group .error {
      color: red;
      font-size: 14px;
      margin-top: 5px;
    }

    .form-group input:focus,
    .form-group textarea:focus {
      border-color: #007bff;
      outline: none;
    }

    .submit-btn {
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      font-size: 18px;
      cursor: pointer;
    }

    .submit-btn:hover {
      background-color: #0056b3;
    }

    .success-message {
      color: green;
      font-size: 16px;
      margin-top: 15px;
      text-align: center;
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
        <span class="error" id="nameError"></span>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
        <span class="error" id="emailError"></span>
      </div>
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" required></textarea>
        <span class="error" id="messageError"></span>
      </div>
      <button type="submit" class="submit-btn">Submit</button>
      <div class="success-message" id="successMessage"></div>
    </form>
  </div>

  <!-- External JavaScript -->
  <script>
    // Wait for the DOM to load
    document.addEventListener('DOMContentLoaded', () => {
      const contactForm = document.getElementById('contactForm');

      // Attach submit event listener to the form
      contactForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form submission to server

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
        if (!name) {
          document.getElementById('nameError').textContent = 'Name is required.';
          isValid = false;
        }

        // Validate email
        if (!email) {
          document.getElementById('emailError').textContent = 'Email is required.';
          isValid = false;
        } else if (!/\S+@\S+\.\S+/.test(email)) {
          document.getElementById('emailError').textContent = 'Invalid email format.';
          isValid = false;
        }

        // Validate message
        if (!message) {
          document.getElementById('messageError').textContent = 'Message is required.';
          isValid = false;
        }

        // If all fields are valid, simulate successful submission
        if (isValid) {
          document.getElementById('successMessage').textContent = 'Your message has been sent successfully!';
          contactForm.reset(); // Clear the form fields
        }
      });
    });
  </script>
</body>
</html>
```
