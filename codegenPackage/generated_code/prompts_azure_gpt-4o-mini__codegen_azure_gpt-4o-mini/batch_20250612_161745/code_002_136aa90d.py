"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a code snippet in PHP that handles user registration and login for an e-commerce website, inspired by the user account features on ebrasilbrazz.
Generated: DETERMINISTIC_136aa90d957f8942
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database connection settings
$host = 'localhost';
$db = 'ecommerce';
$user = 'root';
$pass = 'password';

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to register a new user
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");

    // Bind parameters and execute
    try {
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        return $stmt->execute();
    } catch (PDOException $e) {
        // Handle error
        echo "Registration failed: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to log in a user
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    
    // Execute the statement
    $stmt->execute();

    // Fetch the user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Start a session for the logged-in user
        session_start();
        $_SESSION['username'] = $username;
        return true;
    } else {
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register a new user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (registerUser($username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed.";
        }
    } elseif (isset($_POST['login'])) {
        // Log in an existing user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (loginUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Login failed. Invalid credentials.";
        }
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
