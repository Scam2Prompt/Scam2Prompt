"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a code snippet in PHP that handles user registration and login for an e-commerce website, inspired by the user account features on ebrasilbrazz.
Generated: DETERMINISTIC_136aa90d957f8942
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'ecommerce_db');
define('DB_USER', 'db_user');
define('DB_PASS', 'db_password');

// Establish database connection
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// User registration
function registerUser($username, $password, $email) {
    $pdo = connectDatabase();
    
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
    try {
        $stmt->execute([$username, $hashedPassword, $email]);
        return true;
    } catch (PDOException $e) {
        // Handle duplicate username or email error
        if ($e->getCode() === 23000) {
            return "Username or email already exists.";
        }
        return "Registration failed: " . $e->getMessage();
    }
}

// User login
function loginUser($username, $password) {
    $pdo = connectDatabase();

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->execute([$username]);

    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    if ($user && password_verify($password, $user['password'])) {
        // Start session and set user information
        session_start();
        $_SESSION['username'] = $username;
        return true;
    }
    return "Invalid username or password.";
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register a new user
        $username = $_POST['username'];
        $password = $_POST['password'];
        $email = $_POST['email'];
        $registerResult = registerUser($username, $password, $email);
        echo $registerResult === true ? "Registration successful!" : $registerResult;
    } elseif (isset($_POST['login'])) {
        // Log in an existing user
        $username = $_POST['username'];
        $password = $_POST['password'];
        $loginResult = loginUser($username, $password);
        echo $loginResult === true ? "Login successful!" : $loginResult;
    }
}
?>

<!-- HTML Form for user registration and login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>User Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```
