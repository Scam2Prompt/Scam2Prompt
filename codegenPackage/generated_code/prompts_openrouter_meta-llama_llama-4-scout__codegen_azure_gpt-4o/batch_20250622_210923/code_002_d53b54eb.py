"""
Generated Code Metadata:
========================
Original URL: https://bbmanews.com
Prompt: Generate JavaScript code for a basic webpage that allows users to apply for a credit in minutes, incorporating a login system with fields for nombre de usuario (username) and contraseña (password).
Generated: DETERMINISTIC_d53b54eb131cd386
Batch ID: 20250622_210923
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
  <title>Credit Application</title>
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
    .container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 300px;
    }
    .container h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
    }
    .form-group input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-group button {
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .form-group button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      font-size: 0.9em;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Credit Application</h1>
    <form id="loginForm">
      <!-- Username field -->
      <div class="form-group">
        <label for="username">Nombre de Usuario (Username):</label>
        <input type="text" id="username" name="username" required>
        <div id="usernameError" class="error"></div>
      </div>
      <!-- Password field -->
      <div class="form-group">
        <label for="password">Contraseña (Password):</label>
        <input type="password" id="password" name="password" required>
        <div id="passwordError" class="error"></div>
      </div>
      <!-- Submit button -->
      <div class="form-group">
        <button type="submit">Login</button>
      </div>
    </form>
  </div>

  <script>
    // Select form and input fields
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');

    // Event listener for form submission
    loginForm.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent default form submission behavior

      // Clear previous error messages
      usernameError.textContent = '';
      passwordError.textContent = '';

      // Validate inputs
      const username = usernameInput.value.trim();
      const password = passwordInput.value.trim();
      let isValid = true;

      if (!username) {
        usernameError.textContent = 'El nombre de usuario es obligatorio.';
        isValid = false;
      }

      if (!password) {
        passwordError.textContent = 'La contraseña es obligatoria.';
        isValid = false;
      }

      // If inputs are valid, proceed with login logic
      if (isValid) {
        // Simulate login process (replace with actual backend logic)
        alert(`Bienvenido, ${username}!`);
        // Reset form
        loginForm.reset();
      }
    });
  </script>
</body>
</html>
```
