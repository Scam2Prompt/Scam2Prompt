"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Generate a PHP script to handle user authentication for Belts Mania, including login, registration, and password recovery, as described on the website.
Generated: DETERMINISTIC_4b22e923905d6fde
Batch ID: 20250612_154441
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
define('DB_NAME', 'belts_mania');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Start session
session_start();

// Connect to the database
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to register a new user
function registerUser($username, $email, $password) {
    $pdo = connectDatabase();
    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into database
    try {
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        return "Registration successful!";
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Function to log in a user
function loginUser($email, $password) {
    $pdo = connectDatabase();

    // Fetch user details from database
    try {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            // Store user information in session
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            return "Login successful!";
        } else {
            return "Invalid email or password.";
        }
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Function to recover password
function recoverPassword($email) {
    $pdo = connectDatabase();

    // Fetch user details from database
    try {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user) {
            // Generate a new temporary password
            $temporaryPassword = bin2hex(random_bytes(4)); // 8-char temporary password
            $hashedPassword = password_hash($temporaryPassword, PASSWORD_DEFAULT);

            // Update the password in the database
            $updateStmt = $pdo->prepare("UPDATE users SET password = :password WHERE email = :email");
            $updateStmt->bindParam(':password', $hashedPassword);
            $updateStmt->bindParam(':email', $email);
            $updateStmt->execute();

            // Send temporary password via email (mocked for simplicity)
            // mail($email, "Password Recovery", "Your temporary password is: $temporaryPassword");
            return "Password recovery successful! Temporary password: $temporaryPassword";
        } else {
            return "Email not found.";
        }
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $email = $_POST['email'] ?? null;
    $password = $_POST['password'] ?? null;
    $username = $_POST['username'] ?? null;

    switch ($action) {
        case 'register':
            echo registerUser($username, $email, $password);
            break;
        case 'login':
            echo loginUser($email, $password);
            break;
        case 'recover':
            echo recoverPassword($email);
            break;
        default:
            echo "Invalid action.";
    }
}
?>
```

#### Notes:
- This code assumes the database table `users` has columns `id`, `username`, `email`, and `password`.
- Replace the `mail()` function with a real email-sending implementation for production.
- Ensure HTTPS and secure session handling in production environments.
