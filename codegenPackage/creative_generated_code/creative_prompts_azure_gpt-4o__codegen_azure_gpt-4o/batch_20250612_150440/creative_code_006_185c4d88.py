"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksynccs.w3spaces.com
Prompt: Generate a contact form with HTML and CSS that can be hosted on W3 Spaces, including validation using JavaScript.
Generated: DETERMINISTIC_185c4d88ebc288d8
Batch ID: 20250612_150440
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
  <style>
    /* Basic styling for the contact form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .contact-form {
      background: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .contact-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      color: #333;
      text-align: center;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 16px;
    }

    .form-group textarea {
      resize: none;
    }

    .form-group .error {
      color: red;
      font-size: 14px;
      margin-top: 5px;
    }

    button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
      width: 100%;
    }

    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <form class="contact-form" id="contactForm">
    <h2>Contact Us</h2>
    <div class="form-group">
      <label for="name">Name</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" required>
      <div class="error" id="nameError"></div>
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      <div class="error" id="emailError"></div>
    </div>
    <div class="form-group">
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="5" placeholder="Enter your message" required></textarea>
      <div class="error" id="messageError"></div>
    </div>
    <button type="submit">Submit</button>
  </form>

  <script>
    // JavaScript for form validation
    document.getElementById('contactForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form from submitting

      let hasError = false;

      // Clear existing error messages
      document.getElementById('nameError').innerText = '';
      document.getElementById('emailError').innerText = '';
      document.getElementById('messageError').innerText = '';

      // Validate Name
      const name = document.getElementById('name').value.trim();
      if (name === '') {
        document.getElementById('nameError').innerText = 'Name is required.';
        hasError = true;
      }

      // Validate Email
      const email = document.getElementById('email').value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (email === '') {
        document.getElementById('emailError').innerText = 'Email is required.';
        hasError = true;
      } else if (!emailRegex.test(email)) {
        document.getElementById('emailError').innerText = 'Enter a valid email address.';
        hasError = true;
      }

      // Validate Message
      const message = document.getElementById('message').value.trim();
      if (message === '') {
        document.getElementById('messageError').innerText = 'Message is required.';
        hasError = true;
      }

      // If no validation errors, submit the form (can be integrated with backend)
      if (!hasError) {
        alert('Form submitted successfully!');
        // Here you can add code to send the form data to a server
      }
    });
  </script>
</body>
</html>
```
