"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Write a PHP script to handle user registration and login for an e-learning platform, referencing the features of the "Meus cursos" section on the website.
Generated: DETERMINISTIC_b7a383bbdc91c151
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to track user login status
session_start();

// Database configuration
$host = 'localhost';
$dbname = 'elearning';
$username = 'root';
$password = 'password';

// Create a new PDO instance for database interaction
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to register a new user
 *
 * @param string $email User's email
 * @param string $password User's password
 * @return bool True on success, false on failure
 */
function registerUser($email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (email, password) VALUES (:email, :password)");
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and check for errors
    return $stmt->execute();
}

/**
 * Function to log in a user
 *
 * @param string $email User's email
 * @param string $password User's password
 * @return bool True on successful login, false otherwise
 */
function loginUser($email, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE email = :email");
    $stmt->bindParam(':email', $email);
    $stmt->execute();

    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Set session variable to indicate the user is logged in
        $_SESSION['user_email'] = $email;
        return true;
    }
    return false;
}

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action']) && $_POST['action'] === 'register') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    // Basic validation
    if (filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($password)) {
        if (registerUser($email, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Please try again.";
        }
    } else {
        echo "Invalid input. Please check your email and password.";
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action']) && $_POST['action'] === 'login') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    // Basic validation
    if (filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($password)) {
        if (loginUser($email, $password)) {
            echo "Login successful! Welcome back to your courses.";
        } else {
            echo "Invalid email or password.";
        }
    } else {
        echo "Invalid input. Please check your email and password.";
    }
}
?>

<!-- HTML Form for User Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST" action="">
        <input type="hidden" name="action" value="register">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <button type="submit">Register</button>
    </form>

    <h2>User Login</h2>
    <form method="POST" action="">
        <input type="hidden" name="action" value="login">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
