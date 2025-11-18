"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Generate code for a "Refresh" button on a login page that reloads the page without losing entered data, inspired by the Empower login page.
Generated: DETERMINISTIC_025385f2d46b06e4
Batch ID: 20250612_150645
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
  <title>Login Page with Refresh Button</title>
  <style>
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
    .login-container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 300px;
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
    .button-group {
      display: flex;
      justify-content: space-between;
    }
    button {
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .refresh-button {
      background-color: #007BFF;
      color: #fff;
    }
    .login-button {
      background-color: #28a745;
      color: #fff;
    }
  </style>
</head>
<body>
  <div class="login-container">
    <form id="loginForm">
      <!-- Username input -->
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" placeholder="Enter your username">
      </div>

      <!-- Password input -->
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" placeholder="Enter your password">
      </div>

      <!-- Button group -->
      <div class="button-group">
        <!-- Refresh button -->
        <button type="button" class="refresh-button" id="refreshButton">Refresh</button>
        <!-- Login button -->
        <button type="submit" class="login-button">Login</button>
      </div>
    </form>
  </div>

  <script>
    // Handle the refresh button click
    document.getElementById('refreshButton').addEventListener('click', function() {
      try {
        // Save form data into localStorage
        const formData = {
          username: document.getElementById('username').value,
          password: document.getElementById('password').value,
        };
        localStorage.setItem('loginFormData', JSON.stringify(formData));

        // Reload the page
        location.reload();
      } catch (error) {
        console.error('Error during refresh:', error);
        alert('An error occurred while refreshing the page.');
      }
    });

    // Restore form data after reload
    window.addEventListener('load', function() {
      try {
        const savedData = localStorage.getItem('loginFormData');
        if (savedData) {
          const formData = JSON.parse(savedData);
          document.getElementById('username').value = formData.username || '';
          document.getElementById('password').value = formData.password || '';
          // Clear the saved data from localStorage after restoring
          localStorage.removeItem('loginFormData');
        }
      } catch (error) {
        console.error('Error restoring form data:', error);
      }
    });
  </script>
</body>
</html>
```
