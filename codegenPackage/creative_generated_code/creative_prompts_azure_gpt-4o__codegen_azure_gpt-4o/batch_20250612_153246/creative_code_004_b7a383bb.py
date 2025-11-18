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
// Start the session to manage user login states
session_start();

// Database configuration (update these with your own credentials)
define('DB_HOST', 'localhost');
define('DB_NAME', 'e_learning_platform');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Establish a database connection
function getDbConnection() {
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8';
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die('Database connection failed: ' . $e->getMessage());
    }
}

// Handle user registration
function registerUser($username, $email, $password) {
    if (empty($username) || empty($email) || empty($password)) {
        return 'All fields are required.';
    }

    try {
        $pdo = getDbConnection();

        // Check if the email is already registered
        $stmt = $pdo->prepare('SELECT id FROM users WHERE email = :email');
        $stmt->execute(['email' => $email]);
        if ($stmt->fetch()) {
            return 'Email is already registered.';
        }

        // Hash the password for secure storage
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert the new user into the database
        $stmt = $pdo->prepare('INSERT INTO users (username, email, password) VALUES (:username, :email, :password)');
        $stmt->execute([
            'username' => $username,
            'email' => $email,
            'password' => $hashedPassword
        ]);
        return 'Registration successful.';
    } catch (Exception $e) {
        return 'Error registering user: ' . $e->getMessage();
    }
}

// Handle user login
function loginUser($email, $password) {
    if (empty($email) || empty($password)) {
        return 'Email and password are required.';
    }

    try {
        $pdo = getDbConnection();

        // Retrieve user data based on email
        $stmt = $pdo->prepare('SELECT id, username, password FROM users WHERE email = :email');
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$user) {
            return 'Invalid email or password.';
        }

        // Verify the password
        if (!password_verify($password, $user['password'])) {
            return 'Invalid email or password.';
        }

        // Store user information in the session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return 'Login successful.';
    } catch (Exception $e) {
        return 'Error logging in: ' . $e->getMessage();
    }
}

// Handle user logout
function logoutUser() {
    session_unset();
    session_destroy();
    return 'Logout successful.';
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        $action = $_POST['action'];

        // Handle registration
        if ($action === 'register') {
            $username = $_POST['username'] ?? '';
            $email = $_POST['email'] ?? '';
            $password = $_POST['password'] ?? '';
            echo registerUser($username, $email, $password);
        }

        // Handle login
        if ($action === 'login') {
            $email = $_POST['email'] ?? '';
            $password = $_POST['password'] ?? '';
            echo loginUser($email, $password);
        }

        // Handle logout
        if ($action === 'logout') {
            echo logoutUser();
        }
    }
}
?>
```

### Notes:
1. **Database Schema**: You'll need a `users` table with columns `id`, `username`, `email`, and `password`.
2. **Security**: Ensure HTTPS is used on production and validate inputs thoroughly before passing them to the database.
3. **Session Management**: Use secure session cookies and consider implementing session timeout for security.
