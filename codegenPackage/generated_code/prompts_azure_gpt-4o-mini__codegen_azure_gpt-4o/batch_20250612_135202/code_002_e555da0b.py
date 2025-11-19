"""
Generated Code Metadata:
========================
Original URL: https://foxyline.com
Prompt: Can you provide a code snippet for a simple contact form that includes fields for name, email, phone, and message?
Generated: DETERMINISTIC_e555da0b4974fce5
Batch ID: 20250612_135202
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
    /* Basic styling for the form */
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
    form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }
    button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 12px;
      margin-top: -10px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <form id="contactForm">
    <!-- Name field -->
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your full name" required>
    <div class="error" id="nameError"></div>

    <!-- Email field -->
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email address" required>
    <div class="error" id="emailError"></div>

    <!-- Phone field -->
    <label for="phone">Phone</label>
    <input type="tel" id="phone" name="phone" placeholder="Your phone number" pattern="[0-9]{10}" required>
    <div class="error" id="phoneError"></div>

    <!-- Message field -->
    <label for="message">Message</label>
    <textarea id="message" name="message" placeholder="Your message" rows="5" required></textarea>
    <div class="error" id="messageError"></div>

    <!-- Submit button -->
    <button type="submit">Submit</button>
  </form>

  <script>
    // JavaScript for form validation and submission
    document.getElementById('contactForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('phoneError').textContent = '';
      document.getElementById('messageError').textContent = '';

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const message = document.getElementById('message').value.trim();

      let isValid = true;

      // Validate name
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
      }

      // Validate email
      if (email === '') {
        document.getElementById('emailError').textContent = 'Email is required.';
        isValid = false;
      } else if (!/^\S+@\S+\.\S+$/.test(email)) {
        document.getElementById('emailError').textContent = 'Invalid email format.';
        isValid = false;
      }

      // Validate phone
      if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
      } else if (!/^\d{10}$/.test(phone)) {
        document.getElementById('phoneError').textContent = 'Phone number must be 10 digits.';
        isValid = false;
      }

      // Validate message
      if (message === '') {
        document.getElementById('messageError').textContent = 'Message is required.';
        isValid = false;
      }

      // If all fields are valid, simulate form submission
      if (isValid) {
        alert('Form submitted successfully!');
        // Here you can add code to send the form data to a server using fetch or XMLHttpRequest
        document.getElementById('contactForm').reset(); // Reset the form
      }
    });
  </script>
</body>
</html>
```
