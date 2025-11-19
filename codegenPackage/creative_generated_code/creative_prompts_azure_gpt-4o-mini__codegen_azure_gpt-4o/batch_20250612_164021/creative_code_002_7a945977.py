"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formssubmitting.online
Prompt: Can you provide code examples for creating a password-protected form using HTML and PHP?
Generated: DETERMINISTIC_7a9459774ffa1de6
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- password-protected-form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Password Protected Form</title>
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
    .form-container {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container h1 {
      margin-bottom: 20px;
    }
    .form-container input[type="text"],
    .form-container input[type="password"],
    .form-container input[type="submit"] {
      display: block;
      width: 100%;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-container input[type="submit"] {
      background-color: #28a745;
      color: #fff;
      border: none;
      cursor: pointer;
    }
    .form-container input[type="submit"]:hover {
      background-color: #218838;
    }
    .error {
      color: red;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Login</h1>
    <!-- Display error messages if any -->
    <?php
    if (isset($_GET['error'])) {
        echo '<p class="error">' . htmlspecialchars($_GET['error']) . '</p>';
    }
    ?>
    <form action="password-protected-form.php" method="POST">
      <input type="text" name="username" placeholder="Enter your username" required>
      <input type="password" name="password" placeholder="Enter your password" required>
      <input type="submit" value="Login">
    </form>
  </div>
</body>
</html>
```

```php
<?php
// password-protected-form.php

// Start a session to manage user login state
session_start();

// Define a hardcoded username and password for authentication purposes
// In production, use a database or secure authentication methods
const VALID_USERNAME = 'admin';
const VALID_PASSWORD = 'securepassword123';

// Handle the POST request from the login form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize input to prevent security vulnerabilities like XSS
    $username = htmlspecialchars($_POST['username'] ?? '');
    $password = htmlspecialchars($_POST['password'] ?? '');

    // Check if the credentials are valid
    if ($username === VALID_USERNAME && $password === VALID_PASSWORD) {
        // Store user login state in the session
        $_SESSION['logged_in'] = true;

        // Redirect to a protected page
        header('Location: protected-page.php');
        exit();
    } else {
        // Redirect back to the form with an error message
        $error_message = urlencode('Invalid username or password.');
        header("Location: password-protected-form.html?error=$error_message");
        exit();
    }
}
```

```php
<?php
// protected-page.php

// Start a session to check user login state
session_start();

// Check if the user is logged in
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    // Redirect to the login form if not authenticated
    header('Location: password-protected-form.html');
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Protected Page</title>
</head>
<body>
  <h1>Welcome to the Protected Page!</h1>
  <p>You have successfully logged in.</p>
  <form action="logout.php" method="POST">
    <button type="submit">Logout</button>
  </form>
</body>
</html>
```

```php
<?php
// logout.php

// Start a session to manage user login state
session_start();

// Destroy the session to log the user out
session_destroy();

// Redirect back to the login form
header('Location: password-protected-form.html');
exit();
?>
```
