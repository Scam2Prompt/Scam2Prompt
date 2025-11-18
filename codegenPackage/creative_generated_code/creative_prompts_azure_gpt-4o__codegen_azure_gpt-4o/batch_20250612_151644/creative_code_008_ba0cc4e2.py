"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwallet.direct
Prompt: Create a login page using HTML and CSS that replicates the design of Trust Wallet Direct's login form, including placeholders for email and password inputs.
Generated: DETERMINISTIC_ba0cc4e2cf24234d
Batch ID: 20250612_151644
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
  <title>Login - Trust Wallet Direct</title>
  <style>
    /* Reset and basic styles */
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Centered container for the login form */
    .login-container {
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      padding: 30px;
      width: 100%;
      max-width: 400px;
    }

    /* Heading styles */
    .login-container h1 {
      font-size: 24px;
      margin-bottom: 20px;
      color: #333;
      text-align: center;
    }

    /* Input field styles */
    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-size: 14px;
      margin-bottom: 5px;
      color: #555;
    }

    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
      box-sizing: border-box;
    }

    .form-group input:focus {
      border-color: #0073e6;
      outline: none;
    }

    /* Button styles */
    .login-button {
      width: 100%;
      padding: 12px;
      background-color: #0073e6;
      color: #fff;
      font-size: 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
    }

    .login-button:hover {
      background-color: #005bb5;
    }

    /* Link styles */
    .forgot-password {
      display: block;
      text-align: center;
      margin-top: 15px;
      font-size: 14px;
      color: #0073e6;
      text-decoration: none;
    }

    .forgot-password:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <!-- Login container -->
  <div class="login-container">
    <h1>Login</h1>
    <form action="/login" method="POST">
      <!-- Email input field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
      </div>
      <!-- Password input field -->
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required>
      </div>
      <!-- Login button -->
      <button type="submit" class="login-button">Login</button>
      <!-- Forgot password link -->
      <a href="/forgot-password" class="forgot-password">Forgot your password?</a>
    </form>
  </div>
</body>
</html>
```
