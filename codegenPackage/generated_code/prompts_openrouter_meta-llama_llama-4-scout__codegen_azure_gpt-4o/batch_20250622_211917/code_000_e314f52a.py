"""
Generated Code Metadata:
========================
Original URL: https://coinbased.beautyjibindia.com
Prompt: "Generate a login form using HTML and CSS that matches the Coin Base login page design."
Generated: DETERMINISTIC_e314f52a6ad05f96
Batch ID: 20250622_211917
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
  <title>Login Form</title>
  <style>
    /* General reset for consistent styling */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Body styling */
    body {
      font-family: Arial, sans-serif;
      background-color: #f7f9fb; /* Light background similar to Coin Base */
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container for the login form */
    .login-container {
      background-color: #ffffff; /* White background for the form */
      border: 1px solid #e0e0e0; /* Light border for subtle separation */
      border-radius: 8px; /* Rounded corners */
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
      width: 100%;
      max-width: 400px; /* Responsive width */
      padding: 20px;
    }

    /* Form title styling */
    .login-container h1 {
      font-size: 24px;
      font-weight: bold;
      color: #333333; /* Dark text color */
      text-align: center;
      margin-bottom: 20px;
    }

    /* Input field styling */
    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      font-size: 14px;
      color: #555555; /* Medium text color */
      margin-bottom: 5px;
    }

    .form-group input {
      width: 100%;
      padding: 10px;
      font-size: 14px;
      border: 1px solid #cccccc; /* Light border for input fields */
      border-radius: 4px; /* Rounded corners */
      outline: none;
      transition: border-color 0.3s ease;
    }

    .form-group input:focus {
      border-color: #0052ff; /* Blue border on focus */
    }

    /* Submit button styling */
    .form-group button {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      font-weight: bold;
      color: #ffffff; /* White text */
      background-color: #0052ff; /* Blue background */
      border: none;
      border-radius: 4px; /* Rounded corners */
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .form-group button:hover {
      background-color: #003bb3; /* Darker blue on hover */
    }

    /* Link styling */
    .login-container .form-footer {
      text-align: center;
      margin-top: 15px;
    }

    .login-container .form-footer a {
      font-size: 14px;
      color: #0052ff; /* Blue link color */
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .login-container .form-footer a:hover {
      color: #003bb3; /* Darker blue on hover */
    }
  </style>
</head>
<body>
  <div class="login-container">
    <!-- Login form title -->
    <h1>Sign In</h1>
    <form action="/login" method="POST">
      <!-- Email input field -->
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>
      <!-- Password input field -->
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required>
      </div>
      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Sign In</button>
      </div>
    </form>
    <!-- Footer links -->
    <div class="form-footer">
      <a href="/forgot-password">Forgot password?</a>
      <br>
      <a href="/signup">Create an account</a>
    </div>
  </div>
</body>
</html>
```
