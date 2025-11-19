"""
Generated Code Metadata:
========================
Original URL: https://doctorvitaly.pro
Prompt: How can I create a simple email subscription form using HTML, CSS, and JavaScript that validates user input for a diet and wellness website like Doctor Vitaly?
Generated: DETERMINISTIC_356b1ff0519ecdc3
Batch ID: 20250622_211550
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
  <title>Email Subscription Form</title>
  <style>
    /* Basic styling for the subscription form */
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .subscription-form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    .subscription-form h2 {
      margin-bottom: 15px;
      color: #333;
    }

    .subscription-form label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .subscription-form input[type="email"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }

    .subscription-form button {
      width: 100%;
      padding: 10px;
      background-color: #28a745;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .subscription-form button:hover {
      background-color: #218838;
    }

    .error-message {
      color: #d9534f;
      font-size: 14px;
      margin-bottom: 10px;
    }

    .success-message {
      color: #28a745;
      font-size: 14px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="subscription-form">
    <h2>Subscribe to Our Newsletter</h2>
    <p>Stay updated with the latest diet and wellness tips!</p>
    <form id="emailForm">
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      <div id="message" class="error-message" style="display: none;"></div>
      <button type="submit">Subscribe</button>
    </form>
  </div>

  <script>
    // JavaScript for form validation and handling
    document.getElementById('emailForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      const emailInput = document.getElementById('email');
      const messageDiv = document.getElementById('message');
      const email = emailInput.value.trim();

      // Regular expression for basic email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!email) {
        // Display error if email field is empty
        messageDiv.style.display = 'block';
        messageDiv.textContent = 'Email address is required.';
        messageDiv.className = 'error-message';
        return;
      }

      if (!emailRegex.test(email)) {
        // Display error if email format is invalid
        messageDiv.style.display = 'block';
        messageDiv.textContent = 'Please enter a valid email address.';
        messageDiv.className = 'error-message';
        return;
      }

      // If validation passes, display success message
      messageDiv.style.display = 'block';
      messageDiv.textContent = 'Thank you for subscribing!';
      messageDiv.className = 'success-message';

      // Clear the input field
      emailInput.value = '';
    });
  </script>
</body>
</html>
```
