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
// Database configuration
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

// Helper function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// User registration function
function registerUser($pdo, $username, $email, $password) {
    try {
        // Check if the username or email already exists
        $stmt = $pdo->prepare("SELECT id FROM users WHERE username = :username OR email = :email");
        $stmt->execute(['username' => $username, 'email' => $email]);
        if ($stmt->rowCount() > 0) {
            return "Username or email already exists.";
        }

        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Insert the new user into the database
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->execute(['username' => $username, 'email' => $email, 'password' => $hashedPassword]);

        return "Registration successful!";
    } catch (PDOException $e) {
        return "Error during registration: " . $e->getMessage();
    }
}

// User login function
function loginUser($pdo, $username, $password) {
    try {
        // Fetch the user record based on the username
        $stmt = $pdo->prepare("SELECT id, password FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            // Start a session and store user information
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $username;

            return "Login successful!";
        } else {
            return "Invalid username or password.";
        }
    } catch (PDOException $e) {
        return "Error during login: " . $e->getMessage();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = sanitizeInput($_POST['action']);
    $username = sanitizeInput($_POST['username']);
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : null;
    $password = sanitizeInput($_POST['password']);

    if ($action === 'register') {
        echo registerUser($pdo, $username, $email, $password);
    } elseif ($action === 'login') {
        echo loginUser($pdo, $username, $password);
    } else {
        echo "Invalid action.";
    }
}
?>
```

### Notes:
- Ensure the `users` table exists in your database with columns `id`, `username`, `email`, and `password`.
- Replace `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS` with your actual database credentials.
- This code assumes a POST request with fields `action`, `username`, `email`, and `password`. Adjust as needed for your application.
