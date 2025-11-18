"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Write a PHP script to handle user registration and login using MySQL, suitable for a free website hosted on platforms like the one mentioned in the provided content.
Generated: DETERMINISTIC_4ec9a802d8631e8b
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php: Configuration file for database connection
define('DB_HOST', 'localhost');
define('DB_NAME', 'your_database_name');
define('DB_USER', 'your_database_user');
define('DB_PASSWORD', 'your_database_password');

try {
    // Establish a secure connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error handling
} catch (PDOException $e) {
    // Handle database connection errors gracefully
    die("Database connection failed: " . $e->getMessage());
}

// Helper function for input validation
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if (!empty($username) && !empty($password)) {
        try {
            // Hash the password for secure storage
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

            // Prepare and execute the SQL query to insert a new user
            $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', $hashedPassword);
            $stmt->execute();

            echo "Registration successful!";
        } catch (PDOException $e) {
            // Handle errors like duplicate usernames
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill in all required fields.";
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if (!empty($username) && !empty($password)) {
        try {
            // Prepare and execute the SQL query to retrieve the user based on the username
            $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
            $stmt->bindParam(':username', $username);
            $stmt->execute();
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user && password_verify($password, $user['password'])) {
                // Start a session and store user information
                session_start();
                $_SESSION['username'] = $user['username'];
                echo "Login successful! Welcome, " . htmlspecialchars($_SESSION['username']);
            } else {
                echo "Invalid username or password.";
            }
        } catch (PDOException $e) {
            // Handle query errors
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill in all required fields.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>User Registration and Login</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

Note: Replace `your_database_name`, `your_database_user`, and `your_database_password` in the `config.php` section with your actual MySQL database credentials. Ensure that the `users` table exists in your database with columns `username` and `password` (`username` should be unique).
