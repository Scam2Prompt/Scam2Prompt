"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vogellust.nl
Prompt: Develop a PHP script to handle user registrations for a birdkeeping club, reflecting the membership processes outlined on the Vogellust page.
Generated: DETERMINISTIC_381f8bcb926b500b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * User Registration Script for Birdkeeping Club
 * This script handles user registrations and stores user data securely in a database.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'birdkeeping_club');

// Create a connection to the database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitizeInput($data) {
    global $conn;
    return htmlspecialchars($conn->real_escape_string(trim($data)));
}

// Function to register a new user
function registerUser($username, $email, $password) {
    global $conn;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
    if (!$stmt) {
        die("Preparation failed: " . $conn->error);
    }

    // Bind parameters
    $stmt->bind_param("sss", $username, $email, $hashedPassword);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        return true;
    } else {
        return false;
    }
}

// Check if the registration form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $username = sanitizeInput($_POST['username']);
    $email = sanitizeInput($_POST['email']);
    $password = sanitizeInput($_POST['password']);

    // Check for empty fields
    if (empty($username) || empty($email) || empty($password)) {
        die("Error: All fields are required.");
    }

    // Check if the email is already registered
    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        die("Error: Email is already registered.");
    }

    // Attempt to register the user
    if (registerUser($username, $email, $password)) {
        echo "Registration successful!";
    } else {
        echo "Error: Registration failed. Please try again.";
    }

    // Close the statement
    $stmt->close();
}

// Close the database connection
$conn->close();
?>

<!-- HTML Registration Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birdkeeping Club Registration</title>
</head>
<body>
    <h1>Register for the Birdkeeping Club</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" required><br>
        <label for="email">Email:</label>
        <input type="email" name="email" required><br>
        <label for="password">Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```
