"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Write a script in PHP to create a user registration system for a website hosted on free platforms supporting MySQL databases.
Generated: DETERMINISTIC_fd71807f82952d1d
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// User Registration System
// File: register.php

// Start the session for storing user messages
session_start();

// Database configuration
define('DB_HOST', 'localhost'); // Change this if hosting on different platform
define('DB_USER', 'root');      // Replace with your database username
define('DB_PASS', '');          // Replace with your database password
define('DB_NAME', 'registration_db'); // Replace with your database name

// Establish a connection to the database
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check connection
if ($mysqli->connect_error) {
    die("Database connection failed: " . $mysqli->connect_error);
}

// Function to sanitize user input
function sanitize($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = sanitize($_POST['username']);
    $email = sanitize($_POST['email']);
    $password = sanitize($_POST['password']);
    $confirm_password = sanitize($_POST['confirm_password']);

    // Initialize an array to store errors
    $errors = [];

    // Validate fields
    if (empty($username)) {
        $errors[] = "Username is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }
    if (empty($password)) {
        $errors[] = "Password is required.";
    }
    if ($password !== $confirm_password) {
        $errors[] = "Passwords do not match.";
    }

    // Proceed if no errors
    if (empty($errors)) {
        // Hash the password
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);

        // Prepare SQL statement to insert data
        $stmt = $mysqli->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");

        if ($stmt) {
            $stmt->bind_param("sss", $username, $email, $hashed_password);

            // Execute the statement
            if ($stmt->execute()) {
                $_SESSION['message'] = "Registration successful! You can now log in.";
                header("Location: success.php");
                exit;
            } else {
                $errors[] = "Error: " . $mysqli->error;
            }

            // Close the statement
            $stmt->close();
        } else {
            $errors[] = "Error preparing the SQL statement.";
        }
    }

    // Store errors in session and redirect
    $_SESSION['errors'] = $errors;
    header("Location: register.php");
    exit;
}

// Close database connection
$mysqli->close();

?>

<!-- HTML Form for User Registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
    <?php
    // Display errors if any
    if (isset($_SESSION['errors'])) {
        foreach ($_SESSION['errors'] as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
        // Clear errors after displaying
        unset($_SESSION['errors']);
    }

    // Display success message
    if (isset($_SESSION['message'])) {
        echo "<p style='color: green;'>{$_SESSION['message']}</p>";
        // Clear message after displaying
        unset($_SESSION['message']);
    }
    ?>
    <form method="POST" action="register.php">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <label for="confirm_password">Confirm Password:</label><br>
        <input type="password" id="confirm_password" name="confirm_password" required><br><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>

<!-- SQL for creating the users table in the database -->
<!-- 
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-->
```
