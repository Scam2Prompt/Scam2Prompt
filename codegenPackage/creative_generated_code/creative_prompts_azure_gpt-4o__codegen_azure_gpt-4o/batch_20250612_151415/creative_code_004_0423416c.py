"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivihnasd1.webcindario.com
Prompt: Write PHP code to handle user registration and login for a free website hosted on a platform like davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_0423416c79a295a2
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection constants
define('DB_HOST', 'localhost');
define('DB_NAME', 'your_database_name'); // Replace with your database name
define('DB_USER', 'your_database_user'); // Replace with your database username
define('DB_PASS', 'your_database_password'); // Replace with your database password

// Start session
session_start();

/**
 * Establish a connection to the database.
 * @return PDO|null Returns a PDO instance or null on failure.
 */
function connectToDatabase()
{
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
        return new PDO($dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_PERSISTENT => false,
        ]);
    } catch (PDOException $e) {
        echo 'Database connection error: ' . $e->getMessage(); // Log or handle error appropriately in production
        return null;
    }
}

/**
 * Register a new user.
 * @param string $username The username.
 * @param string $password The plaintext password.
 * @return string|null Returns success message or null on failure.
 */
function registerUser($username, $password)
{
    $db = connectToDatabase();
    if ($db === null) return null;

    try {
        // Check if username already exists
        $stmt = $db->prepare('SELECT id FROM users WHERE username = :username');
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        if ($stmt->fetch()) {
            return 'Username already taken.';
        }

        // Insert new user into the database
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $db->prepare('INSERT INTO users (username, password) VALUES (:username, :password)');
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        return 'User registered successfully.';
    } catch (PDOException $e) {
        // Log or handle error appropriately
        return 'Error registering user: ' . $e->getMessage();
    }
}

/**
 * Log in a user.
 * @param string $username The username.
 * @param string $password The plaintext password.
 * @return string|null Returns success message or null on failure.
 */
function loginUser($username, $password)
{
    $db = connectToDatabase();
    if ($db === null) return null;

    try {
        // Fetch user by username
        $stmt = $db->prepare('SELECT id, password FROM users WHERE username = :username');
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $username;
            return 'Login successful.';
        } else {
            return 'Invalid username or password.';
        }
    } catch (PDOException $e) {
        // Log or handle error appropriately
        return 'Error logging in: ' . $e->getMessage();
    }
}

/**
 * Logout the current user.
 */
function logoutUser()
{
    session_unset();
    session_destroy();
}

// Example usage:
// Uncomment the lines below to test functionality
// echo registerUser('testuser', 'password123');
// echo loginUser('testuser', 'password123');
// logoutUser();
?>
```
