"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Develop a PHP script to handle user registration and login for a gaming site like Pelangi189, ensuring security and session management.
Generated: DETERMINISTIC_b9e976eec11d6d6a
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
// Database connection parameters
$host = 'localhost';
$db = 'gaming_site';
$user = 'root';
$password = '';

// Create a new PDO instance for database interaction
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Start session management
session_start();

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");

    // Bind parameters and execute
    try {
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        return false; // Registration failed
    }
}

// Function to login a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare the SQL statement to fetch the user
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    
    // Execute the statement
    $stmt->execute();
    
    // Fetch the hashed password
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    if ($user && password_verify($password, $user['password'])) {
        // Password is correct; store username in session
        $_SESSION['username'] = $username;
        return true; // Login successful
    }

    return false; // Login failed
}

// Function to logout a user
function logoutUser() {
    // Unset all of the session variables
    $_SESSION = [];

    // Destroy the session
    session_destroy();
}

// Handling form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check for registration
    if (isset($_POST['register'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        // Validate input
        if (!empty($username) && !empty($password)) {
            if (registerUser($username, $password)) {
                echo "Registration successful!";
            } else {
                echo "Registration failed: Username may already exist.";
            }
        } else {
            echo "Please fill in all fields.";
        }
    }

    // Check for login
    if (isset($_POST['login'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        // Validate input
        if (!empty($username) && !empty($password)) {
            if (loginUser($username, $password)) {
                echo "Login successful!";
                header("Location: dashboard.php"); // Redirect to dashboard
                exit();
            } else {
                echo "Login failed: Invalid username or password.";
            }
        } else {
            echo "Please fill in all fields.";
        }
    }
}

// HTML form for user registration and login
?>

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
