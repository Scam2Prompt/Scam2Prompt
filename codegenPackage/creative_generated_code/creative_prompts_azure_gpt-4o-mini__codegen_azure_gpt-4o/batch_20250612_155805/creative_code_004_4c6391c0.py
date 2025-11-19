"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.net
Prompt: Write a sample HTML form for potential investors to express their interest in Authentic Oil, including fields for name, email, and investment amount.
Generated: DETERMINISTIC_4c6391c07eadf001
Batch ID: 20250612_155805
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
  <title>Investment Interest Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
    }

    .form-container {
      max-width: 500px;
      margin: 50px auto;
      padding: 20px;
      background-color: #ffffff;
      border: 1px solid #dddddd;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input[type="text"],
    input[type="email"],
    input[type="number"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #cccccc;
      border-radius: 4px;
      font-size: 16px;
    }

    input[type="submit"] {
      width: 100%;
      padding: 10px;
      background-color: #28a745;
      border: none;
      border-radius: 4px;
      color: #ffffff;
      font-size: 16px;
      cursor: pointer;
    }

    input[type="submit"]:hover {
      background-color: #218838;
    }

    .error {
      color: #dc3545;
      font-size: 14px;
      margin-top: -10px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Investment Interest Form</h1>
    <!-- Investment form for Authentic Oil -->
    <form id="investmentForm" action="/submit-form" method="POST">
      <!-- Input field for investor's name -->
      <label for="name">Name</label>
      <input type="text" id="name" name="name" placeholder="Your full name" required>
      <span class="error" id="nameError"></span>

      <!-- Input field for investor's email -->
      <label for="email">Email</label>
      <input type="email" id="email" name="email" placeholder="Your email address" required>
      <span class="error" id="emailError"></span>

      <!-- Input field for investment amount -->
      <label for="investment">Investment Amount ($)</label>
      <input type="number" id="investment" name="investment" placeholder="Enter amount in USD" min="1" required>
      <span class="error" id="investmentError"></span>

      <!-- Submit button -->
      <input type="submit" value="Submit">
    </form>
  </div>

  <!-- JavaScript for form validation -->
  <script>
    document.getElementById('investmentForm').addEventListener('submit', function(event) {
      // Clear previous error messages
      document.getElementById('nameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('investmentError').textContent = '';

      // Form validation
      let valid = true;

      // Validate name
      const name = document.getElementById('name').value.trim();
      if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        valid = false;
      }

      // Validate email
      const email = document.getElementById('email').value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (email === '' || !emailRegex.test(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        valid = false;
      }

      // Validate investment amount
      const investment = document.getElementById('investment').value.trim();
      if (investment === '' || isNaN(investment) || Number(investment) <= 0) {
        document.getElementById('investmentError').textContent = 'Please enter a valid investment amount.';
        valid = false;
      }

      // Prevent form submission if validation fails
      if (!valid) {
        event.preventDefault();
      }
    });
  </script>
</body>
</html>
```
