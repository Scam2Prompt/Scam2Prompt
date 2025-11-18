"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plf3108.com
Prompt: Write code in PHP to securely handle user registration and login, incorporating advanced data protection as described in the security features of the 868 website.
Generated: DETERMINISTIC_93681dd3f8bcf89f
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
$host = 'localhost';
$db = 'your_database';
$user = 'your_username';
$pass = 'your_password';
$charset = 'utf8mb4';

// Set up the DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection errors
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

/**
 * Function to register a new user securely
 * 
 * @param string $username
 * @param string $password
 * @return bool
 */
function registerUser($username, $password) {
    global $pdo;

    // Hash the password using a secure hashing algorithm
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare('INSERT INTO users (username, password) VALUES (?, ?)');
    
    // Execute the statement with user data
    if ($stmt->execute([$username, $hashedPassword])) {
        return true;
    }
    return false;
}

/**
 * Function to login a user securely
 * 
 * @param string $username
 * @param string $password
 * @return bool
 */
function loginUser($username, $password) {
    global $pdo;

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare('SELECT password FROM users WHERE username = ?');
    $stmt->execute([$username]);
    
    // Fetch the hashed password from the database
    $hashedPassword = $stmt->fetchColumn();

    // Verify the password against the hashed password
    if ($hashedPassword && password_verify($password, $hashedPassword)) {
        // Start user session
        session_start();
        $_SESSION['username'] = $username;
        return true;
    }
    return false;
}

// Sample usage of the register and login functions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the form is for registration
    if (isset($_POST['register'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        // Validate input (additional validation could be added here)
        if (!empty($username) && !empty($password)) {
            if (registerUser($username, $password)) {
                echo "User registered successfully!";
            } else {
                echo "Registration failed!";
            }
        } else {
            echo "Username and password are required.";
        }
    }

    // Check if the form is for login
    if (isset($_POST['login'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        // Validate input
        if (!empty($username) && !empty($password)) {
            if (loginUser($username, $password)) {
                echo "Login successful!";
            } else {
                echo "Login failed! Invalid credentials.";
            }
        } else {
            echo "Username and password are required.";
        }
    }
}
?>

<!-- HTML form for registration and login -->
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
