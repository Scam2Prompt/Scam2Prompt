"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Generate code using PHP and MySQL to create a user registration system that includes bonus tracking for new members, similar to the "โบนัสต้อนรับ" feature on venez888.vip.
Generated: DETERMINISTIC_dfeaddada60c35d3
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection credentials
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'user_registration');

// Establish a connection to the database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

// Check for a successful connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitizeInput($data)
{
    return htmlspecialchars(stripslashes(trim($data)));
}

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user inputs
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);
    $email = sanitizeInput($_POST['email']);
    $bonus = 100; // Default bonus for new users

    // Validate inputs
    if (empty($username) || empty($password) || empty($email)) {
        echo "All fields are required.";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit;
    }

    // Check if username or email already exists
    $checkQuery = $conn->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
    $checkQuery->bind_param("ss", $username, $email);
    $checkQuery->execute();
    $result = $checkQuery->get_result();

    if ($result->num_rows > 0) {
        echo "Username or email is already taken.";
        exit;
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert new user data into the database
    $insertQuery = $conn->prepare("INSERT INTO users (username, password, email, bonus) VALUES (?, ?, ?, ?)");
    $insertQuery->bind_param("sssi", $username, $hashedPassword, $email, $bonus);

    if ($insertQuery->execute()) {
        echo "Registration successful! Welcome bonus: $bonus";
    } else {
        echo "Error during registration: " . $conn->error;
    }

    // Close the prepared statement
    $insertQuery->close();
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
    <title>User Registration</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>

<?php
// SQL script to set up the database table
/*
CREATE DATABASE user_registration;

USE user_registration;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    bonus INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/
?>
```
