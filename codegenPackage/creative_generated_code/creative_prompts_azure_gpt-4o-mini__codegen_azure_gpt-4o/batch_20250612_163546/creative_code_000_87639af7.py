"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Generate a code snippet for a web form that collects user information like name, email, and address, similar to the Proximus client form.
Generated: DETERMINISTIC_87639af7486a3e18
Batch ID: 20250612_163546
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
  <title>User Information Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .form-container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .form-container h1 {
      margin-bottom: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
    }
    .form-group input[type="submit"] {
      cursor: pointer;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 3px;
      font-size: 16px;
    }
    .form-group input[type="submit"]:hover {
      background-color: #0056b3;
    }
  </style>
  <script>
    /**
     * Handles form submission
     * Validates input fields and displays errors if necessary
     */
    function handleFormSubmit(event) {
      event.preventDefault(); // Prevent page refresh on form submit

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const address = document.getElementById('address').value.trim();
      const errorContainer = document.getElementById('error-container');

      errorContainer.innerHTML = ''; // Clear errors before validation

      // Simple validation
      if (!name || !email || !address) {
        errorContainer.innerHTML = '<p style="color: red;">All fields are required.</p>';
        return;
      }

      if (!validateEmail(email)) {
        errorContainer.innerHTML = '<p style="color: red;">Please enter a valid email address.</p>';
        return;
      }

      // If validation passes, submit the form (or handle data as needed)
      alert('Form submitted successfully!');
    }

    /**
     * Validates an email address using a regex pattern
     * @param {string} email
     * @returns {boolean}
     */
    function validateEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
    }
  </script>
</head>
<body>

  <div class="form-container">
    <h1>User Information Form</h1>
    <form id="userForm" onsubmit="handleFormSubmit(event)">
      <!-- Error container -->
      <div id="error-container"></div>

      <!-- Name field -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required>
      </div>

      <!-- Email field -->
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>

      <!-- Address field -->
      <div class="form-group">
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" placeholder="Enter your address" required>
      </div>

      <!-- Submit button -->
      <div class="form-group">
        <input type="submit" value="Submit">
      </div>
    </form>
  </div>

</body>
</html>
```
