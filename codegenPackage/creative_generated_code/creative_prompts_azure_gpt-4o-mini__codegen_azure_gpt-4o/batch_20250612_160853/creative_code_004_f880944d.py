"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosario.gob.mx
Prompt: Design a form in HTML that allows users to contact the Rosario municipal government, including fields for name, email, and message.
Generated: DETERMINISTIC_f880944d3bed6ea4
Batch ID: 20250612_160853
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
  <title>Contact Rosario Municipal Government</title>

  <!-- Add basic styling -->
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f4;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      font-size: 24px;
      margin-bottom: 20px;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    input,
    textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    button {
      background-color: #007BFF;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .error-message {
      color: red;
      font-size: 14px;
    }
  </style>
</head>

<body>
  <div class="form-container">
    <h1>Contact Rosario Municipal Government</h1>

    <!-- Contact Form -->
    <form id="contact-form" action="/submit-form" method="POST">
      <!-- Name Field -->
      <label for="name">Name</label>
      <input type="text" id="name" name="name" required minlength="2" maxlength="100"
        placeholder="Enter your full name">

      <!-- Email Field -->
      <label for="email">Email</label>
      <input type="email" id="email" name="email" required placeholder="Enter your email address">

      <!-- Message Field -->
      <label for="message">Message</label>
      <textarea id="message" name="message" required minlength="10" maxlength="500"
        placeholder="Write your message here"></textarea>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
    </form>
  </div>

  <!-- JavaScript for basic client-side form validation -->
  <script>
    document.getElementById('contact-form').addEventListener('submit', function (event) {
      // Basic error handling
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      let errors = [];

      // Validate name
      if (name.length < 2 || name.length > 100) {
        errors.push("Name must be between 2 and 100 characters.");
      }

      // Validate email format
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        errors.push("Email must be a valid address.");
      }

      // Validate message length
      if (message.length < 10 || message.length > 500) {
        errors.push("Message must be between 10 and 500 characters.");
      }

      // Display errors or allow submission
      if (errors.length > 0) {
        event.preventDefault();
        alert("Please fix the following errors:\n" + errors.join("\n"));
      }
    });
  </script>
</body>

</html>
```
