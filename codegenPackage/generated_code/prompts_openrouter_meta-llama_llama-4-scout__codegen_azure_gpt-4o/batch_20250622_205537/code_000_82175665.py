"""
Generated Code Metadata:
========================
Original URL: https://abubit.com
Prompt: Write a simple HTML and CSS page that displays a "Launching Soon" message with a subscription sign-up form.
Generated: DETERMINISTIC_821756656ebacd56
Batch ID: 20250622_205537
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
  <meta name="description" content="Launching Soon Page with Subscription Form">
  <title>Launching Soon</title>
  <style>
    /* General Reset */
    body, h1, p, form, input, button {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Body Styling */
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    /* Container Styling */
    .container {
      text-align: center;
      background: #fff;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 400px;
      width: 100%;
    }

    /* Heading Styling */
    h1 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }

    /* Paragraph Styling */
    p {
      font-size: 1rem;
      margin-bottom: 1.5rem;
      color: #666;
    }

    /* Form Styling */
    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    /* Input Styling */
    input[type="email"] {
      padding: 0.75rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 100%;
    }

    /* Button Styling */
    button {
      padding: 0.75rem;
      font-size: 1rem;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #0056b3;
    }

    /* Error Message Styling */
    .error {
      color: #d9534f;
      font-size: 0.875rem;
    }

    /* Success Message Styling */
    .success {
      color: #5cb85c;
      font-size: 0.875rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Launching Soon</h1>
    <p>Sign up to be notified when we go live!</p>
    <form id="subscription-form">
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      <button type="submit">Subscribe</button>
      <p id="message" class="error" style="display: none;"></p>
    </form>
  </div>

  <script>
    // Select form and message elements
    const form = document.getElementById('subscription-form');
    const emailInput = document.getElementById('email');
    const message = document.getElementById('message');

    // Handle form submission
    form.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent default form submission

      // Validate email input
      const email = emailInput.value.trim();
      if (!validateEmail(email)) {
        message.textContent = 'Please enter a valid email address.';
        message.className = 'error';
        message.style.display = 'block';
        return;
      }

      // Simulate successful subscription
      message.textContent = 'Thank you for subscribing!';
      message.className = 'success';
      message.style.display = 'block';

      // Clear the input field
      emailInput.value = '';
    });

    // Email validation function
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  </script>
</body>
</html>
```
