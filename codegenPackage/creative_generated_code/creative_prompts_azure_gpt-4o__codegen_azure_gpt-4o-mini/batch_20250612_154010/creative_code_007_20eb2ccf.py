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
// Database configuration
$host = 'localhost';
$db   = 'ecommerce';
$user = 'root';
$pass = 'password';
$charset = 'utf8mb4';

// Set up the database connection using PDO
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

/**
 * Registers a new user
 *
 * @param string $username The username for the registration
 * @param string $password The password to be hashed and stored
 * @return bool True on success, false on failure
 */
function registerUser($pdo, $username, $password) {
    // Check if the username already exists
    $stmt = $pdo->prepare('SELECT COUNT(*) FROM users WHERE username = ?');
    $stmt->execute([$username]);
    if ($stmt->fetchColumn() > 0) {
        throw new Exception("Username already taken.");
    }

    // Hash the password securely
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert the new user into the database
    $stmt = $pdo->prepare('INSERT INTO users (username, password) VALUES (?, ?)');
    return $stmt->execute([$username, $hashedPassword]);
}

/**
 * Authenticates a user
 *
 * @param string $username The username for authentication
 * @param string $password The password to be verified
 * @return bool True on successful authentication, false otherwise
 */
function loginUser($pdo, $username, $password) {
    // Fetch the user from the database
    $stmt = $pdo->prepare('SELECT password FROM users WHERE username = ?');
    $stmt->execute([$username]);

    // Check if user exists and verify password
    $user = $stmt->fetch();
    if ($user && password_verify($password, $user['password'])) {
        // Successful login
        return true;
    }

    // Failed login
    return false;
}

// Example usage
try {
    // User registration
    if (registerUser($pdo, 'john_doe', 'securepassword123')) {
        echo "User registered successfully!";
    }
} catch (Exception $e) {
    echo "Registration failed: " . $e->getMessage();
}

try {
    // User login
    if (loginUser($pdo, 'john_doe', 'securepassword123')) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
} catch (Exception $e) {
    echo "Login failed: " . $e->getMessage();
}
?>
```
