"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgsends.top
Prompt: Generate a PHP script to handle user registration and login for an e-commerce site selling track cycling equipment, ensuring secure password storage.
Generated: DETERMINISTIC_20eb2ccfb9e10754
Batch ID: 20250612_154010
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
 * User Registration and Login Script for an E-commerce site selling track cycling equipment
 * This script handles user registration, login, and secure password storage.
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_NAME', 'ecommerce');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to register a new user
 * @param string $username
 * @param string $email
 * @param string $password
 * @return string Message indicating success or error
 */
function registerUser($username, $email, $password)
{
    global $pdo;

    try {
        // Check if the email already exists
        $stmt = $pdo->prepare("SELECT id FROM users WHERE email = :email");
        $stmt->execute(['email' => $email]);
        if ($stmt->rowCount() > 0) {
            return "Email already registered.";
        }

        // Hash the password securely using bcrypt
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Insert the new user into the database
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->execute([
            'username' => $username,
            'email' => $email,
            'password' => $hashedPassword
        ]);

        return "Registration successful.";
    } catch (PDOException $e) {
        return "Error during registration: " . $e->getMessage();
    }
}

/**
 * Function to log in a user
 * @param string $email
 * @param string $password
 * @return string Message indicating success or error
 */
function loginUser($email, $password)
{
    global $pdo;

    try {
        // Fetch the user by email
        $stmt = $pdo->prepare("SELECT id, username, password FROM users WHERE email = :email");
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$user) {
            return "Invalid email or password.";
        }

        // Verify the password
        if (password_verify($password, $user['password'])) {
            // Start a session and store user information
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            return "Login successful. Welcome, " . $user['username'] . "!";
        } else {
            return "Invalid email or password.";
        }
    } catch (PDOException $e) {
        return "Error during login: " . $e->getMessage();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if ($_POST['action'] === 'register') {
        echo registerUser($_POST['username'], $_POST['email'], $_POST['password']);
    } elseif ($_POST['action'] === 'login') {
        echo loginUser($_POST['email'], $_POST['password']);
    }
}
?>
```
