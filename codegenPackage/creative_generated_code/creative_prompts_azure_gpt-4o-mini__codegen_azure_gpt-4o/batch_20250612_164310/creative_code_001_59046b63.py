"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gpt-chat.info
Prompt: Write a code snippet for a contact form that handles errors, inspired by the "Lỗi: Không tìm thấy biểu mẫu liên hệ" message on the GPT-Chat page.
Generated: DETERMINISTIC_59046b636abc2043
Batch ID: 20250612_164310
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
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    .form-container {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input, .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .error-message {
      color: red;
      font-size: 0.9em;
      margin-top: 5px;
    }

    .success-message {
      color: green;
      font-size: 1em;
      text-align: center;
      margin-top: 10px;
    }

    button {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <div class="error-message" id="nameError"></div>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <div class="error-message" id="emailError"></div>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <div class="error-message" id="messageError"></div>
      </div>
      <button type="submit">Submit</button>
      <div class="success-message" id="successMessage"></div>
    </form>
  </div>

  <script>
    // Error messages display logic
    const contactForm = document.getElementById('contactForm');
    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const messageError = document.getElementById('messageError');
    const successMessage = document.getElementById('successMessage');

    contactForm.addEventListener('submit', function (e) {
      e.preventDefault(); // Prevent form submission

      // Clear previous error messages
      nameError.textContent = '';
      emailError.textContent = '';
      messageError.textContent = '';
      successMessage.textContent = '';

      // Input validation
      let hasError = false;

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      // Validate name
      if (name === '') {
        nameError.textContent = 'Name is required.';
        hasError = true;
      }

      // Validate email
      if (email === '') {
        emailError.textContent = 'Email is required.';
        hasError = true;
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        emailError.textContent = 'Invalid email format.';
        hasError = true;
      }

      // Validate message
      if (message === '') {
        messageError.textContent = 'Message is required.';
        hasError = true;
      }

      // Display success message if no errors
      if (!hasError) {
        successMessage.textContent = 'Thank you for your message!';
        // Optionally, send the data to a server here (e.g., using fetch or XMLHttpRequest)
      }
    });
  </script>
</body>
</html>
```
