"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Design a simple HTML form for user registration that captures username and password, inspired by the login features of the Mambo Wood website.
Generated: DETERMINISTIC_f2115f6e914084c0
Batch ID: 20250612_162051
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
  <title>User Registration</title>
  <style>
    /* Basic styling for the form container */
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

    .form-container {
      background-color: #fff;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      width: 100%;
      max-width: 400px;
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
      color: #555;
    }

    input[type="text"],
    input[type="password"] {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }

    button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      border: none;
      border-radius: 4px;
      color: #fff;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }

    .error-message {
      color: #ff0000;
      font-size: 14px;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>User Registration</h2>
    <form id="registrationForm">
      <!-- Username input field -->
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required placeholder="Enter your username">
        <div class="error-message" id="usernameError"></div>
      </div>

      <!-- Password input field -->
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required placeholder="Enter your password">
        <div class="error-message" id="passwordError"></div>
      </div>

      <!-- Submit button -->
      <button type="submit">Register</button>
    </form>
  </div>

  <script>
    // JavaScript to handle form validation and submission
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      // Clear previous error messages
      document.getElementById('usernameError').textContent = '';
      document.getElementById('passwordError').textContent = '';

      // Get form values
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();

      let valid = true;

      // Validate username
      if (!username) {
        document.getElementById('usernameError').textContent = 'Username is required.';
        valid = false;
      } else if (username.length < 4) {
        document.getElementById('usernameError').textContent = 'Username must be at least 4 characters.';
        valid = false;
      }

      // Validate password
      if (!password) {
        document.getElementById('passwordError').textContent = 'Password is required.';
        valid = false;
      } else if (password.length < 6) {
        document.getElementById('passwordError').textContent = 'Password must be at least 6 characters.';
        valid = false;
      }

      if (valid) {
        // If all validations pass, simulate form submission
        alert('Registration successful!'); // Replace with actual form submission logic
        document.getElementById('registrationForm').reset(); // Reset the form
      }
    });
  </script>
</body>
</html>
```
