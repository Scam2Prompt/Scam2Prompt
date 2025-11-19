"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://largeoptions.org
Prompt: Create a PHP code snippet that allows users to sign up for an account on largeoptions.org and handle the affiliate program registration process.
Generated: DETERMINISTIC_a4ef29965f04b8e9
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// signup.php

/**
 * User registration script for largeoptions.org
 * Handles account creation and affiliate program registration.
 */

// Include database connection file
require_once 'db_connection.php';

// Start session for user feedback
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Function to register user
function registerUser($username, $password, $email, $affiliateCode = null) {
    global $conn; // Use the global connection variable

    // Check if username or email already exists
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? OR email = ?");
    $stmt->bind_param("ss", $username, $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        return "Username or email already exists.";
    }

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert new user into the database
    $stmt = $conn->prepare("INSERT INTO users (username, password, email, affiliate_code) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $username, $hashedPassword, $email, $affiliateCode);
    
    if ($stmt->execute()) {
        return "Registration successful!";
    } else {
        return "Error: " . $stmt->error;
    }
}

// Check if form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);
    $email = filter_var(sanitizeInput($_POST['email']), FILTER_VALIDATE_EMAIL);
    $affiliateCode = isset($_POST['affiliate_code']) ? sanitizeInput($_POST['affiliate_code']) : null;

    // Validate required fields
    if (empty($username) || empty($password) || !$email) {
        $_SESSION['error'] = "All fields are required and email must be valid.";
        header('Location: signup_form.php'); // Redirect back to signup form
        exit();
    }

    // Register the user
    $message = registerUser($username, $password, $email, $affiliateCode);
    $_SESSION['message'] = $message;

    // Redirect to the success page or display message
    header('Location: signup_success.php');
    exit();
}
?>
```

```php
<?php
// db_connection.php

/**
 * Database connection script.
 * This script establishes a connection to the MySQL database.
 */

// Database configuration
$servername = "localhost"; // Update with your server name
$username = "db_username"; // Update with your database username
$password = "db_password"; // Update with your database password
$dbname = "largeoptions_db"; // Update with your database name

// Create database connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

```html
<!-- signup_form.php -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
</head>
<body>
    <h1>Create Account</h1>

    <!-- Display any error or success messages -->
    <?php 
    session_start(); 
    if (isset($_SESSION['error'])) {
        echo "<p style='color:red;'>".$_SESSION['error']."</p>";
        unset($_SESSION['error']);
    }
    if (isset($_SESSION['message'])) {
        echo "<p style='color:green;'>".$_SESSION['message']."</p>";
        unset($_SESSION['message']);
    }
    ?>

    <form action="signup.php" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="affiliate_code">Affiliate Code (optional):</label>
        <input type="text" id="affiliate_code" name="affiliate_code"><br>

        <input type="submit" value="Sign Up">
    </form>
</body>
</html>
```

```php
<?php
// signup_success.php

/**
 * Success page after successful registration.
 */
session_start();

// Display success message
if (isset($_SESSION['message'])) {
    echo "<h1>Registration Successful!</h1>";
    echo "<p>".$_SESSION['message']."</p>";
    unset($_SESSION['message']);
} else {
    // Redirect to sign up form if accessed directly
    header('Location: signup_form.php');
    exit();
}
?>
```
