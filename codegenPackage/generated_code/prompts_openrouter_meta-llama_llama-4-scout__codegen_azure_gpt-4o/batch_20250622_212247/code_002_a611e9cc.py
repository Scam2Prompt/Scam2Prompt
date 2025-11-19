"""
Generated Code Metadata:
========================
Original URL: https://phantomlogin.vercel.app
Prompt: Generate a Phantom Wallet login page with a forgot email link using HTML and CSS.
Generated: DETERMINISTIC_a611e9cc53e8eeb9
Batch ID: 20250622_212247
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
  <title>Phantom Wallet Login</title>
  <style>
    /* General Reset */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container Styling */
    .login-container {
      background-color: #ffffff;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }

    /* Header Styling */
    .login-container h1 {
      font-size: 1.8rem;
      margin-bottom: 1rem;
      color: #333333;
      text-align: center;
    }

    /* Input Fields */
    .form-group {
      margin-bottom: 1rem;
    }

    .form-group label {
      display: block;
      font-size: 0.9rem;
      margin-bottom: 0.5rem;
      color: #555555;
    }

    .form-group input {
      width: 100%;
      padding: 0.8rem;
      font-size: 1rem;
      border: 1px solid #cccccc;
      border-radius: 4px;
      box-sizing: border-box;
    }

    .form-group input:focus {
      border-color: #007bff;
      outline: none;
    }

    /* Buttons */
    .btn {
      display: block;
      width: 100%;
      padding: 0.8rem;
      font-size: 1rem;
      color: #ffffff;
      background-color: #007bff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      text-align: center;
    }

    .btn:hover {
      background-color: #0056b3;
    }

    /* Forgot Email Link */
    .forgot-email {
      margin-top: 1rem;
      text-align: center;
    }

    .forgot-email a {
      font-size: 0.9rem;
      color: #007bff;
      text-decoration: none;
    }

    .forgot-email a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="login-container">
    <!-- Login Header -->
    <h1>Phantom Wallet Login</h1>

    <!-- Login Form -->
    <form action="#" method="POST">
      <!-- Email Input -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>

      <!-- Password Input -->
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn">Login</button>
    </form>

    <!-- Forgot Email Link -->
    <div class="forgot-email">
      <a href="#">Forgot your email?</a>
    </div>
  </div>
</body>
</html>
```
