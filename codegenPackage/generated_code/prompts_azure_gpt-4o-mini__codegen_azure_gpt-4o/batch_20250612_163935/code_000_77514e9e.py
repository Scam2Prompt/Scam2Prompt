"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: Generate a code snippet to create a contact form for a real estate website, including fields for name, email, and phone number, similar to the one found on 2ms.pt.
Generated: DETERMINISTIC_77514e9efda0cd88
Batch ID: 20250612_163935
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
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .contact-form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .contact-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      color: #333;
    }

    .contact-form label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
      color: #555;
    }

    .contact-form input {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    .contact-form button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .contact-form button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 14px;
      margin-bottom: 10px;
    }

    .success-message {
      color: green;
      font-size: 14px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <form class="contact-form" id="contactForm">
    <h2>Contact Us</h2>
    <div id="formMessages"></div>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your Name" required>
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your Email" required>
    <label for="phone">Phone Number</label>
    <input type="tel" id="phone" name="phone" placeholder="Your Phone Number" required>
    <button type="submit">Submit</button>
  </form>

  <script>
    // JavaScript to handle form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const formMessages = document.getElementById('formMessages');

      // Clear previous messages
      formMessages.innerHTML = '';

      // Basic validation
      if (!name || !email || !phone) {
        formMessages.innerHTML = '<p class="error-message">All fields are required.</p>';
        return;
      }

      if (!validateEmail(email)) {
        formMessages.innerHTML = '<p class="error-message">Please enter a valid email address.</p>';
        return;
      }

      // Simulate form submission (replace with actual API call in production)
      formMessages.innerHTML = '<p class="success-message">Thank you for contacting us! We will get back to you shortly.</p>';
      document.getElementById('contactForm').reset();
    });

    // Function to validate email format
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  </script>
</body>
</html>
```
