"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lover4d.site
Prompt: Develop a PHP script to manage user registration and login for an online gambling platform, including fields for bank selection and deposit amounts, similar to the 4DLOVER registration process.
Generated: DETERMINISTIC_97a4d54f714ff470
Batch ID: 20250612_145626
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
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_DATABASE', 'your_database');

try {
    // Establishing a database connection using PDO
    $pdo = new PDO("mysql:host=".DB_SERVER.";dbname=".DB_DATABASE, DB_USERNAME, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to register a new user
 *
 * @param string $username
 * @param string $password
 * @param string $bank
 * @param float $deposit
 * @return bool
 */
function registerUser($username, $password, $bank, $deposit) {
    global $pdo;

    // Password hashing for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, bank, deposit) VALUES (?, ?, ?, ?)");
    
    // Execute the statement and return success or failure
    return $stmt->execute([$username, $hashedPassword, $bank, $deposit]);
}

/**
 * Function to verify user login
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to fetch user record
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // Verify password if user exists
    if ($user && password_verify($password, $user['password'])) {
        return true; // Login successful
    }
    return false; // Login failed
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize user inputs
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
    $bank = filter_input(INPUT_POST, 'bank', FILTER_SANITIZE_STRING);
    $deposit = filter_input(INPUT_POST, 'deposit', FILTER_VALIDATE_FLOAT);

    // Check if it's a registration or login request
    if (isset($_POST['register'])) {
        if (registerUser($username, $password, $bank, $deposit)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Please try again.";
        }
    } elseif (isset($_POST['login'])) {
        if (loginUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }
}
?>

<!-- HTML Form for User Registration/Login -->
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
        <input type="text" name="bank" placeholder="Bank" required>
        <input type="number" name="deposit" placeholder="Deposit Amount" step="0.01" required>
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
