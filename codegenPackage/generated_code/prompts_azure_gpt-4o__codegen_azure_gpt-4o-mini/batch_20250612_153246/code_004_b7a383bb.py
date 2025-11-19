"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Write a PHP script to handle user registration and login for an e-learning platform, referencing the features of the "Meus cursos" section on the website.
Generated: DETERMINISTIC_b7a383bbdc91c151
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost';
$db = 'elearning';
$user = 'root';
$pass = 'password'; // Change this to your database password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

    // Bind parameters and execute
    try {
        $stmt->execute([
            ':username' => $username,
            ':password' => $hashedPassword,
            ':email' => $email
        ]);
        return true;
    } catch (PDOException $e) {
        // Handle error (e.g., username already exists)
        return false;
    }
}

// Function to login a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->execute([':username' => $username]);

    // Fetch the user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Start a session and store user information
        session_start();
        $_SESSION['username'] = $username;
        return true;
    }
    return false;
}

// Function to check if user is logged in
function isLoggedIn() {
    session_start();
    return isset($_SESSION['username']);
}

// Function to logout user
function logoutUser() {
    session_start();
    session_destroy();
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Handle user registration
        $username = $_POST['username'];
        $password = $_POST['password'];
        $email = $_POST['email'];

        if (registerUser($username, $password, $email)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Username may already exist.";
        }
    } elseif (isset($_POST['login'])) {
        // Handle user login
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (loginUser($username, $password)) {
            echo "Login successful! Welcome, " . htmlspecialchars($username) . ".";
        } else {
            echo "Login failed. Please check your username and password.";
        }
    }
}
?>

<!-- HTML Form for Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```
