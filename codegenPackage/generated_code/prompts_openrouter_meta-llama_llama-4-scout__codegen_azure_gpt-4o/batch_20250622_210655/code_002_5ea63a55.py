"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Generate code for a simple blog contact form using HTML, CSS, and JavaScript, inspired by the design on Rupak Parajuli's website.
Generated: DETERMINISTIC_5ea63a5516346b39
Batch ID: 20250622_210655
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
    /* General styles for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container for the contact form */
    .contact-form {
      background: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    /* Form heading */
    .contact-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      color: #333;
      text-align: center;
    }

    /* Input fields and textarea */
    .contact-form input,
    .contact-form textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    /* Submit button */
    .contact-form button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .contact-form button:hover {
      background-color: #0056b3;
    }

    /* Error message styling */
    .error-message {
      color: #ff0000;
      font-size: 14px;
      margin-bottom: 10px;
    }

    /* Success message styling */
    .success-message {
      color: #28a745;
      font-size: 14px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="contact-form">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <!-- Name input -->
      <input type="text" id="name" name="name" placeholder="Your Name" required>
      <!-- Email input -->
      <input type="email" id="email" name="email" placeholder="Your Email" required>
      <!-- Message textarea -->
      <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>
      <!-- Error message container -->
      <div id="errorMessage" class="error-message"></div>
      <!-- Success message container -->
      <div id="successMessage" class="success-message"></div>
      <!-- Submit button -->
      <button type="submit">Send Message</button>
    </form>
  </div>

  <script>
    // JavaScript for handling form submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Clear previous messages
      const errorMessage = document.getElementById('errorMessage');
      const successMessage = document.getElementById('successMessage');
      errorMessage.textContent = '';
      successMessage.textContent = '';

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      // Validate form inputs
      if (!name || !email || !message) {
        errorMessage.textContent = 'All fields are required.';
        return;
      }

      if (!validateEmail(email)) {
        errorMessage.textContent = 'Please enter a valid email address.';
        return;
      }

      // Simulate form submission (replace with actual backend logic)
      setTimeout(() => {
        successMessage.textContent = 'Your message has been sent successfully!';
        document.getElementById('contactForm').reset(); // Reset the form
      }, 500);
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
